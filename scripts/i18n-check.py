#!/usr/bin/env python3
"""
i18n-check.py — translation audit and guard for enaasan.online

The live site translates pages with js/i18n.js, which swaps the text of every
element carrying data-i18n="key" using locales/<lang>.json (en, ta, te, hi).
The English text written in the HTML is what visitors see first; locales/en.json
is used when someone switches back to English.

Usage (from the repo root; Python 3.8+, no dependencies):

  python3 scripts/i18n-check.py check                 # guard: compare with baseline
  python3 scripts/i18n-check.py check --base origin/main
                                                       # also warn about English keys
                                                       # changed since BASE without
                                                       # matching ta/te/hi updates
  python3 scripts/i18n-check.py check --strict        # turn warnings into failures
  python3 scripts/i18n-check.py audit                 # rewrite translation-audit.md
  python3 scripts/i18n-check.py baseline              # accept current known issues

check FAILS (exit 1) on NEW problems not in scripts/i18n-baseline.json:
  - a data-i18n key used on a page but missing from locales/en.json
  - a key in locales/en.json missing from ta, te or hi
  - invalid JSON in a locale file
check WARNS on:
  - English value changed since --base while a language kept its old value
  - page English text (data-i18n element) that no longer matches en.json
"""
import argparse
import html
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from html.parser import HTMLParser

LANGS = ['ta', 'te', 'hi']
LANG_NAMES = {'ta': 'Tamil', 'te': 'Telugu', 'hi': 'Hindi'}
REVIEWERS = {'ta': 'TBD', 'te': 'Vijaya', 'hi': 'Shafi'}
LIVE_DIR = 'locales'
LEGACY_DIR = 'i18n'
BASELINE = 'scripts/i18n-baseline.json'
SKIP_DIRS = ('knowledge/', 'node_modules/', '.github/')

ELEM_RE = re.compile(r'<(\w+)\b([^>]*?)\bdata-i18n="([^"]+)"([^>]*)>(.*?)</\1\s*>', re.S)
META_RE = re.compile(r'<meta\b[^>]*\bdata-i18n="([^"]+)"[^>]*>', re.S)
KEY_RE = re.compile(r'data-i18n="([^"]+)"')
WORDS_RE = re.compile(r'[A-Za-z][A-Za-z\'’-]+')


def run(*args):
    return subprocess.run(args, capture_output=True, text=True, encoding='utf-8').stdout


def norm(text):
    return re.sub(r'\s+', ' ', html.unescape(text)).strip()


def load_json(path, ref=None):
    """Load a JSON file from the working tree, or from a git ref."""
    if ref:
        raw = subprocess.run(['git', 'show', f'{ref}:{path}'], capture_output=True)
        if raw.returncode != 0:
            return None
        text = raw.stdout.decode('utf-8-sig')
    else:
        if not os.path.exists(path):
            return None
        with open(path, encoding='utf-8-sig') as f:
            text = f.read()
    return json.loads(text)


def pages():
    files = run('git', 'ls-files', '*.html').split()
    return sorted(p for p in files if not p.startswith(SKIP_DIRS))


def read(path):
    with open(path, encoding='utf-8-sig') as f:
        return f.read()


def page_keys(src):
    return sorted(set(KEY_RE.findall(src)))


def page_english(src):
    """Return {key: English text on the page} for data-i18n leaf elements and meta tags."""
    out = {}
    for _tag, _a1, key, _a2, inner in ELEM_RE.findall(src):
        if '<' in inner:            # not a leaf; i18n.js would destroy child HTML (issue #1)
            continue
        out.setdefault(key, norm(inner))
    for m in META_RE.finditer(src):
        c = re.search(r'\bcontent="([^"]*)"', m.group(0))
        if c:
            out.setdefault(m.group(1), norm(c.group(1)))
    return out


