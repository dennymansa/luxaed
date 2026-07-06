# Moving24 - мастер-гайд по шаблону (обновлён)

Полное, максимально подробное описание сайта Moving24 как переиспользуемого шаблона лид-ген-сайта. Языковые правила - в `playbooks/`. Правила из реальной сборки - в `LESSONS-FROM-BUILD.md`. Методология под нового клиента - в `NEW-CLIENT-PLAYBOOK.md`. Подпись писем - `email-signature.html`.

## Содержание
1. Обзор, архитектура, сборка и деплой
2. Веб-форма заявки
3. Письмо-заявка (lead.php) целиком
4. Интеграция Google Maps (карта, расстояние, Street View)
5. Трекинг и Google Ads
6. Как устроены переводы
7. Как редактировать под клиента + темизация
8. Инвентарь: все страницы и все картинки
9. Анатомия страниц, структура и SEO
10. Миграция со старого сайта + производительность

---

# 1. Обзор, архитектура, сборка и деплой

## 1.1. Бизнес-модель: локальный лид-ген

Moving24 - это сайт-шаблон для **локального лид-ген-бизнеса** (в оригинале переездная компания в Таллине, но модель универсальна: сантехника, клининг, эвакуатор, ремонт, вывоз мусора, любой местный сервис с телефоном и заявками).

Воронка предельно простая и не требует сложного бэкенда:

```
Органика (SEO) + платный трафик (Google Ads)
        |
        v
   Посадочная страница (доверие: отзывы, рейтинг, фикс-цена, 24/7)
        |
        +--> Форма заявки  --> lead.php --> письмо на почту владельцу
        +--> Клик по телефону (tel:) --> прямой звонок
        |
        v
   Заявка/звонок -> менеджер перезванивает -> сделка
```

Ключевые принципы, которые надо перенести на новый бизнес:
- **Каждая страница = точка входа с трафика.** Поэтому у каждой (`index.html` в своей папке) есть свой `<title>`, `meta description`, canonical, hreflang, JSON-LD.
- **Единственная цель страницы - конверсия в контакт.** Две механики: форма (уходит на почту через `lead.php`) и клик по телефону. Никаких корзин, личных кабинетов, оплаты.
- **Доверие важнее дизайна.** В шапке главной (реальный код `staging/index.html`) в JSON-LD зашиты: `"aggregateRating": {"ratingValue": "5.0", "reviewCount": "37"}`, отзывы (`review[]`), телефон `+372 5687 0101`, адрес, часы работы 24/7. Это и рендерится на странице, и отдаётся Google как Rich Results.

## 1.2. Стек: статический HTML с инлайновым CSS/JS, без фреймворка

Сайт - это **чистые статические `.html`-файлы** + один `.php` для приёма формы. Ни React/Vue, ни сборщика (Webpack/Vite), ни `package.json`, ни `node_modules`.

Как устроена каждая страница:
- **HTML, CSS и JS - всё инлайн** в одном `index.html`. Стили в `<style>` внутри `<head>`, скрипты в `<script>` внизу. `staging/index.html` весит ~157 КБ именно потому, что самодостаточен.
- Внешние ресурсы почти отсутствуют: только шрифты (`fonts.css` + `fonts/`) и изображения (`img/`). Никаких CDN.

Почему так (и почему это правильный выбор для лид-ген-шаблона):
1. **Скорость и SEO.** Нет JS-фреймворка -> нет гидрации, нет пустого HTML до исполнения скрипта. Google видит готовый контент, PageSpeed высокий.
2. **Хостится где угодно.** Любой дешёвый шаред-хостинг с Apache и PHP (zone.ee) поднимает сайт без Node, Docker, CI. Заливаешь файлы - работает.
3. **Нулевая цепочка сборки.** Нет «сломался npm install через год». Файл в репозитории = файл на проде, один в один.
4. **Портируемость под новый бизнес.** Чтобы сделать сайт под другой сервис, достаточно скопировать дерево и заменить тексты/картинки/телефон/JSON-LD. Не нужно разбираться в чужом фреймворке.

Единственная динамика на сервере - `lead.php` (принимает POST формы и шлёт письмо через PHPMailer, лежащий рядом в `staging/phpmailer/src/`: `PHPMailer.php`, `SMTP.php`, `Exception.php`). Секреты (SMTP-логин/пароль) - НЕ в этом файле, а в отдельном `config.php`, которого в дереве нет (см. 1.5).

## 1.3. Мультиязычность: эстонский в корне + /ru /en /fi + hreflang

Язык = папка. Эстонский (`et`) - корневой, остальные три вложены:

| URL | Файл на диске | Язык |
|-----|---------------|------|
| `/` | `staging/index.html` | ET (эстонский, мастер) |
| `/ru/` | `staging/ru/index.html` | RU |
| `/en/` | `staging/en/index.html` | EN |
| `/fi/` | `staging/fi/index.html` | FI |

Слаги внутренних страниц тоже локализованы (услуги «переезд для частных лиц»):
- ET: `/teenused/erakolimine/`
- RU: `/ru/uslugi/chastnyj-pereezd/`
- EN: `/en/service/home-move/`
- FI: `/fi/palvelut/...`

Связывает языки между собой блок `hreflang` в `<head>` (реальный код из `staging/index.html`):

```html
<link rel="canonical" href="https://moving24.ee/">
<link rel="alternate" hreflang="et" href="https://moving24.ee/">
<link rel="alternate" hreflang="en" href="https://moving24.ee/en/">
<link rel="alternate" hreflang="ru" href="https://moving24.ee/ru/">
<link rel="alternate" hreflang="fi" href="https://moving24.ee/fi/">
<link rel="alternate" hreflang="x-default" href="https://moving24.ee/">
```

Правило (проверяется автоматически, см. `validate.py` п.6): если на странице вообще есть hreflang, то набор обязан быть полным - `{et, en, ru, fi, x-default}`, иначе сборка падает. `x-default` указывает на корень (ET). Canonical всегда абсолютный и всегда на `https://moving24.ee/` (проверяется, п.7).

Под новый бизнес языки настраиваются под рынок: убираете лишние, добавляете свои, но набор в hreflang и в валидаторе должен совпадать.

## 1.4. Полная карта дерева `staging/`

`staging/` - это то, что ляжет на прод один в один (за вычетом мусора и секретов, см. 1.5). Корень проекта `/Users/dennymansa/Desktop/moving24/` содержит генераторы и служебное; выкладывается только `staging/`.

```
staging/
├── index.html                 # ET home (мастер-шаблон, ~157 КБ, весь CSS/JS инлайн)
├── 404.html                   # страница ошибки (ErrorDocument в .htaccess)
├── .htaccess                  # Apache-конфиг для zone.ee (редиректы, заголовки, кэш) - см. 1.6
├── robots.txt                 # Allow: / + ссылка на sitemap
├── sitemap.xml                # только индексируемые страницы (legal исключены)
├── llms.txt                   # краткая карта сайта для AI-краулеров (контакты, языки)
├── lead.php                   # приём POST формы -> письмо (использует phpmailer/)
├── fonts.css                  # @font-face
├── fonts/                     # .woff2 шрифты
├── img/                       # все картинки (.jpg + .webp пары, видео .mp4)
│   ├── pack/  partners/       # тематические подпапки
│   └── ...                    # m24-gal*.jpg (галерея), g-*.webp, og.jpg, m24-logo.png
├── phpmailer/src/             # PHPMailer.php, SMTP.php, Exception.php (вендор для lead.php)
│
│   # --- ET (корень) внутренние страницы ---
├── teenused/                  # услуги (ET)
│   ├── erakolimine/index.html         # частный переезд
│   ├── arikolimine/index.html         # бизнес-переезд
│   ├── suuregabariidiline/index.html  # крупногабарит
│   └── prugivedu/index.html           # вывоз мусора
├── meist/index.html           # о нас (ET)
├── kkk/index.html             # FAQ (ET)
├── privaatsus/index.html      # приватность (ET, noindex)
├── tingimused/index.html      # условия (ET, noindex)
│
│   # --- RU ---
├── ru/index.html
│   ├── uslugi/  (chastnyj-pereezd, biznes-pereezd, krupnogabaritnyj, prugivedu…)
│   ├── o-nas/  faq/  privaatsus/  tingimused/
│
│   # --- EN ---
├── en/index.html
│   ├── service/  (home-move, business-move, oversized, junk-removal)
│   ├── about/  faq/  privacy/  terms/
│
│   # --- FI ---
├── fi/index.html
│   ├── palvelut/  meista/  ukk/  tietosuoja/  kayttoehdot/
│
├── turg/index.html            # внутренний дашборд по рынку (НЕ индексируется, без GTM)
│
│   # --- служебное, НЕ уходит в прод (исключается билдером) ---
├── _incoming/  _ai/  .claude/  build.txt  .nojekyll  .DS_Store
```

Каждая страница - это `index.html` в своей папке, чтобы URL был «чистым» (`/meist/`, а не `/meist.html`).

Пара `.jpg` + `.webp` для каждой картинки - это прогрессивная отдача: современным браузерам через `<picture>`/`srcset` идёт лёгкий webp, старым - jpg-фолбэк.

Важное исключение: `turg/` (маркетинговый дашборд по рынку) намеренно без GTM и без индексации - это внутренний документ. В валидаторе он занесён в белый список `UNTRACKED_OK = {'turg/index.html'}`.

## 1.5. `validate.py` - жёсткие инварианты перед сборкой

Файл: `/Users/dennymansa/Desktop/moving24/validate.py`. Запускается **перед каждым zip/деплоем**. Код возврата 0 = можно выкладывать; ненулевой = найдено критичное нарушение, сборка запрещена. Проверяет он не корень, а `ROOT = Path(__file__).parent / 'staging'`.

**Жёсткие ошибки (блокируют сборку):**

1. **Битые внутренние ссылки/ресурсы.** Регэкспами собирает все `href/src/poster`, `srcset`, CSS `url(...)`, резолвит относительные и абсолютные пути и проверяет, что файл реально существует на диске. Внешние (`http`, `//`, `mailto:`, `tel:`, `data:`, `#`) пропускаются.
2. **Невалидный JSON-LD.** Каждый `<script type="application/ld+json">` парсится `json.loads`; кривой JSON -> фейл. (Критично, потому что на JSON-LD держатся Rich Results.)
3. **Длинные тире.** Ищет `-` (U+2014), `-` (U+2013) и ещё три вида. Это правило владельца - только дефис `-`. Любое длинное тире в любом HTML валит сборку.
4. **Отсутствие GTM-контейнера** (`GTM-TSG2CVLC`) на любой отслеживаемой странице. Исключение - только `turg/index.html`.
5. **Нет `<title>` или `meta description`** на странице.
6. **Неполный hreflang.** Если hreflang есть, набор обязан быть ровно `{et, en, ru, fi, x-default}`.
7. **Canonical на чужой хост** (не начинается с `https://moving24.ee/`).
8. **Sitemap.** `sitemap.xml` должен парситься, и каждый `<loc>` обязан соответствовать реально существующей странице на диске.
9. **Оставшиеся плейсхолдеры** вида `__PLACEHOLDER__` (`__[A-Z0-9_]{3,}__`).
10. **`config.php` внутри `staging/`** - секреты не должны попасть в выкладываемое дерево. Наличие файла = фейл.

**Предупреждения (печатаются, но не блокируют):**
- `<!-- TODO`-комментарии в HTML.
- Дубли `<title>` между страницами.
- Активный временный оверлей `id="gal-numbers"` (нумерация фото; надо убрать перед продом).

Вывод в конце: `validate: N pages checked`, список warnings/failures, и либо `OK: all hard invariants hold.`, либо `sys.exit(1)`.

## 1.6. `build_zip.py` - единственный способ собрать артефакт

Файл: `/Users/dennymansa/Desktop/moving24/build_zip.py`. Запуск: `python3 build_zip.py`. Делает три шага и отказывается собирать битое дерево.

**Шаг 1/3 - validate.** Запускает `validate.py` как подпроцесс. Если код возврата не 0 - `BUILD ABORTED`, выход. То есть невозможно собрать zip, минуя проверки.

**Шаг 2/3 - zip.** Удаляет старый `moving24-staging.zip`, детерминированно (по отсортированному `rglob('*')`) кладёт всё дерево `staging/`. Что **исключается**:

```python
EXCLUDE_NAMES = {'.DS_Store', 'config.php', 'build.txt', '.nojekyll'}
EXCLUDE_DIRS  = {'_incoming', '_logotest', '.claude', '_ai', '.git'}
```

То есть в архив НЕ попадают: OS-мусор (`.DS_Store`), **секреты (`config.php`)**, служебная метка сборки (`build.txt`), GitHub-Pages-маркер (`.nojekyll`), а также целые dev-папки (черновики `_incoming`, ассеты ИИ `_ai`, состояние тулинга `.claude`, git). Пути в архиве - относительно `staging/`, поэтому корнем zip сразу становится `index.html` (без обёртки `staging/`).

**Шаг 3/3 - verify.** Проверяет уже собранный архив:
- нигде нет `config.php` (страховка на случай, если бы утёк);
- `lead.php` присутствует ровно один раз и именно в корне (`lead == ['lead.php']`);
- в корне есть `index.html` и `sitemap.xml`;
- присутствуют `ru/index.html`, `en/index.html`, `fi/index.html`, `.htaccess`.

Если что-то не так - **артефакт удаляется** (`OUT.unlink()`), выход с ошибкой. Иначе печатает `zip verified` и `READY TO UPLOAD`.

Итог: гарантированно валидный, без секретов, со всеми языками архив.

## 1.7. Деплой на zone.ee (шаред-хостинг, Apache + PHP)

Прод-хостинг - zone.ee. Модель деплоя - **полная замена содержимого через zip**, без git на сервере:

1. **Собрать артефакт:** `python3 build_zip.py` -> получаем `moving24-staging.zip` (проверенный).
2. **Зайти в файловый менеджер zone.ee** (или по FTP/SFTP), открыть корень сайта `htdocs/`.
3. **Wipe htdocs.** Полностью очистить `htdocs/` (удалить старую версию). Это самый чистый способ - нет «осиротевших» файлов от предыдущего билда.
4. **Распаковать zip прямо в `htdocs/`.** Поскольку в архиве корнем идёт `index.html`, после распаковки сайт сразу лежит правильно (`htdocs/index.html`, `htdocs/ru/…`, `htdocs/.htaccess` и т.д.).
5. **Положить `config.php` вручную** в место, откуда его читает `lead.php` (не в git, не в zip - только руками на сервере). Это единственный файл с секретами (SMTP-креды для отправки писем формы). Отсутствует в дереве по дизайну и защищён `.gitignore` (`**/config.php`, `api/config.php`).

Форма работает так: браузер POST-ит в `lead.php`, тот через PHPMailer (`staging/phpmailer/src/`) и креды из `config.php` шлёт письмо владельцу.

## 1.8. Prod-версия `.htaccess` - снять noindex

