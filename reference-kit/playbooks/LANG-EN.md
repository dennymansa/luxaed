# Плейбук: английский язык (как писать)

Этот раздел - о том, как писать английские тексты для сайта-шаблона так, чтобы они звучали как у Moving24: естественно, ясно, коротко и «по делу». Английская версия живёт в `/Users/dennymansa/Desktop/moving24/staging/en/` (на проде - `moving24.ee/en/`). Все примеры ниже - дословные цитаты из настоящих файлов сайта. Английский цитирую как есть, объяснения даю по-русски.

Важно: `<html lang="en">` и в schema стоит `"inLanguage": "en"` - язык один. Но по стилю тексты написаны на нейтральном британско-ориентированном английском (см. `labelling`, `disassembly and reassembly`, `arve`). Держись этого регистра во всём клоне.

---

## 1. Принципы

**1.1. Естественный, нейтрально-британский английский.** Это не машинный перевод с эстонского и не «американский маркетинг». Тон - как у живого толкового человека, который объясняет услугу. Британское написание там, где оно встречается: `labelling` (не `labeling`), `disassembly and reassembly`, `fit-out`, `haul away`. Не смешивай американское и британское в пределах сайта - выбери одну норму и держи её.

Смотри hero на главной (`en/index.html`):
- кикер: `Hi! A move coming up?`
- H1 + claim: `Moving services` / `One call and your move is handled`

Это разговорно, но не панибратски. `Hi!` задаёт дружелюбие, `One call and your move is handled` - обещание в одну строку.

**1.2. Ясность и краткость важнее «красоты».** Предложения короткие, глаголы активные, обещания конкретные. Пример карточки услуги с главной:

> **Apartment and house** => `A studio, a four-room flat or a country house. We pack, carry it all out, move it and set everything up at the new place. All in a single day.`

Тут нет ни одного лишнего слова: перечисление объектов -> цепочка глаголов (`pack, carry out, move, set up`) -> выгода (`All in a single day.`). Копируй эту структуру: **что -> что мы делаем -> выгода**.

**1.3. Интент-ориентированные заголовки (H1/H2/кикеры).** Заголовки отвечают на то, что человек ищет и о чём думает, а не «продают абстрактно». Кикеры на сервисных страницах прямо озвучивают ситуацию клиента:
- `Home move coming up?` (home-move)
- `Time for a new office?` (business-move)
- `Old furniture in the way?` (junk-removal)

H1 при этом содержат ключевые слова для SEO и город:
- `Home and apartment moves in Tallinn`
- `Old furniture and appliance removal`

H2 секций - функциональные, не рекламные: `What the move includes`, `What we take away`, `What's included in the price, and what costs extra.`, `Four simple steps`, `Where we work`, `What people ask before booking`. Заголовок = обещание содержимого секции.

**1.4. Единая терминология по всему сайту.** Одни и те же вещи всегда называются одним словом. Не «синонимь ради разнообразия» - это путает и вредит SEO. Канон Moving24:

| Понятие | Всегда пишем | НЕ пишем |
|---|---|---|
| грузчики | `movers` | ~~loaders, workers, staff~~ |
| фургон/машина | `van` (мелкий), `truck` (крупный), `vehicle` (общее) | ~~lorry, car~~ |
| разбор/сборка мебели | `disassembly and reassembly` / `disassemble … reassemble` | ~~take apart / put together~~ |
| смета/цена | `quote` (глагол `we quote`), `price`, `estimate` | ~~offer, calculation~~ |
| вынос/занос | `carry-out` / `carry-in` | ~~moving out / moving in~~ |
| вывоз хлама | `junk removal`, `disposal` | ~~garbage collection, trash~~ |
| круглосуточно | `24/7`, `around the clock, 7 days a week` | ~~always open~~ |

**1.5. Никаких длинных тире.** Жёсткое правило проекта (см. память `no-em-dashes`). В английском тоже: только дефис `-`. На сайте это соблюдено дословно - `No hidden fees - describe your move…`, `we clear the room`, `any condition.` Везде, где по-английски напрашивается em-dash (-), ставь дефис с пробелами ` - ` или перестрой фразу.

**1.6. Честность и «без сюрпризов» как голос бренда.** Тема цены проходит через весь сайт одной интонацией: `An honest price up front`, `We tell you upfront, with no hidden fees.`, `No hidden fees`, `Estimates are free.` При клонировании сохрани этот приём - обещание прозрачности повторяется в кикере секции, в карточке и в FAQ.

---

## 2. Таблица: фраза из лайва -> почему так

Все фразы - дословно из файлов `en/`.

