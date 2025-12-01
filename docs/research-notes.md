---
search:
  exclude: true
---

<br>Салют,</br>
Карта дает возможность выбрать выгодные для себя инструменты под все необходимые ситуации: когда нет денег, когда не можем интегрировать большой инструмент, когда никого нет и приходится делать все одному и тд.

Отмечу основные моменты:

* Карта инструментов показывает какие есть классы и типы инструментов
* Карта является прототипом и находится на стадии доработки
* Предыдущая версия карты находится [тут](https://storage.yandexcloud.net/aft-tilda/%D0%9A%D0%B0%D1%80%D1%82%D0%B0%20%D0%B8%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2%20DevSecOps.pdf)
* Агрегируются 'meta' данные о наличии сертификации, типе лицензии ПО, может ли быть импортозамещено, какой язык программирования, какие виды отчетов и иное
* вся верстка натянута на 'material'
* Мы принимаем 'pull requeste' на изменения для того, что бы эта карта шарилась и мы могли работать в едином поле с комьюнити
* Имеется фильтрация по 'meta' данным
* Убрали некоторые инструменты, которые не поддерживаются или пользуются меньшей популярностью, вследствие чего они не обновляются
* Актуализировали списки инструментов, на сейчас готовятся правки по ткстам и добавление материалов описания

***

<div align="center"><h2>Stay tuned ;)</h2></div> 

***

<div id="tools-table-wrapper" style="display:none;">
  {{ tools_table() }}
</div>

<button type="button" data-tools-overlay-trigger class="tools-overlay__trigger">
  <h4>Развернуть карту инструментов</h4>
</button>

<div data-tools-overlay class="tools-overlay">
  <div class="tools-overlay__backdrop"></div>
  <div class="tools-overlay__dialog">
    <button type="button" class="tools-overlay__close">×</button>
    <div id="tools-table-container" class="tools-overlay__table"></div>
  </div>
</div>

***

# Поиск по карте

<div id="tools-search">
  <input
    type="search"
    id="tools-search-input"
    placeholder="Свободный поиск"
  />
  <ul id="tools-search-results"></ul>
</div>