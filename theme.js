/**
 * theme.js — enaasan.online
 * Theme: detection → localStorage → system preference → 'dark'
 * Usage: add data-theme="light|slate" to theme pills; default is 'dark'
 * Themes applied via data-theme attribute on <html>
 */
(function () {
  'use strict';

  var SUPPORTED = ['dark', 'light', 'slate'];
  var DEFAULT_THEME = 'dark';
  var STORAGE_KEY = 'enaasan_theme';

  /* ── 1. Detect theme ── */
  function detectTheme() {
    // 1a. localStorage preference
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored && SUPPORTED.indexOf(stored) !== -1) return stored;

    // 1b. system preference (prefers-color-scheme)
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
      return 'light';
    }

    return DEFAULT_THEME;
  }

  /* ── 2. Apply theme ── */
  function applyTheme(theme) {
    if (SUPPORTED.indexOf(theme) === -1) theme = DEFAULT_THEME;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
    updatePills(theme);
    // Dispatch event so other scripts can react
    document.dispatchEvent(new CustomEvent('themechange', { detail: { theme: theme } }));
  }

  /* ── 3. Mark active pill ── */
  function updatePills(theme) {
    var pills = document.querySelectorAll('.theme-pill');
    for (var i = 0; i < pills.length; i++) {
      var isActive = pills[i].getAttribute('data-theme') === theme;
      pills[i].classList.toggle('active', isActive);
      pills[i].setAttribute('aria-pressed', isActive ? 'true' : 'false');
    }
  }

  /* ── 4. Wire pill buttons ── */
  function wirePills() {
    var pills = document.querySelectorAll('.theme-pill');
    for (var i = 0; i < pills.length; i++) {
      (function (pill) {
        pill.addEventListener('click', function () {
          applyTheme(pill.getAttribute('data-theme'));
        });
      })(pills[i]);
    }
  }

  /* ── 5. Init ── */
  function init() {
    var theme = detectTheme();
    document.documentElement.setAttribute('data-theme', theme);
    wirePills();
    updatePills(theme);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Re-apply saved theme on back-navigation (bfcache / Android Chrome back button)
  window.addEventListener('pageshow', function (event) {
    if (event.persisted) {
      var savedTheme = localStorage.getItem(STORAGE_KEY) || DEFAULT_THEME;
      document.documentElement.setAttribute('data-theme', savedTheme);
      updatePills(savedTheme);
    }
  });

  // Expose globally so inline onclick="switchTheme('light')" also works
  window.switchTheme = function (theme) { applyTheme(theme); };

})();