| Фраза из лайва (дословно) | Где | Почему так написано |
|---|---|---|
| `Hi! A move coming up?` | home, hero kicker | Разговорный крючок в форме вопроса - зеркалит мысль посетителя. Короткое `Hi!` = дружелюбие без фамильярности. |
| `One call and your move is handled` | home, hero claim | Обещание в 6 слов. Пассив `is handled` тут уместен: акцент на результате для клиента, а не на исполнителе. |
| `We pack, carry it all out, move it and set everything up at the new place. All in a single day.` | home, service card | Цепочка активных глаголов = ощущение «всё под ключ». Финальное короткое предложение-выгода. |
| `We move what others turn down.` | home, «Pianos, safes» | Короткая гордая фраза-дифференциатор. Контраст «мы vs остальные» без хвастовства. |
| `Your belongings and your walls stay intact.` | home, «Pianos, safes» | Конкретная выгода (`walls` - неожиданная деталь, показывает аккуратность). Простые слова. |
| `Official disposal, no illegal dumping.` | home, «Junk» | Снимает страх клиента (куда денут хлам). Пара «что делаем / чего не делаем». |
| `We tell you upfront, with no hidden fees.` | home, «Junk» | Ядро бренда - прозрачность цены. Повторяется по всему сайту одной формулировкой. |
| `We also move in the evenings and on weekends so your work never stops.` | home, «Office» | `also` = мы ещё И вечером/в выходные (гибкость, а не «только тогда»). `so …` называет выгоду клиенту. |
| `computers, servers, monitors - disconnect, protective packing and reconnect on site` | business, card | Дефис вместо тире. Телеграфный стиль в карточках допустим: перечисление через запятую, глаголы без «we». |
| `files and cabinets into boxes, numbered and put back in the same order` | business, «Archives» | Конкретика снимает тревогу: клиент боится, что архив перепутают. |
| `Fridges, washing machines, ovens, TVs - recycled the right way.` | junk, «Appliances» | Примеры вместо абстракции («appliances»). `the right way` = мягкое обещание легальности. |
| `Movers carry everything down from any floor - you lift nothing.` | junk, «Carry-out» | Выгода от лица клиента: `you lift nothing` - предельно ясно и приятно. |
| `Everything goes to an official recycling station - nothing dumped.` | junk, «Legal disposal» | Снова пара «делаем / не делаем». Ритм короткий. |
| `The whole move in one pair of hands, with no extra contractors to chase.` | about, «All in one call» | Идиома `one pair of hands` звучит естественно по-английски; `to chase` передаёт реальную боль клиента. |
| `so everything arrives exactly as it left` | about, «Careful» | Обещание сохранности без слова «insurance». Простая, запоминающаяся формула. |
| `We give you the price before the work starts and keep our word: no hidden extras.` | about, «Honest price» | Двоеточие вводит уточнение - допустимо. Разговорное `keep our word`. |
| `Four simple steps` | H2, все сервисы | Заголовок обещает простоту. `simple` - ключевое слово-настроение бренда. |
| `You send a request` / `We prepare a quote` / `We move you` / `We set everything up` | how-we-work | Схема «You … / We …»: чётко делит зоны ответственности. Клиент делает мало, компания - всё. |
| `What's included in the price, and what costs extra.` | H2 pricing | Интент-заголовок: ровно тот вопрос, что в голове у клиента. Запятая + вторая часть = честность встроена в заголовок. |
| `Estimates are free.` | FAQ | Три слова. Снимает барьер к заявке. |
| `You don't lift a thing.` | FAQ | Разговорная идиома, выгода от лица клиента. |
| `We are an officially registered company (reg. code 16978239, VAT EE102734342).` | FAQ | Доверие через факты. Локальный термин `arve` (эстонский счёт) дан в скобках - см. ниже. |
| `Submit a request →` | CTA, везде | Глагол-действие + стрелка. Не «Click here», не «Learn more» - конкретное действие. |

---

## 3. Частые ошибки и как правильно

**3.1. Длинное тире (-) вместо дефиса.**
- Неправильно: `No hidden fees - describe your move`
- Правильно (как в лайве): `No hidden fees - describe your move`
Проверяй всегда: `grep -n "-" en/**/*.html` должен давать пусто.

**3.2. Машинно-переведённый порядок слов / «эстонизмы».** Не переноси структуру эстонского/русского буквально.
- Плохо: `Move of your things we will do in one day.`
- Правильно (лайв): `We pack, carry it all out, move it and set everything up at the new place. All in a single day.`
Английский любит порядок «подлежащее -> глагол -> объект» и активный залог.

**3.3. Заголовок «ни о чём» вместо интент-заголовка.**
- Плохо: `Our Great Services` / `Welcome` / `Quality You Can Trust`
- Правильно (лайв): `What the move includes`, `What we take away`, `Where we work`. Заголовок называет содержимое секции.

**3.4. Пустые CTA.**
- Плохо: `Click here`, `Read more`, `Submit`
- Правильно (лайв): `Submit a request →`, `Call +372 5687 0101`. Кнопка всегда говорит, что произойдёт.

