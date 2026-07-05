# LuxAed — заборы и ворота в Таллинне

Билингвальный (RU + ET) статический сайт компании LuxAed: заборы, ворота, автоматика и ремонт в Таллинне и Харьюмаа.

## Структура

- `index.html` — главная (RU)
- `uslugi/` — страницы услуг (RU): деревянные заборы, профнастил, 3D-сетка, ворота/автоматика, ремонт
- `o-nas/`, `faq/`, `kontakty/`, `privaatsus/`, `tingimused/` — RU-страницы
- `et/` — эстонская версия (зеркало, `/et/aiad/*`, `/et/varavad/`, `/et/meist/` …)
- `assets/luxaed.css` — общий CSS (дизайн-система на CSS-переменных)
- `img/`, `fonts/` — изображения и шрифты
- `sitemap.xml`, `robots.txt`
- `demo-colors/` — демо цветовых палитр

## Генераторы (Python)

Страницы генерируются из общих шаблонов:

```bash
python3 gen_ru.py          # RU-страницы услуг
python3 gen_ru_support.py  # RU: о нас, faq, контакты, юр.
python3 gen_et_home.py     # ET: главная + все страницы (импортирует gen_et)
python3 gen_demo.py        # демо палитр
```

- `build_pages.py` — общая библиотека (nav, footer, head, hreflang, scripts)
- `reviews_data.py` — отзывы с Facebook

## Локальный запуск

```bash
python3 -m http.server 8127
```

## SEO

hreflang RU↔ET, JSON-LD (HomeAndConstructionBusiness, Service, FAQPage, BreadcrumbList), страницы под ключевые запросы (võrkaed, puitaed, liugvärav, väravaautomaatika и др.).

## Деплой на GitHub Pages (подпапка /luxaed/)

Пути на сайте корневые. Для проекта GitHub Pages (`dennymansa.github.io/luxaed/`) выполняется префикс:

```bash
python3 apply_base.py   # BASE="/luxaed" — добавляет префикс ко всем внутренним путям
```

Для деплоя на собственный домен `luxaed.ee` (корень) — оставить пути без префикса (BASE="").
