title: "AppSec Toolchain Map"

***

## Описание для карты инструментов

<a href="#" class="show-tools-overlay">Развернуть карту инструментов</a>

<div id="tools-overlay" class="tools-overlay">
  <div class="tools-overlay__backdrop"></div>
  <div class="tools-overlay__content">
    <button class="tools-overlay__close" aria-label="Закрыть">✕</button>
    <div class="tools-overlay__table">
      {{ generate_html_table_from_config() }}
    </div>
  </div>
</div>

***

## Поиск описания инструментов

<div id="tools-search">
  <input
    type="search"
    id="tools-search-input"
    placeholder="Свободный поиск"
  />
  <ul id="tools-search-results"></ul>
</div>