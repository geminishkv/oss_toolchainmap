# Release Notes

## v2.0.1

### Общий пул проведенных работ

* Добавлены новые инструменты в карту
* Доработана генерация PDF карты инструментов
* Изменены элементы нейминга
* Внесены мелкие правки в структуре файлов директории tools
* Доработаны материалы "о проекте"

### Следующие инструменты были добавлены в карту:
* DAST
  * Shelling
  * Command-injection-attacker

* SAST
  * Shellcheck
  * Shell CGI Static code analysis
  * Xygeni SAST

* MAST
  * Appsec.Cryptex

* MLSECOPS
  * Appsec.GenAi

* SCA
  * Xygeni SCA

## v2.0.0

### Общий пул проведенных работ

* Обновлена директория tools
* Добавлены и скорректированы списки инструментов, а также их описание
* Добавлена краткая дополнительная информация по инструментам в toolchain map
* Подготовлен шаблон для автоматизации сбора информации и обновления данных по инструментам с офф ресурсов инструментов
* Добавлен частичный список российских вендоров
* Добавлен частичный список зарубежных вендоров
* Добавлен частичный список open-source проектов
* Добавлены материалы к типам Лицензий и они были расширены
* Расширены термины и определния для аббревиатур инструментов
* Доработаны материалы "о проекте"
* Доработаны материалы о проекте, политике контрибьютинга, правил проекта и тд
* Проработан вывод карты инструментов на основной странице с уветом адаптива и маркирования колонок
* Реализована интерактивная карта инстурментов с pop-up функционалом из материалов tools.json по описанию данных инструментов
* Доработан код под текущие линтеры проекта, частично выпелины линтеры из CI
* Поиск по карте вынесен в отдельный блок и частично кастомизирован
* Переработана структура репозитория и изменены пути
* Разработана и сформирована логика для генерации PDF карты инструментов
* Добавлен функционал для скачивания PDF карты инструментов
* Доработан и оптимизирован UI/UX, включая адаптив
* Доработан mkdocs.yml
* Доработан stylesheet и layout:
    * Исправлены поисковые запросы по сайту
    * Доработаны и изменены icon
    * Стилизованы иконки
    * Доработаны стили для sidebar, search, burger, table
    * Поправлены features для корректной генерации markdown страниц сайта
    * Исправлены элементы генерации таблиц для статичной и интерактивной карты инструментов

### Плановые доработки далее
* Описан site_description
* Подготовлены мета данные для поисковых запросов, оптимизации этих запросов, а также конфиги .yml
* Добавлен job для сборки и проверки генерации sitemap.xml
* Подготовлен скрипт для генерации sitemap.xml
* Оптимизирован robots.txt
* Оптимизированы отладчики для lint и шаги сборок

### Актуализирована информация по типам некоторых инструментов:

* Procyon - перемещен из OSS в PS tools (BCA)
* Dynamic SBOM - инструмент также добавлен в категорию SCA/ OSA(SBOM)
* OllyDBG - инструмент не найден (удален)
* Falco - Перемещен из OSS в PS (RASP)
* Hdiv - дополнительно добавлен в категорию RASP
* Syft - перемещен из BCA в SCA/OSA
* Conjur - перемещен из PS в OSS (Secrets management)

### Следующие инструменты были добавлены в карту:

* API
  * Salt Security
  * CloudGuard WAF
  * Cloudflare API Shield
  * Imperva API Security
  * Akamai API Security
  * Wallarm

* Attack Surface Analysis
  * Microsoft Defender EASM
  * Palo Alto Cortex Xpanse
  * CyCognito
  * CrowdStrike Falcon Surface
  * FireCompass ASM
  * Detectify ASM
  
* BCA
  * Ghidra
  * BINSEC
  * Manticore
  * BAP
  * cwe_checker
  * binbloom
  * CodeSentry
  * Black Duck Binary Analysis
  * BinSide
  * Veracode Binary SAST
  
* DAST
  * Nikto
  * Arachni
  * arachni-rest
  * Akto OSS
  * Skipfish
  * Invicti
  * FortiDAST
  * AppSpider
  * AppCheck
  * Netsparker Enterprise
  * Probely
  
* Whitebox Fuzzing
  * CI Fuzz
  * Peach Fuzzer
  * Synopsys Defensics
  * Fortra Enterprise Fuzzing

