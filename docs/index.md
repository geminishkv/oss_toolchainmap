{% set data = load_yaml('main.yaml') %}

{{ generate_html_table(data) }}

Виды лицензий:

* [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0);
* [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html);
* [MIT License](https://opensource.org/license/mit/);
* [BSD 2-Clause "Simplified" License](https://opensource.org/license/bsd-2-clause/);
* [BSD 3-Clause "New" or "Revised" License](https://opensource.org/license/bsd-3-clause/);
* [Boost Software License 1.0](https://www.boost.org/users/license.html);
* [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/);
* [Eclipse Public License 2.0](https://www.eclipse.org/legal/epl-2.0/);
* [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html);
* [GNU General Public License v2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html);
* [GNU Lesser General Public License v2.1](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html);
* [Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/);
* The Unlicense — лицензия, которая свидетельствует об отказе от авторских прав.


# AppSec
## SAST:
### OSS
##### Удаленные инструменты
- clj-holmes
- git-secrets

## RASP

### OSS

- Baiduʼs OpenRASP - https://github.com/baidu/openrasp?utm\_source=cybersectools.com - оставила
##### Удаленные инструменты
- OpenRASP (не найден)
- hdiv (последний релиз 4 года назад) - https://github.com/hdiv/hdiv

## SCA_OSA

### SBOM

#### OSS
##### Удаленные инструменты
- spdx-sbom-generator - закрыт - https://github.com/opensbom-generator/spdx-sbom-generator

## MAST
### OSS
##### Удаленные инструменты
- Cycript - Устарел, не обновлялся 8 лет - https://www.cycript.org/
- QARK - Устарел, не обновлялся 10 лет - https://github.com/linkedin/qark
- SandDroid - Не найден (скорее всего устарел) - http://sanddroid.xjtu.edu.cn/
- dexcalibur - Устарел - https://github.com/FrenchYeti/dexcalibur

## IAST
### PS
##### Удаленные инструментыg
- Checkmarx CxIAST - как отдельное решение, скорее всего, больше не существует

## API 
### OSS
##### Примечания
- 42Crunch - не обновлялся год - https://github.com/42Crunch/apisecurity-tutorial
- API Security Empire  - Год не обновлялся - https://github.com/Cyber-Guy1/API-SecurityEmpire
- Astra - устарел - https://github.com/flipkart-incubator/Astra
- SSL Kill Switch 2 - устарел - https://github.com/nabla-c0d3/ssl-kill-switch2

## DAST
### Whitebox_fuzzing
#### OSS
##### Удаленные инструменты

- OlydDBG - Не найден
- Ghidra (Hydra) - устарел - https://github.com/sslab-gatech/hydra
- DNSpy - Устарел - https://github.com/dnSpy/dnSpy
- go-fuzz - Устарел - https://github.com/dvyukov/go-fuzz
- Jazzer и Jazzer.js - Устарел - https://github.com/CodeIntelligenceTesting/jazzer.js
- jsfuzz - Устарел - https://github.com/fuzzitdev/jsfuzz
- Javafuzz - Устарел -https://github.com/fuzzitdev/javafuzz
- pythonfuzz - Устарел - https://github.com/fuzzitdev/pythonfuzz

##### Примечания
OlydDBG - Не найден

### DAST
##### Удаленные инструменты

- nikto - Устарел - https://github.com/sullo/nikto
- golismero - Устарел - https://github.com/golismero/golismero
- BooFuzz - Устарел - https://github.com/jtpereyda/boofuzz
- w3af - Устарел - https://w3af.org/ - не доступен, https://github.com/andresriancho/w3af?tab=readme-ov-file

## BCA
### PS
##### Удаленные инструменты

- rezilion - Компания закрыта (возможно, теперь является часть продуктов от gitlab)
- Procyon - То, что удалось найти, устарело - https://github.com/mstrobel/procyon?tab=readme-ov-file, https://bitbucket.org/mstrobel/procyon/downloads/ - указали в статье на хабре, но открыть не удалось
### OSS
##### Удаленные инструменты
- JDCore - Устарел - https://github.com/java-decompiler/jd-core
##### Примечания
- BinaryNinja - Частично доступен - https://github.com/Vector35 - репозитории с модулями платформы, https://binary.ninja/ - платформа 

## Attack_Surface_Analysis
##### Примечания

- polytracker - релиз был в 2022 году, но есть изменения в проекте поновее - https://github.com/trailofbits/polytracker

# ASPM
### PS
#### Примечания
- Reliability - инструмент не найден
- Ponce" - не нашла

# Дополнение
Данные о лицензиях PS инструментов не всегда указаны на сайте, чтобы получить информацию о предложении вендора, надо подать заявку, поэтому у некоторых инструментов эта графа пустует.  
По недоступным инструментам указана ссылка и заполнена графа доступности.  
Заполненные инструменты:
IAST, MAST, RASP, SAST, SCA_OSA, DAST, BCA, ASPM, codecoverage, Attack_surface_analysis