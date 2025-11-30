def define_env(env):
    from scripts.table_data import build_table_data, load_yaml_absolute
    from scripts.table_render import render_table

    @env.macro
    def generate_html_table_from_config():
        table_cfg = env.conf["extra"]["table"]
        table_data = build_table_data(env, table_cfg)
        return render_table(table_data)

    @env.macro
    def load_yaml(file_path):
        return load_yaml_absolute(env, file_path)