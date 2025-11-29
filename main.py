def define_env(env):
    import yaml
    import os

    CONFIG_DIR = os.path.dirname(env.conf["config_file_path"])

    def _load_yaml_absolute(rel_path: str):
        full_path = os.path.join(CONFIG_DIR, rel_path)
        with open(full_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    @env.macro
    def load_yaml(file_path: str):
        return _load_yaml_absolute(file_path)

    def _build_table_data(table_config):
        data = {"table": []}

        for division in table_config:
            div_copy = dict(division)

            if "type" in div_copy:
                new_types = []
                for tool_type in div_copy["type"]:
                    type_copy = dict(tool_type)
                    new_classes = []
                    for cls in tool_type["class"]:
                        cls_copy = dict(cls)

                        if "OSS_tools" in cls_copy:
                            oss_raw = _load_yaml_absolute(cls_copy["OSS_tools"])
                            cls_copy["OSS_tools"] = oss_raw.get("Tools", [])
                        if "PS_tools" in cls_copy:
                            ps_raw = _load_yaml_absolute(cls_copy["PS_tools"])
                            cls_copy["PS_tools"] = ps_raw.get("Tools", [])

                        new_classes.append(cls_copy)
                    type_copy["class"] = new_classes
                    new_types.append(type_copy)
                div_copy["type"] = new_types

            else:
                if "OSS_tools" in div_copy:
                    oss_raw = _load_yaml_absolute(div_copy["OSS_tools"])
                    div_copy["OSS_tools"] = oss_raw.get("Tools", [])
                if "PS_tools" in div_copy:
                    ps_raw = _load_yaml_absolute(div_copy["PS_tools"])
                    div_copy["PS_tools"] = ps_raw.get("Tools", [])

            data["table"].append(div_copy)

        return data

    def _render_table(data):
        html = ['<table border="1" style="border-collapse: collapse;">']
        html.append(
            """<thead>
                            <tr>
                                <th>Разделение</th>
                                <th>Тип</th>
                                <th>Класс</th>
                                <th colspan="5">Проприетарное ПО</th>  
                                <th colspan="5">Свободное ПО</th>
                            </tr>
                        </thead>"""
        )
        html.append("<tbody>")

        for division in data["table"]:
            div_name = division["division"]
            has_types = "type" in division

            if not has_types:
                ps_tools = division.get("PS_tools", [])
                oss_tools = division.get("OSS_tools", [])

                ps_chunks = [ps_tools[i : i + 5] for i in range(0, len(ps_tools), 5)]
                oss_chunks = [oss_tools[i : i + 5] for i in range(0, len(oss_tools), 5)]
                max_rows = max(len(ps_chunks), len(oss_chunks), 1)

                for i in range(max_rows):
                    html.append("<tr>")

                    if i == 0:
                        html.append(f'<td rowspan="{max_rows}" colspan="3">{div_name}</td>')

                    ps_tools_row = ps_chunks[i] if i < len(ps_chunks) else []
                    for tool in ps_tools_row:
                        html.append(f'<td>{tool["name"]}</td>')
                    if len(ps_tools_row) < 5:
                        html.append(f'<td colspan="{5 - len(ps_tools_row)}"></td>')

                    oss_tools_row = oss_chunks[i] if i < len(oss_chunks) else []
                    for tool in oss_tools_row:
                        html.append(f'<td>{tool["name"]}</td>')
                    if len(oss_tools_row) < 5:
                        html.append(f'<td colspan="{5 - len(oss_tools_row)}"></td>')

                    html.append("</tr>")
            else:
                type_rows = []
                for tool_type in division["type"]:
                    type_name = tool_type["name"]
                    for cls in tool_type["class"]:
                        class_name = cls["name"]

                        ps_tools = cls.get("PS_tools", [])
                        oss_tools = cls.get("OSS_tools", [])

                        ps_chunks = [ps_tools[i : i + 5] for i in range(0, len(ps_tools), 5)]
                        oss_chunks = [oss_tools[i : i + 5] for i in range(0, len(oss_tools), 5)]
                        max_rows = max(len(ps_chunks), len(oss_chunks), 1)

                        for i in range(max_rows):
                            type_rows.append(
                                {
                                    "type_name": type_name,
                                    "class_name": class_name,
                                    "ps_tools": ps_chunks[i] if i < len(ps_chunks) else [],
                                    "oss_tools": oss_chunks[i] if i < len(oss_chunks) else [],
                                }
                            )

                for i, row in enumerate(type_rows):
                    html.append("<tr>")

                    if i == 0:
                        html.append(f'<td rowspan="{len(type_rows)}">{div_name}</td>')

                    if i == 0 or row["type_name"] != type_rows[i - 1]["type_name"]:
                        type_rowspan = sum(
                            1 for r in type_rows if r["type_name"] == row["type_name"]
                        )
                        html.append(
                            f'<td rowspan="{type_rowspan}">{row["type_name"]}</td>'
                        )

                    if i == 0 or row["class_name"] != type_rows[i - 1]["class_name"]:
                        class_rowspan = sum(
                            1 for r in type_rows if r["class_name"] == row["class_name"]
                        )
                        html.append(
                            f'<td rowspan="{class_rowspan}">{row["class_name"]}</td>'
                        )

                    for tool in row["ps_tools"]:
                        html.append(f'<td>{tool["name"]}</td>')
                    if len(row["ps_tools"]) < 5:
                        html.append(
                            f'<td colspan="{5 - len(row["ps_tools"])}"></td>'
                        )

                    for tool in row["oss_tools"]:
                        html.append(f'<td>{tool["name"]}</td>')
                    if len(row["oss_tools"]) < 5:
                        html.append(
                            f'<td colspan="{5 - len(row["oss_tools"])}"></td>'
                        )

                    html.append("</tr>")

        html.append("</tbody></table>")
        return "\n".join(html)

    @env.macro
    def generate_html_table_from_config():
        table_cfg = env.conf["extra"]["table"]
        data = _build_table_data(table_cfg)
        return _render_table(data)