class HardcodedText(HTMLParser):
    """Collect visible English text that is not inside a data-i18n element."""
    TRANSLATABLE_ATTRS = ('placeholder', 'alt', 'aria-label', 'title')
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta',
            'param', 'source', 'track', 'wbr'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []          # (tag, is_i18n)
        self.text, self.attrs, self.script_strings = [], [], []
        self.in_head = False

    def _inside(self, tags):
        return any(t in tags for t, _ in self.stack)

    def _in_i18n(self):
        return any(i for _, i in self.stack)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'head':
            self.in_head = True
        if not self.in_head and not self._in_i18n() and 'data-i18n' not in a:
            for name in self.TRANSLATABLE_ATTRS:
                v = a.get(name)
                if v and len(WORDS_RE.findall(v)) >= 2:
                    self.attrs.append(norm(v))
        if tag not in self.VOID:
            self.stack.append((tag, 'data-i18n' in a))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID and self.stack and self.stack[-1][0] == tag:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag == 'head':
            self.in_head = False
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        t = norm(data)
        if not t:
            return
        if self._inside(('script',)):
            for s in re.findall(r"'((?:[^'\\\n]|\\.){12,})'|\"((?:[^\"\\\n]|\\.){12,})\"|`([^`]{12,})`", data):
                s = next(x for x in s if x)
                s = norm(re.sub(r'<[^>]+>|\$\{[^}]*\}', ' ', s))
                if (len(WORDS_RE.findall(s)) >= 4 and not re.search(r'[{};=]|^\s*[.#]|https?:', s)
                        and not re.match(r'(Failed|Error|Could not|Unable)\b', s)):   # console messages
                    self.script_strings.append(s)
            return
        if self._inside(('style', 'noscript', 'svg')) or self._in_i18n():
            return
        if self.in_head and not self._inside(('title',)):
            return
        if len(WORDS_RE.findall(t)) >= 2:
            self.text.append(t)


def hardcoded(src):
    # structured data for search engines is not page text
    src = re.sub(r'<script[^>]*application/ld\+json[^>]*>.*?</script>', '', src, flags=re.S | re.I)
    p = HardcodedText()
    p.feed(src)
    return p


def blame_times(path):
    """{key: unix time of the commit that last changed that key's line}."""
    out = run('git', 'blame', '--line-porcelain', path)
    times, cur = {}, None
    for line in out.splitlines():
        if line.startswith('author-time '):
            cur = int(line.split()[1])
        elif line.startswith('\t'):
            m = re.match(r'\s*"([^"]+)"\s*:', line[1:])
            if m and cur is not None:
                times[m.group(1)] = cur
    return times


def is_acronym_or_number(v):
    return not re.search(r'[a-z]{4,}', v)


# ─────────────────────────── analysis ───────────────────────────

def analyse():
    en = load_json(f'{LIVE_DIR}/en.json')
    tr = {l: load_json(f'{LIVE_DIR}/{l}.json') for l in LANGS}
    legacy_en = load_json(f'{LEGACY_DIR}/en.json') or {}
    legacy = {l: load_json(f'{LEGACY_DIR}/{l}.json') or {} for l in LANGS}

    page_list = pages()
    key_pages = defaultdict(list)
    per_page = {}
    drift = {}               # key -> (page, page English)
    for p in page_list:
        src = read(p)
        keys = page_keys(src)
        eng = page_english(src)
        hc = hardcoded(src)
        per_page[p] = {'keys': keys, 'hardcoded': hc}
        for k in keys:
            key_pages[k].append(p)
        for k, t in eng.items():
            if k in en and t != norm(en[k]):
                drift.setdefault(k, (p, t))

    missing_en = sorted(k for k in key_pages if k not in en)
    missing = {l: sorted(set(k for k in en if k not in tr[l]) | set(missing_en)) for l in LANGS}

    # stale signals
    legacy_changed = {k: legacy_en[k] for k in en if k in legacy_en and legacy_en[k] != en[k]}
    en_times = blame_times(f'{LIVE_DIR}/en.json')
    stale = {l: {} for l in LANGS}
    for l in LANGS:
        lt = blame_times(f'{LIVE_DIR}/{l}.json')
        for k in en:
            sig = []
            if k in drift:
                sig.append('page-text')
            if k in legacy_changed:
                sig.append('legacy-en')
            if k in en_times and k in lt and en_times[k] > lt[k]:
                sig.append('git-date')
            if sig and k in tr[l]:
                stale[l][k] = sig

    untranslated = {l: sorted(k for k in en if k in tr[l] and tr[l][k] == en[k]
                              and re.search(r'[A-Za-z]{3}', en[k])) for l in LANGS}
    legacy_diff = {l: sorted(k for k in tr[l] if k in legacy[l] and legacy[l][k] != tr[l][k]) for l in LANGS}
    unused = sorted(k for k in en if k not in key_pages)

    return dict(en=en, tr=tr, legacy_en=legacy_en, legacy=legacy, pages=page_list,
                per_page=per_page, key_pages=key_pages, drift=drift, missing_en=missing_en,
                missing=missing, stale=stale, untranslated=untranslated,
                legacy_changed=legacy_changed, legacy_diff=legacy_diff, unused=unused)