**3.5. Раздувание и наречия-паразиты.** Убирай `very`, `really`, `truly`, `world-class», «best-in-class». В лайве максимум - простые слова: `simple`, `honest`, `careful`, `intact`. Сила от конкретики (`you lift nothing`), а не от прилагательных.

**3.6. Плавающая терминология.** Не пиши в одном месте `movers`, в другом `loaders`, в третьем `our guys`. Держи один термин (см. таблицу 1.4). Одна услуга = одно название на всех страницах и в навигации (`Home move`, `Business move`, `Disposal`, `Oversized & heavy`).

**3.7. Американо-британский разнобой.** Если выбрал британскую норму (как в лайве: `labelling`, `disassembly`), не вставляй рядом `labeling`, `organize`, `apartment`+`flat` вперемешку в одном смысле. На сайте оба слова используются осознанно: `apartment/house move` в SEO-заголовке (широкий термин) и `four-room flat` в тексте (естественная британская речь) - это ок, потому что каждое к месту.

**3.8. Стирание локальных терминов и фактов.** Оставляй местные реалии, где они помогают доверию: `a proper invoice (arve)`, `reg. code …, VAT EE…`, названия районов (`Lasnamäe`, `Viimsi`). При клонировании под другой бизнес/страну - **замени факты на свои** (рег. код, VAT, районы, телефон `+372 5687 0101`, e-mail `info@moving24.ee`), но сохрани приём «факт = доверие».

**3.9. Обещания, которые вы не выполняете.** `24/7`, `Estimates are free`, `no hidden fees` - это на сайте буквальные обещания, повторённые в schema (`openingHoursSpecification` 00:00-23:59) и в FAQ. Если ваш бизнес работает не круглосуточно - **не копируйте `24/7`**, поменяйте и текст, и `openingHoursSpecification` в JSON-LD, иначе будет рассинхрон и обман.

---

## 4. Чеклист перед публикацией английской страницы

Проверяй каждый пункт по реальному файлу.

- [ ] **Нет длинных тире.** `grep -n "-" файл.html` пусто. Везде дефис `-`.
- [ ] **H1 содержит услугу + город** (интент + SEO). Пример-эталон: `Home and apartment moves in Tallinn`.
- [ ] **Кикер - в форме вопроса/ситуации клиента.** Эталон: `Home move coming up?`, `Old furniture in the way?`.
- [ ] **H2 секций называют содержимое**, а не «продают». Эталон: `What the move includes`, `What's included in the price, and what costs extra.`
- [ ] **Карточки услуг по схеме «что -> глаголы действия -> выгода»**, короткое финальное предложение. Эталон: `We pack, carry it all out, move it and set everything up at the new place. All in a single day.`
- [ ] **Активный залог и короткие предложения.** Пассив только там, где акцент на результате клиента (`your move is handled`).
- [ ] **CTA - глагол действия.** `Submit a request →`, `Call …`. Ни одного `Click here` / `Read more`.
- [ ] **Единая терминология:** `movers`, `van`/`truck`, `quote`, `carry-out/carry-in`, `disposal`, `24/7`. Прогони `grep -in "loaders\|garbage\|lorry\|click here"` - должно быть пусто.
- [ ] **Одна орфографическая норма** (британская, как в лайве): `labelling`, `disassembly and reassembly`, `fit-out`.
- [ ] **Прозрачность цены присутствует** хотя бы раз: `no hidden fees` / `Estimates are free` / `honest price up front`.
- [ ] **Форма: лейблы совпадают с лайвом.** placeholders дословно: `Full name / company *`, `Email *`, `Phone *`, `e.g. Rotermanni 18, Tallinn`, `Additional info - list of items`. Чипы: `Home move` / `Business move` / `Disposal` / `Oversized items`, `Elevator? Yes/No`, `Packing by us? Yes/No`, `Attach a photo (optional)`. Успех-сообщение: `Thank you! Your request has been received. We will contact you shortly.`
- [ ] **Все факты локализованы под клиента:** телефон, e-mail, рег. код, VAT, районы (`areaServed`), город - заменены (не оставлять `+372 5687 0101`, `info@moving24.ee`, `Tallinn`).
- [ ] **Обещания = реальность и синхрон с schema.** Если убрали `24/7` - поправили `openingHoursSpecification` в JSON-LD.
- [ ] **Нет наречий-паразитов** (`very`, `really`, `truly`, `world-class`). Сила в конкретике (`you lift nothing`).
- [ ] **hreflang/meta на английском:** `<title>` и `og:title` человекочитаемы и с городом (эталон `Home & Apartment Move in Tallinn`), `og:locale` = `en_US`, `inLanguage` = `en`.

---

**Файлы-эталоны (читать при написании нового EN-текста):**
- `/Users/dennymansa/Desktop/moving24/staging/en/index.html` - hero, форма, карточки услуг, «Four simple steps», pricing
- `/Users/dennymansa/Desktop/moving24/staging/en/service/home-move/index.html` - структура сервисной страницы, «What the move includes»
- `/Users/dennymansa/Desktop/moving24/staging/en/service/business-move/index.html` - телеграфный стиль карточек B2B
- `/Users/dennymansa/Desktop/moving24/staging/en/service/junk-removal/index.html` - примеры вместо абстракций, пары «делаем / не делаем»
- `/Users/dennymansa/Desktop/moving24/staging/en/about/index.html` - принципы, голос бренда, lead-абзацы
- `/Users/dennymansa/Desktop/moving24/staging/en/faq/index.html` - тон ответов, длина, честные формулировки
