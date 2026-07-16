# LuxAed — fences and gates in Tallinn

Трёхъязычный статический сайт LuxAed: заборы, ворота, автоматика и ремонт в Таллинне и Харьюмаа. Эстонский язык находится в корне, русский — в `/ru/`, английский — в `/en/`.

## Структура

- `index.html` — главная ET
- `aiad/`, `varavad/`, `aia-remont/` — услуги ET
- `ru/zabory/`, `ru/vorota-avtomatika/`, `ru/remont-zaborov/` — услуги RU
- `en/fences/`, `en/gates-automation/`, `en/fence-repair/` — услуги EN
- `meist/`, `kkk/`, `privaatsus/`, `tingimused/` и языковые аналоги — вспомогательные страницы
- `assets/luxaed.css` — общий CSS (дизайн-система на CSS-переменных)
- `img/`, `fonts/` — изображения и шрифты
- `sitemap.xml`, `robots.txt`
- `demo-colors/` — демо цветовых палитр

## Генераторы (Python)

Страницы генерируются из общих шаблонов:

Полная сборка:

```bash
python3 build_site.py
```

- `service_catalog.py` — единая обязательная матрица 8 услуг × ET/RU/EN
- `service_layout.py` — общий layout и schema всех сервисных страниц
- `build_pages.py` — общая библиотека (nav, footer, head, hreflang, scripts и карта URL)
- `validate_site.py` — блокирует сборку при расхождении переводов, sitemap, schema, ссылок или redirects
- `reviews_data.py` — отзывы с Facebook
- `ru/index.html` — единственная вручную собранная главная; общие скрипты и видео синхронизирует `sync_ru_home.py`

## Локальный запуск

```bash
python3 -m http.server 8127
```

## SEO

hreflang ET↔RU↔EN, canonical, sitemap и JSON-LD (HomeAndConstructionBusiness, Service, FAQPage, BreadcrumbList, ItemList, VideoObject, Person).

## Деплой на GitHub Pages (подпапка /luxaed/)

Пути на сайте корневые. Для проекта GitHub Pages (`dennymansa.github.io/luxaed/`) выполняется префикс:

```bash
python3 apply_base.py   # BASE="/luxaed" — добавляет префикс ко всем внутренним путям
```

Для деплоя на собственный домен `luxaed.ee` (корень) — оставить пути без префикса (BASE="").
