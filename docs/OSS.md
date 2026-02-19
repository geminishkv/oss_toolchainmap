---
hide:
  - toc

title: Open Source инструменты AppSec и их «вендоры»
description: Популярные open source‑проекты в области разработки безопасного ПО и их ключевые инструменты.
---

***

> Под «вендором» понимаются организации, фонды или команды, развивающие open source‑проекты.  
> При внедрении в продуктивную среду рекомендуется сверяться с актуальной документацией и лицензиями на GitHub/официальных сайтах.

<table>
  <thead>
    <tr>
      <th style="width:18%;">Проект / Организация</th>
      <th style="width:25%;">Инструмент</th>
      <th style="width:42%;">Описание</th>
      <th style="width:15%;">Официальный сайт / репозиторий</th>
    </tr>
  </thead>
  <tbody>

    <tr>
      <td rowspan="5"><strong>OWASP Foundation</strong></td>
      <td>OWASP ZAP (Zed Attack Proxy)</td>
      <td>Один из самых популярных open source DAST‑сканеров для web‑приложений и API: перехват и анализ трафика, активное и пассивное сканирование, множество плагинов и профилей под OWASP Top 10.</td>
      <td><a href="https://www.zaproxy.org" target="_blank">zaproxy.org</a></td>
    </tr>
    <tr>
      <td>OWASP Dependency‑Check</td>
      <td>SCA‑инструмент для анализа зависимостей по CVE/NVD и другим источникам: поддерживает Maven/Gradle, npm, NuGet, PyPI и др., умеет работать в CI/CD.</td>
      <td><a href="https://owasp.org/www-project-dependency-check/" target="_blank">Dependency‑Check</a></td>
    </tr>
    <tr>
      <td>OWASP Dependency‑Track</td>
      <td>Платформа для управления SBOM и анализa состава ПО на уровне портфеля: отслеживает уязвимости в компонентах и их влияние на продукты.</td>
      <td><a href="https://dependencytrack.org" target="_blank">dependencytrack.org</a></td>
    </tr>
    <tr>
      <td>OWASP Amass</td>
      <td>Инструмент разведки и картирования поверхностей атак (attack surface mapping), полезен для внешнего AppSec и bug bounty.</td>
      <td><a href="https://owasp.org/www-project-amass/" target="_blank">Amass</a></td>
    </tr>
    <tr>
      <td>OWASP Juice Shop</td>
      <td>Уязвимое web‑приложение для обучения AppSec, CTF и тренировки команд: покрывает множество паттернов уязвимостей и сценариев атак.</td>
      <td><a href="https://owasp.org/www-project-juice-shop/" target="_blank">Juice Shop</a></td>
    </tr>

    <tr>
      <td rowspan="5"><strong>Semgrep (r2c / Semgrep Inc.)</strong></td>
      <td>Semgrep (CLI/Engine)</td>
      <td>Быстрый open source SAST‑движок для 30+ языков: поиск уязвимостей и паттернов в коде по правилам, которые выглядят как сам код. Работает в IDE, pre‑commit и CI/CD.</td>
      <td><a href="https://github.com/semgrep/semgrep" target="_blank">github.com/semgrep/semgrep</a></td>
    </tr>
    <tr>
      <td>Semgrep Rules Registry</td>
      <td>Публичный реестр правил (security, quality, compliance), который можно переиспользовать и адаптировать под свои стандарты secure coding.</td>
      <td><a href="https://semgrep.dev/r" target="_blank">semgrep.dev/r</a></td>
    </tr>
    <tr>
      <td>Semgrep CI</td>
      <td>Готовые конфигурации и обвязка для интеграции Semgrep в GitHub Actions, GitLab CI, CircleCI и прочие пайплайны.</td>
      <td><a href="https://semgrep.dev/docs" target="_blank">docs</a></td>
    </tr>
    <tr>
      <td>Semgrep Supply‑chain (OSS часть)</td>
      <td>Компоненты для анализа зависимостей и цепочки поставок в связке с Semgrep‑платформой (частично open source).</td>
      <td><a href="https://semgrep.dev" target="_blank">semgrep.dev</a></td>
    </tr>
    <tr>
      <td>Semgrep IDE Integrations</td>
      <td>Расширения для VS Code и других IDE, запускающие Semgrep локально и подсвечивающие уязвимости прямо при наборе кода.</td>
      <td><a href="https://marketplace.visualstudio.com/items?itemName=Semgrep.semgrep" target="_blank">VS Code</a></td>
    </tr>

    <tr>
      <td rowspan="5"><strong>Aqua Security (Trivy OSS)</strong></td>
      <td>Trivy</td>
      <td>Универсальный open source‑сканер уязвимостей и misconfig‑ов: контейнеры, Kubernetes, файловые системы, репозитории кода, облака, IaC, секреты и лицензии.</td>
      <td><a href="https://github.com/aquasecurity/trivy" target="_blank">github.com/aquasecurity/trivy</a></td>
    </tr>
    <tr>
      <td>Trivy Operator</td>
      <td>Интеграция Trivy в Kubernetes через оператор: автоматическое сканирование подов, образов и конфигураций, экспорт результатов в CRD.</td>
      <td><a href="https://github.com/aquasecurity/trivy-operator" target="_blank">trivy‑operator</a></td>
    </tr>
    <tr>
      <td>Trivy SBOM</td>
      <td>Функциональность Trivy для генерации SBOM (CycloneDX, SPDX и др.) для образов, репозиториев и артефактов.</td>
      <td><a href="https://aquasec.com/products/trivy/" target="_blank">aquasec.com/trivy</a></td>
    </tr>
    <tr>
      <td>Starboard (deprecated → Trivy Operator)</td>
      <td>Ранний OSS‑проект Aqua для интеграции результатов сканирования в Kubernetes, концептуальный предшественник Trivy Operator.</td>
      <td><a href="https://github.com/aquasecurity/starboard" target="_blank">starboard</a></td>
    </tr>
    <tr>
      <td>tfsec (в экосистеме Aqua)</td>
      <td>Open source‑сканер Terraform на misconfig‑и и нарушения best practices инфраструктурной безопасности.</td>
      <td><a href="https://github.com/aquasecurity/tfsec" target="_blank">tfsec</a></td>
    </tr>

    <tr>
      <td rowspan="5"><strong>Anchore (Syft / Grype)</strong></td>
      <td>Syft</td>
      <td>Open source‑инструмент для генерации SBOM по контейнерным образам, файловым системам и репозиториям. Поддерживает CycloneDX, SPDX и другие форматы.</td>
      <td><a href="https://github.com/anchore/syft" target="_blank">github.com/anchore/syft</a></td>
    </tr>
    <tr>
      <td>Grype</td>
      <td>Сканер уязвимостей, работающий по образам, файловым системам и SBOM (Syft/SPDX/CycloneDX). Хорошо вписывается в CI/CD и GitOps.</td>
      <td><a href="https://github.com/anchore/grype" target="_blank">github.com/anchore/grype</a></td>
    </tr>
    <tr>
      <td>Enterprise Engine (OSS core)</td>
      <td>Коммерческая платформа Anchore использует OSS‑ядра Syft/Grype, которые можно применять отдельно как кирпичики SBOM+Vuln‑аналитики.</td>
      <td><a href="https://anchore.com/opensource/" target="_blank">anchore.com/opensource</a></td>
    </tr>
    <tr>
      <td>Policy Engine (OSS компоненты)</td>
      <td>Компоненты для построения политик по результатам сканирования SBOM и образов, часть стека Anchore.</td>
      <td><a href="https://github.com/anchore" target="_blank">github.com/anchore</a></td>
    </tr>
    <tr>
      <td>Примеры интеграций CI/CD</td>
      <td>Готовые шаблоны GitHub Actions, GitLab CI и др. для запуска Syft/Grype в конвейерах.</td>
      <td><a href="https://anchore.com" target="_blank">anchore.com</a></td>
    </tr>

    <tr>
      <td rowspan="5"><strong>GitLab (Community)</strong></td>
      <td>GitLab SAST Templates</td>
      <td>Набор open source‑шаблонов для включения SAST‑сканирования (на базе сторонних OSS‑инструментов) в GitLab CI в открытых и частных проектах.</td>
      <td><a href="https://docs.gitlab.com/ee/user/application_security/sast/" target="_blank">GitLab SAST</a></td>
    </tr>
    <tr>
      <td>GitLab Dependency Scanning</td>
      <td>Шаблоны и конфигурации для анализа зависимостей (SCA) с использованием OSS‑сканеров, автоматические отчёты в Merge Request и pipeline.</td>
      <td><a href="https://docs.gitlab.com/ee/user/application_security/dependency_scanning/" target="_blank">Dep Scanning</a></td>
    </tr>
    <tr>
      <td>GitLab Secret Detection</td>
      <td>Open source‑правила и обвязка для поиска секретов (ключи, токены, пароли) в репозиториях и истории коммитов.</td>
      <td><a href="https://docs.gitlab.com/ee/user/application_security/secret_detection/" target="_blank">Secret Detection</a></td>
    </tr>
    <tr>
      <td>GitLab Container Scanning</td>
      <td>Интеграция OSS‑сканеров образов (Trivy/Clair и др.) в GitLab CI с отчётами по уязвимостям в контейнерах.</td>
      <td><a href="https://docs.gitlab.com/ee/user/application_security/container_scanning/" target="_blank">Container</a></td>
    </tr>
    <tr>
      <td>GitLab DAST</td>
      <td>DAST‑шаблоны для сканирования web‑приложений с использованием OSS‑движков, запуск прямо из pipeline.</td>
      <td><a href="https://docs.gitlab.com/ee/user/application_security/dast/" target="_blank">DAST</a></td>
    </tr>

    <tr>
      <td rowspan="5"><strong>Прочие Open Source проекты</strong></td>
      <td>Bandit (Python)</td>
      <td>Специализированный SAST‑сканер для Python‑кода: находит типовые security‑антипаттерны, небезопасные вызовы и плохие практики.</td>
      <td><a href="https://github.com/PyCQA/bandit" target="_blank">github.com/PyCQA/bandit</a></td>
    </tr>
    <tr>
      <td>Gitleaks</td>
      <td>Инструмент для поиска секретов в Git‑репозиториях и истории коммитов, удобен как pre‑commit‑хук и в CI/CD.</td>
      <td><a href="https://github.com/gitleaks/gitleaks" target="_blank">github.com/gitleaks/gitleaks</a></td>
    </tr>
    <tr>
      <td>OSV‑Scanner</td>
      <td>SCA‑сканер от Google на базе базы Open Source Vulnerabilities (OSV): проверяет зависимости по lock‑файлам и манифестам.</td>
      <td><a href="https://github.com/google/osv-scanner" target="_blank">github.com/google/osv-scanner</a></td>
    </tr>
    <tr>
      <td>kics</td>
      <td>Open source‑сканер IaC (Terraform, Kubernetes, CloudFormation и др.) на misconfig‑и и нарушения best practices.</td>
      <td><a href="https://github.com/Checkmarx/kics" target="_blank">github.com/Checkmarx/kics</a></td>
    </tr>
    <tr>
      <td>CycloneDX (спеки/утилиты)</td>
      <td>Open source‑спецификация SBOM и набор утилит/библиотек для генерации и работы с SBOM в формате CycloneDX на разных языках.</td>
      <td><a href="https://cyclonedx.org" target="_blank">cyclonedx.org</a></td>
    </tr>

  </tbody>
</table>
