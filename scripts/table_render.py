from typing import Any, Dict, List

def _chunk_tools(tools: List[Dict[str, Any]], size: int = 5) -> List[List[Dict[str, Any]]]:
    return [tools[i : i + size] for i in range(0, len(tools), size)]

def _render_ps_cells(tools: List[Dict[str, Any]]) -> str:
    cells: List[str] = []
    count = min(len(tools), 5)
    for i in range(count):
        name = tools[i].get("name", "")
        cells.append(f'<td><span class="tbl-ps-tool">{name}</span></td>')
    if count < 5:
        cells.append(f'<td colspan="{5 - count}"></td>')
    return "".join(cells)

def _render_oss_cells(tools: List[Dict[str, Any]]) -> str:
    cells: List[str] = []
    count = min(len(tools), 5)
    for i in range(count):
        name = tools[i].get("name", "")
        cells.append(f"<td>{name}</td>")
    if count < 5:
        cells.append(f'<td colspan="{5 - count}"></td>')
    return "".join(cells)

def render_table(data: Dict[str, Any]) -> str:
    html: List[str] = []
    html.append('<table border="1" style="border-collapse: collapse;">')
    html.append(
        """
        <thead>
          <tr>
            <th style="background-color:#1953ff; color:#ffffff;">
              <span class="tbl-division-header">Направление</span>
            </th>
            <th style="background-color:#1953ff; color:#ffffff;">Тип</th>
            <th style="background-color:#1953ff; color:#ffffff;">Класс</th>
            <th style="background-color:#1953ff; color:#ffffff;" colspan="5">Проприетарное ПО</th>
            <th style="background-color:#1953ff; color:#ffffff;" colspan="5">Свободное ПО</th>
          </tr>
        </thead>
        """
    )
    html.append("<tbody>")

    for division in data.get("table", []):
        div_name = division.get("division", "")
        types = division.get("type")

        if not types:
            ps_tools = division.get("PS_tools", []) or []
            oss_tools = division.get("OSS_tools", []) or []

            ps_chunks = _chunk_tools(ps_tools, 5)
            oss_chunks = _chunk_tools(oss_tools, 5)
            max_rows = max(len(ps_chunks), len(oss_chunks), 1)

            for idx in range(max_rows):
                html.append("<tr>")

                if idx == 0:
                    html.append(
                        f'<td rowspan="{max_rows}" colspan="3" '
                        f'style="color:#1953ff; font-weight:700;">'
                        f'{div_name}'
                        f"</td>"
                    )

                ps_row = ps_chunks[idx] if idx < len(ps_chunks) else []
                oss_row = oss_chunks[idx] if idx < len(oss_chunks) else []

                html.append(_render_ps_cells(ps_row))
                html.append(_render_oss_cells(oss_row))

                html.append("</tr>")

            continue

        flat_rows: List[Dict[str, Any]] = []

        for t in types:
            type_name = t.get("name", "")
            for cls in t.get("class", []):
                class_name = cls.get("name", "")

                ps_tools = cls.get("PS_tools", []) or []
                oss_tools = cls.get("OSS_tools", []) or []

                ps_chunks = _chunk_tools(ps_tools, 5)
                oss_chunks = _chunk_tools(oss_tools, 5)
                max_rows = max(len(ps_chunks), len(oss_chunks), 1)

                for idx in range(max_rows):
                    flat_rows.append(
                        {
                            "type": type_name,
                            "class": class_name,
                            "ps": ps_chunks[idx] if idx < len(ps_chunks) else [],
                            "oss": oss_chunks[idx] if idx < len(oss_chunks) else [],
                        }
                    )

        total_rows = len(flat_rows)

        for i, row in enumerate(flat_rows):
            html.append("<tr>")

            if i == 0:
                html.append(
                    f'<td rowspan="{total_rows}" '
                    f'style="color:#1953ff; font-weight:700;">'
                    f'{div_name}'
                    f"</td>"
                )

            if i == 0 or row["type"] != flat_rows[i - 1]["type"]:
                type_span = sum(1 for r in flat_rows if r["type"] == row["type"])
                html.append(
                    f'<td rowspan="{type_span}" style="font-weight:700;">'
                    f'{row["type"]}'
                    f"</td>"
                )

            if i == 0 or row["class"] != flat_rows[i - 1]["class"]:
                class_span = sum(1 for r in flat_rows if r["class"] == row["class"])
                html.append(
                    f'<td rowspan="{class_span}" style="font-weight:700;">'
                    f'{row["class"]}'
                    f"</td>"
                )


            html.append(_render_ps_cells(row["ps"]))
            html.append(_render_oss_cells(row["oss"]))
            html.append("</tr>")

    html.append("</tbody></table>")
    return "\n".join(html)