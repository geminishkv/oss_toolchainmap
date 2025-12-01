<div align="center">
  <h1><a id="intro"> DevSecOps Toolchain Map</a><br></h1>
</div>

<div align="center">
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://cli.github.com/"><img src="https://img.shields.io/github/repo-size/geminishkv/oss_toolchainmap" alt="GitHub_reposize"></a>
</div>

<div align="center">

![License](https://img.shields.io/github/license/geminishkv/oss_toolchainmap)
![CI](https://img.shields.io/github/actions/workflow/status/geminishkv/oss_toolchainmap/ci.yml?branch=master)
![Status](https://img.shields.io/badge/status-active-success)
![Release](https://img.shields.io/github/v/release/geminishkv/oss_toolchainmap)
![Contributor Badge](https://img.shields.io/badge/Contributor-%D0%A8%D0%BC%D0%B0%D0%BA%D0%BE%D0%B2_%D0%98._%D0%A1.-8b9aff?style=flat)
![Contributors](https://img.shields.io/github/contributors/geminishkv/oss_toolchainmap)
![Open pull requests](https://img.shields.io/github/issues-pr/geminishkv/oss_toolchainmap)
![Commit Activity](https://img.shields.io/github/commit-activity/m/geminishkv/oss_toolchainmap)
![Last commit](https://img.shields.io/github/last-commit/geminishkv/oss_toolchainmap)

</div>

***

<br>Салют :wave:,</br>

**MkDocs Material** - фреймворк для создания документации, работающий в связке со статическим генератором сайтов [MkDocs](https://www.mkdocs.org/).

<u>**Лицензия MCDocs Material:**</u> [MIT License](https://wiki.lanit.ru/display/DKSOIRSUDSEC/Permissive+Licenses#tab-MIT+License).    

Карта дает возможность выбрать выгодные для себя инструменты под все необходимые ситуации: когда нет денег, когда не можем интегрировать большой инструмент, когда никого нет и приходится делать все одному и тд.

Отмечу основные моменты:

> * Карта инструментов показывает какие есть классы и типы инструментов
> * Карта является прототипом и находится на стадии доработки
> * Предыдущая версия карты находится [тут](https://storage.yandexcloud.net/aft-tilda/%D0%9A%D0%B0%D1%80%D1%82%D0%B0%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2%20DevSecOps.pdf)
> * Агрегируются 'meta' данные о наличии сертификации, типе лицензии ПО, может ли быть импортозамещено, какой язык программирования, какие виды отчетов и иное
> * вся верстка натянута на 'material'
> * Мы принимаем 'pull requeste' на изменения для того, что бы эта карта шарилась и мы могли работать в едином поле с комьюнити
> * Имеется фильтрация по 'meta' данным
> * Убрали некоторые инструменты, которые не поддерживаются или пользуются меньшей популярностью, вследствие чего они не обновляются
> * Актуализировали списки инструментов, на сейчас готовятся правки по ткстам и добавление материалов описания

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
│   │   ├── burger.css
│   │   ├── footer.css
│   │   ├── header.css
│   │   ├── menu.css
│   │   ├── mobile-heder.css
│   │   ├── mobile-logo.css
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
├── mypy.ini
├── NOTICE.md
├── README.md
├── RELEASE_NOTES.md
├── requirements.txt
├── scripts
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-314.pyc
│   │   ├── table_data.cpython-314.pyc
│   │   └── table_render.cpython-314.pyc
│   ├── build_search_data.py
│   ├── table_data.py
│   └── table_render.py
└── SECURITY.md
```

***

### Tutorial

* Подготовка окружения

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pip install mkdocs mkdocs-material mkdocs-macros-plugin # must-have
$ pip install pyyaml
$ python scripts/build_search_data.py
$ ruff format scripts/build_search_data.py
# or
$ ruff format .
$ python -m mkdocs serve
# or
$ mkdocs serve -a 127.0.0.1:8001 # прямое обозначение адреса
```

* Очистка локального репозитория

```bash
$ rm -rf __pycache__ scripts/__pycache__ docs/assets/search/tools.json
$ lsof -i :8000
$ kill <PID>
```

* Release

```bash
$ git tag -a v1.0.0 -m “Основные изменения: …”; git push origin v1.0.0
# RELEASE_NOTES.md
```

***

### Troubleshoot

* "GET /.well-known/appspecific/com.chrome.devtools.json HTTP/1.1" code 404 игнорируем
* flake 8:
  * E501: разбить длинные строки 
  *	E302/E305: перед каждой функцией/классом – две пустые строки; после определения функций/классов – тоже нужное число пустых строк.
  *	W292: добавить перевод строки в конец файла.
  *	E203: убрать пробел перед двоеточием в срезах/аннотациях.

***

### CI/CD

* Для PR‑ов будет собираться сайт и прикрепляться как артефакт  site-preview
* job build:
	* собирает search JSON: python scripts/build_search_data.py
	*	mkdocs build — в раннере создаёт артефакт сборки site
	* upload-pages-artifact упаковывает
* job deploy:
	*	actions/deploy-pages разворачивает артефакт на GitHub Pages
* site только в раннере
*	при каждом push в master GitHub:
	*	запустит workflow ci
	*	соберёт site;
	*	задеплоит на Pages через Actions
	*	ставит зависимости из requirements.txt
	*	прогоняет ruff (линтинг)
	*	прогоняет bandit
	*	билдит search data
	*	билдит mkdocs
	*	проверяет ссылки в сгенерированном сайте (lychee)
	*	сохраняет сайт как артефакт для Pages
	*	отдельный job deploy GitHub Pages только push (не при PR)
* release:
	*	собрать MkDocs
	* упаковать site в ZIP
	*	создать GitHub Release

***

Copyright (c) 2025 Elijah S Shmakov

![Logo](docs/assets/logotype/logotypemd.jpg)