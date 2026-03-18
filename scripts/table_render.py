"""Docstring для scripts.table_render"""

from typing import Any, Dict, List
from pathlib import Path
import yaml

from scripts.table_data import build_table_data

MAX_TOOLS_PER_ROW = 5
BASE_DIR = Path(__file__).resolve().parent.parent


def _chunk_tools(
    tools: List[Dict[str, Any]],
    size: int = MAX_TOOLS_PER_ROW,
) -> List[List[Dict[str, Any]]]:
    """Chank to string"""
    if not tools:
        return []
    return [tools[i:i + size] for i in range(0, len(tools), size)]


def _render_ps_cells(tools: List[Dict[str, Any]]) -> str:
    """HTML table cells for proprietary tools"""
    cells: List[str] = []
    count = min(len(tools), MAX_TOOLS_PER_ROW)

    for i in range(count):
        name = tools[i].get("name", "")
        cells.append(
            f'<td><span class="tbl-ps-tool">{name}</span></td>',
        )

    if count < MAX_TOOLS_PER_ROW:
        colspan = MAX_TOOLS_PER_ROW - count
        cells.append(f'<td colspan="{colspan}"></td>')

    return "".join(cells)


def _render_oss_cells(tools: List[Dict[str, Any]]) -> str:
    cells: List[str] = []
    count = min(len(tools), MAX_TOOLS_PER_ROW)

    for i in range(count):
        name = tools[i].get("name", "")
        cells.append(f"<td>{name}</td>")

    if count < MAX_TOOLS_PER_ROW:
        colspan = MAX_TOOLS_PER_ROW - count
        cells.append(f'<td colspan="{colspan}"></td>')

    return "".join(cells)


def render_table(data: Dict[str, Any]) -> str:
    """Render HTML tools map"""
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
    <th style="background-color:#1953ff; color:#ffffff;" colspan="5">
      Проприетарное ПО
    </th>
    <th style="background-color:#1953ff; color:#ffffff;" colspan="5">
      Свободное ПО
    </th>
  </tr>
</thead>
"""
    )

    html.append("<tbody>")

    for division in data.get("table", []) or []:
        div_name: str = division.get("division", "") or ""
        types = division.get("type")

        if not types:
            ps_tools = (
                division.get("PS_tools")
                or division.get("PStools")
                or []
            )

            oss_tools = (
                division.get("OSS_tools")
                or division.get("OSStools")
                or []
            )

            ps_chunks = _chunk_tools(ps_tools, MAX_TOOLS_PER_ROW)
            oss_chunks = _chunk_tools(oss_tools, MAX_TOOLS_PER_ROW)
            max_rows = max(len(ps_chunks), len(oss_chunks), 1)

            for idx in range(max_rows):
                html.append("<tr>")

                if idx == 0:
                    html.append(
                        f'<td rowspan="{max_rows}" '
                        f'style="color:#1953ff; font-weight:700;">'
                        f"{div_name}"
                        f"</td>"
                    )

                html.append("<td></td>")
                html.append("<td></td>")

                ps_row = ps_chunks[idx] if idx < len(ps_chunks) else []
                oss_row = oss_chunks[idx] if idx < len(oss_chunks) else []

                html.append(_render_ps_cells(ps_row))
                html.append(_render_oss_cells(oss_row))
                html.append("</tr>")

            continue

        flat_rows: List[Dict[str, Any]] = []

        for t in types or []:
            type_name: str = t.get("name", "") or ""
            classes = t.get("class")

            if not classes:
                classes = [
                    {
                        "name": "",
                        "PS_tools": (
                            t.get("PS_tools")
                            or t.get("PStools")
                            or []
                        ),
                        "OSS_tools": (
                            t.get("OSS_tools")
                            or t.get("OSStools")
                            or []
                        ),
                    },
                ]

            for cls in classes or []:
                class_name: str = cls.get("name", "") or ""

                ps_tools = cls.get("PS_tools") or cls.get("PStools") or []
                oss_tools = cls.get("OSS_tools") or cls.get("OSStools") or []

                ps_chunks = _chunk_tools(ps_tools, MAX_TOOLS_PER_ROW)
                oss_chunks = _chunk_tools(oss_tools, MAX_TOOLS_PER_ROW)
                max_rows = max(len(ps_chunks), len(oss_chunks), 1)

                for idx in range(max_rows):
                    flat_rows.append(
                        {
                            "type": type_name,
                            "class": class_name,
                            "ps": (
                                ps_chunks[idx]
                                if idx < len(ps_chunks)
                                else []
                            ),
                            "oss": (
                                oss_chunks[idx]
                                if idx < len(oss_chunks)
                                else []
                            ),
                        },
                    )

        total_rows = len(flat_rows) or 1

        if not flat_rows:
            flat_rows = [{"type": "", "class": "", "ps": [], "oss": []}]

        for i, row in enumerate(flat_rows):
            html.append("<tr>")

            if i == 0:
                html.append(
                    f'<td rowspan="{total_rows}" '
                    f'style="color:#1953ff; font-weight:700;">'
                    f"{div_name}"
                    f"</td>"
                )

            if i == 0 or row["type"] != flat_rows[i - 1]["type"]:
                type_span = 1
                for j in range(i + 1, len(flat_rows)):
                    if flat_rows[j]["type"] == row["type"]:
                        type_span += 1
                    else:
                        break
                html.append(
                    (
                        f'<td rowspan="{type_span}" style="font-weight:700;">'
                        f"{row['type']}</td>"
                    ),
                )

            if i == 0 or row["class"] != flat_rows[i - 1]["class"]:
                class_span = 1
                for j in range(i + 1, len(flat_rows)):
                    if flat_rows[j]["class"] == row["class"]:
                        class_span += 1
                    else:
                        break
                html.append(
                    (
                        f'<td rowspan="{class_span}" style="font-weight:700;">'
                        f"{row['class']}</td>"
                    ),
                )

            html.append(_render_ps_cells(row["ps"]))
            html.append(_render_oss_cells(row["oss"]))
            html.append("</tr>")

    html.append("</tbody></table>")
    return "\n".join(html)


def _load_mkdocs_env_and_config() -> Dict[str, Any]:
    mkdocs_path = BASE_DIR / "mkdocs.yml"
    with mkdocs_path.open("r", encoding="utf-8") as f:
        mk = yaml.safe_load(f) or {}

    extra = mk.get("extra", {}) or {}
    table_config = extra.get("table_config", []) or []

    class DummyEnv:
        """Minimal MkDocs"""

        def __init__(self, config_file_path: str) -> None:
            self.conf = {"config_file_path": config_file_path}

    env = DummyEnv(str(mkdocs_path))
    data = build_table_data(env, table_config)
    return data


def render_tools_html() -> str:
    """Return rendered from mkdocs.yml"""
    data = _load_mkdocs_env_and_config()
    return render_table(data)