# ─────────────────────────── audit report ───────────────────────────

def md_escape(s, n=90):
    s = s.replace('|', '\\|').replace('\n', ' ')
    return s if len(s) <= n else s[:n - 1] + '…'


def write_audit(a, out='translation-audit.md', appendix='translation-audit-hardcoded.md'):
    en, tr = a['en'], a['tr']
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    head = run('git', 'rev-parse', '--short', 'HEAD').strip()
    L = []
    w = L.append
    w('# Translation Audit — enaasan.online')
    w('')
    w(f'*Generated {today} from commit `{head}` by `scripts/i18n-check.py audit`. '
      'Re-run the script to refresh; do not hand-edit the tables.*')
    w('')
    w('> **Audit only.** No translation file was changed. Human-reviewed translations are untouched. '
      f'Reviewers: Telugu — {REVIEWERS["te"]}, Hindi — {REVIEWERS["hi"]}, Tamil — {REVIEWERS["ta"]}.')
    w('')
    w('## 1. How translation works on this site')
    w('')
    w('- **Engine:** `js/i18n.js` (loaded by 12 pages). On load it detects the language '
      '(saved choice → browser language → English). For Tamil, Telugu or Hindi it fetches '
      '`locales/<lang>.json` and replaces the `textContent` of every element with `data-i18n="key"`, '
      'plus `<title>` and `<meta name="description">`.')
    w('- **English source of truth:** the English written in each HTML page. `locales/en.json` is only '
      'applied when a visitor switches *back* to English, so it can silently drift from the page.')
    w('- **Live files:** `locales/en.json`, `ta.json`, `te.json`, `hi.json` '
      f'({len(en)} keys each).')
    w(f'- **Legacy files — not loaded by any page:** `i18n/*.json` ({len(a["legacy_en"])} keys) and the '
      'root `i18n.js`. Some English fixes and Shafi\'s Hindi review were saved here (see §6). '
      'Decision 2026-10-11: leave both folders as they are; report only.')
    w('- **Rule (issue #1):** `data-i18n` only on leaf elements — `textContent` destroys child HTML.')
    w('')
    w('**Stale-key signals** (git history of `locales/` has only 2 commits, so dates alone cannot show '
      'staleness; three signals are combined):')
    w('')
    w('| Signal | Meaning |')
    w('|---|---|')
    w('| `page-text` | The English on the page no longer matches `locales/en.json` — English was edited in the HTML after the translation was made |')
    w('| `legacy-en` | `i18n/en.json` has a newer English value than `locales/en.json` |')
    w('| `git-date` | `git blame`: the English line in `locales/en.json` was changed after the translated line |')
    w('')

    # summary table
    w('## 2. Summary — page × language')
    w('')
    w('Counts are keys used on that page. **Missing** = no value in the live language file (or not even in `en.json`). '
      '**Stale** = translation exists but English has changed. **Same as EN** = value identical to English. '
      '**OK** = keys with none of these. **Hardcoded** = visible English text not routed through i18n '
      '(text nodes + translatable attributes + English strings in page scripts; approximate).')
    w('')
    w('| Page | Keys | Tamil miss / stale / same / OK | Telugu miss / stale / same / OK | Hindi miss / stale / same / OK | Hardcoded |')
    w('|---|---:|---|---|---|---:|')
    totals = defaultdict(int)
    for p in a['pages']:
        keys = a['per_page'][p]['keys']
        hc = a['per_page'][p]['hardcoded']
        hcn = len(hc.text) + len(hc.attrs) + len(hc.script_strings)
        if not keys and not hcn:
            continue
        cells = []
        for l in LANGS:
            miss = sum(1 for k in keys if k in a['missing'][l])
            st = sum(1 for k in keys if k in a['stale'][l])
            same = sum(1 for k in keys if k in a['untranslated'][l] and k not in a['stale'][l])
            ok = len(keys) - miss - st - same
            totals[l + 'm'] += miss; totals[l + 's'] += st; totals[l + 'u'] += same; totals[l + 'o'] += ok
            cells.append(f'{miss} / {st} / {same} / {ok}' if keys else '—')
        totals['keys'] += len(keys); totals['hc'] += hcn
        w(f'| `{p}` | {len(keys)} | ' + ' | '.join(cells) + f' | {hcn} |')
    w('| **Total** | **{}** | **{} / {} / {} / {}** | **{} / {} / {} / {}** | **{} / {} / {} / {}** | **{}** |'.format(
        totals['keys'], *[totals[l + x] for l in LANGS for x in 'msuo'], totals['hc']))
    w('')
    w('*Keys shared by several pages are counted on each page that uses them.*')
    w('')

    # per language
    w('## 3. Per language')
    w('')
    for l in LANGS:
        w(f'### 3.{LANGS.index(l) + 1} {LANG_NAMES[l]} (`{l}`) — reviewer: {REVIEWERS[l]}')
        w('')
        miss, stl, un = a['missing'][l], a['stale'][l], a['untranslated'][l]
        w(f'- Missing: **{len(miss)}** · Stale: **{len(stl)}** · Same as English: **{len(un)}** '
          f'(of which {sum(1 for k in un if not is_acronym_or_number(en[k]))} look like real untranslated text)')
        w('')
        w(f'**Missing keys ({len(miss)})**')
        w('')
        if miss:
            w('| Key | Page(s) | In en.json? |')
            w('|---|---|---|')
            for k in miss:
                w(f'| `{k}` | {", ".join(a["key_pages"].get(k, ["—"]))} | {"yes" if k in en else "**no** — add English first"} |')
        else:
            w('None.')
        w('')
        w(f'**Stale keys ({len(stl)})**')
        w('')
        if stl:
            w('| Key | Signal | English now | Current translation |')
            w('|---|---|---|---|')
            for k in sorted(stl):
                now = a['drift'][k][1] if k in a['drift'] else a['legacy_changed'].get(k, en[k])
                w(f'| `{k}` | {", ".join(stl[k])} | {md_escape(now, 70)} | {md_escape(tr[l][k], 60)} |')
        else:
            w('None.')
        w('')
        w(f'**Same as English ({len(un)})** — review needed; acronyms and numbers are often fine')
        w('')
        if un:
            w('| Key | Value | Likely |')
            w('|---|---|---|')
            for k in un:
                w(f'| `{k}` | {md_escape(en[k], 70)} | {"acronym/number — probably OK" if is_acronym_or_number(en[k]) else "**untranslated**"} |')
        w('')

    # hardcoded
    w('## 4. Hardcoded English (not routed through i18n)')
    w('')
    w('These strings stay in English whatever language the visitor picks. Counts are approximate '
      '(heuristic: 2+ English words in a text node or attribute; 4+ words in a script string). '
      f'Full list: [`{appendix}`]({appendix}).')
    w('')
    w('| Page | Text nodes | Attributes | Script strings | Total | Uses i18n? |')
    w('|---|---:|---:|---:|---:|---|')
    for p in a['pages']:
        hc = a['per_page'][p]['hardcoded']
        t = len(hc.text) + len(hc.attrs) + len(hc.script_strings)
        if t:
            w(f'| `{p}` | {len(hc.text)} | {len(hc.attrs)} | {len(hc.script_strings)} | {t} | '
              f'{"yes" if a["per_page"][p]["keys"] else "**no**"} |')
    w('')
    w('Script strings are mostly the data behind interactive cards (exam cards on `after12.html`, '
      'stream paths on `streams.html`, career profiles on `careers.html`) — known bugs B-14 / B-15.')
    w('')

    # structural
    w('## 5. Structural problems found')
    w('')
    w('1. **Switching back to English shows old English.** `js/i18n.js` applies `locales/en.json` when a visitor '
      f'switches back to English. {len(a["drift"])} page elements differ from it, e.g. homepage stats revert to '
      '"60+ / 20+" and the About title reverts to the pre-SEO version.')
    fj = [k for k in a['missing_en'] if any('first-job' in p for p in a['key_pages'][k])]
    w(f'2. **`skills/first-job/` cannot translate.** {len(fj)} of its keys are not in any language file, and its '
      'script requests `locales/<lang>.json` relative to `/skills/first-job/`, which does not exist — '
      'Tamil/Telugu/Hindi silently fall back to English.')
    w(f'3. **Legacy `i18n/` folder** holds edits that are not live (§6).')
    w(f'4. **{len(a["unused"])} keys in `en.json` are not used by any page:** ' +
      ', '.join(f'`{k}`' for k in a['unused']))
    w('')

    w('## 6. Legacy folder `i18n/` — differences from the live files')
    w('')
    w('Not loaded by the site. Listed so reviewed work is not lost.')
    w('')
    w('| Language | Keys whose `i18n/` value differs from `locales/` |')
    w('|---|---:|')
    w(f'| English | {len(a["legacy_changed"])} |')
    for l in LANGS:
        w(f'| {LANG_NAMES[l]} | {len(a["legacy_diff"][l])} |')
    w('')
    w('Hindi: commit `1f7841e` (2026-07-02) "Apply Shafi\'s Hindi review decisions" changed 23 values in '
      '`i18n/hi.json` only — **reviewed Hindi that is not live.**')
    w('')
    w('<details><summary>Hindi keys that differ (legacy vs live)</summary>')
    w('')
    w('| Key | `i18n/hi.json` (legacy) | `locales/hi.json` (live) |')
    w('|---|---|---|')
    for k in a['legacy_diff']['hi']:
        w(f'| `{k}` | {md_escape(a["legacy"]["hi"][k], 60)} | {md_escape(tr["hi"][k], 60)} |')
    w('')
    w('</details>')
    w('')
    w('## 7. Re-running and the guard')
    w('')
    w('See README → "Translation checks". `python3 scripts/i18n-check.py audit` regenerates this file; '
      '`check` runs in GitHub Actions on every pull request that touches pages or locale files.')
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')

    A = ['# Hardcoded English — full list', '',
         f'*Generated {today} from `{head}` by `scripts/i18n-check.py audit`. Companion to '
         '`translation-audit.md` §4. Heuristic — includes some brand names and code-like strings.*', '']
    for p in a['pages']:
        hc = a['per_page'][p]['hardcoded']
        if not (hc.text or hc.attrs or hc.script_strings):
            continue
        A.append(f'## `{p}`')
        A.append('')
        for label, items in (('Text', hc.text), ('Attributes', hc.attrs), ('Script strings', hc.script_strings)):
            if items:
                A.append(f'**{label} ({len(items)})**')
                A.append('')
                for s in items:
                    A.append(f'- {md_escape(s, 160)}')
                A.append('')
    with open(appendix, 'w', encoding='utf-8') as f:
        f.write('\n'.join(A) + '\n')
    return totals


