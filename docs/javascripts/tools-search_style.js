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

    // ===== селектор типа лицензии =====
    var kindWrapper = document.createElement("div");
    kindWrapper.style.marginBottom = "0.5rem";

    var kindLabel = document.createElement("label");
    kindLabel.textContent = "Проприетарное или Свободное ПО: ";
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

    var columnsWrapper = document.createElement("div");
    columnsWrapper.style.display = "flex";
    columnsWrapper.style.gap = "2rem";

    var colLeft = document.createElement("div");
    colLeft.style.flex = "1";

    var colRight = document.createElement("div");
    colRight.style.flex = "1";

    columnsWrapper.appendChild(colLeft);
    columnsWrapper.appendChild(colRight);
    filterBlock.appendChild(columnsWrapper);

    var fieldInputs = {};

    function createFieldFilter(parentCol, id, labelText, placeholder) {
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
      inputEl.style.marginTop = "0.25rem";
      inputEl.style.width = "100%";

      wrap.appendChild(label);
      wrap.appendChild(document.createElement("br"));
      wrap.appendChild(inputEl);
      parentCol.appendChild(wrap);

      return inputEl;
    }

    fieldInputs.name = createFieldFilter(
    colLeft,
    "tools-filter-name",
    "Наименование",
    "Поиск по наименованию"
    );
    fieldInputs.vendor = createFieldFilter(
    colLeft,
    "tools-filter-vendor",
    "Поставщик",
    "Поиск по названию вендора"
    );
    fieldInputs.division = createFieldFilter(
    colLeft,
    "tools-filter-division",
    "Направление",
    "Поиск по направлению из таблицы"
    );
    fieldInputs.type = createFieldFilter(
    colLeft,
    "tools-filter-type",
    "Тип инструмента",
    "Поиск по типу классификации (SAST, SCA, etc.)"
    );
    fieldInputs.tool_class = createFieldFilter(
    colRight,
    "tools-filter-class",
    "Класс инструмента",
    "Поиск по классу из таблицы"
    );
    fieldInputs.lic = createFieldFilter(
    colRight,
    "tools-filter-lic",
    "Версия лицензии",
    "Поиск по версии лицензии"
    );
    fieldInputs.FSTEK_cert = createFieldFilter(
    colRight,
    "tools-filter-fstek",
    "Сертификат ФСТЭК",
    "Поиск наличия сертификата" // переделать логику и доьавить атрибут "true", "false"
    );
    fieldInputs.RUS_access = createFieldFilter(
    colRight,
    "tools-filter-rus",
    "Доступность в РФ",
    "Поиск по доступности в РФ"
    );
    fieldInputs.report_formats = createFieldFilter(
    colRight,
    "tools-filter-report",
    "Форматы отчётов",
    "Поиск по форматам отчётов"
    );

    container.insertBefore(filterBlock, input);

    function applyFilterAndSearch() {
      var allTools = getToolsData();
      if (!allTools.length) {
        return;
      }

      var kindValue = (kindSelect.value || "").toLowerCase();
      var searchQuery = (input.value || "").trim().toLowerCase();

      var fieldValues = {};
      Object.keys(fieldInputs).forEach(function (key) {
        fieldValues[key] = (fieldInputs[key].value || "")
          .trim()
          .toLowerCase();
      });

      var filtered = allTools.filter(function (t) {
        var kind = String(t.kind || "").toLowerCase();

        if (kindValue && kind !== kindValue) {
          return false;
        }

        function checkField(fieldKey, toolValue) {
          var fv = fieldValues[fieldKey];
          if (!fv) return true;

          var tv = toolValue;
          if (Array.isArray(tv)) {
            tv = tv.join(" ");
          }
          tv = (tv || "").toString().toLowerCase();
          return tv.includes(fv);
        }

        if (!checkField("name", t.name)) return false;
        if (!checkField("vendor", t.vendor)) return false;
        if (!checkField("division", t.division)) return false;
        if (!checkField("type", t.type)) return false;
        if (!checkField("tool_class", t.tool_class)) return false;
        if (!checkField("lic", t.lic)) return false;
        if (!checkField("FSTEK_cert", t.FSTEK_cert)) return false;
        if (!checkField("RUS_access", t.RUS_access)) return false;
        if (!checkField("report_formats", t.report_formats)) return false;

        if (searchQuery) {
          var detect = t.detect_methods || t.detect_metods || [];
          var searchHaystack = [
            t.name,
            t.vendor,
            t.division,
            t.type,
            t.tool_class,
            t.lic,
            t.description,
            t.link_URL,
            t.ver_edition,
            t.FSTEK_cert,
            t.redaction,
            t.RUS_access,
            t.report_formats,
            detect,
            t.OSS,
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