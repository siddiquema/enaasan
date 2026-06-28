/**
 * i18n.js — enaasan.online
 * Language: detection → localStorage → navigator.language → 'en'
 * Usage: add data-i18n="key" to any element; value becomes textContent
 * Supports: en, ta (te, hi reserved for future tasks)
 */
(function () {
  'use strict';

  var SUPPORTED = ['en', 'ta', 'te', 'hi'];
  var DEFAULT_LANG = 'en';
  var STORAGE_KEY = 'enaasan_lang';
  var cache = {};

  /* ── 1. Detect language ── */
  function detectLang() {
    // 1a. localStorage preference
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored && SUPPORTED.indexOf(stored) !== -1) return stored;

    // 1b. navigator.language (e.g. "ta-IN" → "ta")
    var nav = (navigator.language || navigator.userLanguage || '').split('-')[0].toLowerCase();
    if (SUPPORTED.indexOf(nav) !== -1) return nav;

    return DEFAULT_LANG;
  }

  /* ── 2. Fetch + cache JSON ── */
  function loadMessages(lang, callback) {
    if (cache[lang]) { callback(cache[lang]); return; }

    var url = 'locales/' + lang + '.json';
    fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status + ' loading ' + url);
        return r.json();
      })
      .then(function (data) {
        cache[lang] = data;
        callback(data);
      })
      .catch(function (err) {
        console.warn('[i18n] Failed to load', lang, '— falling back to', DEFAULT_LANG, err);
        if (lang !== DEFAULT_LANG) {
          loadMessages(DEFAULT_LANG, callback);
        }
      });
  }

  /* ── 3. Swap DOM text ── */
  function applyMessages(messages) {
    // Handle <title data-i18n="key">
    var titleEl = document.querySelector('title[data-i18n]');
    if (titleEl) {
      var titleKey = titleEl.getAttribute('data-i18n');
      if (messages[titleKey] !== undefined) { document.title = messages[titleKey]; }
    }
    // Handle <meta name="description" data-i18n="key">
    var metaDesc = document.querySelector('meta[name="description"][data-i18n]');
    if (metaDesc) {
      var metaKey = metaDesc.getAttribute('data-i18n');
      if (messages[metaKey] !== undefined) { metaDesc.setAttribute('content', messages[metaKey]); }
    }
    // Handle all other [data-i18n] elements
    var els = document.querySelectorAll('[data-i18n]');
    for (var i = 0; i < els.length; i++) {
      var el = els[i];
      if (el.tagName === 'TITLE' || (el.tagName === 'META' && el.getAttribute('name') === 'description')) {
        continue; // already handled above
      }
      var key = el.getAttribute('data-i18n');
      if (messages[key] !== undefined) {
        el.textContent = messages[key];
      }
    }
  }

  /* ── 4. Mark active pill ── */
  function updatePills(lang) {
    var pills = document.querySelectorAll('.lang-pill');
    for (var i = 0; i < pills.length; i++) {
      var isActive = pills[i].getAttribute('data-lang') === lang;
      pills[i].classList.toggle('active', isActive);
      pills[i].setAttribute('aria-pressed', isActive ? 'true' : 'false');
    }
  }

  /* ── 5. Public: switch language ── */
  function switchLang(lang) {
    if (SUPPORTED.indexOf(lang) === -1) lang = DEFAULT_LANG;
    localStorage.setItem(STORAGE_KEY, lang);
    document.documentElement.lang = lang;
    updatePills(lang);
    loadMessages(lang, function (messages) {
      applyMessages(messages);
      // Dispatch event so other scripts can react
      document.dispatchEvent(new CustomEvent('langchange', { detail: { lang: lang } }));
    });
  }

  /* ── 6. Wire pill buttons (works for pills added before or after DOMContentLoaded) ── */
  function wirePills() {
    var pills = document.querySelectorAll('.lang-pill');
    for (var i = 0; i < pills.length; i++) {
      (function (pill) {
        pill.addEventListener('click', function () {
          switchLang(pill.getAttribute('data-lang'));
        });
      })(pills[i]);
    }
  }

  /* ── 7. Init ── */
  function init() {
    var lang = detectLang();
    document.documentElement.lang = lang;
    wirePills();
    updatePills(lang);
    if (lang !== DEFAULT_LANG) {
      loadMessages(lang, applyMessages);
    }
    // If lang === 'en' the static HTML already has English text; no swap needed.
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Re-apply saved language on back-navigation (bfcache / Android Chrome back button).
  // DOMContentLoaded does not fire when the page is restored from the back-forward cache,
  // so we also listen to pageshow and check event.persisted.
  window.addEventListener('pageshow', function (event) {
    if (event.persisted) {
      // Page was served from bfcache — DOM is already rendered but language
      // selection may have changed on another page, so re-read and re-apply.
      var savedLang = localStorage.getItem(STORAGE_KEY) || DEFAULT_LANG;
      document.documentElement.lang = savedLang;
      updatePills(savedLang);
      loadMessages(savedLang, applyMessages);
    }
  });

  // Expose globally so inline onclick="switchLang('ta')" also works
  window.switchLang = switchLang;

})();
