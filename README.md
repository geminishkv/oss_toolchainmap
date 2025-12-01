<div align="center">
<h1><a id="intro"> SBOM Generator & Formatter  <sup></sup></a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>

<div align="center">
<img src="https://img.shields.io/github/repo-size/geminishkv/sbom_genform" alt="repo size"></a>
<img src="https://img.shields.io/github/last-commit/geminishkv/sbom_genform" alt="repo size"></a>
<img src="https://img.shields.io/github/commit-activity/m/geminishkv/sbom_genform" alt="repo size"></a>
<img src="https://img.shields.io/github/issues-pr/geminishkv/sbom_genform"></a>
<img src="https://img.shields.io/github/contributors/geminishkv/sbom_genform"></a></div>

***

<br>Салют :wave:,</br>
Инструмент для обработки и анализа SBOM (Software Bill of Materials) файлов с экспортом результатов в различные форматы. Проект посвящен созданию SBOM по проекту в `project_inject` и форматирования отчетов в `.xslx`, .`odt`. 

> В отчетах дорабатывается генерация выявленных уязвимостей (**доработываеся**). **Описание будет добавлено**.

* formatter.py: логгер, dotenv, DetsMemory, основной запуск
* exporter.py: pandas+ODF для отчетов
* sbom_handler.py: файловые операции, парсинг JSON
* dependency.py: обработка каждой зависимости, http-запросы, BeautifulSoup и purl
* utils.py: функции для парсинга, обработки строк, вспомогательные утилиты
* reports/ и /sbom для скрипта, что бы подложить для проверки
* pipeline.sh для сборки SBOM и подписания, прогона SCA и Container Security toolchain
* readJson загружает JSON-файл SBOM для дальнейшей работы и определяется название, версия, тип зависимости и путь
* конвертация SBOM в отчёты формата XLSX и ODT
* в каталоге `project_inject/` должен быть код исследуемого приложения с `composer.json`

<div align="center"><h3>Stay tuned ;)</h3></div> 

![Logo](assets/logotype/logo2.jpg)

***

### Что открыть, чтобы посмотреть результат

* SBOM:
    * `secgensbom_out/app-bom-cdxgen.json`
    * `secgensbom_out/merged-bom-signed.json`
    * `secgensbom_out/app-bom-dedup.json`
* Отчёты по уязвимостям:
    * `secgensbom_out/dependency-check/*`
    * `secgensbom_out/trivy/*`
    * `secgensbom_out/clair/*`
* Конвертированные отчёты:
    * по результатам пайплайна: `secgensbom_reports/excel|odt/*.xlsx|*.odt`
    * по демо-SBOM: `reports/git/...`, `reports/images/...`

***

### Структура репозитория

