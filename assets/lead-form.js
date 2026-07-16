(function () {
  'use strict';
  var form = document.getElementById('leadFormV2');
  if (!form) return;

  var lang = form.dataset.lang || document.documentElement.lang || 'et';
  var messages = {
    et: {
      choose: 'Valige vähemalt üks: aed, väravad või automaatika.',
      required: 'Palun täitke nimi, telefon, e-post ja objekti aadress.',
      email: 'Kontrollige e-posti aadressi.',
      phone: 'Kontrollige telefoninumbrit.',
      photoMax: 'Lisada saab kuni 4 fotot.',
      photoSize: 'Ühe foto suurus võib olla kuni 15 MB.',
      photoType: 'Valige pildifailid.',
      photoFail: 'Üht fotot ei õnnestunud töödelda. Proovige teist faili.',
      send: 'Saatmine ebaõnnestus. Proovige uuesti või helistage.',
      files: 'Fotod',
      remove: 'Eemalda foto'
    },
    ru: {
      choose: 'Выберите хотя бы одно: забор, ворота или автоматику.',
      required: 'Заполните имя, телефон, email и адрес объекта.',
      email: 'Проверьте адрес email.',
      phone: 'Проверьте номер телефона.',
      photoMax: 'Можно добавить не более 4 фотографий.',
      photoSize: 'Размер одной фотографии — не более 15 МБ.',
      photoType: 'Выберите файлы изображений.',
      photoFail: 'Одну из фотографий не удалось обработать. Попробуйте другой файл.',
      send: 'Не удалось отправить. Попробуйте ещё раз или позвоните.',
      files: 'Фото',
      remove: 'Удалить фотографию'
    },
    en: {
      choose: 'Choose at least one: fence, gates or automation.',
      required: 'Enter your name, phone, email and site address.',
      email: 'Check the email address.',
      phone: 'Check the phone number.',
      photoMax: 'You can add up to 4 photos.',
      photoSize: 'Each photo can be up to 15 MB.',
      photoType: 'Please choose image files.',
      photoFail: 'One photo could not be processed. Please try another file.',
      send: 'Sending failed. Please try again or call us.',
      files: 'Photos',
      remove: 'Remove photo'
    }
  }[lang];

  var choices = Array.prototype.slice.call(form.querySelectorAll('.project-choice'));
  var serviceField = form.querySelector('#serviceField');
  var servicesField = form.querySelector('#servicesField');
  var projectError = form.querySelector('#projectError');
  var formError = form.querySelector('#formError');
  var materialSelect = form.querySelector('#materialSelect');
  var lengthSelect = form.querySelector('#lengthSelect');
  var gateTypeSelect = form.querySelector('#gateTypeSelect');

  function selectedServices() {
    return choices.filter(function (button) {
      return button.classList.contains('on');
    }).map(function (button) {
      return button.dataset.service;
    });
  }

  function optionLabel(select) {
    return select && select.options[select.selectedIndex] ? select.options[select.selectedIndex].text : '';
  }

  function syncProject() {
    var selected = selectedServices();
    serviceField.value = selected[0] || '';
    servicesField.value = selected.join(',');
    form.querySelectorAll('[data-condition]').forEach(function (element) {
      var condition = element.dataset.condition;
      var visible = condition === 'gate'
        ? selected.indexOf('varav') >= 0 || selected.indexOf('automaatika') >= 0
        : selected.indexOf(condition) >= 0;
      element.hidden = !visible;
    });
    form.querySelector('#materialField').value = selected.indexOf('aed') >= 0 ? optionLabel(materialSelect) : '';
    form.querySelector('#lengthField').value = selected.indexOf('aed') >= 0 ? optionLabel(lengthSelect) : '';
    form.querySelector('#gateTypeField').value = (selected.indexOf('varav') >= 0 || selected.indexOf('automaatika') >= 0) ? optionLabel(gateTypeSelect) : '';
    var automationChoice = choices.find(function (button) { return button.dataset.service === 'automaatika'; });
    form.querySelector('#automationField').value = selected.indexOf('automaatika') >= 0 && automationChoice ? automationChoice.dataset.label : '';
  }

  choices.forEach(function (button) {
    button.addEventListener('click', function () {
      var on = !button.classList.contains('on');
      button.classList.toggle('on', on);
      button.setAttribute('aria-pressed', on ? 'true' : 'false');
      projectError.classList.remove('is-visible');
      form.querySelector('#projectChoices').classList.remove('has-error');
      syncProject();
    });
  });
  [materialSelect, lengthSelect, gateTypeSelect].forEach(function (select) {
    if (select) select.addEventListener('change', syncProject);
  });
  syncProject();

  var photoInput = form.querySelector('#photoInputV2');
  var previews = form.querySelector('#photoPreviews');
  var photoText = form.querySelector('#photoLabelTxtV2');
  var previewUrls = [];
  form._photoFiles = [];
  photoText.dataset.original = photoText.textContent;

  function showError(text) {
    formError.textContent = text;
    formError.classList.add('is-visible');
  }

  function isImage(file) {
    return /^(image\/(jpeg|png|webp|heic|heif))$/i.test(file.type || '') || /\.(jpe?g|png|webp|heic|heif)$/i.test(file.name || '');
  }

  function renderPhotos() {
    previewUrls.forEach(function (url) { URL.revokeObjectURL(url); });
    previewUrls = [];
    previews.innerHTML = '';
    form._photoFiles.forEach(function (file, index) {
      var url = URL.createObjectURL(file);
      previewUrls.push(url);
      var item = document.createElement('div');
      item.className = 'photo-preview';
      var image = document.createElement('img');
      image.src = url;
      image.alt = '';
      var remove = document.createElement('button');
      remove.type = 'button';
      remove.setAttribute('aria-label', messages.remove);
      remove.textContent = '×';
      remove.addEventListener('click', function () {
        form._photoFiles.splice(index, 1);
        renderPhotos();
      });
      item.appendChild(image);
      item.appendChild(remove);
      previews.appendChild(item);
    });
    photoText.textContent = form._photoFiles.length ? messages.files + ': ' + form._photoFiles.length + '/4' : photoText.dataset.original;
  }

  photoInput.addEventListener('change', function () {
    var incoming = Array.prototype.slice.call(photoInput.files || []);
    var images = incoming.filter(isImage);
    var valid = images.filter(function (file) { return file.size <= 15 * 1024 * 1024; });
    var remaining = 4 - form._photoFiles.length;
    if (images.length !== incoming.length) showError(messages.photoType);
    if (valid.length !== images.length) showError(messages.photoSize);
    var unique = [];
    valid.forEach(function (file) {
      var duplicate = form._photoFiles.concat(unique).some(function (existing) {
        return existing.name === file.name && existing.size === file.size && existing.lastModified === file.lastModified;
      });
      if (!duplicate) unique.push(file);
    });
    if (unique.length > remaining) showError(messages.photoMax);
    unique.slice(0, remaining).forEach(function (file) { form._photoFiles.push(file); });
    photoInput.value = '';
    renderPhotos();
  });

  function getAttribution() {
    var keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'gbraid', 'wbraid'];
    var params = new URLSearchParams(location.search);
    var value = { landing_page: location.href, referrer: document.referrer || '' };
    keys.forEach(function (key) {
      if (params.get(key)) value[key] = params.get(key).slice(0, 300);
    });
    try {
      var first = JSON.parse(sessionStorage.getItem('luxaed_attribution') || 'null');
      if (first) return first;
      sessionStorage.setItem('luxaed_attribution', JSON.stringify(value));
    } catch (_) {}
    return value;
  }
  form._attribution = getAttribution();

  function canvasBlob(canvas, quality) {
    return new Promise(function (resolve) { canvas.toBlob(resolve, 'image/jpeg', quality); });
  }
  function toBase64(blob) {
    return new Promise(function (resolve, reject) {
      var reader = new FileReader();
      reader.onload = function () { resolve(String(reader.result).split(',')[1] || ''); };
      reader.onerror = reject;
      reader.readAsDataURL(blob);
    });
  }
  function compressPhoto(file) {
    return new Promise(function (resolve, reject) {
      var image = new Image();
      var url = URL.createObjectURL(file);
      image.onload = async function () {
        try {
          var scale = Math.min(1, 1600 / Math.max(image.naturalWidth, image.naturalHeight));
          var canvas = document.createElement('canvas');
          canvas.width = Math.max(1, Math.round(image.naturalWidth * scale));
          canvas.height = Math.max(1, Math.round(image.naturalHeight * scale));
          canvas.getContext('2d').drawImage(image, 0, 0, canvas.width, canvas.height);
          var blob = await canvasBlob(canvas, 0.82);
          var quality = 0.72;
          while (blob && blob.size > 650 * 1024 && quality >= 0.5) {
            blob = await canvasBlob(canvas, quality);
            quality -= 0.1;
          }
          var resizePass = 0;
          while (blob && blob.size > 650 * 1024 && resizePass < 3) {
            var shrink = Math.sqrt((620 * 1024) / blob.size);
            var smaller = document.createElement('canvas');
            smaller.width = Math.max(1, Math.round(canvas.width * shrink));
            smaller.height = Math.max(1, Math.round(canvas.height * shrink));
            smaller.getContext('2d').drawImage(canvas, 0, 0, smaller.width, smaller.height);
            canvas = smaller;
            blob = await canvasBlob(smaller, 0.7);
            resizePass += 1;
          }
          URL.revokeObjectURL(url);
          if (!blob || blob.size > 650 * 1024) throw new Error('photo');
          resolve({
            name: (file.name || 'photo').replace(/\.[^.]+$/, '') + '.jpg',
            type: 'image/jpeg',
            data: await toBase64(blob)
          });
        } catch (_) {
          URL.revokeObjectURL(url);
          reject(new Error('photo'));
        }
      };
      image.onerror = function () {
        URL.revokeObjectURL(url);
        reject(new Error('photo'));
      };
      image.src = url;
    });
  }

  form.addEventListener('submit', async function (event) {
    event.preventDefault();
    if (form._gotcha && form._gotcha.value) return;
    syncProject();
    if (!selectedServices().length) {
      projectError.textContent = messages.choose;
      projectError.classList.add('is-visible');
      form.querySelector('#projectChoices').classList.add('has-error');
      choices[0].focus();
      return;
    }
    formError.classList.remove('is-visible');
    var required = Array.prototype.slice.call(form.querySelectorAll('[required]'));
    required.forEach(function (field) { field.removeAttribute('aria-invalid'); });
    var invalid = required.find(function (field) { return !field.value.trim() || !field.checkValidity(); });
    if (invalid) {
      invalid.setAttribute('aria-invalid', 'true');
      showError(messages.required);
      invalid.focus();
      return;
    }
    var phoneDigits = form.elements.phone.value.replace(/\D/g, '');
    if (!/^[^\s@]{1,80}@[^\s@]{1,120}\.[^\s@]{2,30}$/.test(form.elements.email.value.trim())) {
      form.elements.email.setAttribute('aria-invalid', 'true');
      showError(messages.email);
      form.elements.email.focus();
      return;
    }
    if (phoneDigits.length < 7 || phoneDigits.length > 15) {
      form.elements.phone.setAttribute('aria-invalid', 'true');
      showError(messages.phone);
      form.elements.phone.focus();
      return;
    }

    var button = form.querySelector('button[type="submit"]');
    var card = form.closest('.form-card');
    button.disabled = true;
    card.classList.add('is-loading');
    var data = {};
    new FormData(form).forEach(function (value, key) {
      if (key !== 'photos') data[key] = value;
    });
    data.form_version = '2';
    if (!form._submissionId) form._submissionId = (window.crypto && window.crypto.randomUUID) ? window.crypto.randomUUID() : (Date.now().toString(36) + '-' + Math.random().toString(36).slice(2));
    data.submission_id = form._submissionId;
    data.page = location.href;
    data.t = Math.round((Date.now() - (window.__t0 || Date.now())) / 1000);
    data.attribution = form._attribution;

    try {
      data.photos_expected = form._photoFiles.length;
      data.photos_b64 = [];
      for (var photoIndex = 0; photoIndex < form._photoFiles.length; photoIndex += 1) {
        data.photos_b64.push(await compressPhoto(form._photoFiles[photoIndex]));
      }
      var controller = new AbortController();
      var timer = setTimeout(function () { controller.abort(); }, 20000);
      var response = await fetch('/api/lead/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
        signal: controller.signal
      });
      clearTimeout(timer);
      var responseData = {};
      try { responseData = await response.json(); } catch (_) {}
      if (!response.ok) throw new Error(responseData.error === 'invalid_photos' ? 'photo' : (responseData.error === 'required_fields' ? 'required' : 'send'));
      form.querySelector('.form-fields').hidden = true;
      var success = form.querySelector('#formOk');
      success.style.display = 'block';
      success.focus();
      card.classList.remove('is-loading');
      (window.dataLayer = window.dataLayer || []).push({ event: 'generate_lead', form_service: data.service || '', form_services: data.services || '', lead_id: data.submission_id });
      if (window.gtag) {
        window.gtag('event', 'generate_lead', { form_service: data.service || '', form_services: data.services || '', event_id: data.submission_id });
        window.gtag('event', 'conversion', { send_to: 'AW-960623543/dU7wCMWR9swcELfnh8oD', value: 1.0, currency: 'EUR', transaction_id: data.submission_id });
      }
    } catch (error) {
      button.disabled = false;
      card.classList.remove('is-loading');
      showError(error && error.message === 'photo' ? messages.photoFail : (error && error.message === 'required' ? messages.required : messages.send));
    }
  });
})();
