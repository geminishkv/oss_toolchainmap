document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("tools-search-input");
  const resultsList = document.getElementById("tools-search-results");

  if (!input || !resultsList) {
    return;
  }

  let tools = [];

  fetch("/assets/search/tools.json")
    .then((r) => r.json())
    .then((data) => {
      tools = data;
    })
    .catch((err) => {
      console.error("[tools-search] failed to load tools.json", err);
    });

  function renderResults(items) {
    resultsList.innerHTML = "";
    if (!items.length) {
      return;
    }
    items.slice(0, 30).forEach((tool) => {
      const li = document.createElement("li");
      li.textContent = `${tool.name} — ${tool.vendor || ""} (${tool.kind})`;
      resultsList.appendChild(li);
    });
  }

  function onSearch() {
    const q = input.value.trim().toLowerCase();
    if (!q || !tools.length) {
      resultsList.innerHTML = "";
      return;
    }

    const filtered = tools.filter((t) => {
      const haystack = [
        t.name,
        t.vendor,
        t.description,
        t.type,
        t.toolclass,
        t.division
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();

      return haystack.includes(q);
    });

    renderResults(filtered);
  }

  input.addEventListener("input", onSearch);
});
