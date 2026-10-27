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

- `service_catalog.py` — единая обязательная матрица 9 услуг × ET/RU/EN
- `service_layout.py` — общий layout и schema всех сервисных страниц
- `guide_pages.py` — страницы цен, выбора забора и зоны обслуживания Harjumaa на ET/RU/EN
- `intercom_service.py` — общий ET/RU/EN-контент для домофонов, видеодомофонов и управления калиткой
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

- На 28.09.2026: 96 URL, 32 группы ET/RU/EN. Карта URL находится в `build_pages.py`.
- Контент статей: `article_content.py`, `articles_data/`; генератор: `articles.py`.
- Проблемные страницы ремонта: `problem_content.py`, `problem_pages.py`.
- `seo_lastmod.py` и `seo_page_state.json` сохраняют индивидуальные даты содержательных изменений. Не удалять state и не ставить всем страницам текущую дату при каждом деплое.
- `gen_sitemap.py` запускается после `apply_base.py`, затем `validate_site.py`.
- Проверка дат: `python3 -m unittest test_seo_lastmod`.
- Публикация sitemap и отправка в Search Console не означают немедленную индексацию. Подтверждение индексации получать через URL Inspection, не из устаревшего поля `contents.indexed` Sitemaps API.

## Production: Vercel

Актуальная рабочая копия: `/Users/dennymansa/luxaed`. Старые копии на Desktop и в `Developer/luxaed-deploy` не использовать для публикации. В рабочей копии много пользовательских изменений, которые ещё не закоммичены; не сбрасывать их и не публиковать старый git HEAD.

Публичный сайт: https://luxaed.ee. Vercel project: `luxaed`, project ID `prj_9HlhqCLHSpzQdFxBUjHoWZbZO2p6`. Настройки привязки находятся в `.vercel/project.json`. Это не GitHub Pages; `BASE` в `apply_base.py` должен оставаться пустым.

```bash
cd /Users/dennymansa/luxaed
python3 build_site.py
python3 -m unittest test_seo_lastmod
vercel deploy --prod --yes
```

Публиковать только по запросу пользователя. Перед деплоем проверить `.vercelignore`: ключи `gcs-*.json`, `.env*`, внутренние отчёты, Python-исходники и `seo_page_state.json` не должны быть доступны с сайта. После публикации проверить живые страницы, sitemap и мобильные действия. Не отправлять настоящие тестовые заявки без отдельного согласования.