```bash
├── assets
│   └── logotype
│       ├── logo.jpg
│       └── logo2.jpg
├── cheatsheet
│   ├── CHEATSHEET_DOCKER.md
│   └── CHEATSHEET_DOCKERIGNORE.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile.formatter
├── Dockerfile.secgensbom
├── LICENSE.md
├── NOTICE.md
├── project_inject # vulnerability project to insert
│   ├── add.php
│   ├── composer.json
│   ├── composer.lock
│   ├── config
│   │   └── db_connect
│   ├── delete_story.php
│   ├── details.php
│   ├── edit_story.php
│   ├── edit.php
│   ├── en
│   ├── hackers.sql
│   ├── idea.php
│   ├── img
│   │   ├── book-4986 (1).png
│   │   ├── book-4986 (2).png
│   │   ├── book-4986.png
│   │   └── pizza.svg
│   ├── index.php
│   ├── login.php
│   ├── logout.php
│   ├── profile.php
│   ├── README.md
│   ├── reports.php
│   ├── search.php
│   ├── sign.php
│   ├── templates
│   │   ├── footer.php
│   │   └── header.php
│   ├── userSearch.php
│   └── xmlEx.xml
├── README.md
├── reports # reports by manual_formatter.py
│   ├── git
│   │   ├── excel
│   │   │   ├── sbom-git-fullstack.xlsx
│   │   │   ├── sbom-git-minimal.xlsx
│   │   │   ├── sbom-git-overlap.xlsx
│   │   │   ├── sbom-git-sample .xlsx
│   │   │   └── sbom-git-transitive.xlsx
│   │   └── odt
│   │       ├── sbom-git-fullstack.odt
│   │       ├── sbom-git-minimal.odt
│   │       ├── sbom-git-overlap.odt
│   │       ├── sbom-git-sample .odt
│   │       └── sbom-git-transitive.odt
│   └── images
│       ├── excel
│       │   ├── sbom-image-backend-multistage .xlsx
│       │   ├── sbom-image-critical.xlsx
│       │   ├── sbom-image-frontend-node.xlsx
│       │   └── sbom-image-sample.xlsx
│       └── odt
│           ├── sbom-image-backend-multistage .odt
│           ├── sbom-image-critical.odt
│           ├── sbom-image-frontend-node.odt
│           └── sbom-image-sample.odt
├── resolve # nextstep
│   └── SCA.Dockerfile
├── sbom
│   ├── git
│   │   ├── sbom-git-fullstack.json
│   │   ├── sbom-git-minimal.json
│   │   ├── sbom-git-overlap.json
│   │   ├── sbom-git-sample.json
│   │   └── sbom-git-transitive.json
│   └── images
│       ├── sbom-image-backend-multistage.json
│       ├── sbom-image-critical.json
│       ├── sbom-image-frontend-node.json
│       └── sbom-image-sample.json
├── script # formatter logic
│   ├── app.log
│   ├── dependency.py # обработка зависимостей
│   ├── exporter.py # экспорт отчетов
│   ├── formatter.py # auto
│   ├── manual_formatter.py # manual
│   ├── requirements.txt
│   ├── sbom_handler.py # работа с SBOM-файлами
│   ├── setup_secgensbom_env.py
│   └── utils.py
├── secgensbom # custom logic pipeline secgensbom
│   ├── config.env
│   ├── pipeline.sh
│   ├── sbom_dedup.sh
│   ├── sbom_generate.sh
│   ├── sbom_merge_sign.sh
│   ├── sca_entrypoint.sh
│   ├── scan_clair.sh
│   ├── scan_dependency_check.sh
│   └── scan_trivy.sh
├── secgensbom_out # artifacts by pipeline.sh
│   ├── app-bom-cdxgen.json # main SBOM
│   ├── app-bom-dedup.json # дедупликация
│   ├── clair
│   ├── dependency-check
│   │   ├── dependency-check-gitlab.json
│   │   ├── dependency-check-jenkins.html
│   │   ├── dependency-check-junit.xml
│   │   ├── dependency-check-report.csv
│   │   ├── dependency-check-report.html
│   │   ├── dependency-check-report.json
│   │   ├── dependency-check-report.sarif
│   │   └── dependency-check-report.xml
│   ├── merged-bom-signed.json # sign and dedup SBOM
│   └── trivy
│       ├── sbom-vulns.json
│       └── trivy-fs.json
├── secgensbom_reports
│   ├── excel
│   │   ├── app-bom-cdxgen.xlsx
│   │   ├── app-bom-dedup.xlsx
│   │   └── merged-bom-signed.xlsx
│   └── odt
│       ├── app-bom-cdxgen.odt
│       ├── app-bom-dedup.odt
│       └── merged-bom-signed.odt
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

***

### Troubleshooting

* Docker Desktop на macOS сам подтянет x86‑слой  cyclonedx/cyclonedx-cli:latest и будет прогонять его через встроенную виртуализацию для amd64.
* .DS_Store в каталогах, если глобально не потерт

```bash
rm git/.DS_Store
find . -name ".DS_Store" -delete
```

***

### Интеграция с CI/CD

```yaml

