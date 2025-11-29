def define_env(env):
    import yaml
    import os

    def include_constructor(loader, node):
        include_path = loader.construct_scalar(node)
        base_dir = os.path.dirname(loader.name) if hasattr(loader, 'name') else os.getcwd()
        full_path = os.path.join(base_dir, include_path)

        with open(full_path, 'r', encoding='utf-8') as f:
            content = yaml.safe_load(f)

        return content.get("Tools")

    @env.macro
    def load_yaml(file_path):
        yaml.add_constructor('!include', include_constructor, Loader=yaml.SafeLoader)

        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    @env.macro
    def generate_html_table(data):
        html = ['<table border="1" style="border-collapse: collapse;">']
        html.append('''<thead>
                            <tr>
                                <th>Разделение</th>
                                <th>Тип</th>
                                <th>Класс</th>
                                <th colspan="5">Проприетарное ПО</th>  
                                <th colspan="5">Свободное ПО</th>
                            </tr>
                        </thead>''')
        html.append('<tbody>')

        for division in data['table']:
            div_name = division['division']
            has_types = 'type' in division

            if not has_types:
                # Обработка division без type/class
                ps_tools = division.get('PS_tools', [])
                oss_tools = division.get('OSS_tools', [])

                # Разбиваем инструменты на группы по 5
                ps_chunks = [ps_tools[i:i + 5] for i in range(0, len(ps_tools), 5)]
                oss_chunks = [oss_tools[i:i + 5] for i in range(0, len(oss_tools), 5)]
                max_rows = max(len(ps_chunks), len(oss_chunks))

                for i in range(max_rows):
                    html.append('<tr>')

                    if i == 0:
                        html.append(f'<td rowspan="{max_rows}" colspan="3">{div_name}</td>')

                    # PS Tools (5 ячеек)
                    ps_tools_row = ps_chunks[i] if i < len(ps_chunks) else []
                    for j in range(len(ps_tools_row)):
                        html.append(f'<td>{ps_tools_row[j]["name"]}</td>')

                    # Добавляем colspan для оставшихся ячеек
                    if len(ps_tools_row) < 5:
                        html.append(f'<td colspan="{5 - len(ps_tools_row)}"></td>')

                    # OSS Tools (5 ячеек)
                    oss_tools_row = oss_chunks[i] if i < len(oss_chunks) else []
                    for j in range(len(oss_tools_row)):
                        html.append(f'<td>{oss_tools_row[j]["name"]}</td>')

                    # Добавляем colspan для оставшихся ячеек
                    if len(oss_tools_row) < 5:
                        html.append(f'<td colspan="{5 - len(oss_tools_row)}"></td>')

                    html.append('</tr>')
            else:
                # Обработка division с type/class
                type_rows = []
                for tool_type in division['type']:
                    type_name = tool_type['name']
                    for cls in tool_type['class']:
                        class_name = cls['name']

                        ps_tools = cls.get('PS_tools', [])
                        oss_tools = cls.get('OSS_tools', [])

                        # Разбиваем инструменты на группы по 5
                        ps_chunks = [ps_tools[i:i + 5] for i in range(0, len(ps_tools), 5)]
                        oss_chunks = [oss_tools[i:i + 5] for i in range(0, len(oss_tools), 5)]
                        max_rows = max(len(ps_chunks), len(oss_chunks))

                        for i in range(max_rows):
                            type_rows.append({
                                'type_name': type_name,
                                'class_name': class_name,
                                'ps_tools': ps_chunks[i] if i < len(ps_chunks) else [],
                                'oss_tools': oss_chunks[i] if i < len(oss_chunks) else []
                            })

                # Генерируем строки для division с type/class
                for i, row in enumerate(type_rows):
                    html.append('<tr>')

                    if i == 0:
                        html.append(f'<td rowspan="{len(type_rows)}">{div_name}</td>')

                    # Type rowspan
                    if i == 0 or row['type_name'] != type_rows[i - 1]['type_name']:
                        type_rowspan = sum(1 for r in type_rows if r['type_name'] == row['type_name'])
                        html.append(f'<td rowspan="{type_rowspan}">{row["type_name"]}</td>')

                    # Class rowspan
                    if i == 0 or row['class_name'] != type_rows[i - 1]['class_name']:
                        class_rowspan = sum(1 for r in type_rows if r['class_name'] == row['class_name'])
                        html.append(f'<td rowspan="{class_rowspan}">{row["class_name"]}</td>')

                    # PS Tools
                    for tool in row['ps_tools']:
                        html.append(f'<td>{tool["name"]}</td>')

                    # Добавляем colspan для оставшихся PS Tools ячеек
                    if len(row['ps_tools']) < 5:
                        html.append(f'<td colspan="{5 - len(row["ps_tools"])}"></td>')

                    # OSS Tools
                    for tool in row['oss_tools']:
                        html.append(f'<td>{tool["name"]}</td>')

                    # Добавляем colspan для оставшихся OSS Tools ячеек
                    if len(row['oss_tools']) < 5:
                        html.append(f'<td colspan="{5 - len(row["oss_tools"])}"></td>')

                    html.append('</tr>')

        html.append('</tbody></table>')
        return '\n'.join(html)