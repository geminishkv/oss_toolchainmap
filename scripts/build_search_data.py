import json
import pathlib
from typing import Any, Dict, List

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
TOOLS_DIR = DOCS_DIR / "tools"
OUT_DIR = DOCS_DIR / "assets" / "search"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "tools.json"

def _build_record(
    path: pathlib.Path,
    tool: Dict[str, Any],
    meta: Dict[str, Any],
    kind_label: str,
) -> Dict[str, Any]:
    return {
        "id": f"{path.stem}-{kind_label}-{tool.get('name', '')}",
        "name": tool.get("name", "") or "",
        "division": meta.get("division", "") or "",
        "type": meta.get("type", "") or "",
        "tool_class": meta.get("class", "") or "",
        "vendor": meta.get("vendor", "") or "",
        "description": meta.get("description", "") or "",
        "link_URL": meta.get("link_URL", "") or "",
        "ver_edition": meta.get("ver_edition", "") or "",
        "FSTEK_cert": meta.get("FSTEK_cert", "") or "",
        "RUS_access": meta.get("RUS_access", "") or "",
        "report_formats": meta.get("report_formats", []) or [],
        "detect_methods": meta.get("detect_methods")
        or meta.get("detect_metods")
        or [],
        "OSS": meta.get("OSS", ""),
        "lic": meta.get("lic", "") or "",
        "kind": kind_label,  # OSS / PS
        "file": str(path.relative_to(ROOT)),
    }

def load_tools_from_file(path: pathlib.Path) -> List[Dict[str, Any]]:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    records: List[Dict[str, Any]] = []

    for kind_key, kind_label in (("OSS", "OSS"), ("PS", "PS")):
        tools = raw.get(kind_key)
        if isinstance(tools, list):
            for tool in tools:
                if not isinstance(tool, dict):
                    continue
                meta = tool.get("meta", {}) or {}
                records.append(_build_record(path, tool, meta, kind_label))

    if not records:
        tools_raw = raw.get("Tools", raw) if isinstance(raw, (dict, list)) else []
        tools: List[Dict[str, Any]] = (
            tools_raw if isinstance(tools_raw, list) else []
        )
        for tool in tools:
            if not isinstance(tool, dict):
                continue
            meta = tool.get("meta", {}) or {}
            kind_label = "OSS" if meta.get("OSS") == "true" else "PS"
            records.append(_build_record(path, tool, meta, kind_label))

    return records

def main() -> None:
    all_records: List[Dict[str, Any]] = []

    for yaml_path in TOOLS_DIR.rglob("*.yaml"):
        try:
            recs = load_tools_from_file(yaml_path)
            all_records.extend(recs)
        except Exception as e:
            print(f"[WARN] Ошибка при разборе {yaml_path}: {e}")

    OUT_FILE.write_text(
        json.dumps(all_records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[INFO] Записано {len(all_records)} записей в {OUT_FILE}")

if __name__ == "__main__":
    main()
