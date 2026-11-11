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

Для обновления услуги «Бетонные работы» используйте точечную сборку (Python 3.12+):

```bash
python3 gen_concrete.py
python3 gen_sitemap.py
python3 validate_site.py
python3 -m unittest test_concrete_preservation test_seo_lastmod
node test_concrete_lead.mjs
```

Она сохраняет опубликованное содержимое других страниц и добавляет только ссылки на новую услугу. Проверка `test_concrete_preservation` сравнивает существующие HTML и ресурсы с production-коммитом `b4f86b02c1d0b42c2658f23451c3d42e09158e37` от 11.11.2026. Это исходная версия релиза, а не дата создания коммита.

Для статьи «10 советов по бетонным работам» используйте `python3 gen_concrete_guide.py`, затем те же проверки и `gen_sitemap.py`. Генератор обновляет три версии статьи, добавляет по одному блоку со ссылкой в три раздела советов и три страницы бетонных работ, дополняет `llms.txt`. Регрессионная проверка отдельно сравнивает остальные страницы и все прежние медиа с релизом `14d332d9f62a9a8fe01561046c0a4974753ec2b8`.

Полная сборка ниже на 11.11.2026 расходится с опубликованными страницами (в том числе цены и тексты). Не публикуйте её результат без отдельного согласования этих расхождений:

```bash
python3 build_site.py
```

- `service_catalog.py` — единая обязательная матрица 10 услуг × ET/RU/EN
- `concrete_service.py`, `gen_concrete.py` — бетонные работы на ET/RU/EN и точечная сборка
- `concrete_guide_content.py`, `concrete_guide_page.py`, `gen_concrete_guide.py` — статья о бетонных работах на ET/RU/EN, оформление и точечная сборка
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

- На 11.11.2026: 102 URL, 34 группы ET/RU/EN. Карта URL находится в `build_pages.py`.
- Контент статей: `article_content.py`, `articles_data/`; генератор: `articles.py`.
- Проблемные страницы ремонта: `problem_content.py`, `problem_pages.py`.
- `seo_lastmod.py` и `seo_page_state.json` сохраняют индивидуальные даты содержательных изменений. Не удалять state и не ставить всем страницам текущую дату при каждом деплое.
- `gen_sitemap.py` запускается после `apply_base.py`, затем `validate_site.py`.
- Проверка дат: `python3 -m unittest test_seo_lastmod`.
- Публикация sitemap и отправка в Search Console не означают немедленную индексацию. Подтверждение индексации получать через URL Inspection, не из устаревшего поля `contents.indexed` Sitemaps API.

## Production: Vercel

На 11.11.2026 актуальная рабочая копия: `/Users/printer/Documents/ChatGPT/gravityone/luxaed`, GitHub `dennymansa/luxaed`. Перед изменением проверить чистоту рабочей копии и актуальный production-коммит. Старые копии на Desktop и в `Developer/luxaed-deploy` не использовать для публикации; не сбрасывать пользовательские изменения и не публиковать старый git HEAD.

Публичный сайт: https://luxaed.ee. Vercel project: `luxaed`, project ID `prj_9HlhqCLHSpzQdFxBUjHoWZbZO2p6`. Настройки привязки находятся в `.vercel/project.json`. Это не GitHub Pages; `BASE` в `apply_base.py` должен оставаться пустым.

```bash
python3 gen_concrete_guide.py
python3 gen_sitemap.py
python3 validate_site.py
python3 -m unittest test_concrete_preservation test_seo_lastmod
```

Публикация выполняется через GitHub: отдельная ветка, проверка Vercel Preview, затем merge в `main`. Полную сборку не подставлять вместо точечной: см. предупреждение выше.

Публиковать только по запросу пользователя. Перед деплоем проверить `.vercelignore`: ключи `gcs-*.json`, `.env*`, внутренние отчёты, Python-исходники и `seo_page_state.json` не должны быть доступны с сайта. После публикации проверить живые страницы, sitemap и мобильные действия. Не отправлять настоящие тестовые заявки без отдельного согласования.
