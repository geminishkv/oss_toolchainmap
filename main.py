"""MkDocs render"""

import sys
import os

# Ensure project root is in sys.path so `scripts.*` imports work
# regardless of how mkdocs is invoked (with or without PYTHONPATH=.)
_ROOT = os.path.dirname(os.path.abspath(__file__))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from typing import Any, Dict, List

from scripts.table_data import (
    build_table_data,
    load_table_data,
    load_yaml_absolute,
)
from scripts.table_render import render_table, render_tools_html
from scripts.render_tools_popups_from_table import (
    render_tools_popups_from_table,
)


def define_env(env: Any) -> None:
    """Register macros for MkDocs."""
    table_config: List[Dict[str, Any]] = env.conf.get("extra", {}).get(
        "table_config", []
    )

    @env.macro
    def tools_table() -> str:
        """Render tools table from YAML configuration."""
        data: Dict[str, Any] = load_table_data(env, table_config)
        return render_table(data)

    @env.macro
    def generate_html_table_from_config() -> str:
        """Build table data from configuration and render as HTML."""
        table_data: Dict[str, Any] = build_table_data(env, table_config)
        return render_table(table_data)

    @env.macro
    def load_yaml(file_path: str) -> Any:
        """Load a YAML file relative to the MkDocs project root."""
        return load_yaml_absolute(env, file_path)

    @env.macro
    def tools_table_html() -> str:
        """Return the rendered HTML table for use in templates."""
        return render_tools_html()

    @env.macro
    def tools_table_popups(_page: object | None = None) -> str:
        """Render tools table with hover popups."""
        return render_tools_popups_from_table(env)
