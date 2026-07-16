#!/usr/bin/env python3
"""Single source of truth for LuxAed service translations.

Every service must have ET, RU and EN entries. Navigation, footer links,
homepage cards, hreflang rows, sitemap entries and generator coverage checks are
derived from this matrix so one language can no longer silently lose a service.
"""

LANGS = ("et", "ru", "en")

SERVICE_MATRIX = [
    {
        "key": "wood",
        "image": "luxaed-svc-wood",
        "et": {"path": "/aiad/puitaed/", "label": "Puitaed", "badge": "Puit", "title": "Puitaed", "desc": "Horisontaalne või vertikaalne puitaed teraskarkassil."},
        "ru": {"path": "/ru/zabory/derevyannye/", "label": "Деревянные заборы", "badge": "Дерево", "title": "Деревянные заборы", "desc": "Горизонтальные и вертикальные деревянные заборы на прочном стальном каркасе."},
        "en": {"path": "/en/fences/wooden/", "label": "Wooden fences", "badge": "Wood", "title": "Wooden fences", "desc": "Horizontal or vertical timber fencing on a sturdy steel frame."},
    },
    {
        "key": "roll_mesh",
        "image": "luxaed-rullvork-slope-v1",
        "et": {"path": "/aiad/vorkaed/", "label": "Rullvõrkaed", "badge": "Rullvõrk", "title": "Rullvõrkaed", "desc": "Punutud või keevitatud rullvõrk pikemale aiajoonele."},
        "ru": {"path": "/ru/zabory/setka-rabitsa/", "label": "Рулонная сетка и рабица", "badge": "Рулонная сетка", "title": "Заборы из сетки-рабицы", "desc": "Рулонная плетёная или сварная сетка для длинной линии забора и сложного рельефа."},
        "en": {"path": "/en/fences/roll-mesh/", "label": "Roll mesh & chain-link", "badge": "Roll mesh", "title": "Roll mesh fences", "desc": "Woven chain-link or welded roll mesh for long fence lines and sloping plots."},
    },
    {
        "key": "panel_mesh",
        "image": "luxaed-w-mesh-1",
        "et": {"path": "/aiad/paneelaed/", "label": "2D/3D keevisvõrkaed", "badge": "2D / 3D", "title": "Keevisvõrkaed", "desc": "Jäigad keevitatud võrgu sektsioonid eramule või territooriumile."},
        "ru": {"path": "/ru/zabory/2d-3d-setka/", "label": "Сварные 2D/3D-сетки", "badge": "2D / 3D", "title": "Заборы из 2D/3D-сетки", "desc": "Жёсткие секции сварной сетки для частного участка или территории."},
        "en": {"path": "/en/fences/mesh/", "label": "Welded 2D/3D mesh", "badge": "2D / 3D", "title": "Welded mesh fences", "desc": "Rigid welded-mesh sections for private homes and commercial sites."},
    },
    {
        "key": "steel_picket",
        "image": "luxaed-w-lippaed-1",
        "et": {"path": "/aiad/lippaed/", "label": "Metall-lippaed", "badge": "Metall-lipp", "title": "Metall-lippaed", "desc": "Horisontaalsed või vertikaalsed metall-lamellid."},
        "ru": {"path": "/ru/zabory/metallicheskie-lameli/", "label": "Металлический штакетник", "badge": "Штакетник", "title": "Металлический штакетник", "desc": "Горизонтальные или вертикальные металлические ламели с выбранным зазором."},
        "en": {"path": "/en/fences/steel-picket/", "label": "Steel picket fences", "badge": "Steel picket", "title": "Steel picket fences", "desc": "Horizontal or vertical coated steel slats with an adjustable gap."},
    },
    {
        "key": "bar_metal",
        "image": "luxaed-varbaed-gate-v2",
        "et": {"path": "/aiad/metallaed/", "label": "Metallaed / varbaed", "badge": "Varbaed", "title": "Metallaed ja varbaed", "desc": "Keevitatud metallsektsioonid ning dekoratiivsed piirded."},
        "ru": {"path": "/ru/zabory/prutkovye/", "label": "Прутковые металлические заборы", "badge": "Прутковый забор", "title": "Металлические прутковые заборы", "desc": "Сварные стальные секции, декоративные ограждения и ворота в едином стиле."},
        "en": {"path": "/en/fences/metal-bar/", "label": "Metal bar fences", "badge": "Metal bar", "title": "Metal bar fences", "desc": "Welded steel-bar sections, decorative fencing and matching gates."},
    },
    {
        "key": "profiled_sheet",
        "image": "luxaed-profnastil-2",
        "et": {"path": "/aiad/profiilplekk-aed/", "label": "Profiilplekk-aed", "badge": "Profiilplekk", "title": "Profiilplekk-aed", "desc": "Kinnine piire metallkarkassil, eri toonides."},
        "ru": {"path": "/ru/zabory/profnastil/", "label": "Заборы из профнастила", "badge": "Профнастил", "title": "Заборы из профнастила", "desc": "Закрытое ограждение на металлическом каркасе с выбором профиля и цвета."},
        "en": {"path": "/en/fences/profiled-sheet/", "label": "Profiled-sheet fences", "badge": "Profiled sheet", "title": "Profiled-sheet fences", "desc": "A solid fence on a steel frame, available in a range of profiles and colours."},
    },
    {
        "key": "gates",
        "image": "luxaed-svc-gates",
        "et": {"path": "/varavad/", "label": "Väravad ja automaatika", "badge": "Väravad", "title": "Väravad ja automaatika", "desc": "Liug-, tiib- ja jalgväravad koos sobiva automaatikaga."},
        "ru": {"path": "/ru/vorota-avtomatika/", "label": "Ворота, калитки и автоматика", "badge": "Ворота", "title": "Ворота и автоматика", "desc": "Откатные, распашные и пешеходные ворота с подходящей автоматикой."},
        "en": {"path": "/en/gates-automation/", "label": "Gates & automation", "badge": "Gates", "title": "Gates & automation", "desc": "Sliding, swing and pedestrian gates with correctly specified automation."},
    },
    {
        "key": "repair",
        "image": "luxaed-repair-real-v1",
        "et": {"path": "/aia-remont/", "label": "Aia ja värava remont", "badge": "Remont", "title": "Aia ja värava remont", "desc": "Sektsioonide, postide, väravate ja automaatika remont."},
        "ru": {"path": "/ru/remont-zaborov/", "label": "Ремонт заборов и ворот", "badge": "Ремонт", "title": "Ремонт заборов и ворот", "desc": "Ремонт секций, столбов, ворот, фурнитуры и автоматики."},
        "en": {"path": "/en/fence-repair/", "label": "Fence & gate repair", "badge": "Repair", "title": "Fence & gate repair", "desc": "Repairs to sections, posts, gates, hardware and automation."},
    },
]