```

***


Copyright (c) 2025 Elijah S Shmakov


![Logo](assets/logotype/logo.jpg)

# MkDocs

## Полезные ссылки:
1. [Официальная документация](https://pages.github.com/)

***
## Описание: 


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

***
## Установка

>**Примечание:**   
> Инструмент может быть установлен с помощью пакетного менеджера **pip** 
> в виртуальном окружении (приоритетный способ) либо с использованием **Docker** образа.  

#### Установка с помощью pip:

1. Создадим виртуальное окружение и запустим его:
```commandline
python -m vevn venv
source venv/bin/activate
venv/Scripts/activate (для Windows)
```
2. Открываем терминал и устанавливаем необходимые зависимости:
```commandline
pip install mkdocs-material
pip install mkdocs-macros-plugin
```
Первая команда автоматически установит последние версии всех необходимых зависимостей
(MkDocs, Markdown, Pygments и Python Markdown Extensions)

***
## Использование

#### Создание сайта:
Для использования инструмента, заходим в каталог, в котором будет храниться
будущий сайт и пишем команду (точка обозначает текущую директорию):
```commandline
mkdocs new . 
```
>**Примечание:**   
> После исполнения данной команды, в директории появятся два новых файла:
> 1. mkdocs.yml - файл конфигурации. В нем хранятся основные настройки будущего сайта
> (тема, стиль, цвета и т.д.)
> 2. index.md - файл формата markdown, хранящий наполнение сайта, конвертируемое
> при создании сайта в html формат.   

Для предосмотра сайта используется команда ```mkdocs serve```. Она запускает
скрипт, публикующий сайт по адресу localhost:8000:  
![mqdocs](images/img.png)  
Это позволяет одновременно работать с наполнением сайта и смотреть получившиеся изменения. Для примера,
изменим цветовое оформление и после обновления страницы увидим результат.   
![changes](images/after_changes.jpg) 

>**Примечание:**   
> Полноценное описание возможностей генератора сайта в данном документе не затрагивается. Подробные инструкции
 по внешней кастомизации наполнения представлены в официальной документации.  

[Инструкции по работе с оформлением страниц](https://squidfunk.github.io/mkdocs-material/setup/)

## Публикация сайта:

### GitHub Pages
1. В директории проекта, создаем директорию ```.github```, в ней директорию
```workflows```. В данной директории будет лежать файл ```ci.yml``` - конфигурационный файл,
необходимый для автоматизации публикации сайта.
2. Добавить в качестве наполнения скрипт для публикации [ci.yml](images/ci.yml)   
3. Заходим на аккаунт GitHub, создаем новый репозиторий.
4. Отправляем созданный проект сайта на удаленный репозиторий:
```commandline
git init
git add .
git commit -m "message"
git remote add origin "repo_link"
git push origin "branch name"
```
>**Примечание:**   
> Опционально можно создать .gitignore для ограничения отправки ненужных файлов в репозиторий.
5. После отправки файлов на GitHub заходим в Настройки - раздел "Pages". В этом разделе выбираем ветку, в
которую запушили изменения и нажимаем "Save".
6. Выходим из настроек, заходим во вкладку "Actions" и видим наш пайплайн, который автоматически выгрузит
и опубликает сайт на GitHub Pages. Ссылка на страницу доступна в том же разделе.   
[page_deploy](images/page_deploy.jpg)

### GitLab Pages
1. В директории проекта, создаем конфигурационный файл c названием **.gitlab-ci.yml**
2. Вставляем в данный файл следующее содержимое и сохраняем файл.
```commandline
stages:
  - deploy

# Pages
pages: 
  stage: deploy
  image: javanile/mkdocs
  script: mkdocs build
  artifacts:
    paths:
      - public # public deploy
  needs: []
  only:
    - branch_name  # В данный параметр необходимо вписать 
     название ветки с размещаемым сайтом
```
3. Отправляем созданный проект сайта на удаленный репозиторий:
```commandline
git init
git add .
git commit -m "message"
git remote add origin "repo_link"
git push origin "branch name"
```
4. В GitLab заходим в раздел Deploy - Pages. После успешной отработки написанного пайплайна в разделе будет выделена ссылка  
на опубликованную страницу.


### Анализ применимости инструмента
- **CI/CD:** возможна интеграция с GitHub Actions и GitLab CI для автоматизации публикации страниц с документацией.
- **Интеграции:** Возможна интеграция плагинов MkDocs material для более комфортной генерации сайтов.
- **Командная строка/pipeline:** пример встраивания в пайплайн представлен в инструкции по публикации сайта.

***
## Особенности, выявленные при исследовании:

### Ограничения
- Для работы с инструментом необходимо досконально погружаться в документацию, понимать принципы работы со стилями и HTML.
- Большинство плагинов для MkDocs-material требуют спонсорской подписки.
- Сайты на GitHub Pages статичны, на них нельзя прикрутить ролевой доступ или формы авторизации.
- Создание сайта с помощью markdown достаточно удобно, но требует большого количества времени.

### Применимость на проектах Ланит

MkDocs-material может быть применим на проектах для создания и публикации внутренней вики проекта
(техническая документация и т.д.), а также продуктовой и пользовательской документации.

### Политики

Отсутствуют