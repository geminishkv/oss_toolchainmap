document.addEventListener("DOMContentLoaded", () => {
  const topic = document.querySelector(".md-header__title .md-header__topic");
  if (!topic) return;

  topic.textContent = "";

  const link1 = Object.assign(document.createElement("a"), {
    href: "https://findevsecops.ru",
    target: "_blank",
    rel: "noopener noreferrer",
    textContent: "2026 FinDevSecOps"
  });

  const separator = document.createTextNode(" · ");

  const link2 = Object.assign(document.createElement("a"), {
    href: "https://t.me/shmakovis_appsec",
    target: "_blank",
    rel: "noopener noreferrer",
    textContent: "collaborated with geminishkv (c)"
  });

  topic.append(link1, separator, link2);
});
