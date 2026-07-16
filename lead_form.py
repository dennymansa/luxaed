#!/usr/bin/env python3
"""Single multilingual lead form used by every LuxAed landing page."""

import html


COPY = {
    "et": {
        "tag": "Tasuta konsultatsioon", "title": "Kirjeldage projekti — võtame ühendust",
        "sub": "Valige teenus ja jätke kontaktandmed.",
        "what": "Mida vajate?", "multi": "Võite valida mitu",
        "services": [("aed", "Aed"), ("varav", "Väravad"), ("automaatika", "Automaatika")],
        "fence_type": "Aia tüüp",
        "materials": [("unknown", "Ei tea — aidake valida"), ("panel_mesh", "2D/3D keevisvõrkaed"),
                      ("roll_mesh", "Rullvõrkaed"), ("wood", "Puitaed"), ("steel_picket", "Metall-lippaed"),
                      ("bar_metal", "Metallaed / varbaed"), ("profiled_sheet", "Profiilplekk-aed"),
                      ("other", "Muu / näidisfoto järgi")],
        "length": "Aia pikkus",
        "lengths": [("unknown", "Ei tea veel"), ("up_to_50", "Kuni 50 m"),
                    ("over_50", "Üle 50 m")],
        "gate_type": "Värava tüüp", "gate_types": [("unknown", "Ei tea veel"), ("sliding", "Liugvärav"), ("swing", "Tiibvärav")],
        "choose_error": "Valige vähemalt üks: aed, väravad või automaatika.",
        "contact_title": "Kontaktandmed", "name": "Nimi *", "phone": "Telefon *",
        "email": "E-post *", "address": "Objekti aadress *",
        "photo_title": "Krundi fotod", "photo_optional": "valikuline · kuni 4",
        "photo_hint": "Üldvaade, sissepääs ja pinnas.", "photo_button": "Valige fotod",
        "comment": "Kommentaar", "comment_optional": "valikuline",
        "comment_placeholder": "Kirjeldage oma soovi.", "send": "Saada hinnapäring →",
        "assure1": "Vastame tööpäevaga", "assure2": "Tasuta mõõdistus",
        "consent": "Saates nõustute <a href=\"/privaatsus/\">privaatsuse</a> ja <a href=\"/tingimused/\">tingimustega</a>.",
        "success": "<b>Aitäh, päring on vastu võetud.</b><br>Võtame teiega ühe tööpäeva jooksul ühendust.",
    },
    "ru": {
        "tag": "Бесплатная консультация", "title": "Расскажите о проекте — мы свяжемся",
        "sub": "Выберите услугу и оставьте контакты.",
        "what": "Что вам нужно?", "multi": "Можно выбрать несколько",
        "services": [("aed", "Забор"), ("varav", "Ворота"), ("automaatika", "Автоматика")],
        "fence_type": "Тип забора",
        "materials": [("unknown", "Не знаю — помогите выбрать"), ("panel_mesh", "Сетка 2D/3D"),
                      ("roll_mesh", "Рулонная сетка"), ("wood", "Деревянный"),
                      ("steel_picket", "Металлический штакетник"), ("bar_metal", "Металлический / прутковый"),
                      ("profiled_sheet", "Профнастил"), ("other", "Другой / по фотографии")],
        "length": "Длина забора",
        "lengths": [("unknown", "Пока не знаю"), ("up_to_50", "До 50 м"),
                    ("over_50", "Более 50 м")],
        "gate_type": "Тип ворот", "gate_types": [("unknown", "Пока не знаю"), ("sliding", "Откатные"), ("swing", "Распашные")],
        "choose_error": "Выберите хотя бы одно: забор, ворота или автоматику.",
        "contact_title": "Контактные данные", "name": "Имя *", "phone": "Телефон *",
        "email": "Email *", "address": "Адрес объекта *",
        "photo_title": "Фото участка", "photo_optional": "необязательно · до 4",
        "photo_hint": "Общий вид, въезд и грунт.", "photo_button": "Выбрать фотографии",
        "comment": "Комментарий", "comment_optional": "необязательно",
        "comment_placeholder": "Опишите пожелания.", "send": "Отправить заявку →",
        "assure1": "Ответим за рабочий день", "assure2": "Бесплатный замер",
        "consent": "Отправляя, вы принимаете <a href=\"/ru/privaatsus/\">политику</a> и <a href=\"/ru/tingimused/\">условия</a>.",
        "success": "<b>Спасибо, заявка принята.</b><br>Мы свяжемся с вами в течение рабочего дня.",
    },
    "en": {
        "tag": "Free consultation", "title": "Tell us about the project — we’ll get in touch",
        "sub": "Choose a service and leave your details.",
        "what": "What do you need?", "multi": "Select all that apply",
        "services": [("aed", "Fence"), ("varav", "Gates"), ("automaatika", "Automation")],
        "fence_type": "Fence type",
        "materials": [("unknown", "Not sure — help me choose"), ("panel_mesh", "2D/3D welded mesh"),
                      ("roll_mesh", "Roll mesh"), ("wood", "Wooden fence"), ("steel_picket", "Steel picket"),
                      ("bar_metal", "Metal / bar fence"), ("profiled_sheet", "Profiled sheet"),
                      ("other", "Other / from a reference photo")],
        "length": "Fence length",
        "lengths": [("unknown", "Not sure yet"), ("up_to_50", "Up to 50 m"),
                    ("over_50", "Over 50 m")],
        "gate_type": "Gate type", "gate_types": [("unknown", "Not sure yet"), ("sliding", "Sliding"), ("swing", "Swing")],
        "choose_error": "Choose at least one: fence, gates or automation.",
        "contact_title": "Contact details", "name": "Name *", "phone": "Phone *",
        "email": "Email *", "address": "Site address *",
        "photo_title": "Site photos", "photo_optional": "optional · up to 4",
        "photo_hint": "Overview, entrance and ground.", "photo_button": "Choose photos",
        "comment": "Comment", "comment_optional": "optional",
        "comment_placeholder": "Describe your request.", "send": "Send quote request →",
        "assure1": "Reply within 1 workday", "assure2": "Free site measurement",
        "consent": "By sending, you accept our <a href=\"/en/privacy/\">privacy</a> and <a href=\"/en/terms/\">terms</a>.",
        "success": "<b>Thank you, we have received your request.</b><br>We will contact you within one working day.",
    },
}

