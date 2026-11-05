/* Free Vercel Speed Insights. No form values or query parameters. */
(function () {
  'use strict';
  var hosts = ["luxaed.ee", "www.luxaed.ee"];
  if (hosts.indexOf(location.hostname) === -1) return;
  window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
  window.si('beforeSend', function (event) {
    try {
      var url = new URL(event.url);
      if (hosts.indexOf(url.hostname) === -1 || /^\/(admin|api)(\/|$)/.test(url.pathname)) return null;
      url.search = ''; url.hash = '';
      return Object.assign({}, event, {url: url.toString()});
    } catch (_) { return null; }
  });
  var script = document.createElement('script');
  script.defer = true; script.src = '/_vercel/speed-insights/script.js';
  script.dataset.sdkn = 'plain-html'; script.dataset.sdkv = '2.0.0';
  document.head.appendChild(script);
})();