* IAST
  * DongTai IAST
    * DongTai Java Agent
    * DongTai Go Agent
    * DongTai Python Agent
    * DongTai Base Image
    * DongTai IDEA Plugin
  * 4A
  * Middleware IAST Agent
  * OWASP Benchmark Java (IAST target)
  * EvoMaster (white-box API IAST-like)
  * IAST Demo Agent (Contrast CE sample)
  * Checkmarx IAST
  * Invicti Shark IAST
  * Acunetix AcuSensor
  * New Relic IAST
  * Fortify IAST (Fortify on Demand)

* MAST
  * Needle
  * QARK
  * AndroBugs
  * QVMAP (Qiling VM Android Profiling)
  * Frida
  * Q-mast
  * NowSecure Platform
  * Appknox
  * AppSweep
  * Edgescan Mobile
  
* RASP
  * freeRASP Android
  * freeRASP iOS
  * Free-RASP Community
  * android-rasp
  * rasp-poc
  * Contrast Protect
  * Talsec RASP+
  * Pradeo RASP
  * Digital.ai Application Protection (RASP)
  * Promon SHIELD

* SAST
  * SonarQube Community
  * Cppcheck
  * Infer
  * Brakeman
  * PHPStan
  * ESLint
    * ESLint Plugin Security
  * SpotBugs
  * Yasca
  * SonarLint
  * Veracode Static Analysis
  * Snyk Code
  * Cycode SAST
  * HCL AppScan Source
  * Spectral SAST
  * AccuKnox SAST
  * Aikido Static Analysis
  * Codacy Security
  * DeepSource Static Analysis
  * Mend SAST
  * Wiz SAST

* SCA/ OSA
  * Syft
  * OpenSCA
    * OpenSCA Web
  * Tern
  * Veracode Software Composition Analysis
  * Sonatype Nexus Lifecycle
  * FOSSA SCA
  * Jit SCA
  * Aikido SCA
  * Cycode SCA
  * Plexicus ASPM (SCA)
  * GitLab Dependency Scanning
  * Qodana + Mend SCA
  * Endor Labs
  * Arnica SCA

* SBOM
  * CycloneDX CLI
  * Tern CycloneDX Generator
  * Syft for SBOM (language‑specific)
  * BOM (Java SBOM tool)
  * Retire.js (SBOM mode)
  * Jake (npm SBOM tool)

* ASPM
  * Open ASPM
  * Faraday Community
  * PatrOwl
  * Mixeway Platform
  * Jackhammer
  * Seccubus
  * Kvasir
  * Watchdog (Flipkart)
  * OpenVAS + Greenbone Community UI
  * OpsMx Delivery Shield (community components)

* CodeCoverage
  * Cobertura
  * Coverage.py
  * pytest-cov
  * Istanbul / nyc
  * scoverage
  * OpenCppCoverage
  * Coverlet
  * EMMA
  * ReportGenerator
  * go-test-coverage
  * OpenCov
  * Codecov Uploader (OSS client)
  * Visual Studio Enterprise Code Coverage
  * dotCover
  * Parasoft Code Coverage (C/C++test/Jtest)
  * Squish Coco
  * RKTracer
  * Cantata Coverage
  * NCover
  * Squish Test Center Coverage
  * BullseyeCoverage
  * VectorCAST/Cover
  * Parasoft C/C++test (coverage‑only use)

* Container Secuirty
  * Trivy
  * Anchore Engine
  * Clair
  * kube-bench
  * kube-hunter
  * Dagda
  * OpenSCAP oscap-docker
  * Sysdig open-source
  * kube-capacity / kube-psp-advisor (policy helpers)
  * kubeaudit
  * Dockle
  * kube-score
  * Wiz Container Security
  * Sysdig Secure
  * Check Point CloudGuard Container Security
  * Trend Micro Cloud One – Container Security
  * Bitdefender GravityZone Security for Containers
  * Uptycs CNAPP (Container & K8s Security)
  * SentinelOne Singularity Cloud (Container Security)
  * Hillstone CloudArmour CNAPP
  * Sysdig Secure for Cloud (Kubernetes & Container)
  * CloudGuard CNAPP (Workload & Container Protection)
  * CloudDefense.AI Container Security

* Secret Management
  * Open Policy Agent (OPA)
  * Casbin
  * Permify
  * OpenFGA
  * OPAL (Open Policy Administration Layer)
  * HashiCorp Vault (OSS)
  * Wazuh
  * Security Onion
  * Elastic Stack (Elastic Security)
  * SPIFFE / SPIRE
  * Keycloak
  * OSSEC
  * Suricata
  * Zeek
  * Trivy Operator (Kubernetes)
  * kube-bench (as security governance)

