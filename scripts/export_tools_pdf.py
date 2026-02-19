"""Export DevSecOps tools table to PDF"""

from pathlib import Path
import sys
import traceback

from weasyprint import HTML, CSS
from scripts.table_render import render_tools_html

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

BASE_DIR = ROOT
OUTPUT = BASE_DIR / "docs" / "pdf_table" / "tools-map.pdf"


def main() -> None:
    """Render HTML with tools table and save it as PDF"""
    html_content = render_tools_html()

    full_html = """\
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Карта инструментов безопасной разработки</title>
  </head>
  <body>
  <h1>DevSecOps Toolchain Map</h1>
      <div class="page-footer">
        <div class="footer-logos">
          <a href="https://geminishkv.github.io/gpages_intro/" target="_blank">
            <img src="docs/assets/logotype/site/logo_pdf.png" \
class="footer-logo" />
          </a>
          <a href="https://findevsecops.ru" target="_blank">
            <img src="docs/assets/logotype/site/logo.png" \
class="footer-logo" />
          </a>
          <!--
          <a href="https://lanit.ru" target="_blank">
            <img src="docs/assets/logotype/site/LANIT_logo.png" \
class="footer-logo" />
          </a>
          -->
        </div>
      </div>
      <div class="page-footer_copyright">
        <div class="footer-copyright">© \
          <a href="https://geminishkv.github.io/gpages_intro/" target="_blank">
          2026 FinDevSecOps Community collaborated with geminishkv
          </a>
          &amp;
          <a href="https://findvesecops.ru/" target="_blank">
          FinDevSecOps
          </a>
      </div>
    </div>
    """
    full_html = f"{full_html}{html_content}\n  </body>\n</html>\n"

    css_path = BASE_DIR / "docs" / "stylesheets" / "tools-pdf.css"

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=full_html, base_url=str(BASE_DIR)).write_pdf(
        str(OUTPUT),
        stylesheets=[CSS(filename=str(css_path))],
    )
    print(f"PDF saved to {OUTPUT}")


if __name__ == "__main__":
    try:
        main()
    except OSError:
        traceback.print_exc()
