"""Интерактивная карта инструментов"""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Tuple
import os
import yaml

MAX_TOOLS_PER_ROW = 1


def _get_root_dir(env: Any) -> str:
    path = env.conf["config_file_path"]
    return os.path.dirname(str(path))


def _load_yaml_absolute(env: Any, rel_path: str) -> Any:
    root_dir = _get_root_dir(env)
    full_path = os.path.join(root_dir, rel_path)
    with open(full_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _normalize_tools(raw: Any) -> List[Dict[str, Any]]:
    if isinstance(raw, dict):
        tools = raw.get("Tools")
        if isinstance(tools, list):
            return tools
    if isinstance(raw, list):
        return raw
    return []


def _chunk(
    tools: Iterable[Dict[str, Any]],
    size: int = MAX_TOOLS_PER_ROW,
) -> List[List[Dict[str, Any]]]:
    tools_list = [t for t in tools if t]

    return (
        [tools_list[i:i + size] for i in range(0, len(tools_list), size)]
        if tools_list
        else []
    )


def _extract_meta(tool: Any) -> Tuple[str, Dict[str, Any]]:
    if isinstance(tool, str):
        return tool, {}
    if isinstance(tool, dict):
        name = str(tool.get("name", "") or "")
        meta = tool.get("meta") or {}
        if not isinstance(meta, dict):
            meta = {}
        return name, meta
    return str(tool), {}


def _fmt_list(value: Any) -> str:
    if isinstance(value, list):
        return ", ".join(str(v) for v in value if v)
    return ""


def _render_tool_with_popup(
    tool: Dict[str, Any],
    kind: str,
    division: str,
    type_name: str,
    class_name: str,
) -> str:
    name, meta = _extract_meta(tool)

    description = str(meta.get("description", "") or "")
    vendor = str(meta.get("vendor", "") or "")
    lic = str(meta.get("lic", "") or "")
    ver_edition = str(
        meta.get("ver_edition", "")
        or meta.get("veredition", "")
        or ""
    )

    fstec = str(
        meta.get("FSTEK_cert", "")
        or meta.get("FSTEKcert", "")
        or ""
    )

    rus_access = str(
        meta.get("RUS_access", "")
        or meta.get("RUSaccess", "")
        or ""
    )
    link_url = str(meta.get("link_URL", "") or meta.get("linkURL", "") or "")
    report_formats_str = _fmt_list(
        meta.get("report_formats") or meta.get("reportformats") or []
    )
    detect_methods = (
        meta.get("detect_methods")
        or meta.get("detect_metods")
        or meta.get("detectmethods")
        or []
    )
    detect_methods_str = _fmt_list(detect_methods)

    popup_id = (
        "tool-popup-"
        f"{hash(division + type_name + class_name + name) & 0xFFFFFFFF}"
    )

    html: List[str] = []

    html.append('<div class="tool">')
    html.append(
        f'<button type="button" '
        f'class="tool__name js-tool-popup-trigger" '
        f'data-popup-id="{popup_id}">'
        f"{name}</button>"
    )

    html.append(
        f'<div class="tool-popup js-tool-popup" id="{popup_id}" '
        f'role="dialog" aria-modal="true" aria-label="{name}">'
    )
    html.append('  <div class="tool-popup__inner">')
    html.append('    <header class="tool-popup__header">')
    html.append(f'      <h3 class="tool-popup__title">{name}</h3>')
    html.append(
        '      <button type="button" '
        'class="tool-popup__close js-tool-popup-close" '
        'aria-label="Закрыть">&times;</button>'
    )
    html.append("    </header>")
    html.append('    <div class="tool-popup__body">')

    if description:
        html.append(f"      <p><strong>Описание:</strong> {description}</p>")
    if division:
        html.append(f"      <p><strong>Направление:</strong> {division}</p>")
    if type_name:
        html.append(f"      <p><strong>Тип:</strong> {type_name}</p>")
    if class_name:
        html.append(f"      <p><strong>Класс:</strong> {class_name}</p>")
    if vendor:
        html.append(f"      <p><strong>Вендор:</strong> {vendor}</p>")
    if lic:
        html.append(f"      <p><strong>Лицензия:</strong> {lic}</p>")
    if kind:
        html.append(f"      <p><strong>Категория:</strong> {kind}</p>")
    if ver_edition:
        html.append(
            "      <p><strong>Версия / издание:</strong> "
            f"{ver_edition}</p>"
        )
    if fstec:
        html.append(
            "      <p><strong>Сертификация ФСТЭК:</strong> "
            f"{fstec}</p>"
        )
    if rus_access:
        html.append(
            "      <p><strong>Доступность в РФ:</strong> "
            f"{rus_access}</p>"
        )
    if report_formats_str:
        html.append(
            "      <p><strong>Форматы отчетов:</strong> "
            f"{report_formats_str}</p>"
        )
    if detect_methods_str:
        html.append(
            f"      <p><strong>Методы обнаружения:</strong> "
            f"{detect_methods_str}</p>"
        )
    if link_url:
        html.append(
            "      <p><strong>Ссылка:</strong> "
            f'<a href="{link_url}" target="_blank" '
            f'rel="noopener noreferrer">{link_url}</a></p>'
        )

    html.append("    </div>")
    html.append("  </div>")
    html.append("</div>")  # .tool-popup
    html.append("</div>")  # .tool

    return "\n".join(html)


def _load_mkdocs_config(env: Any) -> Dict[str, Any]:
    config_path = env.conf["config_file_path"]
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _load_table_config(env: Any) -> List[Dict[str, Any]]:
    mkdocs_cfg = _load_mkdocs_config(env)
    extra = mkdocs_cfg.get("extra") or {}
    table_config = extra.get("table_config") or []
    return table_config if isinstance(table_config, list) else []


def _load_tools_for_entry(
    env: Any,
    entry: Dict[str, Any],
) -> List[Dict[str, Any]]:
    division = str(entry.get("division", "") or "")

    rows: List[Dict[str, Any]] = []

    if "type" in entry:
        for tool_type in entry.get("type", []) or []:
            type_name = str(tool_type.get("name", "") or "")
            classes = tool_type.get("class", []) or []

            if classes:
                for cls in classes:
                    class_name = str(cls.get("name", "") or "")
                    oss_tools_path = cls.get("OSS_tools")
                    ps_tools_path = cls.get("PS_tools")

                    oss_tools: List[Dict[str, Any]] = []
                    ps_tools: List[Dict[str, Any]] = []

                    if oss_tools_path:
                        oss_raw = _load_yaml_absolute(env, oss_tools_path)
                        oss_tools = _normalize_tools(oss_raw)
                    if ps_tools_path:
                        ps_raw = _load_yaml_absolute(env, ps_tools_path)
                        ps_tools = _normalize_tools(ps_raw)

                    rows.append(
                        {
                            "division": division,
                            "type_name": type_name,
                            "class_name": class_name,
                            "ps_tools": ps_tools,
                            "oss_tools": oss_tools,
                        }
                    )
            else:
                oss_tools_path = tool_type.get("OSS_tools")
                ps_tools_path = tool_type.get("PS_tools")

                oss_tools = []
                ps_tools = []

                if oss_tools_path:
                    oss_raw = _load_yaml_absolute(env, oss_tools_path)
                    oss_tools = _normalize_tools(oss_raw)
                if ps_tools_path:
                    ps_raw = _load_yaml_absolute(env, ps_tools_path)
                    ps_tools = _normalize_tools(ps_raw)

                rows.append(
                    {
                        "division": division,
                        "type_name": type_name,
                        "class_name": "",
                        "ps_tools": ps_tools,
                        "oss_tools": oss_tools,
                    }
                )
    else:
        oss_tools_path = entry.get("OSS_tools")
        ps_tools_path = entry.get("PS_tools")

        oss_tools = []
        ps_tools = []

        if oss_tools_path:
            oss_raw = _load_yaml_absolute(env, oss_tools_path)
            oss_tools = _normalize_tools(oss_raw)
        if ps_tools_path:
            ps_raw = _load_yaml_absolute(env, ps_tools_path)
            ps_tools = _normalize_tools(ps_raw)

        rows.append(
            {
                "division": division,
                "type_name": "",
                "class_name": "",
                "ps_tools": ps_tools,
                "oss_tools": oss_tools,
            }
        )

    return rows


def _build_rows_from_table_config(env: Any) -> List[Dict[str, Any]]:
    table_config = _load_table_config(env)
    all_rows: List[Dict[str, Any]] = []
    for entry in table_config:
        all_rows.extend(_load_tools_for_entry(env, entry))
    return all_rows


def render_tools_popups_from_table(env: Any) -> str:
    """Попап"""
    rows = _build_rows_from_table_config(env)

    if not rows:
        return '<p class="tools-table__empty">Нет данных для таблицы</p>'

    html: List[str] = []
    html.append('<div class="tools-table-wrapper">')
    html.append('<table class="tools-table">')
    html.append("<thead>")
    html.append("<tr>")
    html.append(
        '<th class="tools-table__th" style="width: 8%;">'
        "Направление"
        "</th>"
    )
    html.append('<th class="tools-table__th" style="width: 10%;">Тип</th>')
    html.append('<th class="tools-table__th" style="width: 10%;">Класс</th>')
    html.append('<th class="tools-table__th">PS инструменты</th>')
    html.append('<th class="tools-table__th">OSS инструменты</th>')
    html.append("</tr>")
    html.append("</thead>")
    html.append("<tbody>")

    for row in rows:
        division = row["division"]
        type_name = row["type_name"]
        class_name = row["class_name"]
        ps_tools = row["ps_tools"] or []
        oss_tools = row["oss_tools"] or []

        ps_chunks = _chunk(ps_tools)
        oss_chunks = _chunk(oss_tools)
        max_subrows = max(len(ps_chunks), len(oss_chunks), 1)

        for i in range(max_subrows):
            html.append("<tr>")

            if i == 0:
                html.append(
                    f'<td class="tools-table__td" style="width: 8%;" '
                    f'rowspan="{max_subrows}">{division}</td>'
                )
                html.append(
                    f'<td class="tools-table__td" style="width: 10%;" '
                    f'rowspan="{max_subrows}">{type_name}</td>'
                )
                html.append(
                    f'<td class="tools-table__td" style="width: 12%;" '
                    f'rowspan="{max_subrows}">{class_name}</td>'
                )

            if i < len(ps_chunks):
                ps_html = "".join(
                    _render_tool_with_popup(
                        t,
                        "PS",
                        division,
                        type_name,
                        class_name,
                    )
                    for t in ps_chunks[i]
                )
                html.append(
                    '<td class="tools-table__td tools-table__td--ps">'
                    f"{ps_html}"
                    "</td>"
                )
            else:
                html.append(
                    '<td class="tools-table__td tools-table__td--ps"></td>'
                )

            if i < len(oss_chunks):
                oss_html = "".join(
                    _render_tool_with_popup(
                        t,
                        "OSS",
                        division,
                        type_name,
                        class_name,
                    )
                    for t in oss_chunks[i]
                )
                html.append(
                    '<td class="tools-table__td tools-table__td--oss">'
                    f"{oss_html}"
                    "</td>"
                )
            else:
                html.append(
                    '<td class="tools-table__td tools-table__td--oss"></td>'
                )

            html.append("</tr>")

    html.append("</tbody>")
    html.append("</table>")
    html.append("</div>")

    return "\n".join(html)