# ─────────────────────────── guard ───────────────────────────

def current_issues(a):
    return {
        'missing_in_en': a['missing_en'],
        'missing_in_lang': {l: sorted(k for k in a['missing'][l] if k in a['en']) for l in LANGS},
        'page_text_drift': sorted(a['drift']),
    }


def annotate(level, msg):
    if os.environ.get('GITHUB_ACTIONS'):
        print(f'::{level}::{msg}')
    else:
        print(f'{level.upper()}: {msg}')


def check(args):
    errors, warnings = 0, 0
    for l in ['en'] + LANGS:
        try:
            load_json(f'{LIVE_DIR}/{l}.json')
        except json.JSONDecodeError as e:
            annotate('error', f'{LIVE_DIR}/{l}.json is not valid JSON: {e}')
            return 1
    a = analyse()
    base = load_json(BASELINE) or {'missing_in_en': [], 'missing_in_lang': {}, 'page_text_drift': []}
    cur = current_issues(a)

    for k in cur['missing_in_en']:
        if k not in base['missing_in_en']:
            annotate('error', f'Key "{k}" is used on {", ".join(a["key_pages"][k])} but missing from {LIVE_DIR}/en.json')
            errors += 1
    for l in LANGS:
        known = set(base['missing_in_lang'].get(l, []))
        for k in cur['missing_in_lang'][l]:
            if k not in known:
                annotate('error', f'Key "{k}" is in en.json but missing from {LIVE_DIR}/{l}.json ({LANG_NAMES[l]}) — '
                                  'add a value (an English placeholder is acceptable; it will be listed for review)')
                errors += 1
    for k in cur['page_text_drift']:
        if k not in base['page_text_drift']:
            p, t = a['drift'][k]
            annotate('warning', f'{p}: English for "{k}" is "{t[:80]}" but en.json has "{a["en"][k][:80]}" — '
                                'update en.json and flag ta/te/hi for re-translation')
            warnings += 1

    if args.base:
        old_en = load_json(f'{LIVE_DIR}/en.json', ref=args.base) or {}
        old_tr = {l: load_json(f'{LIVE_DIR}/{l}.json', ref=args.base) or {} for l in LANGS}
        for k, v in a['en'].items():
            if k in old_en and old_en[k] != v:
                stale_in = [LANG_NAMES[l] for l in LANGS if a['tr'][l].get(k) == old_tr[l].get(k)]
                if stale_in:
                    annotate('warning', f'English for "{k}" changed but {", ".join(stale_in)} kept the old translation '
                                        '— update it or note it in the language\'s Translation sync issue')
                    warnings += 1

    fixed = (len(base['missing_in_en']) - len(cur['missing_in_en'])
             + sum(len(base['missing_in_lang'].get(l, [])) - len(cur['missing_in_lang'][l]) for l in LANGS))
    print(f'\ni18n check: {errors} new error(s), {warnings} warning(s). '
          f'Known issues in baseline: {len(base["missing_in_en"])} keys missing from en.json, '
          f'{len(base["page_text_drift"])} page-text drifts.')
    if fixed > 0:
        print(f'{fixed} baseline issue(s) are now fixed — run "python3 scripts/i18n-check.py baseline" to shrink the baseline.')
    if errors or (args.strict and warnings):
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('mode', choices=['check', 'audit', 'baseline'])
    ap.add_argument('--base', help='git ref to compare English changes against (check mode)')
    ap.add_argument('--strict', action='store_true', help='treat warnings as errors')
    args = ap.parse_args()
    os.chdir(run('git', 'rev-parse', '--show-toplevel').strip() or '.')

    if args.mode == 'check':
        sys.exit(check(args))
    a = analyse()
    if args.mode == 'audit':
        t = write_audit(a)
        print('Wrote translation-audit.md and translation-audit-hardcoded.md')
        for l in LANGS:
            print(f'{LANG_NAMES[l]:7s} missing {len(a["missing"][l]):3d}  stale {len(a["stale"][l]):3d}  '
                  f'same-as-en {len(a["untranslated"][l]):3d}')
    else:
        with open(BASELINE, 'w', encoding='utf-8') as f:
            json.dump(current_issues(a), f, indent=2, ensure_ascii=False)
            f.write('\n')
        print(f'Wrote {BASELINE}')


if __name__ == '__main__':
    main()