def service_rows():
    return [{lang: item[lang]["path"] for lang in LANGS} for item in SERVICE_MATRIX]


def service_nav(lang):
    return [(item[lang]["path"], item[lang]["label"]) for item in SERVICE_MATRIX]


def service_tiles(lang):
    return [
        (item[lang]["path"], item["image"], item[lang]["badge"], item[lang]["title"], item[lang]["desc"])
        for item in SERVICE_MATRIX
    ]


def service_paths(lang):
    return [item[lang]["path"] for item in SERVICE_MATRIX]


def assert_service_coverage(lang, generated_paths):
    expected, actual = set(service_paths(lang)), set(generated_paths)
    if expected != actual:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise RuntimeError(f"{lang.upper()} service parity failed; missing={missing}, extra={extra}")


_keys = [item.get("key") for item in SERVICE_MATRIX]
if len(_keys) != len(set(_keys)):
    raise RuntimeError("Service catalog contains duplicate keys")

for _lang in LANGS:
    _paths = service_paths(_lang)
    if len(_paths) != len(set(_paths)):
        raise RuntimeError(f"Service catalog contains duplicate {_lang.upper()} paths")

for _item in SERVICE_MATRIX:
    missing = [lang for lang in LANGS if lang not in _item]
    if missing:
        raise RuntimeError(f"Service {_item.get('key')} is missing translations: {missing}")
    for _lang in LANGS:
        missing_fields = [field for field in ("path", "label", "badge", "title", "desc")
                          if not _item[_lang].get(field)]
        if missing_fields:
            raise RuntimeError(
                f"Service {_item.get('key')} has incomplete {_lang.upper()} content: {missing_fields}"
            )
