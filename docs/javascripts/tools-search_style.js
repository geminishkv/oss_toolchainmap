(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var input = document.getElementById("tools-search-input");
    var resultsList = document.getElementById("tools-search-results");

    if (!input || !resultsList) {
      return;
    }

    if (document.getElementById("tools-search-filters")) {
      return;
    }

    function getToolsData() {
      return (window.toolsSearchData && window.toolsSearchData.tools) || [];
    }

    var container = document.getElementById("tools-search");
    if (!container) return;

    var filterBlock = document.createElement("div");
    filterBlock.id = "tools-search-filters";
    filterBlock.style.marginBottom = "1rem";

    var kindWrapper = document.createElement("div");
    kindWrapper.style.marginBottom = "0.5rem";

    var kindLabel = document.createElement("label");
    kindLabel.textContent = "Тип лицензии: ";
    kindLabel.style.fontWeight = "bold";
    kindLabel.htmlFor = "tools-filter-kind";

    var kindSelect = document.createElement("select");
    kindSelect.id = "tools-filter-kind";
    kindSelect.style.marginLeft = "0.5rem";

    var optAny = document.createElement("option");
    optAny.value = "";
    optAny.textContent = "Любой";

    var optOss = document.createElement("option");
    optOss.value = "OSS";
    optOss.textContent = "OSS (open-source)";

    var optPs = document.createElement("option");
    optPs.value = "PS";
    optPs.textContent = "PS (вендор)";

    kindSelect.appendChild(optAny);
    kindSelect.appendChild(optOss);
    kindSelect.appendChild(optPs);

    kindWrapper.appendChild(kindLabel);
    kindWrapper.appendChild(kindSelect);
    filterBlock.appendChild(kindWrapper);

    var fieldInputs = {};

    function createFieldFilter(id, labelText, placeholder) {
      var wrap = document.createElement("div");
      wrap.style.marginBottom = "0.5rem";

      var label = document.createElement("label");
      label.textContent = labelText + ": ";
      label.style.fontWeight = "bold";
      label.htmlFor = id;

      var inputEl = document.createElement("input");
      inputEl.type = "search";
      inputEl.id = id;
      inputEl.placeholder = placeholder;
      inputEl.style.marginLeft = "0.5rem";
      inputEl.style.width = "60%";

      wrap.appendChild(label);
      wrap.appendChild(inputEl);
      filterBlock.appendChild(wrap);

      return inputEl;
    }

    fieldInputs.name = createFieldFilter(
      "tools-filter-name",
      "Наименование",
      "Поиск по наименованию"
    );
    fieldInputs.vendor = createFieldFilter(
      "tools-filter-vendor",
      "Вендор",
      "Поиск по вендору"
    );
    fieldInputs.division = createFieldFilter(
      "tools-filter-division",
      "Раздел карты",
      "Поиск по разделу карты"
    );
    fieldInputs.type = createFieldFilter(
      "tools-filter-type",
      "Тип",
      "Поиск по типу"
    );
    fieldInputs.tool_class = createFieldFilter(
      "tools-filter-class",
      "Класс",
      "Поиск по классу"
    );
    fieldInputs.lic = createFieldFilter(
      "tools-filter-lic",
      "Лицензия",
      "Поиск по лицензии"
    );
    fieldInputs.description = createFieldFilter(
      "tools-filter-description",
      "Описание",
      "Поиск по описанию"
    );
    fieldInputs.link_URL = createFieldFilter(
      "tools-filter-link",
      "Ссылка",
      "Поиск по ссылке"
    );

    container.insertBefore(filterBlock, input);

    function applyFilterAndSearch() {
      var allTools = getToolsData();
      if (!allTools.length) {
        return;
      }

      var kindValue = (kindSelect.value || "").toLowerCase();
      var searchQuery = (input.value || "").trim().toLowerCase();

      // Собираем значения по каждому конкретному полю
      var fieldValues = {};
      Object.keys(fieldInputs).forEach(function (key) {
        fieldValues[key] = (fieldInputs[key].value || "")
          .trim()
          .toLowerCase();
      });

      var filtered = allTools.filter(function (t) {
        if (kindValue && String(t.kind || "").toLowerCase() !== kindValue) {
          return false;
        }

        if (
          fieldValues.name &&
          !(t.name || "").toLowerCase().includes(fieldValues.name)
        ) {
          return false;
        }

        if (
          fieldValues.vendor &&
          !(t.vendor || "").toLowerCase().includes(fieldValues.vendor)
        ) {
          return false;
        }

        if (
          fieldValues.division &&
          !(t.division || "")
            .toLowerCase()
            .includes(fieldValues.division)
        ) {
          return false;
        }

        if (
          fieldValues.type &&
          !(t.type || "").toLowerCase().includes(fieldValues.type)
        ) {
          return false;
        }

        if (
          fieldValues.tool_class &&
          !(t.tool_class || "")
            .toLowerCase()
            .includes(fieldValues.tool_class)
        ) {
          return false;
        }

        if (
          fieldValues.lic &&
          !(t.lic || "").toLowerCase().includes(fieldValues.lic)
        ) {
          return false;
        }

        if (
          fieldValues.description &&
          !(t.description || "")
            .toLowerCase()
            .includes(fieldValues.description)
        ) {
          return false;
        }

        if (
          fieldValues.link_URL &&
          !(t.link_URL || "")
            .toLowerCase()
            .includes(fieldValues.link_URL)
        ) {
          return false;
        }

        if (searchQuery) {
          var searchHaystack = [
            t.name,
            t.vendor,
            t.division,
            t.type,
            t.tool_class,
            t.lic,
            t.description,
            t.link_URL,
            t.kind
          ]
            .filter(Boolean)
            .join(" ")
            .toLowerCase();

          if (!searchHaystack.includes(searchQuery)) {
            return false;
          }
        }

        return true;
      });

      if (typeof window.renderToolsSearchResults === "function") {
        window.renderToolsSearchResults(filtered, resultsList);
      }
    }

    kindSelect.addEventListener("change", applyFilterAndSearch);
    Object.keys(fieldInputs).forEach(function (key) {
      fieldInputs[key].addEventListener("input", applyFilterAndSearch);
    });
    input.addEventListener("input", applyFilterAndSearch);

    if (getToolsData().length) {
      applyFilterAndSearch();
    }

    window.toolsSearchApplyFilters = applyFilterAndSearch;
  });
})();