* MLSecOps - обьемное количество инструментов, включая тестируемые на рынке в текущий момент времени

### Следующие инструменты удалены из карты:

* Models-are-code - инструмент не найден
* AI Validation - инструмент не найден
* Veil - инструмент не найден
* Reliability - инструмент не найден

### Следующие инструменты возвращены в карту после обновления информации:

* SSL Kill Switch 2
* Hdiv
* Open RASP
* 42 Crunch
* Procyon
* Dynamic SBOM (Rezillion)
* Binary ninja
* Polytracker
* Ponce

## v1.1.2

* fix release-from-notes.yml
* Выстроена логика работы для сайта, таблицы инструментов и ее фильтрации
* Построены конфиги и подготовлен полноценный релиз 

Удаленные инструменты

* clj-holmes
* git-secrets
* OpenRASP - инструмент не найден
* hdiv (последний релиз 4 года назад) - https://github.com/hdiv/hdiv
* spdx-sbom-generator - закрыт - https://github.com/opensbom-generator/spdx-sbom-generator
* Cycript - Устарел, не обновлялся 8 лет - https://www.cycript.org/
* QARK - Устарел, не обновлялся 10 лет - https://github.com/linkedin/qark
* SandDroid - инструмент не найден (скорее всего устарел) - http://sanddroid.xjtu.edu.cn/
* dexcalibur - Устарел - https://github.com/FrenchYeti/dexcalibur
* Checkmarx CxIAST - как отдельное решение, скорее всего, больше не существует
* 42Crunch - не обновлялся год - https://github.com/42Crunch/apisecurity-tutorial
* API Security Empire  - Год не обновлялся - https://github.com/Cyber-Guy1/API-SecurityEmpire
* Astra - устарел - https://github.com/flipkart-incubator/Astra
* SSL Kill Switch 2 - устарел - https://github.com/nabla-c0d3/ssl-kill-switch2
* OlydDBG - инструмент не найден
* Ghidra (Hydra) - устарел - https://github.com/sslab-gatech/hydra
* DNSpy - Устарел - https://github.com/dnSpy/dnSpy
* go-fuzz - Устарел - https://github.com/dvyukov/go-fuzz
* Jazzer и Jazzer.js - Устарел - https://github.com/CodeIntelligenceTesting/jazzer.js
* jsfuzz - Устарел - https://github.com/fuzzitdev/jsfuzz
* Javafuzz - Устарел -https://github.com/fuzzitdev/javafuzz
* pythonfuzz - Устарел - https://github.com/fuzzitdev/pythonfuzz
* OlydDBG - инструмент не найден
* nikto - Устарел - https://github.com/sullo/nikto
* golismero - Устарел - https://github.com/golismero/golismero
* BooFuzz - Устарел - https://github.com/jtpereyda/boofuzz
* w3af - Устарел - https://w3af.org/ - не доступен, https://github.com/andresriancho/w3af?tab=readme-ov-file
* rezilion - Компания закрыта (возможно, теперь является часть продуктов от gitlab)
* Procyon - То, что удалось найти, устарело - https://github.com/mstrobel/procyon?tab=readme-ov-file, https://bitbucket.org/mstrobel/procyon/downloads/ 
* JDCore - Устарел - https://github.com/java-decompiler/jd-core
* BinaryNinja - Частично доступен - https://github.com/Vector35 - репозитории с модулями платформы, https://binary.ninja/ - платформа 
* polytracker - релиз был в 2022 году, но есть изменения в проекте поновее - https://github.com/trailofbits/polytracker
* Reliability - инструмент не найден
* Ponce" - инструмент не найден

### Дополнение

* Данные о лицензиях PS инструментов не всегда указаны на сайте, чтобы получить информацию о предложении вендора, надо подать заявку, поэтому у некоторых инструментов эта графа пустует.  
* По недоступным инструментам указана ссылка и заполнена графа доступности.  
*Заполненные инструменты: IAST, MAST, RASP, SAST, SCA_OSA, DAST, BCA, ASPM, codecoverage, Attack_surface_analysis

## v1.0.1
- Изменено: подход и цветовая палитра, форматирование и т.д.

## v1.0.0
- Первый публичный черновой релиз.