`.htaccess` (`staging/.htaccess`) - Apache-конфиг только для zone.ee (на любом статик-хостинге без Apache он игнорируется). В нём:
- `ErrorDocument 404 /404.html`;
- **301-редиректы** со старых WordPress-URL на новые слаги (сохранение SEO из GSC), для всех языков;
- security-заголовки (`X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, задел под HSTS);
- gzip-компрессия и годовой кэш статики (webp/jpg/png/woff2), а для HTML - `access plus 0 seconds`.

**Критично при выкатке на боевой домен.** В staging-версии стоит строка, полностью запрещающая индексацию:

```apache
# !!! STAGING ONLY - REMOVE THIS LINE AT moving24.ee CUTOVER (blocks ALL indexing, PSI SEO=69 is caused by this) !!!
Header always set X-Robots-Tag "noindex, nofollow"
```

Пока сайт на стейджинге - эта строка защищает от преждевременной индексации черновика. **При переезде на боевой `moving24.ee` её надо удалить**, иначе Google не проиндексирует прод (и SEO-скор в PageSpeed проседает именно из-за неё). Это и есть главная разница staging vs prod: прод-`.htaccess` идентичен, но БЕЗ строки `X-Robots-Tag "noindex, nofollow"`.

Дополнительно при cutover: в `robots.txt` строку `Sitemap:` держать на `https://moving24.ee/sitemap.xml` (уже так), и убедиться, что абсолютные пути указывают на боевой домен.

---

Ключевые файлы для этой секции (абсолютные пути):
- `/Users/dennymansa/Desktop/moving24/validate.py` - инварианты
- `/Users/dennymansa/Desktop/moving24/build_zip.py` - сборщик zip
- `/Users/dennymansa/Desktop/moving24/staging/.htaccess` - Apache-конфиг (noindex снять на проде)
- `/Users/dennymansa/Desktop/moving24/staging/index.html` - мастер-шаблон ET home (`<head>` с canonical/hreflang/JSON-LD)
- `/Users/dennymansa/Desktop/moving24/staging/lead.php` + `/Users/dennymansa/Desktop/moving24/staging/phpmailer/src/` - приём формы
- `/Users/dennymansa/Desktop/moving24/.gitignore` - защита `config.php` от коммита

Примечание: в корне проекта также есть старый пайплайн через папку `deploy/` (GitHub Pages), описанный в `OPERATIONS.md`. Актуальный источник правды и способ выкладки - это `staging/` + `build_zip.py` -> zip -> zone.ee, задокументированный выше.


---

# 2. Веб-форма заявки (на сайте)

Это главный конвертер сайта - «умная» форма в hero-блоке, которая раскрывается по клику на нужную услугу и показывает только релевантные поля. Весь код (разметка + CSS + JS) лежит в одном файле `/Users/dennymansa/Desktop/moving24/staging/index.html`. Внешних зависимостей нет - чистый ванильный JS, всё работает без сборки.

## 2.1. Что видит пользователь (логика в двух словах)

1. Сверху заголовок формы и 4 чипа-услуги (`Kodukolimine / Ärikolimine / Utiliseerimine / Rasked esemed`).
2. Всегда видны 3 обязательных поля: имя/компания, e-mail, телефон, и одно необязательное «Kust?» (откуда).
3. Пользователь кликает чип услуги - форма плавно «раскрывается», и появляются ТОЛЬКО те поля, которые нужны для этой услуги (этаж, лифт, куда, дата/время, упаковка, фото и т.д.).
4. Клик по кнопке отправки - фото сжимаются прямо в браузере, всё уходит POST-ом на бэкенд с человекочитаемыми подписями полей на языке страницы.

Итог: короткая форма, которая не пугает длиной, но собирает детальный бриф под конкретную услугу.

## 2.2. Разметка `#leadForm` (что где лежит)

Форма находится внутри hero-блока: `.form-slot > .form-card#form > form#leadForm`. Обёртка `.form-slot` нужна, чтобы при раскрытии на десктопе карточка «наезжала» поверх сетки (position:absolute), а не расталкивала соседние блоки - об этом ниже.

Ключевые узлы (index.html, начиная с строки 1250):

```html
<div class="form-card" id="form">
  <span class="form-tag">Esita päring</span>
  <h2>Valige teenus</h2>
  <form id="leadForm">
    <button type="button" class="form-close" id="formClose" ... style="display:none">&times;</button>
    <!-- скрытые технические поля -->
    <input type="hidden" name="service" id="serviceField">
    <input type="hidden" name="utm_source" ...><input type="hidden" name="gclid" ...>
    <!-- honeypot -->
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true"
           style="position:absolute;left:0;top:0;width:1px;height:1px;opacity:0;...">
    <!-- чипы услуг -->
    <div class="chips" id="svcChips" role="radiogroup"> ... 4 кнопки ... </div>
    <!-- всегда видимые обязательные поля -->
    <div class="form-grid">
      <input type="text"  name="name"  required ...>
      <input type="email" name="email" required ...>
      <input type="tel"   name="phone" required ...>
    </div>
    <div class="ff-base"><label>Kust?</label><input name="from_address" ...></div>
    <!-- условные поля (скрыты) -->
    <div style="display:none" class="ff ..." data-svc="private,business,garbage"> ... </div>
    ...
  </form>
</div>
```

Три «слоя» полей:
- `.form-grid` - имя/email/телефон, всегда видимы, `required`.
- `.ff-base` - «Kust?» (адрес откуда), всегда видим, не обязателен.
- `.ff` с `data-svc="..."` и `style="display:none"` - условные поля, показываются JS-ом по выбранной услуге.

## 2.3. Чипы услуг -> показ полей по услуге

### Чипы (svcChips)

Каждый чип - это `<button type="button" class="chip" data-svc="КОД_УСЛУГИ">`. Коды услуг - машинные ключи: `private`, `business`, `garbage`, `transport`. Именно они связывают чип с условными полями.

```html
<button type="button" class="chip" data-svc="private">...Kodukolimine<span class="chip-tick">✓</span></button>
<button type="button" class="chip" data-svc="business">...Ärikolimine...</button>
<button type="button" class="chip" data-svc="garbage">...Utiliseerimine...</button>
<button type="button" class="chip" data-svc="transport">...Rasked esemed...</button>
```

`role="radiogroup"` на контейнере и `role="radio"` на чипах (навешивается JS-ом) - это радиогруппа: выбрать можно только одну услугу.

### Привязка полей к услугам через `data-svc`

Каждое условное поле помечено атрибутом `data-svc` со списком услуг (через запятую), для которых оно нужно. Примеры реальных полей:

| Поле (name) | data-svc | Для каких услуг видно |
|---|---|---|
| `from_floor` + `from_lift` (этаж/лифт откуда) | `private,business,garbage` | дом, бизнес, вывоз |
| `to_address` (куда) | `private,business,transport` | дом, бизнес, перевозка |
| `to_floor` + `to_lift` (этаж/лифт куда) | `private,business` | дом, бизнес |
| `date` + `time` (дата/время) | `private,business,garbage,transport` | все 4 |
| `packing` (упаковка от нас) | `private,business` | дом, бизнес |
| `msg` (доп. инфо) | `private,business,garbage,transport` | все 4 |
| `photos` (фото) | `private,business,garbage` | дом, бизнес, вывоз |

То есть один и тот же список полей комбинируется по-разному под каждую услугу - логика полностью декларативная, вся «карта видимости» задаётся в HTML через `data-svc`, а не в JS.

### JS: `showGroups` / `select` / `apply`

Вся механика раскрытия - в самозапускающейся функции (index.html, строки 1835-1879).

`showGroups(v)` - показывает/прячет условные поля под услугу `v`:

```js
function showGroups(v){
  document.querySelectorAll('#leadForm .ff').forEach(function(g){
    var ok = v && ((g.getAttribute('data-svc')||'').split(',').indexOf(v) > -1);
    g.style.display = ok ? '' : 'none';
    g.querySelectorAll('input,select,textarea').forEach(function(el){ el.disabled = !ok; });
  });
  if(closeBtn) closeBtn.style.display = v ? '' : 'none';
}
```

Важная деталь: скрытые поля не просто прячутся (`display:none`), но и получают `disabled=true`. Это гарантирует, что скрытое поле не попадёт в отправку (`FormData` игнорирует disabled-поля) - даже если в нём случайно осталось значение от прошлого выбора.

`select(v, btn)` - обработчик клика по чипу: подсвечивает выбранный чип (`.on`, `aria-checked`), пишет код услуги в скрытое `#serviceField` и зовёт `apply(v)`:

```js
function select(v,btn){
  chips.querySelectorAll('.chip').forEach(function(c){
    var on = c === btn;
    c.classList.toggle('on', on);
    c.setAttribute('aria-checked', on ? 'true' : 'false');
  });
  if(hidden) hidden.value = v;   // hidden = #serviceField
  apply(v);
}
```

`apply(v)` - раскрывает карточку и на десктопе (ширина > 760px) превращает её в оверлей поверх сетки, чтобы соседние блоки не «прыгали»:

```js
function apply(v){
  if(card) card.classList.toggle('expanded', !!v);
  resetPos(); showGroups('');
  if(v && slot && card && window.innerWidth > 760){
    var h = card.offsetHeight;
    slot.style.minHeight = h + 'px';           // резервируем место под слот
    card.style.position = 'absolute';          // карточка "наезжает" поверх
    card.style.top='0'; card.style.left='0'; card.style.right='0'; card.style.zIndex='40';
  }
  showGroups(v);
}
```

Кнопка-крестик `#formClose` вызывает `closeForm()` - сбрасывает выбор чипа, чистит `#serviceField` и сворачивает форму обратно (`window.m24CloseForm` тоже вызывается после успешной отправки, чтобы форма схлопнулась).

Тумблеры «Lift?» / «Kas soovite pakkimisteenust?» (`.lift-toggle`) - это пары кнопок Jah/Ei; клик пишет значение в скрытый `input[type=hidden]` внутри группы (строки 1871-1876).

## 2.4. ПОЧЕМУ условные поля скрыты прямо в HTML через `style="display:none"`

Каждое условное поле в разметке уже имеет инлайновый `style="display:none"`:

```html
<div style="display:none" class="ff form-grid2" data-svc="private,business,garbage"> ... </div>
```

Казалось бы, это дублирует работу JS (`showGroups('')` в конце инициализации и так всё прячет). Но инлайн-стиль здесь принципиален - он убирает «вспышку» (flash) при загрузке страницы:

- HTML парсится и рисуется браузером ДО того, как отработает `<script>` в конце страницы.
- Если бы поля прятал только JS, то на долю секунды (пока грузится/выполняется скрипт) пользователь увидел бы длинную развёрнутую форму со всеми полями сразу, а потом она резко «схлопнулась» бы в короткую - визуальный «дребезг».
- Инлайновый `display:none` в самой разметке означает: поля скрыты с первого кадра рендера, ещё до JS. Пользователь всегда видит аккуратную короткую форму, а поля появляются только осознанно - после клика по услуге.

Это стандартный приём против FOUC (flash of unstyled/unhidden content) для форм с условной логикой. При адаптации шаблона: любое новое условное поле обязательно добавляйте с `style="display:none"` в самой разметке, не полагайтесь только на JS.

## 2.5. Заголовок формы: `Valige teenus` (4 языка)

В `index.html` (эстонская версия) заголовок захардкожен как `<h2>Valige teenus</h2>` (строка 1252). Это призыв к действию - «Выберите услугу», прямая подсказка, что первый шаг - клик по чипу, а не заполнение полей.

Сайт четырёхъязычный, и для остальных языковых копий страницы заголовок звучит так:
- ET (эстонский): `Valige teenus`
- RU (русский): `Выбрать услугу`
- EN (английский): `Select a service`
- FI (финский): `Valitse palvelu`

Заголовок статичен в каждой языковой версии файла (не переключается JS-ом) - у каждого языка свой `index.html` со своим текстом. При создании нового языка меняете этот `<h2>` вручную под язык.

## 2.6. Дата «одним кликом»: `type=date` + `showPicker()`

Поле даты (index.html, строка 1272):

```html
<input type="date" name="date"
       onclick="try{this.showPicker()}catch(_){}"
       onfocus="try{this.showPicker()}catch(_){}"
       aria-label="Kuupäev">
```

Нативный `<input type=date>` обычно требует клика именно по маленькой иконке календаря, чтобы открылся выпадающий выбор дат - неудобно на мобильных. Вызов `this.showPicker()` по `onclick`/`onfocus` открывает системный календарь при клике по любому месту поля - выбор даты в один тап. `try/catch` нужен потому, что `showPicker()` поддерживается не всеми браузерами (в старых он просто молча не сработает, поле останется обычным).

Дополнительно:
- Прошлые даты заблокированы: отдельный скрипт (строка 1882) ставит `min` = сегодня, вычисляя дату в локальной таймзоне.
- Иконка календаря нарисована через CSS (блок `<style id="date-fix">`, строка 1169): SVG-фон + скрытие нативной иконки (`::-webkit-calendar-picker-indicator{opacity:0}`), чтобы вид был единым во всех браузерах.

## 2.7. Honeypot `_gotcha` (антиспам без капчи)

Скрытое поле-ловушка для ботов (строка 1256):

```html
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true"
       style="position:absolute;left:0;top:0;width:1px;height:1px;opacity:0;overflow:hidden;pointer-events:none">
```

Живой человек это поле не видит и не заполняет (оно 1x1px, прозрачное, вне табуляции, `aria-hidden`). Боты, которые тупо заполняют все поля формы, впишут туда что-нибудь. При отправке первым делом проверяется honeypot (строки 1919-1921):

```js
var hp = form.querySelector('input[name="_gotcha"]');
if(hp && hp.value){ ok.style.display='block'; return; }
```

Если поле не пустое - боту показывается «успех» (зелёная плашка), но НИЧЕГО не отправляется. Бот думает, что заявка ушла, и уходит; реальная заявка не создаётся, менеджера не спамят. Это дешёвая замена капче - без трения для живых пользователей.

## 2.8. Сжатие фото в браузере: `compressImage`

Клиент может приложить до 8 фото (мебель, груз, объём) - но полноразмерные фото с телефона это 3-8 МБ каждое, они бы грузились медленно и раздували письмо. Поэтому фото сжимаются прямо в браузере через canvas ДО отправки (index.html, строки 1895-1912):

```js
function compressImage(file, maxDim, quality){
  return new Promise(function(resolve){
    if(!/^image\//.test(file.type)){ resolve(file); return; }  // не картинка - как есть
    var img=new Image(), url=URL.createObjectURL(file);
    img.onload=function(){
      var w=img.width, h=img.height, scale=Math.min(1, maxDim/Math.max(w,h));
      var cw=Math.round(w*scale), ch=Math.round(h*scale);
      var cv=document.createElement('canvas'); cv.width=cw; cv.height=ch;
      cv.getContext('2d').drawImage(img,0,0,cw,ch);
      URL.revokeObjectURL(url);
      cv.toBlob(function(blob){
        resolve(blob ? new File([blob], file.name.replace(/\.\w+$/,'')+'.jpg', {type:'image/jpeg'}) : file);
      }, 'image/jpeg', quality||0.8);
    };
    img.onerror=function(){ URL.revokeObjectURL(url); resolve(file); };  // ошибка - шлём оригинал
    img.src=url;
  });
}
```

Что делает:
- Масштабирует картинку так, чтобы бОльшая сторона была максимум `maxDim` px (при отправке вызывается с `1600`), меньшие не увеличивает (`Math.min(1, ...)`).
- Перекодирует в JPEG с качеством `0.8` (при отправке).
- Переименовывает в `.jpg`.
- Устойчиво к сбоям: если файл не картинка или не декодировался - вернёт оригинал, форма не сломается.

Итог - несколько сотен КБ вместо мегабайтов, быстрая отправка даже с мобильного интернета.

Отдельно кусок выбора фото (строки 1884-1892): выбранные файлы копятся в массив `selectedPhotos` (максимум 8, без дублей по имени+размеру), а подпись поля показывает счётчик (`N fotot valitud`). При отправке берётся `selectedPhotos.slice(0,8)` и каждый прогоняется через `compressImage(f, 1600, 0.8)`.

## 2.9. Что уходит POST-ом (локализованные подписи полей)

Собственно отправка - в обработчике `submit` (строки 1948-1963). Логика:

1. Определяется язык страницы: `var L = (document.documentElement.lang||'et').slice(0,2);`
2. Есть два словаря переводов:
   - `LBALL` - подписи полей на 4 языках (ru/et/en/fi). Например `from_floor` -> «Этаж (откуда)» / «Korrus (kust)» / «Floor (from)» / «Kerros (mistä)».
   - `SVCALL` - названия услуг на 4 языках. Например `private` -> «Частный переезд» / «Erakolimine» / «Home move» / «Kotimuutto».
3. Из формы читается «сырой» `FormData` (машинные ключи), и собирается новый `out` c ЧЕЛОВЕКОЧИТАЕМЫМИ подписями на языке страницы:

```js
var LB = LBALL[L]||LBALL.et, SVC = SVCALL[L]||SVCALL.et;
var raw = new FormData(form), out = new FormData();
['service','name','phone','email','from_address','from_floor','from_lift',
 'to_address','to_floor','to_lift','date','time','packing','msg'].forEach(function(k){
  var v = (raw.get(k)||'').toString().trim(); if(!v) return;
  if(k==='service') v = SVC[v]||v;     // код услуги -> человеческое название
  out.append(LB[k]||k, v);             // ключ -> локализованная подпись
});
out.append(LB.page, location.href);    // "Страница" -> URL заявки
```

Почему так: заявка приходит менеджеру (в письмо/CRM) уже с понятными подписями на нужном языке - «Услуга: Частный переезд», «Этаж (откуда): 3», «Лифт (откуда): Jah», а не сырыми `service=private, from_floor=3`. Менеджер читает заявку без расшифровки. Пустые поля не отправляются вообще (`if(!v) return`).

Дальше к отправке добавляются:
- UTM-метки и `gclid` (для сквозной аналитики источника лида) - реальными ключами, не переведёнными (строка 1958):
  ```js
  ['utm_source','utm_medium','utm_campaign','utm_term','utm_content','gclid'].forEach(...)
  ```
- Сжатые фото как `photo1..photoN` (строка 1959).
- `_subject` - готовая тема письма: `Moving24: <услуга> - <имя/телефон>` (строка 1960).

Отправка (строки 1949, 1961):

```js
var endpoint = (window.M24 && M24.FORM_ENDPOINT) || '/lead.php';
...
fetch(endpoint, { method:'POST', body:out, headers:{'Accept':'application/json'} })
  .then(function(r){ done(r.ok, false); });
```

Эндпоинт берётся из глобального конфига `window.M24.FORM_ENDPOINT` (бэкенд-приёмник, см. отдельную секцию про серверную часть - реальные ключи/адреса в `config.php`, в репозиторий не коммитятся). Если эндпоинт не задан - форма уходит в «демо-режим» (строки 1930-1934): показывает «Päringut ei saadetud - helistage ...», ничего не шлёт. Это защита для копий шаблона, где бэкенд ещё не подключён.

После успешного ответа (`done(true)`, строки 1935-1941): показывается зелёная плашка «Aitäh! Päring on vastu võetud», форма очищается и сворачивается, и в `dataLayer` пушится событие `ajaxComplete` - по нему тег в GTM засчитывает конверсию (детали трекинга - в секции про аналитику).

## 2.10. Как менять поля/услуги под клиента

Всё редактируется прямо в `index.html`, без сборки. Три типовые задачи:

### A. Переименовать/заменить услугу
1. В блоке `#svcChips` (строки 1257-1262) поменяйте текст чипа и, при необходимости, машинный код в `data-svc`. Коды - произвольные латиницей (`private/business/...`), но должны совпадать везде.
2. Если поменяли код `data-svc` у чипа - обновите его во ВСЕХ `data-svc` условных полей, в списке ключей отправки (строка 1956) и в словарях `SVCALL`/`LBALL` (строки 1952-1953).
3. Добавьте перевод новой услуги в `SVCALL` для всех 4 языков.

### B. Добавить новое условное поле
1. Скопируйте один из блоков `.ff` и вставьте в форму. Обязательно с `style="display:none"` (против «вспышки», см. 2.4) и с атрибутом `data-svc="список,услуг"`, для которых поле нужно.
2. Дайте полю осмысленный `name` (машинный ключ, латиницей).
3. Добавьте этот ключ в массив ключей отправки (строка 1956) - иначе поле не уйдёт в POST.
4. Добавьте локализованную подпись ключа в словарь `LBALL` для всех 4 языков.
   Пример: новое поле «Кол-во комнат» `name="rooms"` -> в `LBALL`: `ru:{...rooms:'Комнат'...}`, `et:{...rooms:'Tuba'...}` и т.д.

### C. Сделать поле обязательным / сменить набор языков
- Обязательность: добавьте `required` на input (как у name/email/phone в `.form-grid`). Помните: условные поля становятся `disabled` когда скрыты, так что `required` сработает только когда услуга их показывает.
- Языки: словари `LBALL` и `SVCALL` (строки 1952-1953) плюс заголовок `<h2>` (2.5) - точки, где живёт весь текст формы. Определение языка идёт от `<html lang="...">`; если языка нет в словаре, откат на `et` (`LBALL[L]||LBALL.et`).

Главное правило шаблона: связка «чип `data-svc` -> поле `data-svc` -> ключ в массиве отправки -> подпись в `LBALL`» должна быть согласована во всех четырёх местах. Разорвёте цепочку - поле либо не покажется, либо не уйдёт, либо придёт менеджеру с машинным ключом вместо подписи.

---

Все пути и строки указаны для `/Users/dennymansa/Desktop/moving24/staging/index.html` (эстонская версия; остальные языковые копии устроены идентично, отличаются только текстами `<h2>` и содержимым словарей `LBALL`/`SVCALL`).


---

# 3. Письмо-заявка (lead.php) - полностью

`lead.php` - это единственный серверный файл шаблона. Один PHP-скрипт на бекенде: принимает POST от любой формы сайта (на любом из 4 языков), собирает из полей красивое HTML-письмо со схемой переезда, картой, панорамами зданий и вложенными фото, и отправляет его владельцу бизнеса через Gmail SMTP. Фронту он возвращает только JSON-статус (`{"ok":true}` = ушло), чтобы форма показала "спасибо".

Путь: `/Users/dennymansa/Desktop/moving24/staging/lead.php`

Ключевая идея для переиспользования: форма не знает про роли полей - она шлёт человекочитаемые подписи (`Откуда`, `Kust`, `From`, `Mistä`). Скрипт сам сопоставляет любую из этих подписей с внутренней ролью (`from`). Значит одну и ту же `lead.php` можно повесить на страницы всех языков без изменений.

## 3.1. Заголовки, CORS и preflight

Файл сразу объявляет, что ответ - JSON, и открывает CORS (форма может стоять на другом хосте / поддомене):

```php
header('Content-Type: application/json; charset=UTF-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Accept');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST')    { fail(405, 'method'); }
```

- `OPTIONS` - это preflight-запрос браузера перед POST с JSON/файлами. Отвечаем `204 No Content` и выходим.
- Любой метод кроме POST - `405` через хелпер `fail()` (см. 3.16).

## 3.2. Подключение config.php и honeypot

```php
$cfgPath = __DIR__ . '/config.php';
if (!is_file($cfgPath)) { fail(500, 'no-config'); }
$cfg = require $cfgPath;

if (trim((string)($_POST['_gotcha'] ?? '')) !== '') { ok(); }

$values = $_POST;
unset($values['_gotcha'], $values['_subject']);
```

- `config.php` лежит рядом (`__DIR__`), возвращает массив с секретами (структура в 3.17). Если его нет - `500`, письмо не уйдёт, но и секреты никуда не попадут.
- `_gotcha` - honeypot-поле. Оно скрыто в форме от людей; если бот его заполнил - мы вызываем `ok()` (возвращаем `{"ok":true}`, будто всё хорошо), но письмо не шлём. Спам молча отбрасывается.
- `$values` - это все POST-поля, кроме служебных `_gotcha` и `_subject` (тему берём отдельно).

## 3.3. Маппинг локализованных подписей на роли ($ROLE_LABELS)

Сердце "мультиязычности". Каждая роль - массив из подписей на русском, эстонском, английском и финском. Форма прислала `Kust` -> скрипт понял, что это роль `from`.

```php
$ROLE_LABELS = [
  'name'       => ['Имя / компания','Nimi / ettevõte','Name / company','Nimi / yritys'],
  'phone'      => ['Телефон','Telefon','Phone','Puhelin'],
  'email'      => ['Email','E-post','Sähköposti'],
  'service'    => ['Услуга','Teenus','Service','Palvelu'],
  'from'       => ['Откуда','Kust','From','Mistä'],
  'from_floor' => ['Этаж (откуда)','Korrus (kust)','Floor (from)','Kerros (mistä)'],
  'from_lift'  => ['Лифт (откуда)','Lift (kust)','Lift (from)','Hissi (mistä)'],
  'to'         => ['Куда','Kuhu','To','Minne'],
  'to_floor'   => ['Этаж (куда)','Korrus (kuhu)','Floor (to)','Kerros (minne)'],
  'to_lift'    => ['Лифт (куда)','Lift (kuhu)','Lift (to)','Hissi (minne)'],
  'date'       => ['Дата','Kuupäev','Date','Päivä'],
  'time'       => ['Время','Kellaaeg','Time','Aika'],
  'packing'    => ['Упаковка от нас','Pakkimine meilt','Packing by us','Pakkaus meiltä'],
  'msg'        => ['Сообщение','Sõnum','Message','Viesti'],
  'page'       => ['Страница','Leht','Page','Sivu'],
];
```

Как это работает при приёме POST (цикл по всем полям):

```php
$V = [];          // роль => значение
$replyTo = '';
$flat = '';
foreach ($values as $label => $val) {
    $clean = str_replace('_', ' ', $label);
    $v = is_array($val) ? implode(', ', $val) : trim((string)$val);
    $flat .= $v;
    if ($replyTo === '' && $v !== '' && filter_var($v, FILTER_VALIDATE_EMAIL)) { $replyTo = $v; }
    foreach ($ROLE_LABELS as $role => $labs) {
        if (in_array($clean, $labs, true)) { $V[$role] = $v; break; }
    }
}
if (trim($flat) === '') { fail(400, 'empty'); }
```

Разбор по строкам:
- `$clean = str_replace('_', ' ', $label)` - HTML-формы часто присылают `name="Этаж_(откуда)"` (пробелы -> подчёркивания). Возвращаем пробелы, чтобы совпало с подписью в `$ROLE_LABELS`.
- `$v` - значение поля. Если поле-массив (мультивыбор) - склеиваем через запятую.
- `$flat` - накапливает всё подряд; если в итоге пусто (`trim($flat) === ''`) - форма пустая, `400`.
- `$replyTo` - первый валидный email среди значений. Позже он ставится как `Reply-To` письма, чтобы владелец нажал "Ответить" и попал прямо клиенту.
- Внутренний цикл: если очищенная подпись есть в массиве роли - записываем `$V['from'] = 'Таллинн, ...'` и `break`. Итог: `$V` - это нормализованные роли, независимо от языка формы.

## 3.4. Подсчёт фото-вложений

```php
$photoCount = 0;
foreach ($_FILES as $key => $f) {
    if (strpos($key, 'photo') === 0 && !empty($f['tmp_name']) && (int)$f['error'] === 0) { $photoCount++; }
}
```

Любое загруженное файл-поле с именем, начинающимся на `photo` (`photo`, `photo1`, `photo[]`...), без ошибок загрузки - считается фотографией. Число `$photoCount` потом показывается в письме плашкой (см. 3.10). Само прикрепление - позже, при сборке письма (3.14).

## 3.5. Тема письма

```php
$subject = trim((string)($_POST['_subject'] ?? '')) ?: 'Заявка с сайта Moving24';
```

Форма может прислать своё `_subject` (например `Заявка: Квартирный переезд`). Если не прислала - дефолт `Заявка с сайта Moving24`. Тема используется и в `$mail->Subject`, и как подзаголовок в шапке письма.

## 3.6. Расстояние и время через Directions API + полилиния маршрута

```php
$mapCid = ''; $mapPng = ''; $routeInfo = '';
$mapsKey = isset($cfg['maps_key']) ? trim((string)$cfg['maps_key']) : '';
$fromA = trim((string)vv($V,'from')); $toA = trim((string)vv($V,'to'));
if ($mapsKey !== '' && $fromA !== '' && $toA !== '') {
    $poly = '';
    $dj = json_decode(fetchUrl('https://maps.googleapis.com/maps/api/directions/json?units=metric&origin='
        . rawurlencode($fromA) . '&destination=' . rawurlencode($toA) . '&key=' . rawurlencode($mapsKey)), true);
    if (isset($dj['routes'][0])) {
        $poly = isset($dj['routes'][0]['overview_polyline']['points']) ? $dj['routes'][0]['overview_polyline']['points'] : '';
        $leg  = isset($dj['routes'][0]['legs'][0]) ? $dj['routes'][0]['legs'][0] : null;
        if ($leg) {
            $d = isset($leg['distance']['text']) ? $leg['distance']['text'] : '';
            $t = isset($leg['duration']['text']) ? $leg['duration']['text'] : '';
            $routeInfo = trim($d . ($d !== '' && $t !== '' ? '  ·  ~' : '') . $t);
        }
    }
    ...
```

- Всё завёрнуто в условие: нужен ключ Maps (`maps_key` из config) И оба адреса. Нет чего-то - весь блок пропускается (мягкая деградация, см. 3.12), письмо всё равно уйдёт.
- Запрос к Directions API даёт две вещи:
  - `overview_polyline.points` - закодированную полилинию маршрута (`$poly`), её потом рисуем на статической карте.
  - `legs[0].distance.text` и `duration.text` - человекочитаемые "12,3 km" и "18 mins". Склеиваются в `$routeInfo` = `12,3 km  ·  ~18 mins`.

## 3.7. Статическая карта маршрута (Static Maps, path=enc:polyline)

```php
    $murl = 'https://maps.googleapis.com/maps/api/staticmap?size=624x300&scale=2'
        . ($poly !== '' ? '&path=' . rawurlencode('color:0x1d4ed8cc|weight:5|enc:' . $poly) : '')
        . '&markers=' . rawurlencode('color:0x1d4ed8|label:A|' . $fromA)
        . '&markers=' . rawurlencode('color:0x0f9d58|label:B|' . $toA)
        . '&key=' . rawurlencode($mapsKey);
    $png = fetchUrl($murl);
    if ($png !== '' && strncmp($png, "\x89PNG", 4) === 0) { $mapPng = $png; $mapCid = 'routemap'; }
}
```

- Static Maps API рендерит картинку `624x300` при `scale=2` (ретина).
- `path=...enc:$poly` - именно закодированная полилиния из Directions рисуется линией (синяя `0x1d4ed8cc`, толщина 5). Так карта показывает реальный маршрут по дорогам, а не прямую.
- Два маркера: `A` синий на "Откуда", `B` зелёный (`0x0f9d58`) на "Куда".
- Проверка `strncmp($png, "\x89PNG", 4) === 0` - убеждаемся, что скачали настоящий PNG (первые байты сигнатуры PNG), а не JSON-ошибку. Только тогда запоминаем байты (`$mapPng`) и присваиваем CID `routemap` для inline-вставки (см. 3.11 и 3.14).

## 3.8. Street View зданий (метадата-проверка + вставка, source=outdoor)

```php
$svFromPng = ''; $svFromCid = ''; $svToPng = ''; $svToCid = '';
if ($mapsKey !== '') {
    if ($fromA !== '') { list($svFromPng, $svFromCid) = streetView($fromA, $mapsKey, 'svfrom'); }
    if ($toA   !== '') { list($svToPng, $svToCid)     = streetView($toA,   $mapsKey, 'svto'); }
}
```

Сам хелпер (низ файла):

```php
function streetView($addr, $key, $cid) {
    $addr = trim((string)$addr);
    if ($addr === '' || $key === '') { return ['', '']; }
    $meta = json_decode(fetchUrl('https://maps.googleapis.com/maps/api/streetview/metadata?source=outdoor&location=' . rawurlencode($addr) . '&key=' . rawurlencode($key)), true);
    if (!isset($meta['status']) || $meta['status'] !== 'OK') { return ['', '']; }
    $img = fetchUrl('https://maps.googleapis.com/maps/api/streetview?size=560x220&fov=78&source=outdoor&location=' . rawurlencode($addr) . '&key=' . rawurlencode($key));
    if ($img !== '' && (strncmp($img, "\xFF\xD8", 2) === 0 || strncmp($img, "\x89PNG", 4) === 0)) { return [$img, $cid]; }
    return ['', ''];
}
```

Важная деталь - сначала метадата, потом картинка:
- `streetview/metadata` - бесплатный запрос, отвечает `status: OK` только если у Google реально есть панорама этого адреса. Если панорамы нет (`ZERO_RESULTS`) - возвращаем `['', '']` и не тратим платный запрос на "нет фото".
- `source=outdoor` - брать только уличные панорамы (не интерьеры магазинов), чтобы видно было именно здание/подъезд.
- Реальную картинку скачиваем `560x220`, `fov=78` (угол обзора). Проверяем сигнатуру JPEG (`\xFF\xD8`) или PNG - защита от битого ответа.
- CID: `svfrom` для здания "Откуда", `svto` для "Куда". Эти панорамы вставляются прямо в карточки адресов (см. 3.9, функция `addrBlock`).

## 3.9. Сборка HTML: шапка, блок КЛИЕНТ, блок МАРШРУТ

Готовим строки таблиц через хелперы:

```php
$clientRows = row('Имя / компания', vv($V,'name')) . phoneRow('Телефон', vv($V,'phone')) . mailRow('Email', vv($V,'email'));
$detailRows = row('Услуга', vv($V,'service')) . row('Дата', fmtDate(vv($V,'date'))) . row('Время', vv($V,'time'))
            . row('Упаковка от нас', vv($V,'packing'));
$pageUrl = vv($V,'page');
```

Само письмо - таблично-вёрстанный HTML (так надёжнее в почтовиках), выровнен по левому краю. Ключевые части:

Шапка (синяя, с темой как подзаголовком):
```php
  . '<tr><td style="background:#1d4ed8;padding:22px 26px">'
  . '<div style="color:#ffffff;font-size:21px;font-weight:800;letter-spacing:.2px">Moving24 - новая заявка</div>'
  . '<div style="color:#bfd2ff;font-size:13px;margin-top:5px">' . esc($subject) . '</div></td></tr>'
```

Блок КЛИЕНТ и блок МАРШРУТ:
```php
  . sectionTitle('Клиент')
  . '<table role="presentation" cellpadding="0" cellspacing="0" width="100%">' . $clientRows . '</table>'
  . sectionTitle('Маршрут')
  . '<table role="presentation" cellpadding="0" cellspacing="0" width="100%"><tr>'
  . addrBlock('Откуда', vv($V,'from'), vv($V,'from_floor'), vv($V,'from_lift'), '#1d4ed8', $svFromCid)
  . '<td width="36" align="center" valign="middle" style="color:#c2ccd9;font-size:22px;font-weight:700">&rarr;</td>'
  . addrBlock('Куда', vv($V,'to'), vv($V,'to_floor'), vv($V,'to_lift'), '#0f9d58', $svToCid)
  . '</tr></table>'
```

Маршрут - две карточки "Откуда" -> (стрелка `&rarr;`) -> "Куда". `addrBlock` рисует карточку с панорамой (если CID есть), заголовком, адресом и мета-строкой этаж/лифт:

```php
function addrBlock($title, $addr, $floor, $lift, $accent, $svCid = '') {
    $a = ($addr === '') ? '<span style="color:#aab2bf">-</span>' : esc($addr);
    $meta = [];
    if ($floor !== '') { $meta[] = 'Этаж&nbsp;<b style="color:#334155">' . esc($floor) . '</b>'; }
    if ($lift  !== '') { $meta[] = 'Лифт&nbsp;<b style="color:#334155">' . esc($lift) . '</b>'; }
    $metaStr = $meta ? implode('&nbsp;&nbsp;·&nbsp;&nbsp;', $meta) : '';
    return '<td width="50%" valign="top" style="padding:16px 18px;background:#f6f8fb;border:1px solid #e7ecf3;border-radius:12px">'
        . ($svCid !== '' ? '<div style="margin-bottom:11px;border-radius:9px;overflow:hidden;border:1px solid #e2e8f0"><img src="cid:' . $svCid . '" alt="' . esc($title) . '" width="100%" style="display:block;width:100%;height:auto"></div>' : '')
        . '<div style="color:' . $accent . ';font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.6px;margin-bottom:7px">' . esc($title) . '</div>'
        . '<div style="color:#0f172a;font-size:17px;font-weight:800;line-height:1.35">' . $a . '</div>'
        . ($metaStr ? '<div style="color:#64748b;font-size:13px;margin-top:9px">' . $metaStr . '</div>' : '')
        . '</td>';
}
```

Обратите внимание: панорама вставляется как `<img src="cid:svfrom">` - inline через CID, не по URL (см. 3.11).

## 3.10. Расстояние/время, карта, кнопки навигации, детали, фото-плашка

Сразу после карточек маршрута:

```php
  . ($routeInfo !== '' ? '<div style="margin-top:10px;color:#334155;font-size:14px;font-weight:700">&#128662;&nbsp;' . esc($routeInfo) . '</div>' : '')
  . ($mapCid !== '' ? '<div style="margin-top:12px;border-radius:12px;overflow:hidden;border:1px solid #e7ecf3"><img src="cid:' . $mapCid . '" alt="Маршрут" width="624" style="display:block;width:100%;max-width:624px;height:auto"></div>' : '')
  . routeButton(vv($V,'from'), vv($V,'to'))
  . sectionTitle('Детали')
  . '<table role="presentation" cellpadding="0" cellspacing="0" width="100%">' . $detailRows . '</table>'
  . msgBlock(vv($V,'msg'))
  . ($photoCount ? '<div style="margin-top:16px;background:#eef4ff;border:1px solid #d6e4ff;border-radius:10px;padding:12px 16px;color:#1d4ed8;font-size:13px;font-weight:600">&#128206; Фото во вложении: ' . $photoCount . ' шт.</div>' : '')
```

- `$routeInfo` (12,3 km · ~18 mins) - показывается только если получилось. Иконка грузовика `&#128662;`.
- Карта - тоже `<img src="cid:routemap">`, только если `$mapCid` не пуст.
- `routeButton()` - кнопки навигации (см. ниже).
- `msgBlock()` - выделенный блок сообщения клиента (см. 3.13).
- Плашка "Фото во вложении: N шт." - только если `$photoCount > 0`.

Кнопки "Маршрут в Google Maps" и "Waze: Откуда/Куда":

```php
function routeButton($from, $to) {
    $from = trim((string)$from); $to = trim((string)$to);
    $links = '';
    if ($from !== '' && $to !== '') {
        $g = 'https://www.google.com/maps/dir/?api=1&origin=' . rawurlencode($from) . '&destination=' . rawurlencode($to);
        $links .= mapBtn($g, '&#128506;&nbsp;Маршрут в Google Maps &rarr;', '#1d4ed8', '#ffffff');
    }
    if ($from !== '') { $links .= mapBtn('https://waze.com/ul?q=' . rawurlencode($from) . '&navigate=yes', 'Waze: Откуда', '#33ccff', '#062a3a'); }
    if ($to   !== '') { $links .= mapBtn('https://waze.com/ul?q=' . rawurlencode($to)   . '&navigate=yes', 'Waze: Куда',   '#33ccff', '#062a3a'); }
    return $links === '' ? '' : '<div style="margin-top:12px">' . $links . '</div>';
}
```

Владелец на телефоне жмёт кнопку и сразу строит навигацию к клиенту в Google Maps или Waze. `deep-link` формы Waze: `waze.com/ul?q=АДРЕС&navigate=yes`.

## 3.11. Кликабельный телефон (tel:) и email (mailto:)

В блоке КЛИЕНТ телефон и email - не просто текст, а ссылки, чтобы владелец на телефоне звонил в один тап.

Телефон:
```php
function phoneRow($label, $val) {
    if ($val === '') { return row($label, ''); }
    $href = preg_replace('/[^0-9+]/', '', $val);
    $link = '<a href="tel:' . esc($href) . '" style="color:#1d4ed8;font-weight:700;font-size:16px;text-decoration:none">&#128222;&nbsp;' . esc($val) . '</a>';
    return '<tr><td style="padding:6px 0;color:#5b6472;font-size:13px;width:140px;vertical-align:top">' . esc($label) . '</td>'
         . '<td style="padding:6px 0">' . $link . '</td></tr>';
}
```
- `preg_replace('/[^0-9+]/', '', $val)` - для `href="tel:"` оставляем только цифры и `+` (убираем пробелы, скобки, дефисы), иначе часть телефонов не наберётся. При этом показываем оригинал `$val` как есть. Иконка телефона `&#128222;`.

Email:
```php
function mailRow($label, $val) {
    if ($val === '') { return row($label, ''); }
    $link = '<a href="mailto:' . esc($val) . '" style="color:#1d4ed8;font-weight:600;text-decoration:none">' . esc($val) . '</a>';
    ...
}
```
- Обычный `mailto:`. Плюс, этот же email стал `Reply-To` письма (3.3), так что и "Ответить" сработает.

## 3.12. Дата ДД.ММ.ГГГГ + день недели (fmtDate)

Форма шлёт `<input type="date">` в ISO (`2026-07-20`). Владельцу это читать неудобно - переводим в `20.07.2026 (понедельник)`:

```php
function fmtDate($v) {
    $v = trim((string)$v);
    if (preg_match('/^(\d{4})-(\d{2})-(\d{2})$/', $v, $m)) {
        $days = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'];
        $wd = $days[(int)date('w', mktime(0, 0, 0, (int)$m[2], (int)$m[3], (int)$m[1]))];
        return $m[3] . '.' . $m[2] . '.' . $m[1] . ' (' . $wd . ')';
    }
    return $v;
}
```
- Регуляркой ловим строго ISO-формат. `date('w', ...)` даёт номер дня недели 0-6 (0 = воскресенье), берём русское название из массива.
- Если формат не ISO (вдруг ввели текстом) - возвращаем как есть. Используется и в HTML, и в текстовой версии.

## 3.13. Выделенный блок "Сообщение клиента"

```php
function msgBlock($msg) {
    if (trim((string)$msg) === '') { return ''; }
    return sectionTitle('Сообщение клиента')
        . '<div style="background:#fffbeb;border:1px solid #fde68a;border-left:5px solid #f59e0b;border-radius:12px;padding:16px 18px;color:#1f2937;font-size:16px;line-height:1.55;font-weight:600;white-space:pre-wrap">' . nl2br(esc($msg)) . '</div>';
}
```
- Если сообщения нет - блок вообще не рисуется.
- Если есть - жёлтая "заметка" с оранжевой полосой слева, крупнее остального текста, чтобы владелец точно прочитал что клиент написал руками. `white-space:pre-wrap` + `nl2br` сохраняют переносы строк. `esc()` защищает от HTML-инъекций.

## 3.14. Отправка через PHPMailer / Gmail SMTP + вложения + inline-картинки

Текстовая (plain) версия письма для клиентов без HTML:
```php
$alt = "Заявка Moving24\n\nКЛИЕНТ\n  Имя: " . vv($V,'name') . ...
```

Подключение PHPMailer и настройка SMTP:
```php
require __DIR__ . '/phpmailer/src/Exception.php';
require __DIR__ . '/phpmailer/src/PHPMailer.php';
require __DIR__ . '/phpmailer/src/SMTP.php';
$mail = new PHPMailer\PHPMailer\PHPMailer(true);
try {
    $mail->isSMTP();
    $mail->Host = 'smtp.gmail.com';
    $mail->SMTPAuth = true;
    $mail->Username = $cfg['gmail_user'];
    $mail->Password = $cfg['gmail_app_password'];
    $mail->SMTPSecure = PHPMailer\PHPMailer\PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port = 587;
    $mail->CharSet = 'UTF-8';

    $mail->setFrom($cfg['gmail_user'], 'moving24.ee - и еще одна');
    $mail->addAddress($cfg['lead_to']);
    if ($replyTo !== '') { $mail->addReplyTo($replyTo); }
```
- PHPMailer лежит локально в `phpmailer/src/` (не через Composer - удобно для простого хостинга типа zone.ee, просто заливаешь папку).
- SMTP Gmail: хост `smtp.gmail.com`, порт `587`, STARTTLS. Логин - `gmail_user`, пароль - `gmail_app_password` (это App Password, не обычный пароль аккаунта; создаётся в настройках Google при включённом 2FA).
- `setFrom` - от чьего имени. `addAddress($cfg['lead_to'])` - куда падают заявки (может отличаться от `gmail_user`). `addReplyTo($replyTo)` - чтобы "Ответить" шло клиенту.

Прикрепление фото-вложений:
```php
    foreach ($_FILES as $key => $f) {
        if (strpos($key, 'photo') !== 0) { continue; }
        if (!empty($f['tmp_name']) && is_uploaded_file($f['tmp_name']) && (int)$f['error'] === 0) {
            $mail->addAttachment($f['tmp_name'], $f['name'] ?: ($key . '.jpg'));
        }
    }
```
- Каждое `photo*`-поле прикрепляется как файл. `is_uploaded_file()` - защита: точно принят через HTTP-загрузку, а не подставленный путь.

Inline-картинки через CID (addStringEmbeddedImage):
```php
    $embeds = [
        [$mapPng,    $mapCid,    'route.png', 'image/png'],
        [$svFromPng, $svFromCid, 'from.jpg',  'image/jpeg'],
        [$svToPng,   $svToCid,   'to.jpg',    'image/jpeg'],
    ];
    foreach ($embeds as $e) {
        if ($e[1] !== '' && $e[0] !== '') {
            $mail->addStringEmbeddedImage($e[0], $e[1], $e[2], PHPMailer\PHPMailer\PHPMailer::ENCODING_BASE64, $e[3]);
        }
    }

    $mail->isHTML(true);
    $mail->Subject = $subject;
    $mail->Body = $html;
    $mail->AltBody = $alt;

    $mail->send();
    ok();
} catch (Throwable $e) {
    error_log('moving24 lead mail failed: ' . $e->getMessage());
    fail(502, 'send');
}
```

Почему картинки встраиваются inline через CID, а не по URL - ключевая мысль:
- `addStringEmbeddedImage($данные, $cid, ...)` кладёт сами байты картинки (карта, панорамы) внутрь письма и привязывает к `$cid`. В HTML они подключены как `<img src="cid:routemap">` (см. 3.9, 3.10).
- Причина 1 - ключ Maps не светится. Если бы карта была `<img src="https://maps.googleapis.com/...&key=ВАШ_КЛЮЧ">`, то ключ уехал бы в письмо и был бы виден любому получателю (в исходнике письма). Тут ключ используется только на сервере при `fetchUrl`, а в письмо попадают готовые байты картинки.
- Причина 2 - картинки видны сразу, без "Загрузить изображения". Почтовики (Gmail, Outlook) по умолчанию блокируют внешние картинки. Inline-CID картинки - это часть письма, они не блокируются, владелец сразу видит карту и здания.
- Данные передаются строкой (`addStringEmbeddedImage`, а не `addEmbeddedImage` с файлом), потому что мы держим байты прямо в памяти (`$mapPng`, `$svFromPng`) - никаких временных файлов на диске.
- `send()` при успехе -> `ok()` (JSON `{"ok":true}`). Любая ошибка (`Throwable`) -> пишем в error_log и отдаём `502`, без раскрытия деталей фронту.

## 3.15. Хелпер fetchUrl (cURL + фолбэк)

Единая точка для всех обращений к Google (Directions, Static Maps, Street View):

```php
function fetchUrl($url) {
    if (function_exists('curl_init')) {
        $ch = curl_init($url);
        curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 7, CURLOPT_CONNECTTIMEOUT => 5, CURLOPT_FOLLOWLOCATION => true, CURLOPT_SSL_VERIFYPEER => true]);
        $r = curl_exec($ch); curl_close($ch);
        return $r === false ? '' : (string)$r;
    }
    $ctx = stream_context_create(['http' => ['timeout' => 7], 'https' => ['timeout' => 7]]);
    $r = @file_get_contents($url, false, $ctx);
    return $r === false ? '' : (string)$r;
}
```
- Сначала cURL (есть почти везде): таймаут 7 сек, коннект 5 сек, проверка SSL включена.
- Если cURL нет - фолбэк на `file_get_contents` со stream-контекстом. Так скрипт работает и на урезанных хостингах.
- При любой ошибке возвращает `''` - вызывающий код видит пустоту и просто пропускает соответствующий блок (карту/панораму). Именно это делает деградацию мягкой.

## 3.16. Мягкая деградация и хелперы-заглушки

- Нет `maps_key`, нет адреса, Google не ответил, скачался не PNG/JPEG - соответствующий блок (маршрут-инфо, карта, панорама) просто не добавляется в письмо. Письмо всё равно уходит с тем, что есть.
- `vv($V, $k)` - безопасное чтение роли (нет ключа -> `''`), поэтому пустые поля не роняют скрипт.
- `esc()` - `htmlspecialchars(..., ENT_QUOTES, 'UTF-8')`, экранирует любой пользовательский ввод в HTML.
- `row()` показывает `-` для пустых значений (владелец видит, что поле просто не заполнили).

Финальные заглушки, формирующие JSON-ответ фронту:
```php
function ok() { echo json_encode(['ok' => true]); exit; }
function fail($code, $err) { http_response_code($code); echo json_encode(['ok' => false, 'error' => $err]); exit; }
```

## 3.17. config.php - структура (без значений)

`config.php` НЕ входит в репозиторий и НЕ показывается публично. Он лежит рядом с `lead.php` и возвращает массив. Структура (только ключи, значения свои):

```php
<?php
return [
    'gmail_user'         => '',  // Gmail-адрес для SMTP-логина и в поле From (напр. leads@ваш-домен)
    'gmail_app_password' => '',  // App Password Google (16 символов, создаётся при включённом 2FA; НЕ обычный пароль)
    'lead_to'            => '',  // куда слать заявки (email владельца/отдела; может = gmail_user или отличаться)
    'maps_key'           => '',  // Google Maps API key (Directions + Static Maps + Street View). Пусто = карты/панорамы отключены, письмо всё равно уходит
];
```

Что нужно для нового бизнеса на этом шаблоне:
1. Создать Gmail (или Google Workspace) аккаунт, включить 2FA, сгенерировать App Password -> `gmail_user` + `gmail_app_password`.
2. Указать `lead_to` - куда падают заявки.
3. (Опционально) Завести Google Cloud проект, включить Directions API + Maps Static API + Street View Static API, создать ключ -> `maps_key`. Без него карты/панорамы/расстояние просто не появятся, форма и письмо продолжат работать.
4. Залить папку `phpmailer/` рядом с `lead.php`.

---

Файлы, относящиеся к секции:
- Исходник: `/Users/dennymansa/Desktop/moving24/staging/lead.php`
- Зависимость (локально): `/Users/dennymansa/Desktop/moving24/staging/phpmailer/src/` (`Exception.php`, `PHPMailer.php`, `SMTP.php`)
- Секреты (рядом, не в git): `/Users/dennymansa/Desktop/moving24/staging/config.php`


---

# 4. Интеграция Google Maps (карта, расстояние, Street View)

Это одна из самых мощных фишек шаблона: когда клиент оставляет заявку с адресами "откуда" и "куда", письмо диспетчеру приходит не просто с текстом, а с готовой картой маршрута, посчитанным расстоянием и временем в пути, плюс фото зданий из Street View по обоим адресам. Диспетчер сразу видит подъезды, этажность района, ширину улицы - и точнее оценивает работу, не переспрашивая клиента.

Вся логика живёт в одном файле - `/Users/dennymansa/Desktop/moving24/staging/lead.php` (обработчик формы). Ключ берётся из конфига, никаких ключей в коде нет:

```php
$mapsKey = isset($cfg['maps_key']) ? trim((string)$cfg['maps_key']) : '';
```

Если ключа нет (`$mapsKey === ''`) - весь блок карт просто пропускается, форма продолжает работать и слать заявки без карты. То есть интеграция необязательная: сначала запускаешь сайт, карту прикручиваешь потом.

## 4.1. Какие три API нужны и что каждое даёт

В `lead.php` используются три разных Google-эндпоинта. Все три вызываются **с сервера** (через `fetchUrl()`, серверный HTTP-запрос), а не из браузера клиента. Это принципиально важно - об этом ниже в разделе про ограничения ключа.

### 1. Directions API - расстояние и время в пути

```php
$dj = json_decode(fetchUrl('https://maps.googleapis.com/maps/api/directions/json?units=metric&origin='
    . rawurlencode($fromA) . '&destination=' . rawurlencode($toA) . '&key=' . rawurlencode($mapsKey)), true);
if (isset($dj['routes'][0])) {
    $poly = isset($dj['routes'][0]['overview_polyline']['points']) ? $dj['routes'][0]['overview_polyline']['points'] : '';
    $leg  = isset($dj['routes'][0]['legs'][0]) ? $dj['routes'][0]['legs'][0] : null;
    if ($leg) {
        $d = isset($leg['distance']['text']) ? $leg['distance']['text'] : '';
        $t = isset($leg['duration']['text']) ? $leg['duration']['text'] : '';
        $routeInfo = trim($d . ($d !== '' && $t !== '' ? '  ·  ~' : '') . $t);
    }
}
```

Что даёт:
- `distance.text` - расстояние человекочитаемо ("12,4 km").
- `duration.text` - время в пути ("23 mins").
- `overview_polyline.points` - закодированная линия маршрута (encoded polyline). Её потом скармливаем в статичную карту, чтобы нарисовать сам маршрут поверх дорог, а не прямую линию А-Б.

В письме это превращается в строку вроде `12,4 km · ~23 mins` (см. `$routeInfo`, строка 117 файла).

### 2. Maps Static API - картинка карты с маршрутом

```php
$murl = 'https://maps.googleapis.com/maps/api/staticmap?size=624x300&scale=2'
    . ($poly !== '' ? '&path=' . rawurlencode('color:0x1d4ed8cc|weight:5|enc:' . $poly) : '')
    . '&markers=' . rawurlencode('color:0x1d4ed8|label:A|' . $fromA)
    . '&markers=' . rawurlencode('color:0x0f9d58|label:B|' . $toA)
    . '&key=' . rawurlencode($mapsKey);
$png = fetchUrl($murl);
if ($png !== '' && strncmp($png, "\x89PNG", 4) === 0) { $mapPng = $png; $mapCid = 'routemap'; }
```

Что даёт: готовый PNG-файл карты. Разбор параметров:
- `size=624x300&scale=2` - карта 624x300, но `scale=2` = ретина (по факту 1248x600 пикселей, чётко на любом экране).
- `&path=...color:0x1d4ed8cc|weight:5|enc:<polyline>` - рисуем синий маршрут поверх дорог по той самой polyline из Directions. `cc` в конце цвета - альфа (полупрозрачность).
- две `&markers=` - метка A (синяя, точка старта) и B (зелёная, `0x0f9d58`, точка финиша).
- Проверка `strncmp($png, "\x89PNG", 4) === 0` - убеждаемся, что вернулся именно PNG (сигнатура файла), а не JSON с ошибкой. Если Google вернул ошибку - `$mapPng` остаётся пустым, картинку в письмо не вставляем.

Картинка встраивается в письмо как inline-вложение через `cid:routemap` (не ссылкой, а самим файлом внутри письма - см. массив вложений на строке 164).

### 3. Street View Static API - фото зданий по адресам

```php
function streetView($addr, $key, $cid) {
    $addr = trim((string)$addr);
    if ($addr === '' || $key === '') { return ['', '']; }
    $meta = json_decode(fetchUrl('https://maps.googleapis.com/maps/api/streetview/metadata?source=outdoor&location=' . rawurlencode($addr) . '&key=' . rawurlencode($key)), true);
    if (!isset($meta['status']) || $meta['status'] !== 'OK') { return ['', '']; }
    $img = fetchUrl('https://maps.googleapis.com/maps/api/streetview?size=560x220&fov=78&source=outdoor&location=' . rawurlencode($addr) . '&key=' . rawurlencode($key));
    if ($img !== '' && (strncmp($img, "\xFF\xD8", 2) === 0 || strncmp($img, "\x89PNG", 4) === 0)) { return [$img, $cid]; }
    return ['', ''];
}
```

Хитрость тут в **двухшаговости**, и это важный приём:
- Сначала дёргается **бесплатный** эндпоинт `streetview/metadata` - он говорит, есть ли вообще панорама по этому адресу (`status === 'OK'`).
- Только если панорама есть - дёргается **платный** `streetview` за самой картинкой (JPEG, 560x220, `fov=78` - угол обзора; `source=outdoor` - только уличные съёмки, не панорамы из помещений).

Так мы не платим за картинки, которых нет (в глухих деревнях Street View может отсутствовать), и не суём в письмо серую заглушку "нет изображения". Вызывается для обоих адресов:

```php
if ($fromA !== '') { list($svFromPng, $svFromCid) = streetView($fromA, $mapsKey, 'svfrom'); }
if ($toA   !== '') { list($svToPng, $svToCid)     = streetView($toA,   $mapsKey, 'svto'); }
```

## 4.2. Как получить ключ

1. Заходишь в [Google Cloud Console](https://console.cloud.google.com/), создаёшь проект (или берёшь существующий).
2. Включаешь биллинг (карта обязательна, но см. раздел про стоимость - платить почти не придётся).
3. В меню **APIs & Services -> Library** находишь и жмёшь **Enable** для трёх штук:
   - **Directions API**
   - **Maps Static API**
   - **Street View Static API**
4. **APIs & Services -> Credentials -> Create credentials -> API key**. Получаешь строку вида `AIza...`.
5. Кладёшь её в конфиг под ключом `maps_key` (файл `config.php`, который лежит вне git и в доки не попадает). В `lead.php` она читается как `$cfg['maps_key']`.

## 4.3. ДВА вида ограничений ключа - и главные грабли

Это тот пункт, на котором ломается большинство людей. У Google-ключа **два независимых раздела ограничений**, и путать их нельзя.

### Ограничение 1: "API restrictions" (какие API ключу разрешены)

В настройках ключа есть раздел **API restrictions**. По умолчанию там "Don't restrict key" - работает, но небезопасно (украденный ключ можно использовать где угодно). Правильно: выбрать **Restrict key** и в списке отметить ровно эти три:
- Directions API
- Maps Static API
- Street View Static API

Грабли: если забыл добавить хотя бы один из трёх - именно этот кусок молча отвалится. Например, забыл Street View - карта и расстояние есть, а фото зданий нет, и никакой ошибки в письме. Проверяй, что отмечены все три.

### Ограничение 2: "Application restrictions" (кто может звать ключ) - ГЛАВНАЯ ЛОВУШКА

В разделе **Application restrictions** Google по привычке предлагает "HTTP referrers (web sites)" - и почти все выбирают его, потому что "у меня же сайт". **Это ломает весь наш блок карт.**

Почему: ограничение по HTTP referrers работает только для запросов **из браузера**, где браузер сам подставляет заголовок `Referer` с адресом страницы. А в нашем шаблоне все вызовы Maps идут **с сервера** через `fetchUrl()` в `lead.php`. У серверного запроса нет referrer'а - Google видит "запрос ниоткуда" и отвечает `REQUEST_DENIED`. Итог: заявки приходят, но всегда без карты, без расстояния и без Street View, и ты часами гадаешь почему.

Правильные варианты для **Application restrictions**:
- **None** (самый простой, но тогда ключ защищён только через API restrictions - для лид-формы приемлемо).
- **IP addresses** - вписать IP твоего сервера/хостинга. Безопаснее: даже если ключ утёк, звать его можно только с твоего сервера. Рекомендуется, если хостинг даёт статичный IP.

Запомни правило: **HTTP referrers - только для ключей, которые вызывает JavaScript в браузере. Для серверных вызовов (наш случай) - None или IP.**

## 4.4. Как быстро проверить ключ через браузер

Не надо гонять всю форму, чтобы понять, живой ли ключ. Открой в браузере (подставив свой ключ и любой адрес):

```
https://maps.googleapis.com/maps/api/directions/json?origin=Tallinn&destination=Tartu&key=ТВОЙ_КЛЮЧ
```

Смотришь поле `status` в JSON-ответе:
- `"status": "OK"` - ключ рабочий, API включён, ограничения не мешают. Готово.
- `"status": "REQUEST_DENIED"` - и в поле `error_message` будет причина. Чаще всего: не включён этот API в Library, либо стоит ограничение по HTTP referrers (см. выше), либо не подключён биллинг.

Важный нюанс: этот тест из браузера идёт **с referrer'ом**, поэтому если у тебя ключ ограничен по referrers, тест может показать `OK`, а сервер всё равно получит `REQUEST_DENIED`. Поэтому надёжнее тестировать `curl` без referrer'а прямо с сервера:

```
curl "https://maps.googleapis.com/maps/api/directions/json?origin=Tallinn&destination=Tartu&key=ТВОЙ_КЛЮЧ"
```

Если тут `OK`, а из формы карты не приходят - проблема уже не в ключе.

## 4.5. Стоимость на реальном объёме

На типичном объёме лид-формы (~150 заявок в месяц) это **фактически бесплатно, максимум центы**. Прикидка на одну заявку:
- 1 вызов Directions API
- 1 вызов Maps Static API
- 2 вызова Street View metadata (бесплатные, не тарифицируются)
- 0-2 вызова Street View Static (только если панорама реально есть)

Итого ~4 платных обращения на заявку. 150 заявок = ~600 платных вызовов в месяц. У Google по каждому из этих API большой бесплатный порог в месяц (десятки тысяч запросов), и всё это укладывается в него с гигантским запасом. На практике счёт по такому проекту - ноль или несколько центов. Тем не менее биллинг подключить обязательно (без карты ключ не выдаст даже бесплатные вызовы), и полезно выставить в Cloud Console бюджетный алерт (например, на 5 евро), чтобы спать спокойно.

## 4.6. Waze: почему две отдельные кнопки, а не один маршрут

Помимо встроенной картинки, в письме есть кликабельные кнопки навигации (функция `routeButton`):

```php
function routeButton($from, $to) {
    $from = trim((string)$from); $to = trim((string)$to);
    $links = '';
    if ($from !== '' && $to !== '') {
        $g = 'https://www.google.com/maps/dir/?api=1&origin=' . rawurlencode($from) . '&destination=' . rawurlencode($to);
        $links .= mapBtn($g, '&#128506;&nbsp;Маршрут в Google Maps &rarr;', '#1d4ed8', '#ffffff');
    }
    if ($from !== '') { $links .= mapBtn('https://waze.com/ul?q=' . rawurlencode($from) . '&navigate=yes', 'Waze: Откуда', '#33ccff', '#062a3a'); }
    if ($to   !== '') { $links .= mapBtn('https://waze.com/ul?q=' . rawurlencode($to)   . '&navigate=yes', 'Waze: Куда',   '#33ccff', '#062a3a'); }
    return $links === '' ? '' : '<div style="margin-top:12px">' . $links . '</div>';
}
```

Обрати внимание на асимметрию:
- **Google Maps** - одна кнопка с полным маршрутом: `origin` + `destination`. Google умеет через URL построить маршрут "откуда -> куда".
- **Waze** - **две отдельные** кнопки: "Waze: Откуда" и "Waze: Куда", каждая через `waze.com/ul?q=<адрес>&navigate=yes`.

Почему у Waze так: **Waze через URL-схему не умеет маршрут "из точки А в точку Б".** Параметр `q` задаёт только пункт назначения, а старт Waze всегда берёт от текущего GPS-положения телефона. Передать "откуда" в ссылке некуда - Waze это проигнорирует и построит маршрут от того места, где сейчас водитель. Поэтому единственный честный вариант - дать две кнопки: одна ведёт водителя к адресу загрузки, вторая (когда он уже там) - к адресу выгрузки. `navigate=yes` сразу запускает навигацию, не показывая промежуточный экран.

## 4.7. Компромисс: встроенные картинки vs кнопки-ссылки

В шаблоне сознательно используются **оба** подхода одновременно, и это не избыточность, а страховка. У них разный баланс надёжности:

**Встроенные картинки** (Static Map + Street View, вставляются в письмо через `cid:`):
- Плюс: видно сразу, прямо в теле письма, ничего нажимать не надо - диспетчер открыл письмо и уже оценивает маршрут и подъезды.
- Минус: генерируются **на сервере** в момент отправки. Если Google ответил ошибкой, ключ протух, кончился лимит или сеть моргнула - картинки просто не будет (код это честно проверяет: `strncmp(...PNG...)`, `status === 'OK'` - при неудаче вставка пропускается). То есть картинка может "не прийти".

**Кнопки-ссылки** (Google Maps / Waze):
- Плюс: это **просто ссылки**, в них не зашивается ключ и они не требуют серверного вызова при отправке. Они работают всегда, пока живо письмо. А открываются они в **живом, интерактивном** Google Maps / Street View - диспетчер может покрутить панораму, посмотреть двор с других ракурсов, переключиться на спутник.
- Минус: нужно кликнуть и уйти из письма в приложение/браузер.

Логика такая: **картинки - для мгновенного превью в 90% случаев, кнопки - как надёжный fallback и для глубокого разглядывания.** Если сервер в момент отправки не смог сгенерить карту (истёк лимит, сбой) - кнопки всё равно на месте и ведут в живой сервис. Именно поэтому не стоит выкидывать "дублирующие" кнопки ради чистоты письма: они и есть гарантия, что диспетчер в любом случае доберётся до карты.

---

Основной файл раздела: `/Users/dennymansa/Desktop/moving24/staging/lead.php` (Directions - строки 69-79, Static Map - 80-86, Street View - 263-271, кнопки Google/Waze - 239-249).


---

# 5. Трекинг и Google Ads

Весь трекинг сайта построен вокруг ОДНОГО контейнера Google Tag Manager. Внутри GTM уже настроены GA4, Google Ads, конверсии и триггеры - сам HTML про них ничего не знает, он лишь грузит контейнер и кладёт в `dataLayer` правильные события. Это ключевая идея шаблона: разметка не трогает рекламный кабинет, она просто "кормит" его данными в том формате, который кабинет уже умеет ловить.

Все ссылки на реальный код - файл `/Users/dennymansa/Desktop/moving24/staging/index.html`.

## 5.1. Один GTM-контейнер + гейт по hostname

Блок трекинга стоит максимально высоко в `<head>` (строки 269-281), чтобы контейнер грузился раньше остального:

```html
<!-- ===== Только контейнер GTM (GTM-TSG2CVLC). GA4, Google Ads, конверсии и триггеры настроены ВНУТРИ GTM. Гейт по hostname: грузится только на moving24.ee. Consent Mode v2 default=denied до контейнера. ===== -->
<script>
  window.M24={GTM:'GTM-TSG2CVLC',FORM_ENDPOINT:'/lead.php'};
  window.dataLayer=window.dataLayer||[];
  function gtag(){dataLayer.push(arguments);}
  gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});
  gtag('set','ads_data_redaction',true);
  gtag('set','url_passthrough',true);
  (function(){
    var prod=/(^|\.)moving24\.ee$/i.test(location.hostname);
    if(prod){(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer',window.M24.GTM);}
  })();
</script>
```

Что здесь происходит по порядку:

- `window.M24={GTM:'GTM-TSG2CVLC',FORM_ENDPOINT:'/lead.php'}` - крошечный конфиг сайта. ID контейнера и адрес обработчика формы лежат в одном месте, чтобы их не искать по всему файлу.
- **Гейт по hostname.** Регулярка `/(^|\.)moving24\.ee$/i.test(location.hostname)` даёт `true` только если сайт открыт на боевом домене `moving24.ee` (или его поддомене, например `www.moving24.ee`). На всём остальном (`localhost`, `127.0.0.1`, staging-домен, файл, открытый напрямую) `prod` будет `false`, и загрузчик GTM просто не выполнится.
  - Зачем: пока идёт разработка или предпросмотр, вы НЕ засоряете статистику GA4 и, что важнее, НЕ шлёте фейковые конверсии в Google Ads. Кабинет видит только реальный трафик с боевого домена.
  - `dataLayer` при этом создаётся и наполняется событиями всегда, независимо от гейта - просто на не-боевых доменах эти события никто не читает (контейнер не загружен). Это удобно: логику событий можно тестировать через `console.log(dataLayer)` прямо на staging.

## 5.2. Consent Mode v2 (согласие до контейнера)

Три строки над загрузчиком - это Google Consent Mode v2, и они стоят СТРОГО до вставки GTM. Порядок важен: Google требует, чтобы дефолтное состояние согласия было задано раньше, чем загрузятся теги.

```js
gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});
gtag('set','ads_data_redaction',true);
gtag('set','url_passthrough',true);
```

- `consent default ... denied` - по умолчанию всё запрещено (реклама и аналитика). Пока пользователь не нажал "Принять" в баннере, теги работают в урезанном "cookieless" режиме: конверсии моделируются, куки не ставятся. Это соответствие GDPR из коробки.
- `wait_for_update:500` - GTM подождёт 500 мс на решение пользователя, прежде чем сработать, чтобы клик "Принять" успел обновить согласие ДО отправки первых хитов.
- `ads_data_redaction:true` - пока рекламное согласие `denied`, из запросов к Google Ads вычищаются идентификаторы кликов (редактируются данные). Дополнительный слой приватности.
- `url_passthrough:true` - при отсутствии кук Google передаёт `gclid` и подобные параметры через URL, чтобы атрибуция клика по объявлению не терялась в cookieless-режиме.

Само обновление согласия делает отдельный скрипт cookie-баннера в конце страницы (строка 2018). При клике по кнопкам он вызывает `gtag("consent","update",{...})` и переводит нужные категории в `granted`, а выбор сохраняет в `localStorage` под ключом `m24_consent_v2`, чтобы не спрашивать повторно:

```js
function apply(a,d){gtag("consent","update",{analytics_storage:a?"granted":"denied",ad_storage:d?"granted":"denied",ad_user_data:d?"granted":"denied",ad_personalization:d?"granted":"denied"});...}
```

где `a` - согласие на аналитику, `d` - на рекламу (две независимые галочки в баннере).

## 5.3. `<noscript>`-часть контейнера (правится ВРУЧНУЮ)

У GTM есть вторая, `<noscript>`, половина - для браузеров без JS. Она стоит сразу после `<body>` (строки 1173-1174):

```html
<!-- Google Tag Manager (noscript). ВАЖНО: этот ID правится ВРУЧНУЮ (JS-конфиг window.M24 сюда не дотянется) - при вставке реального GTM замени GTM-XXXXXXX и здесь. -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-TSG2CVLC" height="0" width="0" style="display:none;visibility:hidden" title="gtm"></iframe></noscript>
```

**Грабль:** ID контейнера здесь захардкожен в `src` iframe и НЕ подставляется из `window.M24.GTM` (JS туда не дотягивается). Когда меняете контейнер под нового клиента, правьте ID в ДВУХ местах: в `window.M24` (строка 271) и в этом `<noscript>` (строка 1174).

## 5.4. Событие конверсии формы: воспроизведение WPForms `ajaxComplete`

Сайт статический (форма шлётся своим `fetch` на `/lead.php`), но существующий GTM-контейнер изначально настроен под WordPress-плагин WPForms. Внутри контейнера уже живёт триггер, который слушает кастомное событие `ajaxComplete` с определённой структурой (URL `admin-ajax.php`, `statusCode:200`, HTML-подтверждение WPForms внутри `response`).

Чтобы НЕ трогать контейнер и НЕ пересобирать триггер, сайт просто воспроизводит ровно такое событие после успешной отправки своей формы. Код в функции `done()` (строка 1941), выполняется только в ветке `if(sent)`:

```js
dataLayer.push({event:'ajaxComplete',attributes:{type:'POST',url:'https://moving24.ee/wp-admin/admin-ajax.php',pathname:'/wp-admin/admin-ajax.php',statusCode:200,statusText:'success',response:{success:true,data:{confirmation:'<div class="wpforms-confirmation-container-full wpforms-confirmation-scroll" id="wpforms-confirmation-895"><p>Täname päringu eest. Võtame Teiega peatselt ühendust!</p></div>'}}}}); /* конверсию формы считает тег в GTM */
```

Логика: это "муляж" события, которое раньше генерировал WPForms на живом WordPress. Триггер в GTM видит знакомый ему `event:'ajaxComplete'` с нужными полями и срабатывает как обычно - засчитывает конверсию отправки формы в Google Ads / GA4. Сайт при этом остаётся полностью статическим, а рекламный кабинет ничего не заметил.

Важно: это событие пушится ТОЛЬКО при реальном успехе (`sent` истинно, то есть `fetch` на `/lead.php` вернул `r.ok`). В демо-режиме (endpoint не задан) и при ошибке отправки конверсия не засчитывается - см. ветки `if(demo)` и `else` в той же функции.

## 5.5. Клики по телефону и e-mail: нативный `gtm.linkClick` + свои события

Для звонков и писем работают ДВА механизма одновременно, и это сделано намеренно.

Первый - нативный. GTM умеет сам ловить клики по ссылкам и генерировать встроенное событие `gtm.linkClick` (Just Links trigger). Никакого кода на сайте для этого не нужно - достаточно обычных ссылок `<a href="tel:...">` и `<a href="mailto:...">`, которых на странице много (шапка, hero, футер, плавающая мобильная кнопка "Helista" и т. д.).

Второй - свои дублирующие события. Дополнительно на каждую такую ссылку вешается обработчик, который кладёт в `dataLayer` собственное именованное событие (строки 1991-1997):

```js
/* ---- Track phone & email link clicks (mirror live GTM events) ---- */
document.querySelectorAll('a[href^="tel:"]').forEach(function(a){
  a.addEventListener('click',function(e){ try{dataLayer.push({event:'phone_link_klick'});}catch(_){} }); /* конверсию звонка считает тег в GTM (с задержкой навигации) */
});
document.querySelectorAll('a[href^="mailto:"]').forEach(function(a){
  a.addEventListener('click',function(e){ try{dataLayer.push({event:'email_link_click'});}catch(_){} });
});
```

- `phone_link_klick` - на все `tel:`-ссылки (имя именно с таким написанием - оно должно совпадать с тем, что настроено в контейнере, не "исправляйте" опечатку).
- `email_link_click` - на все `mailto:`-ссылки.
- `try/catch` - чтобы если `dataLayer` вдруг недоступен, клик по ссылке не сломался.
- Обработчик НЕ вызывает `e.preventDefault()` - навигация по `tel:`/`mailto:` идёт как обычно, событие просто пушится попутно.

Зачем дублировать нативный `gtm.linkClick` своими событиями: два независимых пути дают гибкость в кабинете (можно триггерить конверсию хоть по нативному `gtm.linkClick`, хоть по своему `phone_link_klick`) и понятные, читаемые имена событий в отладчике.

## 5.6. ГЛАВНЫЙ ГРАБЛЬ: не добавлять `stopPropagation()` на tel/mailto

Нативный триггер GTM "Just Links" (`gtm.linkClick`) ловит клик на уровне `document` - событие клика должно ВСПЛЫТЬ до документа. Если на обработчик `tel:`/`mailto:`-ссылки добавить `e.stopPropagation()`, всплытие прервётся, и **нативный `gtm.linkClick` не сработает** - конверсия звонка/письма тихо потеряется (при этом ваш собственный `phone_link_klick` ещё может пушнуться, что маскирует проблему).

Поэтому в обработчиках из 5.5 сознательно НЕТ `stopPropagation()` и НЕТ `preventDefault()`. Клик спокойно всплывает до `document`, где его подхватывает GTM.

Для сравнения: `stopPropagation()` в этом файле применяется намеренно только там, где всплытие ВРЕДНО и с трекингом не связано - например, крестик закрытия лайтбокса галереи (строка 1980) и подавление "ложного клика" после свайпа карусели отзывов (строка 2020). На ссылки-конверсии его переносить нельзя.

Правило для шаблона: на `<a href="tel:...">` и `<a href="mailto:...">` (и на любые элементы конверсии, которые должен ловить нативный триггер GTM) - никаких `stopPropagation`. Пушьте своё событие и дайте клику всплыть.

## 5.7. Что менять под нового клиента (и что НЕ трогать)

**Менять в HTML (только идентификаторы):**

1. `window.M24.GTM` в `<head>` (строка 271) - новый ID контейнера `GTM-XXXXXXX`.
2. `<noscript>`-iframe (строка 1174) - тот же новый ID, ВРУЧНУЮ (см. 5.3).
3. Гейт по домену (строка 278) - заменить регулярку `/(^|\.)moving24\.ee$/i` на боевой домен нового клиента.
4. В muляже конверсии формы (строка 1941) домен `https://moving24.ee/...` можно оставить/поправить - главное, чтобы структура события (`event:'ajaxComplete'`, `admin-ajax.php`, `statusCode:200`, HTML WPForms) совпадала с тем, что ждёт триггер в контейнере клиента.

**Оставлять как есть (имена событий - контракт с контейнером):**

- `ajaxComplete`, `phone_link_klick`, `email_link_click` - это НЕ произвольные названия, а имена, на которые уже настроены триггеры внутри GTM. Переименуете на сайте - конверсии перестанут считаться. Меняются они только парой "сайт + контейнер" вместе.

**НЕ трогать вообще:**

- Сам контейнер GTM, его теги, триггеры, GA4 и конверсии Google Ads - вся эта настройка живёт ВНУТРИ кабинета GTM/Ads, а не в файле. Задача HTML - лишь загрузить контейнер (с гейтом и Consent Mode) и класть в `dataLayer` события с правильными именами. Кабинет и контейнер остаются нетронутыми; под нового клиента подключается новый аккаунт GTM/GA4/Ads с той же схемой событий.

Итог схемы: `<head>` (Consent default denied → set ads_data_redaction/url_passthrough → загрузка GTM только на боевом домене) → пользователь жмёт "Принять" в баннере (`consent update → granted`) → сайт пушит в `dataLayer` события конверсий (`ajaxComplete` для формы, `phone_link_klick`/`email_link_click` + нативный `gtm.linkClick` для звонков и писем) → триггеры внутри GTM ловят их и отправляют конверсии в GA4 и Google Ads.


---

# 6. Как устроены переводы (мультиязычность)

Сайт Moving24 существует на четырёх языках: **ET** (эстонский, корень `/`), **EN** (`/en/`), **RU** (`/ru/`), **FI** (`/fi/`). Это НЕ плагин-переводчик и НЕ автоперевод на лету. Каждый язык - это отдельный набор статических HTML-файлов в своей папке, свёрстанных руками (генераторами) один раз. Ниже - вся механика: как языки связаны между собой, как переведены URL-ы, как настроен hreflang, как локализованы поля формы и как добавить/поправить язык.

## 6.1. Один язык - мастер, остальные - нативные адаптации

Ключевой принцип, который надо усвоить до того, как трогать тексты:

**Языки не переводятся дословно друг из друга. Мастер задаёт СМЫСЛ и структуру, а каждый язык - это самостоятельный, "родной" для носителя текст.**

В проекте роль мастера де-факто играет русский (RU) - именно на нём написаны рабочие заметки, генераторы и `_ai/GUIDE.md` (сам гайд внутри сайта написан по-русски). Эстонский (ET) - это боевой "первый" язык для рынка (сайт живёт на домене `.ee`, корень `/` = ET). Практически это выглядит так:

- Мастер фиксирует: какие блоки на странице, в каком порядке, какие смыслы и офферы ("честная фиксированная цена заранее", "5.0 в Google", "работаем 24/7").
- Дальше каждый язык пишется как будто его писал местный копирайтер. Не "переведи эту фразу", а "скажи то же самое так, как это звучит на этом языке для этого рынка".

Это прямо видно в реальных заголовках и мета-описаниях - они НЕ совпадают пословно, каждый бьёт по своей аудитории:

| Язык | `<title>` (реальный текст из файла) |
|------|--------|
| ET | `Kolimisteenus Tallinnas ja üle Eesti \| Moving24` |
| RU | `Переезд в Таллинне и по Эстонии` |
| EN | `Moving Company in Tallinn & Estonia` |
| FI | `Muuttofirma Tallinnassa ja koko Virossa` |

И `meta description` (обратите внимание: RU-описание длиннее и "продающее", ET сделан под SEO-паритет, FI - максимально сухой и деловой, как любит финская аудитория):

- **ET**: `Usaldusväärne kolimisfirma Tallinnas - 5.0 hinne Google'is, 4500+ kolimist ja aus fikseeritud hind ette. Töötame 24/7. Küsi tasuta pakkumist!`
- **RU**: `Квартирный и офисный переезд по всей Эстонии. Честная фиксированная цена заранее, работаем 24/7, оценка 5.0 в Google. Звоните или получите бесплатный расчёт.`
- **EN**: `Moving company in Tallinn serving all Estonia. 5.0 on Google, 4500+ moves done, available 24/7 with a fair fixed price upfront. Get your free quote today.`
- **FI**: `Luotettava muuttofirma Tallinnassa ja koko Virossa. 5.0 Googlessa, yli 4500 muuttoa ja kiinteä hinta etukäteen. Pyydä ilmainen tarjous jo tänään.`

Смыслы одни и те же (5.0 в Google, 4500+ переездов, фикс-цена, 24/7, бесплатный расчёт), но формулировки родные. Это осознанное правило: **дословный перевод читается как машинный и роняет доверие и конверсию.** Для нового бизнеса делайте так же - определите мастер-язык, пропишите смыслы, а остальные языки пишите нативно.

Единственное, что переносится один-в-один между языками, - это факты в schema.org (`telephone`, `address`, `vatID`, `areaServed`, `aggregateRating`). Их переводить нельзя, это данные, а не текст. В `ru/index.html` и `index.html` блок `<script type="application/ld+json">` с адресом `Tartu mnt 2, Tallinn`, `vatID: EE102734342`, рейтингом `5.0` идентичен.

## 6.2. Переведённые слаги (URL) в каждом языке

URL-ы тоже локализованы - каждый сегмент пути переведён на язык страницы. Домашняя страница - это `/`, `/en/`, `/ru/`, `/fi/`, а внутренние страницы получают "родные" слаги. Реальное соответствие из `sitemap.xml`:

| Смысл страницы | ET (корень) | EN | RU | FI |
|---|---|---|---|---|
| Услуги (папка) | `/teenused/` | `/en/service/` | `/ru/uslugi/` | `/fi/palvelut/` |
| Квартирный переезд | `/teenused/erakolimine/` | `/en/service/home-move/` | `/ru/uslugi/chastnyj-pereezd/` | `/fi/palvelut/kotimuutto/` |
| Бизнес-переезд | `/teenused/arikolimine/` | `/en/service/business-move/` | `/ru/uslugi/biznes-pereezd/` | `/fi/palvelut/yritysmuutto/` |
| Вывоз мусора | `/teenused/prugivedu/` | `/en/service/junk-removal/` | `/ru/uslugi/vyvoz-musora/` | `/fi/palvelut/romun-poisvienti/` |
| Крупногабарит | `/teenused/suuregabariidiline/` | `/en/service/oversized/` | `/ru/uslugi/krupnogabaritnyj/` | `/fi/palvelut/raskaat-tavarat/` |
| О нас | `/meist/` | `/en/about/` | `/ru/o-nas/` | `/fi/meista/` |
| FAQ | `/kkk/` | `/en/faq/` | `/ru/faq/` | `/fi/ukk/` |

Почему так, а не единый `/services/home/` для всех:

- **Локальный SEO.** Человек в Финляндии ищет "kotimuutto", эстонец - "erakolimine", русскоязычный - "квартирный переезд". Слаг в URL - это сигнал релевантности. Английские слаги для русского раздела убивают попадание в местную выдачу.
- **Доверие.** Родной URL выглядит "своим", а не автопереведённым.

Практический вывод для шаблона: **слаги - это часть контента, а не техническая деталь.** Заводя новую услугу, придумайте нативный слаг под каждый язык (не транслит с одного языка, а как реально ищут на этом рынке). Русские слаги - латиницей в транслите (`chastnyj-pereezd`, `vyvoz-musora`), это норма для рунета и корректно индексируется.

## 6.3. hreflang в `<head>` КАЖДОЙ страницы

Чтобы Google понимал, что четыре URL - это один и тот же контент на разных языках (и не считал их дублями), в `<head>` каждой страницы стоит ПОЛНЫЙ набор `hreflang`-ссылок. Правила:

1. Набор одинаковый на всех четырёх языковых версиях одной страницы (симметрия обязательна - если A ссылается на B, B должен ссылаться на A).
2. Ссылки абсолютные (`https://moving24.ee/...`).
3. Обязательно есть `x-default` - куда слать пользователя с "неопределённым" языком (тут это ET-корень).
4. `canonical` на каждой странице указывает сам на себя (self-canonical), НЕ на мастер.

Реальный блок из корневого `index.html` (ET):

```html
<link rel="canonical" href="https://moving24.ee/">
<link rel="alternate" hreflang="et" href="https://moving24.ee/">
<link rel="alternate" hreflang="en" href="https://moving24.ee/en/">
<link rel="alternate" hreflang="ru" href="https://moving24.ee/ru/">
<link rel="alternate" hreflang="fi" href="https://moving24.ee/fi/">
<link rel="alternate" hreflang="x-default" href="https://moving24.ee/">
```

Тот же блок в `ru/index.html` - идентичный набор alternate, но `canonical` уже свой (`.../ru/`):

```html
<link rel="canonical" href="https://moving24.ee/ru/">
<link rel="alternate" hreflang="et" href="https://moving24.ee/">
<link rel="alternate" hreflang="en" href="https://moving24.ee/en/">
<link rel="alternate" hreflang="ru" href="https://moving24.ee/ru/">
<link rel="alternate" hreflang="fi" href="https://moving24.ee/fi/">
<link rel="alternate" hreflang="x-default" href="https://moving24.ee/"><!-- TODO: на проде заменить на https://moving24.ee/ -->
```

Для внутренних страниц hreflang использует ПЕРЕВЕДЁННЫЕ слаги. Например, на странице квартирного переезда набор такой (виден в sitemap, и точно так же должен стоять в `<head>` каждой из этих 4 страниц):

```html
<link rel="alternate" hreflang="et" href="https://moving24.ee/teenused/erakolimine/">
<link rel="alternate" hreflang="en" href="https://moving24.ee/en/service/home-move/">
<link rel="alternate" hreflang="ru" href="https://moving24.ee/ru/uslugi/chastnyj-pereezd/">
<link rel="alternate" hreflang="fi" href="https://moving24.ee/fi/palvelut/kotimuutto/">
<link rel="alternate" hreflang="x-default" href="https://moving24.ee/teenused/erakolimine/">
```

Также в `<head>` каждой версии задан `og:locale` под язык: ET - `et_EE`, RU - `ru_RU` и т.д. И `<html lang="...">` в самом верху документа (`lang="et"`, `lang="ru"`, `lang="en"`, `lang="fi"`) - это отдельный сигнал для браузера и скринридеров, его тоже надо менять при копировании страницы.

## 6.4. Альтернативы в sitemap (`xhtml:link`)

`sitemap.xml` дублирует ту же карту языков, но в своём формате. В корне указано пространство имён xhtml:

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
```

И для КАЖДОГО `<url>` перечислены все языковые альтернативы через `xhtml:link` - тот же полный набор et/en/ru/fi/x-default, что и в `<head>`. Реальный узел для главной:

```xml
<url>
  <loc>https://moving24.ee/</loc>
  <lastmod>2026-07-06</lastmod>
  <changefreq>weekly</changefreq>
  <priority>1.0</priority>
  <xhtml:link rel="alternate" hreflang="et" href="https://moving24.ee/"/>
  <xhtml:link rel="alternate" hreflang="en" href="https://moving24.ee/en/"/>
  <xhtml:link rel="alternate" hreflang="ru" href="https://moving24.ee/ru/"/>
  <xhtml:link rel="alternate" hreflang="fi" href="https://moving24.ee/fi/"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://moving24.ee/"/>
</url>
```

Важные детали, которые легко упустить:

- В sitemap каждая языковая версия - это **отдельный `<url>`-узел** со своим `<loc>`, но с ОДИНАКОВЫМ блоком `xhtml:link`. То есть четыре узла (по одному на язык) несут один и тот же набор альтернатив. Это правильно и обязательно.
- Главные страницы имеют `priority 1.0`, внутренние - `0.8`.
- `lastmod` у всех проставлен единой датой сборки (`2026-07-06`) - это генерируется, не пишется руками.

Итог: **язык-связки прописаны в ДВУХ местах - в `<head>` каждой страницы И в sitemap. Оба должны совпадать.** Если добавили страницу - правьте оба.

## 6.5. Локализованные подписи полей формы (уходят в письмо)

Это тонкое, но важное место. Форма заявки одна и та же на всех языках по СТРУКТУРЕ, но подписи полей (`placeholder`, `aria-label`, `<label>`) локализованы. При этом **машинные имена полей (`name="..."`) во всех языках ОДИНАКОВЫЕ** - `lead.php` и письмо на почту не должны зависеть от языка сайта.

Сравните одно и то же поле "адрес откуда" в трёх языках (обратите внимание: `name="from_address"` везде один, меняется только видимый текст):

```html
<!-- ET (index.html) -->
<div class="ff-base"><label>Kust?</label>
  <input type="text" name="from_address" aria-label="Kust?" placeholder="nt. Rotermanni 18, Tallinn"></div>

<!-- RU (ru/index.html) -->
<div class="ff-base"><label>Адрес: откуда</label>
  <input type="text" name="from_address" aria-label="Адрес: откуда" placeholder="напр. Rotermanni 18, Tallinn"></div>

<!-- EN (en/index.html) -->
<label>From</label>  ... name="from_address"
```

Соответствие подписей по языкам (реальные строки из файлов):

| `name=` (не менять) | ET | RU | EN |
|---|---|---|---|
| `name` | `Täisnimi / ettevõtte nimi *` | `Полное имя / Название компании *` | `Full name / company *` |
| `email` | `E-post *` | `Email *` | `Email *` |
| `phone` | `Telefon *` | `Телефон *` | `Phone *` |
| `from_address` | `Kust?` | `Адрес: откуда` | `From` |
| `to_address` | `Kuhu?` | `Адрес: куда` | `To` |
| `from_floor` / `to_floor` | `Korrus` | `Этаж` | (localized) |
| `from_lift` / `to_lift` | `Lift?` / `Jah`/`Ei` | `Лифт?` / `Да`/`Нет` | (localized) |
| `date` / `time` | `Kuupäev` / `Aeg` | `Дата` / `Время` | (localized) |
| `packing` | `Kas soovite pakkimisteenust?` | (localized) | (localized) |
| `msg` | `Lisainfo - esemete loetelu` | `Дополнительная информация, список вещей` | `Additional info - list of items` |

Почему это критично для лид-ген-сайта:

- Клиент видит форму на своём языке (конверсия), а менеджер получает письмо со СТАБИЛЬНОЙ структурой полей независимо от того, с какой языковой версии пришла заявка. Логика `lead.php` завязана на `name`, а не на подпись.
- Значения переключателей (`Jah/Ei`, `Да/Нет`) - это `data-val`, который кладётся в скрытый `<input type="hidden" name="from_lift">`. То есть в письмо уйдёт локализованное значение "Да"/"Jah" - это ОК, менеджер понимает, но `name` поля одинаков.
- Есть honeypot-поле `name="_gotcha"` (скрытый антиспам-инпут) - оно тоже одинаково на всех языках, не трогайте.

Правило для шаблона: **переводите видимый текст полей, НИКОГДА не переводите атрибут `name`.** Иначе сломается парсинг заявки на бэкенде.

## 6.6. Переключатель языков (одинаков на всех страницах)

В шапке каждой страницы есть блок `.lang-switch` с четырьмя ссылками. Он идентичен по разметке во всех версиях - меняется только то, на какой ссылке стоит `is-active` + `aria-current="page"`. Реальный блок из ET-главной:

```html
<div class="lang-switch" role="navigation" aria-label="Keel / Language / Язык / Kieli">
  <a href="/"    class="lang-link is-active" hreflang="et" lang="et" aria-current="page">ET</a>
  <a href="/en/" class="lang-link"           hreflang="en" lang="en">EN</a>
  <a href="/ru/" class="lang-link"           hreflang="ru" lang="ru">RU</a>
  <a href="/fi/" class="lang-link"           hreflang="fi" lang="fi">FI</a>
</div>
```

В `ru/index.html` тот же блок, но `is-active`/`aria-current` уже на ссылке `RU`. Обратите внимание на детали доступности: `aria-label` переключателя написан сразу на всех языках (`Keel / Language / Язык / Kieli`), у каждой ссылки проставлены `hreflang` и `lang`.

Важное ограничение текущей реализации: на ГЛАВНЫХ страницах переключатель ведёт на корни языков (`/`, `/en/`, `/ru/`, `/fi/`). На внутренних страницах ссылки в идеале должны вести на ПЕРЕВЕДЁННЫЙ аналог этой же страницы (например, со страницы `chastnyj-pereezd` кнопка EN должна вести на `/en/service/home-move/`, а не на `/en/`), чтобы язык переключался "на месте". Проверяйте это при сборке внутренних страниц - соответствие берите из карты слагов (раздел 6.2) и из hreflang в `<head>` этой страницы.

## 6.7. Как ДОБАВИТЬ или поправить язык

### Поправить текст в существующем языке
1. Правьте текст ПРЯМО в нужном файле (`ru/index.html`, `en/service/home-move/index.html` и т.д.). Это статический HTML.
2. Не трогайте `name="..."` в форме, блок schema.org (факты), структуру hreflang.
3. Пишите нативно, а не дословным переводом с мастера (см. 6.1).
4. Тире не используйте - только дефис (`-`). Это жёсткое правило проекта (в текстах уже так: `Lisainfo - esemete loetelu`, `Additional info - list of items`).

### Добавить НОВУЮ страницу в существующих языках
1. Придумайте нативный слаг под каждый язык (6.2).
2. Создайте 4 файла в правильных папках (`teenused/новый/`, `en/service/new/`, `ru/uslugi/novyj/`, `fi/palvelut/uusi/`).
3. В `<head>` каждого из 4 файлов пропишите ПОЛНЫЙ симметричный набор hreflang на все 4 слага + x-default, и self-canonical (6.3). Поставьте правильный `<html lang>` и `og:locale`.
4. Добавьте 4 узла `<url>` в `sitemap.xml` с блоком `xhtml:link` (6.4).
5. Проверьте, что переключатель языков на этих страницах ведёт на переводы-аналоги (6.6).

### Добавить ЦЕЛЫЙ новый язык (например, LV/латышский)
1. Заведите папку-корень `/lv/` и всю структуру услуг с латышскими слагами.
2. Во ВСЕ существующие страницы всех языков добавьте новую `hreflang="lv"` строку в `<head>` (симметрия) и `xhtml:link hreflang="lv"` во все узлы sitemap.
3. Добавьте пятую ссылку в `.lang-switch` на всех страницах.
4. Локализуйте подписи формы (видимый текст), оставив `name` неизменными.
5. Напишите контент нативно от мастера.
6. Обновите `og:locale`, `<html lang="lv">`, robots/sitemap.

Практический совет: в этом проекте языки не пишутся руками страница за страницей - они собираются генераторами (в корне репозитория лежат `fi_build.py`, `fi_scaffold.py`, `fi_strings.json`, `fi_map.json`, `assemble.py` и т.п.). То есть новый язык = новый набор строк (JSON со всеми подписями/текстами) + карта слагов + прогон сборщика, который проставит hreflang и sitemap автоматически. Это надёжнее ручной правки 4×N файлов. Детали пайплайна сборки - в `/Users/dennymansa/Desktop/moving24/OPERATIONS.md`.

## 6.8. Подробные языковые правила (playbooks)

Принципы копирайтинга, живые примеры формулировок и чеклисты по каждому языку выносятся в отдельные плейбуки:

- `playbooks/LANG-ET.md` - эстонский: тон, типичные обороты, чего избегать, SEO-нюансы под рынок EE.
- `playbooks/LANG-RU.md` - русский (мастер): как формулировать смыслы, что можно, что нельзя, транслит слагов.
- `playbooks/LANG-EN.md` - английский: нейтральный international English, без региональных идиом.

Каждый плейбук содержит: (1) принципы нативной адаптации для языка, (2) примеры "плохо/дословно -> хорошо/нативно", (3) чеклист перед публикацией (hreflang симметричен, `name` полей не тронуты, тире нет, слаг нативный, schema-факты не переведены).

> Примечание по факту на диске: на момент написания в исходниках лежит только сводный гайд `/Users/dennymansa/Desktop/moving24/staging/_ai/GUIDE.md` (по-русски, описывает форму/трекинг/структуру). Отдельных файлов `playbooks/LANG-ET|RU|EN.md` в репозитории пока НЕТ - это плановое место для детальных языковых правил. Если их ещё не создали, при работе с языком опирайтесь на `_ai/GUIDE.md` и на реальные тексты в файлах как на эталон, а сами плейбуки заведите по структуре из этого раздела.

---

Ключевые файлы, на которые опирается этот раздел (все пути абсолютные):
- `/Users/dennymansa/Desktop/moving24/staging/index.html` (ET, мастер-разметка head + форма + lang-switch)
- `/Users/dennymansa/Desktop/moving24/staging/ru/index.html`, `/en/index.html`, `/fi/index.html` (нативные версии)
- `/Users/dennymansa/Desktop/moving24/staging/sitemap.xml` (карта слагов + `xhtml:link` альтернативы)
- `/Users/dennymansa/Desktop/moving24/staging/_ai/GUIDE.md` (внутренний гайд по форме/трекингу/структуре)
- Генераторы языков в корне репозитория: `fi_build.py`, `fi_scaffold.py`, `fi_strings.json`, `fi_map.json`, `assemble.py`


---

# 7. Как редактировать под нового клиента + темизация

Этот шаблон - статический HTML на 4 языка (`et` в корне, `en/`, `ru/`, `fi/`) плюс один PHP-обработчик формы (`lead.php`). Всё вшито прямо в HTML - никакой CMS, никакой БД. Чтобы получить сайт под другого локального клиента, вы правите **тексты и константы**, но **не трогаете каркас** (проводку трекинга, логику формы, honeypot, шаблоны hreflang/canonical). Ниже - точная карта.

## 7.1. Что менять (таблица «ЧТО → ГДЕ → КАК НАЙТИ»)

Все пути от `/Users/dennymansa/Desktop/moving24/staging/`. Правки нужно повторить во **всех 4 языковых копиях** (`index.html`, `en/index.html`, `ru/index.html`, `fi/index.html`) плюс на внутренних страницах (`teenused/`, `meist/`, `tingimused/`, `privaatsus/` и т.д.).

| Что | Где (файл) | Как найти / реальный образец из кода |
|---|---|---|
| **Название компании / бренд** | все `*.html`, `.nav-logo`, `<address>`, schema | `grep -rn "Moving24" staging/`. В футере: `Moving24 OÜ · Reg 16978239 · VAT EE102734342` (строка 1775 `index.html`) |
| **Телефон** | все `*.html` (много вхождений) | `grep -n "+37256870101\|+372 5687 0101" index.html` - встречается ~15 раз: в nav, hero, футере, mob-bar. **Два формата всегда парой**: `href="tel:+37256870101"` (без пробелов) и видимый `+372 5687 0101` (с пробелами). Меняйте оба |
| **E-mail (публичный)** | все `*.html` | `grep -n "info@moving24.ee" index.html` → строки 34, 1772, 1815. Формат: `<a href="mailto:info@moving24.ee">` |
| **E-mail (куда приходят заявки)** | `config.php` (НЕ в HTML) | ключ `lead_to` - читается в `lead.php:153` `$mail->addAddress($cfg['lead_to'])`. В самом HTML этого адреса нет |
| **Юр. адрес** | футер `<address>`, schema `PostalAddress` | строка 1774: `Tartu mnt 2, 10145 Tallinn, Eesti`. Также в JSON-LD в `<head>` |
| **Reg / VAT (рег. номер и НДС)** | футер `<address>`, schema | строка 1775: `Reg 16978239 · VAT EE102734342`. Если новый клиент без НДС - убрать `· VAT ...` целиком |
| **Отзывы** | JSON-LD `"review": [...]` в `<head>` (стр. 92+), + видимый блок отзывов на странице | `"reviewBody": "..."`, `"reviewCount": "37"`, `"ratingValue": "5.0"` (стр. 69-70). **⚠️ Только реальные отзывы клиента. Никогда не выдумывать** - `reviewCount`, `ratingValue` и тексты должны совпадать с настоящим профилем Google/Facebook. Если отзывов нет - удалить весь блок `aggregateRating` и `review`, иначе это ложные structured data (риск ручной санкции Google) |
| **Услуги + карточки-чипсы формы** | форма `#svcChips` (стр. 1257), `data-svc="..."`, блок услуг на странице | 4 услуги: `data-svc="private"` (Kodukolimine / переезд квартиры), `business` (Ärikolimine / офис), `garbage` (Utiliseerimine / вывоз), `transport` (Rasked esemed / тяжёлые вещи). Меняете текст чипсов и логику показа полей `data-svc` (см. 7.4) |
| **Картинки / фото** | `img/`, hero-фон `imagebg-*.webp/jpg` | `ls staging/img/`. Hero-фон: `imagebg-1920.webp`, `imagebg-1920.jpg`, `imagebg-768.webp`, `imagebg-1920.jpg`. og-image в `<head>`. Замените файлы (те же имена = меньше правок) или обновите пути |
| **Домен / все URL** | canonical, hreflang, og:url, schema, sitemap | `grep -rn "moving24.ee" staging/`. Canonical стр. 10: `https://moving24.ee/`; hreflang стр. 11-15; плюс `sitemap.xml`, `robots.txt`, `llms.txt` |
| **GTM-контейнер** | `index.html:271` (JS) **и** `index.html:1174` (noscript) | `window.M24={GTM:'GTM-TSG2CVLC',FORM_ENDPOINT:'/lead.php'};`. ⚠️ **Два места**: JS-конфиг `window.M24` (стр. 271) и `<noscript><iframe ...id=GTM-TSG2CVLC>` (стр. 1174) - второй правится ВРУЧНУЮ, JS туда не дотянется. GA4/Ads/конверсии настроены ВНУТРИ GTM, не в коде |
| **config.php (SMTP + Maps)** | `config.php` (рядом с `lead.php`, в репо НЕ хранится) | `lead.php` читает: `maps_key` (стр. 65, Google Maps для картинки маршрута в письме), `gmail_user` (стр. 146), `gmail_app_password` (стр. 147), `lead_to` (стр. 153). Структура: `<?php return ['maps_key'=>'...','gmail_user'=>'...','gmail_app_password'=>'...','lead_to'=>'...'];` |

## 7.2. Что НЕ трогать

Это «двигатель» шаблона. Меняете тут - ломаете конверсии/индексацию/антиспам.

- **Проводку трекинга.** НЕ трогать `gtag('consent','default',{...denied})` (Consent Mode v2, стр. 274), `dataLayer.push({event:'phone_link_klick'})` (стр. 1993), `email_link_click` (стр. 1996), `ajaxComplete`-пуш после успешной формы (стр. 1941). Конверсии считаются тегами внутри GTM по этим событиям - переименуете event → сломаете счёт лидов/звонков. Меняется только сам `GTM-...` ID (см. таблицу).
- **Логику формы.** НЕ трогать submit-обработчик, `FORM_ENDPOINT:'/lead.php'`, скрытые поля `utm_source/medium/campaign/term/content` и `gclid` (стр. 1255) - они прокидывают источник лида в письмо. Логику показа полей по `data-svc` можно расширять (7.4), но каркас оставить.
- **Honeypot.** НЕ трогать и НЕ показывать поле `name="_gotcha"` (стр. 1256): `<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" style="...opacity:0;pointer-events:none">`. В `lead.php:20` проверка: `if (trim((string)($_POST['_gotcha'] ?? '')) !== '') { ok(); }` - если бот заполнил, сервер тихо возвращает «успех» и НЕ шлёт письмо. Уберёте поле или переименуете - откроете спам.
- **Шаблон hreflang/canonical.** НЕ менять *структуру* блока (стр. 10-15): один `canonical`, четыре `alternate` (`et/en/ru/fi`) плюс `x-default`. Меняется только домен внутри. Каждая языковая копия должна ссылаться на один и тот же набор - иначе Google склеит/не так проиндексирует языки.
- **PHPMailer** (`phpmailer/src/*`) и порядок `require` в `lead.php:138-140` - это вендор-библиотека, не редактировать.

## 7.3. Темизация (CSS-переменные)

Вся палитра - в блоке `:root{}` в `index.html`, **строки 627-655**. Меняете значения тут (и в остальных 3 языковых копиях) - перекрашивается весь сайт: hero, кнопки, карточки, линии. Реальные переменные и их назначение:

| Переменная | Значение | Назначение |
|---|---|---|
| `--hero-bg` | `#0b0f15` | Основной тёмный фон hero-секции |
| `--hero-bg-2` | `#101c2c` | Второй тон градиента hero |
| `--hero-text` | `#ffffff` | Текст на тёмном (заголовки hero, телефон в nav) |
| `--hero-text-dim` | `#9fb4c8` | Приглушённый текст на тёмном (адрес в футере) |
| `--body-bg` | `#fafbfc` | Фон светлой части страницы (`body`) |
| `--body-bg-2` | `#edf3fa` | Второй тон / секции-подложки |
| `--body-card` | `#ffffff` | Фон карточек |
| `--body-text` | `#1c2330` | Основной текст на светлом |
| `--body-text-dim` | `#4a5a6b` | Вторичный текст |
| `--body-text-mute` | `#5f6f7c` | Самый тихий текст (подписи) |
| `--line` | `#dde7f0` | Обычные разделители / рамки |
| `--line-strong` | `#c2d3e2` | Усиленные рамки |
| `--line-hero` | `#1e2d3d` | Рамки/разделители на тёмном фоне |
| `--accent` | `#1968cd` | **Главный акцент** - кнопки `.btn-accent`, ссылки, логотип `<b>` |
| `--accent-deep` | `#1450a0` | Тёмный акцент - hover кнопок |
| `--accent-soft` | `#e8f2fc` | Мягкая заливка акцентом (бейджи, подложки) |
| `--accent-line` | `#bdd5f5` | Рамка в тон акценту |
| `--cool` | `#79b6f2` | Дополнительный голубой |
| `--cool-soft` | `#dceafa` | Мягкий голубой |
| `--cool-deep` | `#103a66` | Тёмный голубой |
| `--green` | `#3e7a4a` | Успех (галочки, «0 € скрытых») |
| `--warn` | `#b3452f` | Предупреждение / ошибка |

Ключевые связки (стр. 695-696): `.btn-accent{background:var(--accent)}` и `.btn-accent:hover{background:var(--accent-deep)}`. То есть по сути достаточно поменять `--accent` + `--accent-deep`, чтобы сменить «фирменный цвет» кнопок и ссылок целиком.

**Готовая палитра «тёплое дерево»** (например под забор/столярку/переезды с деревянным брендом) - заменяете строки 627-655:

```css
:root{
  --hero-bg:#1a1410;        /* тёмный кофе вместо сине-чёрного */
  --hero-bg-2:#2a2018;
  --hero-text:#fbf6ef;
  --hero-text-dim:#c9b8a4;

  --body-bg:#faf6f0;        /* тёплый кремовый фон */
  --body-bg-2:#f0e7da;
  --body-card:#fffdf9;
  --body-text:#2b241d;
  --body-text-dim:#5c5044;
  --body-text-mute:#7a6d5d;

  --line:#e7dccb;
  --line-strong:#d3c3ab;
  --line-hero:#3a2e22;

  --accent:#a9611f;         /* тёплое дерево / охра - главный акцент */
  --accent-deep:#824709;
  --accent-soft:#f6ead9;
  --accent-line:#e0c39a;

  --cool:#c99a5b;
  --cool-soft:#f2e5d0;
  --cool-deep:#6b4415;

  --green:#5b7a3e;          /* оливково-зелёный «успех» */
  --warn:#b3452f;
}
```

Проверьте контраст `--accent` на белом (кнопки с белым текстом `.btn-accent{color:#fff}`) - охра `#a9611f` даёт достаточный контраст; если возьмёте светлее, текст кнопки придётся сделать тёмным.

## 7.4. Пошаговый рецепт: клон под компанию заборов

Цель - за один проход получить сайт «Установка заборов» вместо переездов.

1. **Скопировать каркас.** `cp -r staging/ zabor/`. Работать в `zabor/`. Все правки повторять в `zabor/index.html`, `zabor/en/`, `zabor/ru/`, `zabor/fi/` (или удалить ненужные языки вместе с их `hreflang`-строками во всех файлах).

2. **Домен и URL.** `grep -rln "moving24.ee" zabor/` → заменить на новый домен (напр. `aiadpro.ee`) во всех файлах, включая `canonical`/`hreflang` (стр. 10-15), `og:url`, JSON-LD, `sitemap.xml`, `robots.txt`, `llms.txt`.

3. **Бренд, контакты, реквизиты.** Заменить `Moving24` → название; телефон в обоих форматах (`tel:+372...` и видимый); `info@moving24.ee` → новый; `<address>` (стр. 1774-1775): новый адрес, `Reg`/`VAT` нового ООО. Логотип в `.nav-logo img` - подменить файл в `img/`.

4. **Услуги.** В форме `#svcChips` (стр. 1257) переопределить 4 чипса под забор: напр. `private`→«Aiapaigaldus» (монтаж), `business`→«Objektid» (объекты/B2B), `garbage`→«Vana aia demontaaž» (демонтаж старого), `transport`→«Materjali vedu» (доставка материала). Ключи `data-svc` можно оставить теми же - тогда не придётся трогать JS-логику показа полей. Поля формы (`from_address`/`to_address`/`from_floor`/`packing`...) переосмыслить: для забора «этаж/лифт» не нужны - у скрытых блоков `.ff` меняете `data-svc`-список, чтобы, например, `from_floor`/`to_floor`/`packing` не показывались никогда (уберите их из `data-svc`), а добавьте своё поле «Длина забора, м» по образцу существующего `<input>`. Тексты услуг на странице и в `<title>`/`meta description` (стр. 7) переписать под заборы.

5. **Отзывы - только реальные.** Открыть настоящий профиль клиента (Google Business/Facebook). Если отзывы есть - вписать их дословно в JSON-LD `review[]` (стр. 92+), выставить честные `reviewCount` и `ratingValue` (стр. 69-70) и синхронный видимый блок на странице. **Если реального рейтинга нет - удалить целиком `aggregateRating` + `review` и убрать упоминания «5.0 Google'is» из `meta`/hero.** Выдумывать запрещено.

6. **Картинки.** Заменить hero-фон `imagebg-1920.webp/.jpg/-768.webp` и og-image своими (заборы), сохранив имена файлов - тогда пути в HTML/CSS менять не надо. Прочие фото в `img/` - по списку `ls img/`.

7. **Тема.** Вставить палитру «тёплое дерево» из 7.3 в `:root` (стр. 627-655) во всех языковых копиях. Проверить контраст кнопок.

8. **Трекинг.** Создать НОВЫЙ GTM-контейнер для клиента, взять его ID и заменить `GTM-TSG2CVLC` в **двух** местах: `window.M24.GTM` (стр. 271) и `<noscript>`-iframe (стр. 1174). Внутри GTM настроить GA4/Ads/конверсии на уже существующие события (`phone_link_klick`, `email_link_click`, `ajaxComplete` формы) - их в коде НЕ трогаем.

9. **config.php (секреты, вне репо).** На сервере рядом с `lead.php` создать `config.php` вида `<?php return ['maps_key'=>'...','gmail_user'=>'...','gmail_app_password'=>'...','lead_to'=>'zayavki@aiadpro.ee'];`. Без него `lead.php:17` вернёт `500 no-config`. `lead_to` - куда падают заявки; `maps_key` - Google Maps для картинки маршрута в письме (для заборов маршрут не нужен - можно оставить ключ пустым, картинка просто не встроится).

10. **НЕ трогать при клоне:** honeypot `_gotcha` (форма стр. 1256 + `lead.php:20`), скрытые UTM/gclid-поля (стр. 1255), структуру hreflang/canonical, вендор `phpmailer/`, имена событий `dataLayer`. Это то, что делает клон работоспособным «из коробки».

**Финальная проверка:** `grep -rn "moving24\|Moving24\|+37256870101\|Reg 16978239" zabor/` не должен выдавать НИ одного вхождения (кроме, возможно, вашего осознанного). Отправьте тестовую заявку - письмо должно прийти на новый `lead_to`, а бот-заполнение `_gotcha` - НЕ приходить.

---

Ключевые файлы, к которым отсылает секция (абсолютные пути):
- `/Users/dennymansa/Desktop/moving24/staging/index.html` - `:root` палитра (627-655), `window.M24` GTM (271), noscript GTM (1174), форма + honeypot (1254-1300), футер/реквизиты (1771-1776), hreflang/canonical (10-15), review JSON-LD (67-244)
- `/Users/dennymansa/Desktop/moving24/staging/lead.php` - обработчик: config (16-18), honeypot (20), maps_key (65), SMTP-ключи (146-153)
- `/Users/dennymansa/Desktop/moving24/staging/config.php` - секреты (на сервере, не в репо): `maps_key`, `gmail_user`, `gmail_app_password`, `lead_to`


---

# 8. Инвентарь: все страницы и все картинки

Это справочник для того, кто клонирует шаблон под свой бизнес: слева - что лежит в исходниках, справа - где это используется и что менять. Все пути даны от корня `/Users/dennymansa/Desktop/moving24/staging/`.

## 8.1 Все страницы

Всего 37 страниц (`index.html`). Структура: 4 языка (эстонский - в корне без префикса; английский `/en/`; русский `/ru/`; финский `/fi/`), плюс одна отдельная маркетинговая страница `/turg/` (карта рынка, только на русском).

На каждый язык приходится один набор: главная + 4 услуги + "о нас" + FAQ + условия + приватность. URL-слаги локализованы под каждый язык (это важно для SEO), поэтому один и тот же тип страницы называется по-разному в разных папках.

### Эстонский (корень, без языкового префикса) - основной язык

| Файл | URL | Назначение | Ключевые секции |
|---|---|---|---|
| `index.html` | `/` | Главная (кол homepage) | hero + форма заявки, 4 карточки услуг, шаги процесса, галерея работ, упаковочные материалы, партнёры, отзывы, FAQ-тизер, футер |
| `teenused/erakolimine/index.html` | `/teenused/erakolimine/` | Услуга: домашний/квартирный переезд | hero, что входит, упаковка (pack), фото-галерея, форма, FAQ |
| `teenused/arikolimine/index.html` | `/teenused/arikolimine/` | Услуга: офисный/бизнес-переезд | hero, кейсы (IMG_0018/0060), галерея офисов, форма |
| `teenused/suuregabariidiline/index.html` | `/teenused/suuregabariidiline/` | Услуга: крупногабарит + пианино | hero, видео-блоки (krupno-video), до/после, форма |
| `teenused/prugivedu/index.html` | `/teenused/prugivedu/` | Услуга: вывоз мебели/мусора, утилизация | hero, процесс, галерея, форма |
| `meist/index.html` | `/meist/` | О компании | текст о фирме, партнёры, галерея |
| `kkk/index.html` | `/kkk/` | FAQ (частые вопросы) | аккордеон вопрос-ответ |
| `tingimused/index.html` | `/tingimused/` | Условия использования (юр.) | правовой текст, шапка/футер как на сайте |
| `privaatsus/index.html` | `/privaatsus/` | Политика конфиденциальности | правовой текст |

### Английский `/en/`

| Файл | URL | Назначение |
|---|---|---|
| `en/index.html` | `/en/` | Главная (EN) |
| `en/service/home-move/index.html` | `/en/service/home-move/` | Домашний переезд |
| `en/service/business-move/index.html` | `/en/service/business-move/` | Бизнес-переезд |
| `en/service/oversized/index.html` | `/en/service/oversized/` | Крупногабарит/пианино |
| `en/service/junk-removal/index.html` | `/en/service/junk-removal/` | Вывоз мусора |
| `en/about/index.html` | `/en/about/` | О нас |
| `en/faq/index.html` | `/en/faq/` | FAQ |
| `en/terms/index.html` | `/en/terms/` | Условия |
| `en/privacy/index.html` | `/en/privacy/` | Приватность |

### Русский `/ru/`

| Файл | URL | Назначение |
|---|---|---|
| `ru/index.html` | `/ru/` | Главная (RU) |
| `ru/uslugi/chastnyj-pereezd/index.html` | `/ru/uslugi/chastnyj-pereezd/` | Частный переезд |
| `ru/uslugi/biznes-pereezd/index.html` | `/ru/uslugi/biznes-pereezd/` | Бизнес-переезд |
| `ru/uslugi/krupnogabaritnyj/index.html` | `/ru/uslugi/krupnogabaritnyj/` | Крупногабарит |
| `ru/uslugi/vyvoz-musora/index.html` | `/ru/uslugi/vyvoz-musora/` | Вывоз мусора |
| `ru/o-nas/index.html` | `/ru/o-nas/` | О нас |
| `ru/faq/index.html` | `/ru/faq/` | FAQ |
| `ru/tingimused/index.html` | `/ru/tingimused/` | Условия (слаг остался эстонским) |
| `ru/privaatsus/index.html` | `/ru/privaatsus/` | Приватность (слаг эстонский) |

### Финский `/fi/`

| Файл | URL | Назначение |
|---|---|---|
| `fi/index.html` | `/fi/` | Главная (FI) |
| `fi/palvelut/kotimuutto/index.html` | `/fi/palvelut/kotimuutto/` | Домашний переезд |
| `fi/palvelut/yritysmuutto/index.html` | `/fi/palvelut/yritysmuutto/` | Бизнес-переезд |
| `fi/palvelut/raskaat-tavarat/index.html` | `/fi/palvelut/raskaat-tavarat/` | Тяжёлые/крупные вещи |
| `fi/palvelut/romun-poisvienti/index.html` | `/fi/palvelut/romun-poisvienti/` | Вывоз хлама |
| `fi/meista/index.html` | `/fi/meista/` | О нас |
| `fi/ukk/index.html` | `/fi/ukk/` | FAQ |
| `fi/kayttoehdot/index.html` | `/fi/kayttoehdot/` | Условия |
| `fi/tietosuoja/index.html` | `/fi/tietosuoja/` | Приватность |

### Отдельная страница

| Файл | URL | Назначение |
|---|---|---|
| `turg/index.html` | `/turg/` | Внутренняя маркетинговая страница "Карта рынка переездов Эстонии" (конкуренты/ключи/доля рынка). Не часть публичной воронки, язык - русский. Клонирующему её удалять/заменять. |

Схема соответствия типов страниц между языками (что переименовать при клонировании):

| Тип | ET (корень) | EN | RU | FI |
|---|---|---|---|---|
| Главная | `/` | `/en/` | `/ru/` | `/fi/` |
| Дом. переезд | `teenused/erakolimine` | `service/home-move` | `uslugi/chastnyj-pereezd` | `palvelut/kotimuutto` |
| Бизнес-переезд | `teenused/arikolimine` | `service/business-move` | `uslugi/biznes-pereezd` | `palvelut/yritysmuutto` |
| Крупногабарит | `teenused/suuregabariidiline` | `service/oversized` | `uslugi/krupnogabaritnyj` | `palvelut/raskaat-tavarat` |
| Вывоз мусора | `teenused/prugivedu` | `service/junk-removal` | `uslugi/vyvoz-musora` | `palvelut/romun-poisvienti` |
| О нас | `meist` | `about` | `o-nas` | `meista` |
| FAQ | `kkk` | `faq` | `faq` | `ukk` |
| Условия | `tingimused` | `terms` | `tingimused` | `kayttoehdot` |
| Приватность | `privaatsus` | `privacy` | `privaatsus` | `tietosuoja` |

## 8.2 Все картинки

Общий принцип шаблона: **каждая контентная фотография лежит в двух форматах - `.jpg` (fallback) и `.webp` (современный, легче).** В HTML они подаются через `<picture>` с `<source type="image/webp">`. Логотипы партнёров - в `.svg` (векторные, без дублей) либо `.webp`. Иконки упаковки - `.svg` (вектор) + растровые `.jpg`/`.webp` дубли. Видео крупногабарита - `.mp4` с постером `.jpg`.

### 8.2.1 Hero-фоны (фоновая картинка первого экрана)

Лежат в **корне** `staging/` (не в `img/`), потому что задаются как CSS `background-image` и должны грузиться максимально рано.

| Файл | Формат | Где используется | Зачем |
|---|---|---|---|
| `imagebg-1920.webp` | webp | CSS-фон hero, десктоп. Прописан в **71** HTML-файле | Основной фоновый фон первого экрана на широких экранах |
| `imagebg-1920.jpg` | jpg | fallback к тому же фону | Резерв для браузеров без webp |
| `imagebg-768.webp` | webp | CSS-фон hero, мобильный (`max-width:768`). В **7** файлах | Облегчённый фон для телефонов |
| `img/m24-hero-vans-768.webp` | webp | `<img>`/preload внутри hero на главных (8 файлов), парой с `imagebg-1920.webp` | Фото фургонов Moving24 поверх/в hero; в preload для LCP |

Замена при клонировании: подменить `imagebg-1920.*` и `imagebg-768.webp` на свой брендовый фон (сохранить те же имена, чтобы не трогать CSS в 71 файле), и `m24-hero-vans-768.webp` - на своё hero-фото.

### 8.2.2 Карточки услуг (блок "услуги" на главной + hero услуг)

| Файл (jpg+webp) | Секция | Alt в исходнике | Зачем |
|---|---|---|---|
| `img/m24-step-house.*` | Карточка "домашний переезд" | `Kodukolimine: tõstukiga kaubik maja ees` | Иллюстрация услуги дом. переезда |
| `img/m24-svc-office.*` | Карточка "офисный переезд" | `Kontorikolimine: Moving24 kaubikud` | Услуга офис/бизнес |
| `img/m24-svc-heavy.*` | Карточка "крупногабарит/пианино" | `Klaveri ja raskete esemete vedu` | Услуга тяжёлых вещей |
| `img/m24-step-util.*` | Карточка "вывоз мусора" | `Mööbli ja prügi äravedu utiliseerimiseks` | Услуга утилизации |

Эти четыре - в связке (4 карточки услуг). Ссылаются 4 файла главных (по одному на язык). Меняются под 4 услуги клиента.

### 8.2.3 Галерея работ (сетка фото "наши работы")

Основная галерея-сетка на главной (строки ~1676-1685 в `index.html`) и в облегчённом виде на страницах услуг.

| Файл (только jpg) | Где | Зачем |
|---|---|---|
| `img/m24-gal29.jpg` | Самая частая - в **20** файлах | Ключевое фото галереи / превью |
| `img/m24-gal10.jpg` | 13 файлов | Галерея |
| `img/m24-gal7.jpg`, `m24-gal12.jpg`, `m24-gal22.jpg`, `m24-gal23.jpg`, `m24-gal25.jpg`, `m24-gal35.jpg`, `m24-gal42.jpg` | по 9 файлов | Основная сетка галереи на главных |
| `img/m24-gal1.jpg`, `m24-gal2.jpg`, `m24-gal3.jpg` | по 4 файла | Галерея на отдельных страницах услуг |

Замечание: галерейные `m24-gal*` идут **только в jpg** (без webp-дублей) - это осознанное упрощение для второстепенной сетки. Клонирующему: заменить своими фото работ; можно оставить только jpg.

### 8.2.4 Дополнительные тематические фото (галерея / врезки)

| Файл (jpg+webp) | Где (кол-во файлов) | Зачем |
|---|---|---|
| `img/g-office1.*` | 3 | Фото офисного переезда |
| `img/g-office2.*` | 16 | Офис - в галерее большинства страниц |
| `img/g-office3.*` | 7 | Офис, врезка (рядом с `IMG_0061` в блоке партнёров/траста на главной) |
| `img/g-heavy1.*` | 16 | Тяжёлые/крупные вещи - широко по галереям |
| `img/g-pack1.*` | 16 | Процесс упаковки |
| `img/g-pack2.*` | 16 | Процесс упаковки |
| `img/IMG_0061.*` | 7 | Реальное фото (врезка доверия на главной, блок ~строка 1373) |
| `img/IMG_0018.*` | 3 (дом-переезд EN/RU/FI) | Кейс/фото на странице домашнего переезда |
| `img/IMG_0060.*` | 3 (дом-переезд EN/RU/FI) | Кейс/фото на странице домашнего переезда |

### 8.2.5 Крупногабарит и видео (страница "oversized")

Используются только на страницах крупногабарита (по 4 файла - 4 языка). Здесь единственное на сайте видео.

| Файл | Формат | Зачем |
|---|---|---|
| `img/m24-krupno-video.mp4` | mp4 | Видео перевозки крупногабарита (блок 1) |
| `img/m24-krupno-video2.mp4` | mp4 | Второе видео (блок 2) |
| `img/m24-krupno-poster.jpg` | jpg | Постер (превью до старта) для video 1 |
| `img/m24-krupno-poster2.jpg` | jpg | Постер для video 2 |
| `img/m24-krupno-main.jpg` | jpg | Главное фото секции |
| `img/m24-krupno-wide.jpg` | jpg | Широкий баннер секции |
| `img/m24-krupno1.jpg`, `m24-krupno2.jpg` | jpg | Доп. фото крупногабарита |
| `img/m24-industrial.jpg` | jpg | Только `ru/index.html` (1 файл) - индустриальная врезка на русской главной |
| `img/m24-util.jpg` | jpg | 4 файла - утилизация/вывоз |
| `img/m24-pereezd-hero.jpg` | jpg | Только `ru/uslugi/chastnyj-pereezd/` (1 файл) - hero русской страницы частного переезда |

Клонирующему: если у бизнеса нет видео - удалить `.mp4`/постеры и заменить блок статичным фото. `m24-industrial.jpg` и `m24-pereezd-hero.jpg` - "сироты" (по 1 ссылке), это остатки локальных правок; можно удалить/заменить.

### 8.2.6 Упаковочные материалы (блок "мы дадим коробки/материалы")

Папка `img/pack/`. Каждый предмет в трёх формах: `.svg` (векторная иконка), `.jpg` + `.webp` (фото). Используется на главных и страницах переездов (15 файлов).

| Файл | Формат | Что | Зачем |
|---|---|---|---|
| `img/pack/box.svg` / `.jpg` / `.webp` | svg+jpg+webp | Картонная коробка | Иконка/фото упаковочного материала |
| `img/pack/wardrobe.svg` / `.jpg` / `.webp` | svg+jpg+webp | Гардеробная коробка (для одежды) | То же |
| `img/pack/bubble.svg` / `.jpg` / `.webp` | svg+jpg+webp | Пузырчатая плёнка | То же |

В HTML (напр. `teenused/erakolimine/index.html`, строки 1233-1235) подаётся связкой из трёх позиций. Меняется под материалы, которые выдаёт клиент.

### 8.2.7 Логотипы партнёров (лента "нам доверяют")

Папка `img/partners/`. Бегущая лента логотипов на главной (блок ~строка 1532, дублируется трижды для бесшовной анимации) и на "о нас". Векторные - `.svg`; растровые/сложные - `.webp` (в двух размерах `-102`/`-132` под retina).

| Файл | Формат | Партнёр |
|---|---|---|
| `bolt.svg` | svg | Bolt |
| `lhv.svg` | svg | LHV (банк) |
| `wallester.svg` | svg | Wallester |
| `bauhof.svg` | svg | Bauhof |
| `mapon.svg` | svg | Mapon |
| `pohjala.svg` | svg | Põhjala |
| `placet.svg` | svg | Placet |
| `intercars.svg` | svg | Inter Cars |
| `adbaltic.svg` | svg | AD Baltic |
| `olerex.webp` | webp | Olerex |
| `alexela.webp` | webp | Alexela |
| `pakendikeskus.png` + `pakendikeskus-102.webp` + `pakendikeskus-132.webp` | png+webp x2 | Pakendikeskus (в ленте берётся `-132.webp`) |
| `admirals-logo.png` + `admirals-102.webp` + `admirals-132.webp` | png+webp x2 | Admirals (в ленте `-132.webp`) |
| `fohow-icon.png` + `fohow-icon.webp` | png+webp | Fohow (иконка, повторяется в ленте) |

Клонирующему: полностью заменить своими логотипами клиентов/партнёров, сохранив приём "svg для простых, webp `-132` для сложных". `.png` здесь - legacy fallback к webp.

### 8.2.8 Служебные / SEO-картинки

| Файл | Формат | Где (кол-во) | Зачем |
|---|---|---|---|
| `img/m24-logo.png` + `img/m24-logo.webp` | png+webp | 37 файлов (все страницы) | Логотип в шапке. png - fallback, webp - основной |
| `img/og.jpg` | jpg | 36 файлов | Open Graph / Twitter-card превью для соцсетей и мессенджеров (в `<meta og:image>`). Меняется под бренд |

---

**Итог для клонирующего.** Обязательно заменить: hero-фоны (`imagebg-*`, `m24-hero-vans-768.webp`), 4 карточки услуг (`m24-step-house`, `m24-svc-office`, `m24-svc-heavy`, `m24-step-util`), логотип (`m24-logo.*`), OG-превью (`og.jpg`), логотипы партнёров (`img/partners/*`). Заменить по смыслу: галерею (`m24-gal*`, `g-*`, `IMG_*`), упаковку (`img/pack/*`), крупногабарит/видео (`m24-krupno*`, `*.mp4`). Сохранять имена файлов при замене - тогда HTML/CSS в десятках файлов трогать не нужно. Соблюдать парность `jpg`+`webp` для контентных фото и одиночный `svg` для простых логотипов/иконок.


---

# 9. Анатомия страницы, структура и SEO

Эта секция разбирает одну реальную страницу услуги (`/teenused/prugivedu/` - вывоз и утилизация мебели) как эталонный шаблон: из чего она собрана сверху вниз, как связаны URL / canonical / hreflang / sitemap, как правильно наращивать локальные страницы по городам и что проверять по чеклисту перед публикацией каждой страницы.

Все примеры кода ниже - дословные цитаты из `/Users/dennymansa/Desktop/moving24/staging/teenused/prugivedu/index.html`, `/Users/dennymansa/Desktop/moving24/staging/sitemap.xml` и `/Users/dennymansa/Desktop/moving24/staging/.htaccess`. Когда будете клонировать шаблон под другой бизнес, меняете тексты и schema, а каркас оставляете.

## 9.1. Анатомия страницы услуги (сверху вниз)

Порядок блоков в `<body>` строго один и тот же на всех страницах услуг. Именно это делает шаблон переиспользуемым: копируете файл, меняете только тексты внутри блоков.

### 9.1.1. `<head>`: техническая часть (строки 3-441)

Идёт до любого видимого контента. Порядок важен для скорости (см. 9.5):

1. **Кодировка и viewport** (строки 4-5) - обязательны первыми.
2. **`<title>` и `<meta name="description">`** (строки 6-7) - уникальны для каждой страницы:
   ```html
   <title>Vana mööbli äravedu ja utiliseerimine Tallinnas</title>
   <meta name="description" content="Vana mööbli ja koli äravedu Tallinnas koos utiliseerimisega. Kiire, korrektne ja ausa hinnaga. 5.0 Google'is. Küsi tasuta pakkumist!">
   ```
   Формула title: `<что за услуга> + <город>`. Description: выгода + город + соц-доказательство (рейтинг) + призыв.
3. **Canonical + hreflang + x-default** (строки 10-15) - разбор в 9.2.
4. **Open Graph + Twitter Card** (строки 16-26) - для превью в соцсетях и мессенджерах.
5. **Четыре блока JSON-LD** (строки 27-87 в `<head>` + строки 985-987 перед `</body>`) - разбор в 9.3.
6. **GTM-контейнер с Consent Mode** (строки 88-100) - грузится только на боевом хосте (gate по `location.hostname`).
7. **Preconnect / preload** критичных ресурсов (строки 101-106): hero-картинка + шрифты.
8. **Инлайн `@font-face` и весь CSS** (строки 107-441) - вшиты в `<head>`, внешних CSS-файлов нет (важно для скорости, см. 9.5).

### 9.1.2. Навигация (строки 998+)

Плавающая «таблетка» `nav-pill` со `sticky`-позиционированием, логотип с `<picture>` (webp + png fallback), выпадающие меню услуг, телефон и CTA-кнопка. Одинаковая на всех страницах.

### 9.1.3. Герой (`<section class="hero">`, строки 1048-1106)

Первый экран, самая конверсионная зона. Составные части:

- **Фоновое фото** отдельным слоем: `<div class="hero-photo-bg"></div>` (строка 1049). Само фото задаётся в CSS (`background:url('/imagebg-1920.webp')`) и предзагружается через `<link rel="preload" as="image" ... fetchpriority="high">`.
- **Kicker** рукописным шрифтом-зацепка (строка 1053): `Vana mööbel jalus?` (класс `hero-kicker hand`).
- **Trust-строка со звёздами и рейтингом** (строки 1054-1059): `★★★★★ 5.0 · 37 arvustust Google'is`.
- **Единственный `<h1>`** (строка 1060):
  ```html
  <h1>Vana mööbli ja kodumasinate äravedu</h1>
  ```
  H1 на странице ровно один и совпадает по смыслу с title и услугой.
- **Две CTA-кнопки** (строки 1061-1064): «Esita päring →» (якорь `#form`) и «Helista +372 5687 0101» (`tel:`).
- **Форма-лид** `form-card` (строки 1067-1097): чипы выбора услуги (`radiogroup`), скрытые UTM/gclid-поля, honeypot `_gotcha` (антиспам), поля адресов «Kust/Kuhu», выбор этажа/лифта/даты/времени, загрузка фото, согласие с политикой. Форма условно показывает поля в зависимости от выбранной услуги (`data-svc`).
- **Полоса статистики** `hero-stats` (строки 1100-1104): `24/7`, `0 € varjatud lisatasusid`, `4500+ edukat kolimist`.

### 9.1.4. Контентные секции (строки 1107+)

Все обёрнуты в `<section class="section">` / `.section--alt` (чередование фона) с `<div class="wrap">` внутри. Порядок:

1. **Лид-абзац** (строка 1107) - один абзац `lead lead--lg`, задаёт контекст.
2. **«Mida me ära veame»** - сетка карточек `svc-cards`, каждая с `<h3>` и описанием (что именно входит в услугу).
3. **«Miks valida Moving24»** - список преимуществ `svc-bens` с ценой, скоростью, легальностью, рейтингом.
4. **Мини-CTA** `svc-cta` - повтор призыва по центру страницы.
5. **Галерея** `gal` (строки 1123-1133) - фото с `loading="lazy"` и осмысленными `alt` (см. 9.5).
6. **FAQ** (`<section id="kkk">`, строки 1136-1143) - видимый аккордеон вопросов-ответов; его текст обязан совпадать с FAQPage-schema (9.3.3).
7. **Финальный CTA** `cta-final` (строки 1145+) - крупный призыв на тёмном фоне.
8. **Футер** с логотипом, контактами, ссылками на услуги и юридические страницы.

**Правило шаблона:** видимый H1, видимые вопросы FAQ и видимый список услуг должны текстуально совпадать с тем, что зашито в JSON-LD. Google не любит schema, которой нет на странице.

## 9.2. Связка URL / canonical / hreflang / sitemap

Это ядро мультиязычного SEO. Ошибка здесь ломает индексацию сразу на 4 языках.

### 9.2.1. Схема URL

Каждая услуга существует в 4 языковых версиях с человекочитаемым путём на своём языке (не `?lang=`, а отдельные папки):

| Язык | URL услуги «вывоз мусора» |
|------|---------------------------|
| ET (базовый) | `https://moving24.ee/teenused/prugivedu/` |
| EN | `https://moving24.ee/en/service/junk-removal/` |
| RU | `https://moving24.ee/ru/uslugi/vyvoz-musora/` |
| FI | `https://moving24.ee/fi/palvelut/romun-poisvienti/` |

Эстонский - корень (без языкового префикса), остальные под `/en/`, `/ru/`, `/fi/`. Все URL заканчиваются слэшем (папка + `index.html`).

### 9.2.2. Canonical

Каждая страница указывает canonical сама на себя (строка 10):
```html
<link rel="canonical" href="https://moving24.ee/teenused/prugivedu/">
```
canonical - абсолютный, с `https`, с завершающим слэшем, совпадает с `<loc>` в sitemap. Языковые версии НЕ канонизируются друг на друга - у каждой свой self-canonical, а связывает их hreflang.

### 9.2.3. Hreflang

Блок из 5 строк, идентичный на всех 4 языковых версиях одной услуги (строки 11-15):
```html
<link rel="alternate" hreflang="et" href="https://moving24.ee/teenused/prugivedu/">
<link rel="alternate" hreflang="en" href="https://moving24.ee/en/service/junk-removal/">
<link rel="alternate" hreflang="ru" href="https://moving24.ee/ru/uslugi/vyvoz-musora/">
<link rel="alternate" hreflang="fi" href="https://moving24.ee/fi/palvelut/romun-poisvienti/">
<link rel="alternate" hreflang="x-default" href="https://moving24.ee/teenused/prugivedu/">
```
Правила hreflang, которые нельзя нарушать:
- **Взаимность.** Если ET ссылается на EN, то EN обязан сослаться на ET. Все 4 версии содержат один и тот же набор из 5 строк.
- **Самоссылка.** Каждая версия включает hreflang на саму себя.
- **x-default** указывает на эстонскую (базовую) версию - её показывают тем, для кого нет подходящего языка.
- **Абсолютные URL** с завершающим слэшем.

### 9.2.4. Sitemap

`sitemap.xml` дублирует ту же hreflang-связку, но уже средствами `xhtml:link` внутри каждого `<url>`. Namespace объявлен в корне (строка 2):
```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
```
Запись одной услуги (строки 135-145) - каждый язык это отдельный `<url>`, но с полным набором alternate-ссылок:
```xml
<url>
  <loc>https://moving24.ee/teenused/prugivedu/</loc>
  <lastmod>2026-07-06</lastmod>
  <changefreq>weekly</changefreq>
  <priority>0.8</priority>
  <xhtml:link rel="alternate" hreflang="et" href="https://moving24.ee/teenused/prugivedu/"/>
  <xhtml:link rel="alternate" hreflang="en" href="https://moving24.ee/en/service/junk-removal/"/>
  <xhtml:link rel="alternate" hreflang="ru" href="https://moving24.ee/ru/uslugi/vyvoz-musora/"/>
  <xhtml:link rel="alternate" hreflang="fi" href="https://moving24.ee/fi/palvelut/romun-poisvienti/"/>
  <xhtml:link rel="alternate" hreflang="x-default" href="https://moving24.ee/teenused/prugivedu/"/>
</url>
```
Приоритеты: главные страницы `priority=1.0`, `changefreq=weekly` (строки 3-46); страницы услуг и остальные - `priority=0.8`. `lastmod` обновляется при каждой правке.

**Три источника правды об URL должны совпадать до символа:** (1) `<link canonical>` и `hreflang` в `<head>` каждой страницы, (2) `<loc>` и `xhtml:link` в sitemap, (3) реальный путь файла на диске. Любое расхождение (лишний/пропущенный слэш, http вместо https) - это баг индексации.

## 9.3. JSON-LD schema: четыре блока на странице услуги

Страница несёт 4 разных типа structured data. Первые два (организация и сайт) одинаковы на всех страницах, последние два (Service и BreadcrumbList) уникальны для страницы + FAQPage при наличии FAQ.

### 9.3.1. MovingCompany (организация, строки 27-86)

Идентичен на всех страницах. Описывает сам бизнес: имя, телефон, адрес, гео-координаты, VAT, часы работы, соцсети и - ключевое для локального SEO - `areaServed` со списком районов и городов (строки 49-66):
```json
"areaServed": [
  "Tallinn", "Kesklinn", "Lasnamäe", "Mustamäe", "Õismäe",
  "Haabersti", "Kristiine", "Põhja-Tallinn", "Pirita", "Nõmme",
  "Harjumaa", "Maardu", "Viimsi", "Saue", "Keila", "Estonia"
]
```
Под другой бизнес меняете `@type` (например `Plumber`, `Electrician`, `HVACBusiness`), `name`, `telephone`, `address`, `geo`, `vatID`, `areaServed` и `sameAs`.

### 9.3.2. Service (сама услуга, строка 986)

Уникален для страницы. Описывает конкретную услугу и её зону покрытия:
```json
{"@context": "https://schema.org", "@type": "Service",
 "name": "Vana mööbli ja kodumasinate äravedu",
 "description": "Vana mööbli, kodumasinate ja muu koli äravedu Tallinnas, sageli juba samal päeval. Veame ära ja anname käitlusse. Küsi hinda.",
 "provider": {"@type": "MovingCompany", "name": "Moving24", "telephone": "+372 5687 0101", "url": "https://moving24.ee/"},
 "areaServed": ["Tallinn", "Harjumaa", "Estonia"],
 "url": "https://moving24.ee/teenused/prugivedu/"}
```
`name` совпадает по смыслу с H1. `url` совпадает с canonical. `areaServed` тут короче, чем у организации - это зона именно этой услуги.

### 9.3.3. FAQPage (строка 985)

Отражает видимый FAQ-блок (`<section id="kkk">`). Каждый вопрос - `Question` с вложенным `acceptedAnswer` типа `Answer`. Первый вопрос из реального файла:
```json
{"@type": "Question", "name": "Kui palju maksab vana mööbli äravedu?",
 "acceptedAnswer": {"@type": "Answer",
 "text": "Äraveo ja utiliseerimise orienteeruv hind on 30 €/m3, millele lisandub tõstjate töö. Täpse summa ütleme ette mahu, korruse ja juurdepääsu järgi - üllatusi arvel pole."}}
```
Всего 6 вопросов. **Текст в schema обязан дословно повторять видимые вопросы и ответы на странице** - иначе Google снимет rich-результат. Обратите внимание: даже здесь соблюдён запрет на длинное тире, везде дефис.

### 9.3.4. BreadcrumbList (строка 987)

Хлебные крошки для отображения пути в выдаче:
```json
{"@context": "https://schema.org", "@type": "BreadcrumbList",
 "itemListElement": [
   {"@type": "ListItem", "position": 1, "name": "Avaleht", "item": "https://moving24.ee/"},
   {"@type": "ListItem", "position": 2, "name": "Utiliseerimine", "item": "https://moving24.ee/teenused/prugivedu/"}
 ]}
```
Два уровня: главная → страница услуги. `item` последнего уровня = canonical этой страницы.

## 9.4. Как правильно делать страницы по ГОРОДАМ (локальное SEO)

Городские страницы (например `/teenused/prugivedu-tartu/` - «вывоз мусора в Тарту») - главный способ масштабировать локальный трафик. Но это зона риска: сделанные небрежно, они превращаются в doorway-страницы и попадают под фильтр за тонкий/дублированный контент. Правила:

### 9.4.1. Уникальный контент, а не подмена города

Нельзя взять `prugivedu/index.html`, заменить «Tallinn» на «Tartu» и опубликовать - это тонкий дубль. На каждой городской странице переписывайте под местную реальность:
- **H1, title, description** с названием города: `Vana mööbli äravedu ja utiliseerimine Tartus`.
- **Лид-абзац и «Miks meie»** - местные детали: районы города, местная свалка/`jäätmejaam`, время выезда из вашей базы, локальные ориентиры в плейсхолдерах формы (в шаблоне они эстолица-специфичны: `nt. Rotermanni 18, Tallinn`, строка 1085 - под город меняете на местную улицу).
- **FAQ** - хотя бы часть вопросов адаптировать под город (куда возим отходы в этом городе, обслуживаем ли пригороды).
- **Фото галереи** - в идеале с местных объектов; как минимум `alt` с названием города.

### 9.4.2. `areaServed` под конкретный город

В MovingCompany и Service меняете `areaServed` на районы этого города и его пригород. Для Тарту это был бы список районов Тарту + Tartumaa вместо таллинского набора из строк 49-66. Так вы явно сообщаете Google зону покрытия страницы.

### 9.4.3. URL, canonical, hreflang, sitemap для города

Городская страница - полноценный участник схемы из 9.2:
- Свой человекочитаемый путь на каждом языке (`/teenused/prugivedu-tartu/`, `/en/service/junk-removal-tartu/` и т.д.).
- Self-canonical на себя.
- Полный набор из 5 hreflang для 4 языков + x-default.
- Отдельная запись `<url>` в sitemap.xml с `xhtml:link` (по образцу строк 135-178), `priority` порядка 0.7.
- Обновить `lastmod`.

### 9.4.4. Перелинковка

Городские страницы не должны висеть в вакууме:
- Ссылка с общей страницы услуги (`/teenused/prugivedu/`) вниз, в блок «Piirkonnad» - в шаблоне уже есть готовый компонент `area-pills` (CSS на строке 439, секция `#piirkonnad`), это ряд «таблеток» с районами/городами. Каждую делаете ссылкой на городскую страницу.
- Обратная ссылка с городской страницы на общую услугу и на главную (хлебные крошки это уже дают).
- Взаимная перелинковка соседних городов, где уместно.

### 9.4.5. 301 при смене/склейке URL

Если городская или услуговая страница переезжает на новый URL (или вы схлопываете старые WordPress-адреса), ставьте 301 в `.htaccess`. В проекте это целый блок «old WordPress URLs → new equivalents» (строки 7-41), например:
```apache
RedirectMatch 301 ^/en/service/garbage-collection/?$   /en/service/junk-removal/
RedirectMatch 301 ^/teenused/raskete-esemete-teisaldamine/?$  /teenused/suuregabariidiline/
```
Паттерн `?$` ловит адрес и со слэшем, и без. Старые sitemap-ы Yoast тоже редиректятся на новый (строки 10-12). Это сохраняет накопленный вес ссылок и позиции при переезде. Каждый добавленный/переименованный URL города - повод проверить, не нужен ли 301 со старого адреса.

## 9.5. SEO-чеклист на каждую страницу (перед публикацией)

Прогоняйте по этому списку любую новую или изменённую страницу. В скобках - где смотреть эталон в `prugivedu/index.html`.

**Мета и заголовки**
- [ ] `<title>` уникален, формула `услуга + город`, длина адекватна выдаче (строка 6).
- [ ] `<meta name="description">` уникален, с выгодой + городом + рейтингом + призывом (строка 7).
- [ ] Ровно один `<h1>`, совпадает по смыслу с title и услугой (строка 1060).
- [ ] Подзаголовки `<h2>`/`<h3>` в логичной иерархии, без пропусков уровней.

**Canonical / hreflang / язык**
- [ ] `<html lang="...">` соответствует языку страницы (строка 2 - `lang="et"`).
- [ ] Self-canonical, абсолютный, https, со слэшем (строка 10).
- [ ] Полный блок hreflang: 4 языка + x-default, взаимные, с самоссылкой (строки 11-15).
- [ ] Страница добавлена в `sitemap.xml` отдельным `<url>` с `xhtml:link`, обновлён `lastmod`.
- [ ] При переезде URL - 301 в `.htaccess` со старого адреса.

**Structured data (JSON-LD)**
- [ ] MovingCompany/локальный бизнес присутствует, `areaServed` актуален для страницы (строки 27-86).
- [ ] Service с `name` = H1, `url` = canonical, своим `areaServed` (строка 986).
- [ ] FAQPage совпадает дословно с видимым FAQ-блоком (строка 985 vs `<section id="kkk">`).
- [ ] BreadcrumbList, последний `item` = canonical (строка 987).
- [ ] Все schema-тексты без длинного тире (только дефис).

**Social / OG**
- [ ] OG-теги: `og:url` = canonical, `og:title`, `og:description`, `og:image` 1200×630, `og:locale` под язык (строки 16-26).
- [ ] Twitter Card `summary_large_image` (строки 23-26).

**Изображения**
- [ ] У всех значимых `<img>` осмысленный `alt` (галерея, строки 1128-1130: `alt="Kolu äravedu ja utiliseerimine - furgoon täis"`).
- [ ] Указаны `width`/`height` (защита от layout shift).
- [ ] `<picture>` с webp + fallback для логотипа/ключевых картинок (строка 1000).
- [ ] Ниже первого экрана - `loading="lazy"` (строки 1128-1130).

**Скорость (Core Web Vitals)**
- [ ] Hero-картинка в `<link rel="preload" as="image" fetchpriority="high">` (строка 102).
- [ ] Шрифты `preload` + `font-display:swap`, подмножества по `unicode-range` (строки 104-106, 107-438).
- [ ] CSS вшит в `<head>` инлайном, внешних блокирующих CSS нет (строки 107-441).
- [ ] `preconnect` к домену тега/аналитики (строка 101).
- [ ] Сжатие (`mod_deflate`) и кэш статики на год (`.htaccess`, строки 55-71); HTML - `access plus 0 seconds`.

**Индексация (критично при выкатке)**
- [ ] На боевом домене снят `X-Robots-Tag "noindex, nofollow"` - в стейджинге он стоит в `.htaccess` (строки 46-47) и намеренно блокирует индексацию. При переезде на `moving24.ee` эту строку обязательно удалить, иначе весь сайт выпадет из индекса (в комментарии прямо помечено, что из-за неё PSI SEO=69).

---

**Файлы, использованные для этой секции (абсолютные пути):**
- `/Users/dennymansa/Desktop/moving24/staging/teenused/prugivedu/index.html`
- `/Users/dennymansa/Desktop/moving24/staging/sitemap.xml`
- `/Users/dennymansa/Desktop/moving24/staging/.htaccess`


---

# 10. Миграция со старого сайта + производительность

Эта секция описывает самый нервный момент проекта: замену уже работающего (обычно WordPress) сайта на новый статический шаблон на хостинге zone.ee, без потери позиций в Google. Всё, что ниже, основано на реальном `.htaccess` из `/Users/dennymansa/Desktop/moving24/staging/.htaccess` и опыте с moving24.ee. Пути и правила приведены дословно - меняй только домены и слаги под свой бизнес.

## 10.1 Общая логика миграции (почему по шагам)

Ключевая проблема: у zone.ee (Apache + классический shared-хостинг с `htdocs/`) старый WordPress оставляет после себя `index.php`, `.htaccess` WordPress, папку `wp-content` и т.д. Если ты просто зальёшь новые файлы ПОВЕРХ, то:

- старый `index.php` перебьёт твой новый `index.html` (Apache по DirectoryIndex обычно отдаёт `index.php` раньше `index.html`);
- старые WordPress-правила в `.htaccess` (`RewriteRule . /index.php`) перехватят все URL и уведут их обратно в мёртвый движок;
- останется мусор (плагины, кэш, старые sitemap), который Google продолжит краулить.

Поэтому порядок жёсткий: снапшот -> полный wipe -> заливка нового -> снятие noindex -> редиректы -> работа в Search Console.

## 10.2 Шаг 1. Снапшот старого сайта (обязательно, до любых действий)

Перед тем как что-либо трогать на боевом хостинге, забери полную копию. Она нужна на два случая: (а) откатиться, если что-то пойдёт не так; (б) вытащить из старого `.htaccess` / sitemap реальные старые URL, чтобы построить 301-редиректы.

Что снять:

- Весь `htdocs/` (или `public_html/`) целиком - по FTP/SFTP zone.ee или через файловый менеджер в панели.
- Старый `.htaccess` отдельно (в нём часто уже есть чужие редиректы, которые нельзя терять).
- Дамп базы MySQL, если это WordPress (не для переноса контента, а как страховка).
- Скриншот текущего PageSpeed и текущих позиций/списка страниц из Google Search Console.

Практично сложить снапшот рядом с проектом, например `/Users/dennymansa/Desktop/<проект>/old-site-snapshot-YYYYMMDD/`, и не удалять его минимум пару месяцев после переезда.

## 10.3 Шаг 2. Полный wipe `htdocs` (не заливать поверх)

На zone.ee зайди в файловый менеджер или по SFTP и удали ВСЁ содержимое `htdocs/` до пустой папки. Именно удали, а не «залей сверху». Причина - в комментарии нашего рабочего `.htaccess`:

```
# Apache config for zone.ee (Apache). GitHub Pages ignores this file.
```

zone.ee - это Apache, он уважает `.htaccess` и `DirectoryIndex`. Если оставить старый `index.php`, твой новый `index.html` не откроется на корне. Симптом «залил новый сайт, а на главной всё ещё старый WordPress» - это ровно оставшийся `index.php`.

После очистки залей чистую сборку из `deploy/` (боевой вариант) в `htdocs/`. Проверь, что `.htaccess` из твоего репозитория попал в корень и что в корне нет ни одного `.php`.

## 10.4 Шаг 3. Снять noindex (иначе весь трафик умрёт)

В staging-версии `.htaccess` стоит намеренная блокировка индексации, чтобы тестовый поддомен не попал в Google:

```apache
<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  # !!! STAGING ONLY - REMOVE THIS LINE AT moving24.ee CUTOVER (blocks ALL indexing, PSI SEO=69 is caused by this) !!!
  Header always set X-Robots-Tag "noindex, nofollow"
  Header always set X-Frame-Options "SAMEORIGIN"
  ...
</IfModule>
```

Этот `X-Robots-Tag: noindex, nofollow` полностью запрещает Google индексировать сайт и, как отмечено в комментарии, роняет SEO-оценку в PageSpeed до 69. На боевом домене эту строку надо УДАЛИТЬ. В нашем проекте это уже сделано в `deploy/.htaccess` - сравни сам:

```
$ diff staging/.htaccess deploy/.htaccess
...
< # !!! STAGING ONLY - REMOVE THIS LINE AT moving24.ee CUTOVER ... !!!
< Header always set X-Robots-Tag "noindex, nofollow"
```

То есть боевая версия отличается от staging тремя вещами: (1) убран `X-Robots-Tag noindex`, (2) включён HSTS (`Strict-Transport-Security`), (3) базовый путь в комментарии - корень `/`, а не `/moving24-landing/`.

Дополнительно проверь на боевом:

- `robots.txt` разрешает краул. Наш файл (`staging/robots.txt`):

```
User-agent: *
Allow: /

# Privacy pages are crawlable but carry <meta name="robots" content="noindex">

Sitemap: https://moving24.ee/sitemap.xml
```

- В самих HTML нет случайного `<meta name="robots" content="noindex">` на индексируемых страницах (у нас noindex стоит только на юридических страницах - это норма).

## 10.5 Шаг 4. 301-редиректы со старых URL на новые

Это сердце сохранения SEO. У WordPress-сайта слаги были другие (у Yoast ещё и свои sitemap-файлы). Каждый старый URL, который имел трафик или ссылки, надо через 301 перенаправить на его новый эквивалент - иначе весь накопленный вес страницы теряется, и пользователь ловит 404.

Полный рабочий блок из `staging/.htaccess` (это готовый образец структуры - меняешь слаги под свой бизнес):

```apache
# --- 301 redirects: old WordPress URLs -> new equivalents (from GSC, SEO preservation) ---
<IfModule mod_alias.c>
  # old WordPress (Yoast) sitemaps -> new sitemap
  RedirectMatch 301 ^/sitemap_index\.xml$ /sitemap.xml
  RedirectMatch 301 ^/page-sitemap\.xml$  /sitemap.xml
  RedirectMatch 301 ^/post-sitemap\.xml$  /sitemap.xml
  # EN
  RedirectMatch 301 ^/en/service/garbage-collection/?$          /en/service/junk-removal/
  RedirectMatch 301 ^/en/service/moving-for-business/?$         /en/service/business-move/
  RedirectMatch 301 ^/en/service/corporate-services/?$          /en/service/business-move/
  RedirectMatch 301 ^/en/service/moving-for-individuals/?$      /en/service/home-move/
  RedirectMatch 301 ^/en/service/moving-heavy-objects/?$        /en/service/oversized/
  RedirectMatch 301 ^/en/service/moving-services/?$             /en/
  RedirectMatch 301 ^/en/service/about-us/?$                    /en/about/
  RedirectMatch 301 ^/en/mission-and-values-of-moving24/?$      /en/about/
  RedirectMatch 301 ^/en/contact/?$                             /en/
  RedirectMatch 301 ^/en/service/?$                             /en/
  # RU
  RedirectMatch 301 ^/ru/uslugi/chastnye-uslugi-pereezda/?$     /ru/uslugi/chastnyj-pereezd/
  RedirectMatch 301 ^/ru/uslugi/perevozka-tyazhelyh-predmetov/?$ /ru/uslugi/krupnogabaritnyj/
  RedirectMatch 301 ^/ru/uslugi/korporativnye-uslugi/?$         /ru/uslugi/biznes-pereezd/
  RedirectMatch 301 ^/ru/uslugi/biznes-pereezdy/?$              /ru/uslugi/biznes-pereezd/
  RedirectMatch 301 ^/ru/uslugi/uslugi-po-pereezdu/?$           /ru/
  RedirectMatch 301 ^/ru/kontakty/?$                            /ru/
  RedirectMatch 301 ^/ru/uslugi/?$                              /ru/
  # ET
  RedirectMatch 301 ^/teenused/raskete-esemete-teisaldamine/?$  /teenused/suuregabariidiline/
  RedirectMatch 301 ^/teenused/kolimisteenus-eraisikule/?$      /teenused/erakolimine/
  RedirectMatch 301 ^/teenused/kolimisteenus-arikliendile/?$    /teenused/arikolimine/
  RedirectMatch 301 ^/teenused/ettevotte-teenused/?$            /teenused/arikolimine/
  RedirectMatch 301 ^/teenused/meist/?$                         /meist/
  RedirectMatch 301 ^/teenused/kolimisteenus/?$                 /
  RedirectMatch 301 ^/teenused/?$                               /
  RedirectMatch 301 ^/kontaktid/?$                              /
</IfModule>
```

Как построить свой список (по опыту с этим сайтом):

- **Источник правды - Google Search Console -> Pages (Indexing -> Pages / Performance -> Pages).** Экспортируй список всех URL, которые Google уже знает и по которым идёт показ/трафик. Это и есть кандидаты на редирект. Комментарий в самом файле прямо это фиксирует: `from GSC, SEO preservation`.
- **Топовые URL сохраняй как есть.** Если старый URL хороший, короткий и уже ранжируется - не выдумывай новый слаг, оставь тот же путь на новом сайте. Редирект нужен только там, где слаг реально поменялся. Чем меньше редиректов на важных страницах, тем лучше (каждый 301 - это небольшая потеря веса и лишний хоп).
- **Обрабатывай слэш на конце.** Обрати внимание на `/?$` в конце каждого шаблона - он ловит URL и со слэшем, и без. Обязательно копируй этот приём, иначе половина старых ссылок не сматчится.
- **Только `301` (постоянный), не `302`.** 302 не передаёт вес.
- **Redirect старых sitemap.** Отдельно замечу первые три строки: старые Yoast-sitemap (`sitemap_index.xml`, `page-sitemap.xml`, `post-sitemap.xml`) редиректятся на новый `/sitemap.xml`. Это важно: Google долго держит старые sitemap в очереди и продолжает по ним ходить; редирект гасит это чисто.

Порядок правил имеет значение: более специфичные слаги должны идти ВЫШЕ общих (`^/teenused/kolimisteenus-eraisikule/?$` раньше, чем `^/teenused/?$`), иначе общий шаблон перехватит частный.

## 10.6 Шаг 5. Работа в Google Search Console после переезда

Порядок действий в GSC сразу после cutover:

1. **Удалить старые sitemap.** В разделе Sitemaps удали `sitemap_index.xml` и все старые `*-sitemap.xml`. Даже с 301-редиректом их лучше убрать из очереди руками.
2. **Добавить новый sitemap.** Отправь `https://<домен>/sitemap.xml`. Проверь, что в нём стоят абсолютные URL нового сайта и свежий `lastmod`. Наш `sitemap.xml` строится генератором, вот его голова:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://moving24.ee/</loc>
    <lastmod>2026-07-06</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
    <xhtml:link rel="alternate" hreflang="et" href="https://moving24.ee/"/>
```

3. **Проверь несколько ключевых URL через URL Inspection -> Request indexing.** Топ-3-5 самых важных страниц (главная, основные услуги) можно вручную попросить переиндексировать, чтобы ускорить.
4. **"Couldn't fetch" - часто это НЕ ошибка.** Когда сразу после отправки sitemap или запроса на индексацию GSC пишет `Couldn't fetch` / «Не удалось получить», в большинстве случаев Google просто ещё не дочитал - статус висит в очереди. Не паникуй, не переотправляй по десять раз. Проверь, что страница реально отдаётся (открой в инкогнито, глянь код ответа 200, отсутствие noindex), и подожди - обычно за часы-дни статус сам меняется на «Success». Реальная ошибка - это когда curl/браузер тоже не открывает страницу или ловит 403/500/noindex.

## 10.7 Шаг 6. Кэш Open Graph в Telegram (и других мессенджерах)

После смены сайта старые превью-карточки (OG-картинка, заголовок) залипают в кэше платформ. Особенно заметно в Telegram: при вставке ссылки он показывает СТАРУЮ картинку и старый заголовок из WordPress.

Решение для Telegram: напиши боту **@WebpageBot**, отправь ему свой URL - он сбросит серверный кэш Open Graph для этой ссылки, и следующее превью подтянется уже с нового сайта. Полезно прогнать так все ключевые URL (главная + основные услуги на каждом языке) сразу после переезда, до того как кто-то начнёт кидать ссылки в чаты.

(Facebook/LinkedIn имеют собственные дебаггеры OG для сброса кэша, но для нашего трафика решающим был именно Telegram.)

---

## 10.8 Производительность (PageSpeed / Core Web Vitals)

После того как переезд состоялся и сайт индексируется, второй фронт - скорость. Ниже - конкретные вещи из этого проекта, которые двигают PageSpeed.

### 10.8.1 Не превышай бюджет preload: логотипы и картинки ниже экрана крадут канал у LCP

Главная ошибка новичков - напрелоадить всё подряд. Preload - это команда браузеру «качай ЭТО в первую очередь, с высоким приоритетом». Если ты прелоадишь картинку, которой нет на первом экране (логотип в футере, иконка ниже сгиба), она конкурирует за канал с реальным LCP-элементом (большая картинка героя) и замедляет его. Правило: **preload только для того, что видно на первом экране и участвует в LCP.**

Смотри, как это сделано у нас (`staging/index.html`, строки 283-290). Прелоадится РОВНО две картинки - только герой, причём с разбивкой по вьюпорту через `media`, чтобы мобильный не тянул десктопную:

```html
<link rel="preconnect" href="https://www.googletagmanager.com" crossorigin>
<link rel="preload" as="image" href="img/m24-hero-vans-768.webp" media="(max-width:760px)" fetchpriority="high">
<link rel="preload" as="image" href="imagebg-1920.webp" media="(min-width:761px)" fetchpriority="high">

<link rel="preload" as="font" type="font/woff2" crossorigin href="/fonts/inter-400-latin.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="/fonts/plus-jakarta-sans-700-latin.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="/fonts/inter-700-latin.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="/fonts/plus-jakarta-sans-800-latin.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="/fonts/caveat-700-latin.woff2">
```

Разбор приёмов:

- **`media="(max-width:760px)"` vs `media="(min-width:761px)"`** - мобильному прелоадится маленький `m24-hero-vans-768.webp`, десктопу - большой `imagebg-1920.webp`. Один вьюпорт никогда не качает лишнюю версию.
- **`fetchpriority="high"`** на картинке героя - явно поднимает её приоритет, помогает LCP.
- **Никаких логотипов/иконок/футерных картинок в preload.** Всё, что ниже первого экрана, грузится лениво в обычном потоке.
- **Шрифты** прелоадятся только те, что реально нужны на первом экране (латиница основных начертаний). Кириллические/расширенные подмножества подключены обычным `@font-face` с `font-display: swap` без preload.

Практика: если PageSpeed ругается «Preload key requests» или наоборот «avoid chaining critical requests», первым делом пересчитай, что у тебя в preload, и выкинь всё, что не на первом экране.

### 10.8.2 Кэш SVG и статики в `.htaccess`

zone.ee (Apache) позволяет задать долгий кэш статике - это прямой прирост для повторных визитов и часть PageSpeed «Serve static assets with an efficient cache policy». Наш блок:

```apache
# --- Cache static assets (fingerprint with ?v= when updating) ---
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/webp "access plus 1 year"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType image/jpeg "access plus 1 year"
  ExpiresByType image/png "access plus 1 year"
  ExpiresByType font/woff2 "access plus 1 year"
  ExpiresByType text/css "access plus 1 month"
  ExpiresByType application/javascript "access plus 1 month"
  ExpiresByType text/html "access plus 0 seconds"
</IfModule>
```

Важные моменты:

- **`image/svg+xml "access plus 1 year"`** - именно эта строка есть в staging, но её НЕ было в одной из ранних боевых версий (её видно в `diff staging/.htaccess deploy/.htaccess`). Если у тебя много SVG-иконок, обязательно добавь этот тип - иначе SVG отдаются без кэша и тянут вниз оценку. Убедись, что он присутствует в боевом `.htaccess`.
- **`text/html "access plus 0 seconds"`** - HTML не кэшируем, чтобы правки контента появлялись мгновенно.
- **CSS/JS - месяц**, картинки/шрифты - год. Комментарий подсказывает механику обновления: при смене файла добавляй `?v=` (фингерпринт) к ссылке, тогда годовой кэш не помешает выкатить новую версию.
- Плюс включена компрессия (`mod_deflate`) для html/css/js/json/svg - это отдельный блок в том же `.htaccess`.

### 10.8.3 Размер картинок и что тянет вниз LCP

LCP (Largest Contentful Paint) на этом лендинге - картинка героя. Всё крутится вокруг того, чтобы она была лёгкой и грузилась первой. Реальные размеры файлов у нас:

```
imagebg-1920.webp          133628 байт (~130 KB)  - десктоп hero
imagebg-768.webp            73520 байт  (~72 KB)  - планшет/узкий
img/m24-hero-vans-768.webp  94626 байт  (~92 KB)  - мобильный hero
```

Выводы для шаблона:

- **Формат WebP** для всех фото - в разы легче JPEG/PNG при том же качестве.
- **Разные размеры под разные вьюпорты** - десктопу большой файл, мобильному отдельный маленький (через `media` в preload и через `<picture>`/`srcset` в разметке). Мобильный никогда не должен качать 1920px-версию.
- **Держи hero в районе 100-150 KB.** Если LCP-картинка весит мегабайты, никакой preload не спасёт.
- Всё, что не на первом экране, - `loading="lazy"`, чтобы не отбирать канал у LCP.

### 10.8.4 Core Web Vitals: на что смотреть

- **LCP** - разобрано выше: лёгкий hero + preload + `fetchpriority=high`. Цель - под 2.5 c.
- **CLS (сдвиг макета)** - у картинок и медиа-блоков задавай размеры/aspect-ratio, чтобы контент не прыгал при подгрузке. Шрифты с `font-display: swap` могут давать небольшой сдвиг - поэтому основные латинские начертания и прелоадятся, чтобы swap случился раньше.
- **INP/отзывчивость** - на статическом лендинге почти не проблема: минимум JS, GTM подключён через `preconnect`, тяжёлых скриптов на первом экране нет.

### 10.8.5 Троттлинг в лабе vs реальные пользователи (не гонись за 100)

Ключевой момент, который экономит нервы: **PageSpeed Insights показывает две разные вещи.**

- **Lab data (Lighthouse)** - синтетический прогон с искусственным троттлингом: эмулируется медленный 4G и слабый CPU. Это намеренно пессимистичный сценарий. Именно из-за него мобильный балл всегда ниже десктопного, и именно там тот самый `X-Robots-Tag noindex` ронял SEO до 69.
- **Field data / CrUX** - реальные Core Web Vitals от настоящих пользователей Chrome за последние 28 дней. Вот ЭТО и есть то, что учитывает Google для ранжирования.

Практический вывод: не убивайся ради «100/100» в лабе под троттлингом - это часто недостижимо и не нужно. Ориентир - зелёные Core Web Vitals в field data (реальные юзеры). Лабой пользуйся как диагностикой (она называет конкретные проблемы: preload, кэш, размер картинок), а оценку успеха бери из поля. Field data накапливается неделями, так что сразу после переезда его может не быть - это нормально, дай сайту набрать статистику.

---

**Использованные исходники (абсолютные пути):**

- `/Users/dennymansa/Desktop/moving24/staging/.htaccess` - 301-редиректы, noindex-строка, кэш, компрессия
- `/Users/dennymansa/Desktop/moving24/deploy/.htaccess` - боевой вариант (noindex убран, HSTS включён) для сравнения через `diff`
- `/Users/dennymansa/Desktop/moving24/staging/robots.txt` - разрешение краула + строка Sitemap
- `/Users/dennymansa/Desktop/moving24/staging/sitemap.xml` - новый sitemap с абсолютными URL и hreflang
- `/Users/dennymansa/Desktop/moving24/staging/index.html` (строки 283-290) - preload только hero + шрифтов, `media` + `fetchpriority`
- Файлы hero: `/Users/dennymansa/Desktop/moving24/staging/imagebg-1920.webp`, `imagebg-768.webp`, `img/m24-hero-vans-768.webp` - реальные размеры для раздела про LCP
