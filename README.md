<div align="center">
  <h1><a id="intro"> DevSecOps Toolchain Map</a><br></h1>

  
</div>

![Contributor Badge](https://img.shields.io/badge/Contributor-%D0%A8%D0%BC%D0%B0%D0%BA%D0%BE%D0%B2_%D0%98._%D0%A1.-8b9aff?style=flat)
![Shields.io](https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=ffffff&label=Badges&message=shields.io&color=36393f&style=flat)
![Unicode](https://img.shields.io/static/v1?logo=unicode&logoColor=ffffff&label=Table&message=Unicode&color=36393f&style=flat)
![Markdown](https://img.shields.io/static/v1?logo=markdown&logoColor=ffffff&label=Docs&message=Markdown&color=36393f&style=flat)
![GitHub Docs](https://img.shields.io/static/v1?logo=github&logoColor=ffffff&label=Docs&message=GitHub&color=36393f&style=flat)

<div align="center">

![Contributors](https://img.shields.io/github/contributors/geminishkv/sbom_genform)
![Open pull requests](https://img.shields.io/github/issues-pr/geminishkv/sbom_genform)
![Commit Activity](https://img.shields.io/github/commit-activity/m/geminishkv/sbom_genform)
![Commits](https://img.shields.io/github/last-commit/geminishkv/sbom_genform)
![Repo Size](https://img.shields.io/github/repo-size/geminishkv/sbom_genform)

</div>


![License](https://img.shields.io/github/license/USER/REPO)
![Release](https://img.shields.io/github/v/release/USER/REPO)
![Last commit](https://img.shields.io/github/last-commit/USER/REPO)
![CI](https://img.shields.io/github/actions/workflow/status/USER/REPO/ci.yml?branch=master)
![Status](https://img.shields.io/badge/status-active-success)
![Docs](https://img.shields.io/badge/docs-MkDocs%20Material-informational)
![Python](https://img.shields.io/badge/python-3.x-blue)

***


<br>Салют :wave:,</br>

**MkDocs material** - фреймворк для создания документации, работающий
в связке со статическим генератором сайтов [MkDocs](https://www.mkdocs.org/).

#### Основные функции:

- Создание документации в формате markdown.
- Кастомизация и генерация статических сайтов в формате HTML.
- Публикация сайтов на различных облачных платформах (GitHub Pages, Amazon s3 и т.д.).

#### Метаданные:

<u>**Лицензия:**</u> [MIT License](https://wiki.lanit.ru/display/DKSOIRSUDSEC/Permissive+Licenses#tab-MIT+License).    
<u>**Наличие API:**</u> отсутствует.

#### Преимущества:

- Наличие большого количества тем для сайта
- Простота кастомизации
- Возможность предосмотра при редактировании

#### Недостатки:

- Невозможность разделения доступа

![Logo](docs/assets/site/logotype/logotypemd2.jpg)

***

### Что открыть, чтобы посмотреть результат

***

### Структура репозитория

```bash
├── __pycache__
│   └── main.cpython-314.pyc
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── docs
│   ├── about.md
│   ├── appsec_tt.md
│   ├── assets
│   │   ├── logotype
│   │   │   ├── logotypemd.jpg
│   │   │   ├── logotypemd2.jpg
│   │   │   └── site
│   │   │       ├── favicon.ico
│   │   │       ├── logo_menu.png
│   │   │       └── logo.png
│   │   └── search
│   │       └── tools.json
│   ├── external.md
│   ├── index.md
│   ├── javascripts
│   │   ├── custom-title.js
│   │   ├── menu-logo.js
│   │   ├── tools-interpretator.js
│   │   ├── tools-overlay.js
│   │   ├── tools-search_pagging.js
│   │   ├── tools-search_style.js
│   │   └── tools-search.js
│   ├── licenses.md
│   ├── liders.md
│   ├── materials_iso.md
│   ├── OSS.md
│   ├── research-notes.md
│   ├── stylesheets
│   │   ├── footer.css
│   │   ├── header.css
│   │   ├── menu.css
│   │   ├── search.css
│   │   ├── sidebar.css
│   │   ├── table.css
│   │   ├── tools-overlay.css
│   │   └── typeset.css
│   ├── tools
│   │   ├── AppSec
│   │   │   ├── API
│   │   │   │   ├── OSS_tools.yaml
│   │   │   │   └── PS_tools.yaml
│   │   │   ├── Attack_Surface_Analysis
│   │   │   │   ├── OSS_tools.yaml
│   │   │   │   └── PS_tools.yaml
│   │   │   ├── BCA
│   │   │   │   ├── OSS_tools.yaml
│   │   │   │   └── PS_tools.yaml
│   │   │   ├── DAST
│   │   │   │   ├── DAST
│   │   │   │   │   ├── OSS_tools.yaml
│   │   │   │   │   └── PS_tools.yaml
│   │   │   │   └── Whitbox_fuzzing
│   │   │   │       ├── OSS_tools.yaml
│   │   │   │       └── PS_tools.yaml
│   │   │   ├── IAST
│   │   │   │   ├── OSS_tools.yaml
│   │   │   │   └── PS_tools.yaml
│   │   │   ├── MAST
│   │   │   │   ├── OSS_tools.yaml
│   │   │   │   └── PS_tools.yaml
│   │   │   ├── RASP
│   │   │   │   ├── OSS_tools.yaml
│   │   │   │   └── PS_tools.yaml
│   │   │   ├── SAST
│   │   │   │   ├── OSS_tools.yaml
│   │   │   │   └── PS_tools.yaml
│   │   │   └── SCA_OSA
│   │   │       ├── Analizator
│   │   │       │   ├── OSS_tools.yaml
│   │   │       │   └── PS_tools.yaml
│   │   │       └── SBOM
│   │   │           ├── OSS_tools.yaml
│   │   │           └── PS_tools.yaml
│   │   ├── ASPM
│   │   │   ├── OSS_tools.yaml
│   │   │   └── PS_tools.yaml
│   │   ├── codecoverage
│   │   │   ├── OSS_tools.yaml
│   │   │   └── PS_tools.yaml
│   │   ├── Container_Security
│   │   │   ├── OSS_tools.yaml
│   │   │   └── PS_tools.yaml
│   │   ├── MLSecOps
│   │   │   ├── OSS_tools.yaml
│   │   │   └── PS_tools.yaml
│   │   └── Secrets_Management
│   │       ├── OSS_tools.yaml
│   │       └── PS_tools.yaml
│   └── vendor_rf.md
├── LICENSE.md
├── main.py
├── mkdocs.yml
├── NOTICE.md
├── README.md
├── RELEASE_NOTES.md
├── requirements.txt
├── scripts
│   ├── __pycache__
│   │   ├── table_data.cpython-314.pyc
│   │   └── table_render.cpython-314.pyc
│   ├── build_search_data.py
│   ├── table_data.py
│   └── table_render.py
└── SECURITY.md
```

***

### Tutorial

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install mkdocs mkdocs-material mkdocs-macros-plugin # must-have
pip install pyyaml
python scripts/build_search_data.py
python -m mkdocs serve
# or
mkdocs serve -a 127.0.0.1:8001 # прямое обозначение адреса

rm -rf __pycache__ scripts/__pycache__ docs/assets/search/tools.json
lsof -i :8000
kill <PID>


	•	job build:
	•	собирает search JSON: python scripts/build_search_data.py;
	•	делает mkdocs build — в раннере это создаёт директорию site (артефакт сборки);
	•	upload-pages-artifact упаковывает site как артефакт. 
	•	job deploy:
	•	actions/deploy-pages разворачивает этот артефакт на GitHub Pages.

site создаётся только в раннере. Локально можешь проверить:
	•	python scripts/build_search_data.py
	•	mkdocs build
В корне появится site/
	
	•	при каждом push в master/main GitHub сам:
	•	запустит workflow ci;
	•	соберёт site;
	•	задеплоит на Pages — без отдельной ветки gh-pages, всё через Actions.

mkdir -p docs/assets/search
echo '[]' > docs/assets/search/tools.json



"GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" code 404 # игнорируем


При push в master и pull_request:
	•	собирает окружение;
	•	ставит зависимости из requirements.txt;
	•	прогоняет ruff (линтинг);
	•	прогоняет bandit (поиск уязвимостей в Python-коде);
	•	билдит search data;
	•	билдит сайт mkdocs;
	•	проверяет ссылки в сгенерированном сайте (lychee);
	•	сохраняет сайт как артефакт для Pages.
	•	Отдельный job deploy деплоит на GitHub Pages только при push (не при PR).


release

	•	собрать сайт;
	•	упаковать site в ZIP;
	•	создать GitHub Release с этим архивом.
Шаги по подключению:
	1.	Создай файл .github/workflows/release.yml.
	2.	Вставь код ниже.
	3.	Для релиза создавай тег, например v1.0.0:
	•	git tag v1.0.0
	•	git push origin v1.0.0

	•	аннотированный тег: git tag -a v1.0.0 -m “Основные изменения: …”; git push origin v1.0.0
	•	RELEASE_NOTES.md и обновляй его перед тегом – содержимое файла попадёт в текст релиза.


flake 8

	•	E501: разбить длинные строки 
	•	E302/E305: перед каждой функцией/классом – две пустые строки; после определения функций/классов – тоже нужное число пустых строк.
	•	W292: добавить перевод строки в конец файла.
	•	E203: убрать пробел перед двоеточием в срезах/аннотациях.
***

### Troubleshooting



***

### Интеграция с CI/CD

```

```

***


Copyright (c) 2025 Elijah S Shmakov