---
title: 
description:
---

<div align="center">

<img src="https://img.shields.io/badge/Language-%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-2448a2?style=flat" alt="Language: Russian">
<img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
<a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
<img src="https://img.shields.io/badge/git-%23F05033.svg?style=flat-square&logo=git&logoColor=white" alt="Git">
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3670A0.svg?logo=python&logoColor=ffdd54" alt="Python"></a>
<a href="https://www.mkdocs.org/"><img src="https://img.shields.io/badge/MkDocs-326ce5.svg?logo=MaterialForMkDocs&logoColor=white" alt="MkDocs"></a>
<a href="https://www.markdownguide.org/"><img src="https://img.shields.io/badge/Markdown-000000.svg?logo=markdown&logoColor=white" alt="Markdown"></a>
<a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
<a href="https://mypy-lang.org/"><img src="https://img.shields.io/badge/type_checked-mypy-039dfc?style=flat" alt="mypy"></a>
<a href="https://flake8.pycqa.org/"><img src="https://img.shields.io/badge/Code%20style-flake8-orange?style=flat" alt="flake8"></a>
<a href="https://pylint.readthedocs.io/"><img src="https://img.shields.io/badge/linting-pylint-1254a0?style=flat" alt="pylint"></a>
<a href="https://github.com/geminishkv/oss_toolchainmap/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/geminishkv/oss_toolchainmap/ci.yml?branch=develop&label=GitHub%20Actions&logo=githubactions&logoColor=white" alt="CI" /></a>
<a href="https://github.com/geminishkv/oss_toolchainmap/releases"><img src="https://img.shields.io/github/v/release/geminishkv/oss_toolchainmap?label=Release" alt="Latest release" /></a>
<a href="https://github.com/geminishkv/oss_toolchainmap"><img src="https://img.shields.io/github/repo-size/geminishkv/oss_toolchainmap?label=Repo%20size" alt="Repo size" /></a></div>

***


**AppSec Toolchain Map** — это интерактивная карта инструментов по направлению разработки безопасного ПО, которая помогает специалисту выбрать необходимые инструменты под свои ззадачи с учетом ограничений: бюджет, санкции, стэк, размер команды и зрелость процессов.

Проект задуман как открытый справочник и рабочий инструмент сообщества в котором возможно посмотреть, изучить различные классы решений, их отличия, доступность инструментов, и как выстроить из них понятную архитектуру безопасности разработки.

***

<div align="center"><h2 id="typewriter-target"></h2></div>

***

## Зачем это нужно

* показывает, какие **классы и типы инструментов** для разработки безопасного ПО существуют (SAST, DAST, SCA/OSA, secrets‑management, container security, CNAPP, MLSecOps, coverage и др.);
* связывает инструменты в **единую карту**, понятную архитекторам, безопасникам и разработчикам;
* даёт структурированные **meta‑данные** по каждому инструменту.

***

## Что есть внутри

**Основные возможности проекта:**

* **Карта классов и типов инструментов** - определение возможности использования инструментов в рамках жизненного цикла разработки на различных этапах: от анализа кода и зависимостей до рантайм‑защиты и управления рисками.

* **Структурированные meta‑данные по инструментам**  
    * лицензия (OSS / коммерческая / гибридная / trial);
    * наличие и тип сертификаций (включая ФСТЭК, при наличии);
    * доступность в РФ и риски санкций;
    * поддерживаемые языки, платформы, окружения;
    * форматы отчётов (HTML, PDF, JSON, SBOM, SARIF и др.);
    * поддерживаемые стандарты и методики (OWASP, NIST, PCI DSS, MITRE, CIS Benchmarks и т.п.);
    * роль инструмента: анализ кода, зависимости, рантайм‑защита, governance & compliance, MLSecOps и др.

* **Фильтрация по meta‑данным**  
    * лицензии и модели распространения;
    * сертификации и требованиям к регуляторике;
    * доступности в РФ;
    * типам отчётов и интеграциям;
    * классу/типу решения и назначению.

* **Фокус на импортозамещении и гибридных стэках**  
    * OSS‑альтернативы;
    * Российские решения;
    * сценарии комбинирования OSS + PS (proprietary software).

 * **Актуальность и жизненный цикл**  
     * убраны/помечены устаревшие и давно не обновляемые инструменты;
     * регулярно актуализируются версии, описания и ссылки;
     * добавляются новые классы (MLSecOps, CNAPP, ASPM и т.д.) по мере появления устойчивой практики.

***

## Как этим пользоваться

Карта рассчитана на разные роли и уровни зрелости:

* **Малые команды и специалисты** - сформировать необходимый стек из доступных инструментов, который возможно установить и настроить в инфраструктуре.

* **Крупные организации**
    * разработка целевой архитектуры DevSecOps конвейера;
    * планирование дорожной карты импортозамещения;
    * планирование миграции с «зоопарка» инструментов к более управляемому ландшафту.

*  **Архитекторы, AppSec, DevSecOps‑инженеры**  
    * референс при защите архитектурных решений;
    * инструмент для сравнения опций по прозрачным критериям;
    * материал для онбординга новых участников команды.

* **Обучение и исследования**  
    * что вообще бывает в мире security‑инструментов;
    * чем отличается один класс от другого;
    * какие есть Open Source и коммерческие инструменты в каждом сегменте.

***

## Открытость и вклад

* Репозиторий открыт, принимаются **pull‑requests**:
    * добавление и правка инструментов;
    * улучшение описаний, актуализация версий и ссылок;
    * новые категории и meta‑поля, когда появляются устойчивые практики.
* В **Issues** можно:
    * предложить новые инструменты или классы;
    * сообщить об ошибке в данных;
    * обсудить архитектуру или подход к категоризации.

Мы придерживаемся **Кодекса поведения**, чтобы обсуждения оставались профессиональными и уважительными, даже когда мнения расходятся.

***