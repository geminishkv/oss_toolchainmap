(function () {
  const labels = {
    name: "Наименование",
    vendor: "Поставщик",
    division: "Направление",
    type: "Тип",
    tool_class: "Класс",
    kind: "Тип лицензии",
    lic: "Название лицензии",
    description: "Описание",
    link_URL: "link",
    ver_edition: "Версия",
    FSTEK_cert: "Сертификация ФСТЭК",
    redaction: "Редакции",
    RUS_access: "Доступность в РФ",
    report_formats: "Форматы отчётов",
    detect_metods: "Методы обнаружения",
    OSS: "Есть ли версия OSS?"
  };

  function addLine(parent, label, value, isBoldValue) {
    if (value == null) return;
    if (Array.isArray(value) && !value.length) return;
    if (typeof value === "string" && !value.trim()) return;

    const line = document.createElement("div");

    const labelSpan = document.createElement("span");
    labelSpan.textContent = label + ": ";
    labelSpan.style.fontWeight = "bold";

    const valueSpan = document.createElement("span");

    let textValue = value;
    if (Array.isArray(value)) {
      textValue = value.join(", ");
    }

    valueSpan.textContent = textValue;
    if (isBoldValue) {
      valueSpan.style.fontWeight = "bold";
    }

    line.appendChild(labelSpan);
    line.appendChild(valueSpan);
    parent.appendChild(line);
  }

  window.renderToolsSearchResultsRaw = function (items, resultsList) {
    resultsList.innerHTML = "";
    if (!items.length) {
      return;
    }

    items.forEach(function (tool) {
      const li = document.createElement("li");
      li.className = "tool-item";

      addLine(li, labels.name, tool.name, true);
      addLine(li, labels.vendor, tool.vendor, false);
      addLine(li, labels.division, tool.division, false);
      addLine(li, labels.type, tool.type, false);
      addLine(li, labels.tool_class, tool.tool_class, false);

      const kindText = tool.kind === "OSS" ? "OSS" : "PS";
      addLine(li, labels.kind, kindText, false);

      addLine(li, labels.lic, tool.lic, false);
      addLine(li, labels.description, tool.description, false);
      addLine(li, labels.ver_edition, tool.ver_edition, false);
      addLine(li, labels.FSTEK_cert, tool.FSTEK_cert, false);
      addLine(li, labels.redaction, tool.redaction, false);
      addLine(li, labels.RUS_access, tool.RUS_access, false);
      addLine(li, labels.report_formats, tool.report_formats, false);

      const detect = tool.detect_methods || tool.detect_metods || [];
      addLine(li, labels.detect_metods, detect, false);

      if (typeof tool.OSS !== "undefined") {
        addLine(li, labels.OSS, String(tool.OSS), false);
      }

      if (tool.link_URL) {
        const urlContainer = document.createElement("div");

        const labelSpan = document.createElement("span");
        labelSpan.textContent = labels.link_URL + ": ";
        labelSpan.style.fontWeight = "bold";
        urlContainer.appendChild(labelSpan);

        const firstUrl = (tool.link_URL || "").split(",")[0].trim();
        if (firstUrl) {
          const link = document.createElement("a");
          link.href = firstUrl;
          link.target = "_blank";
          link.rel = "noopener";
          link.textContent = "Сайт";
          link.className = "tool-link";
          urlContainer.appendChild(link);
        }

        li.appendChild(urlContainer);
      }

      resultsList.appendChild(li);

      const sep = document.createElement("hr");
      sep.style.margin = "12px 0";
      sep.style.border = "none";
      sep.style.borderTop = "1px solid #ccc";
      resultsList.appendChild(sep);
    });
  };

  window.renderToolsSearchResults = function (items, resultsList) {
    window.renderToolsSearchResultsRaw(items, resultsList);
  };
})();