MATERIAL_ALIASES = {
    "Rullvõrkaed": "roll_mesh", "Puit": "wood", "Metallaed / varbaed": "bar_metal",
    "Metall-lippaed": "steel_picket", "2D/3D keevisvõrkaed": "panel_mesh", "Profiilplekk-aed": "profiled_sheet",
    "2D/3D сварная сетка": "panel_mesh", "Дерево": "wood", "Профнастил": "profiled_sheet",
    "Металлический штакетник": "steel_picket", "2D/3D welded mesh": "panel_mesh", "Wood": "wood",
    "Corrugated sheet": "profiled_sheet", "Steel picket": "steel_picket",
}


def _options(items, selected):
    return "".join(f'<option value="{html.escape(code)}"{" selected" if code == selected else ""}>{html.escape(label)}</option>' for code, label in items)


def render_lead_form(lang="et", default_service="", default_material=""):
    c = COPY[lang]
    material_code = MATERIAL_ALIASES.get(default_material, "unknown")
    request_context = default_service if default_service == "remont" else ""
    visible_services = {code for code, _ in c["services"]}
    selected = {default_service} if default_service in visible_services else set()
    buttons = "".join(
        f'<button class="project-choice{" on" if code in selected else ""}" type="button" data-service="{code}" data-label="{html.escape(label)}" aria-pressed="{"true" if code in selected else "false"}"><span class="project-choice-check" aria-hidden="true">✓</span>{html.escape(label)}</button>'
        for code, label in c["services"]
    )
    fence_hidden = "" if "aed" in selected else " hidden"
    gate_hidden = "" if selected.intersection({"varav", "automaatika"}) else " hidden"
    return f'''<!-- LEAD_FORM_START -->
<div class="form-slot"><div class="form-card form-card-v2" id="form">
  <span class="form-tag">{c["tag"]}</span><h2>{c["title"]}</h2><p class="form-sub">{c["sub"]}</p>
  <form id="leadFormV2" data-form-version="2" data-lang="{lang}" data-default-service="{html.escape(default_service)}" data-default-material="{html.escape(material_code)}" novalidate>
    <input type="hidden" name="service" id="serviceField" value="{html.escape(default_service)}"><input type="hidden" name="services" id="servicesField" value="{html.escape(default_service)}">
    <input type="hidden" name="material" id="materialField"><input type="hidden" name="length" id="lengthField"><input type="hidden" name="gate_type" id="gateTypeField"><input type="hidden" name="automation" id="automationField">
    <input type="hidden" name="request_context" value="{html.escape(request_context)}">
    <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true" class="form-honeypot">
    <div class="form-fields">
      <div class="form-question"><b>{c["what"]}</b><span>{c["multi"]}</span></div><div class="project-choices" id="projectChoices">{buttons}</div>
      <div class="form-inline-error" id="projectError" role="alert"></div>
      <div class="conditional-fields" data-condition="aed"{fence_hidden}>
        <label class="ff"><span>{c["fence_type"]}</span><select id="materialSelect" name="material_code">{_options(c["materials"], material_code)}</select></label>
        <label class="ff"><span>{c["length"]}</span><select id="lengthSelect" name="length_code">{_options(c["lengths"], "unknown")}</select></label>
      </div>
      <div class="conditional-fields conditional-fields--single" data-condition="gate"{gate_hidden}>
        <label class="ff"><span>{c["gate_type"]}</span><select id="gateTypeSelect" name="gate_type_code">{_options(c["gate_types"], "unknown")}</select></label>
      </div>
      <div class="form-question form-question--contact"><b>{c["contact_title"]}</b></div>
      <div class="form-grid form-grid--contact">
        <label><span class="form-field-label">{c["name"]}</span><input type="text" name="name" autocomplete="name" maxlength="100" required></label>
        <label><span class="form-field-label">{c["phone"]}</span><input type="tel" name="phone" autocomplete="tel" inputmode="tel" maxlength="40" required></label>
        <label><span class="form-field-label">{c["email"]}</span><input type="email" name="email" autocomplete="email" maxlength="160" required></label>
        <label><span class="form-field-label">{c["address"]}</span><input type="text" name="address" autocomplete="street-address" maxlength="200" required></label>
      </div>
      <div class="photo-box"><div class="photo-box-head"><b>{c["photo_title"]}</b><span>{c["photo_optional"]}</span></div><p>{c["photo_hint"]}</p>
        <label class="photo-upload" id="photoLabelV2"><input type="file" name="photos" accept="image/jpeg,image/png,image/webp,image/heic,image/heif" multiple id="photoInputV2"><svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg><span id="photoLabelTxtV2">{c["photo_button"]}</span></label><div class="photo-previews" id="photoPreviews"></div>
      </div>
      <label class="form-field form-comment"><span class="form-field-label">{c["comment"]} <small>{c["comment_optional"]}</small></span><textarea name="msg" placeholder="{c["comment_placeholder"]}" maxlength="1200"></textarea></label>
      <div class="form-submit-row"><button class="btn btn-accent" type="submit">{c["send"]}</button></div>
      <div class="form-inline-error form-submit-error" id="formError" role="alert" aria-live="assertive"></div><div class="form-assure"><span>{c["assure1"]}</span><span>{c["assure2"]}</span></div><p class="form-consent">{c["consent"]}</p>
    </div>
    <div class="form-ok" id="formOk" role="status" aria-live="polite" tabindex="-1">{c["success"]}</div>
  </form>
</div></div>
<!-- LEAD_FORM_END -->'''
