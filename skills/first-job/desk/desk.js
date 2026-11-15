/* First Job Desk. Everything runs in the browser: no network calls except loading
   the two JSON content files from this folder. Nothing the visitor types is stored or sent. */
(function () {
  'use strict';

  var PAGE_URL = 'https://enaasan.online/skills/first-job/desk/';

  /* Usage events. Sent only if the visitor allowed analytics (the consent banner
     creates window.dataLayer). Event names and tool choices only: never typed text. */
  function track(name, params) {
    if (!window.dataLayer) return;
    (function () { window.dataLayer.push(arguments); })('event', name, params || {});
  }

  /* ---------- helpers ---------- */
  function el(tag, attrs) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (k) {
        var v = attrs[k];
        if (v === null || v === undefined || v === false) return;
        if (k === 'class') node.className = v;
        else if (k === 'text') node.textContent = v;
        else if (k.slice(0, 2) === 'on') node.addEventListener(k.slice(2), v);
        else node.setAttribute(k, v === true ? '' : v);
      });
    }
    for (var i = 2; i < arguments.length; i++) {
      var c = arguments[i];
      if (c === null || c === undefined || c === false) continue;
      if (Array.isArray(c)) c.forEach(function (x) { if (x) node.appendChild(x); });
      else node.appendChild(typeof c === 'string' ? document.createTextNode(c) : c);
    }
    return node;
  }
  function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }
  function shuffle(arr) {
    var a = arr.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }
  function rupees(n) {
    return '₹' + Math.round(n).toLocaleString('en-IN');
  }
  var toastTimer;
  function toast(msg) {
    var old = document.querySelector('.toast');
    if (old) old.remove();
    var t = el('div', { class: 'toast', role: 'status', text: msg });
    document.body.appendChild(t);
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { t.remove(); }, 2400);
  }
  function copyText(text, okMsg) {
    function fallback() {
      var ta = el('textarea', { 'aria-hidden': 'true' });
      ta.value = text;
      ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      ta.remove();
      toast(ok ? okMsg : 'Could not copy. Select the text and copy it yourself.');
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { toast(okMsg); }, fallback);
    } else fallback();
  }
  function loadJSON(path) {
    return fetch(path).then(function (r) {
      if (!r.ok) throw new Error(path + ' ' + r.status);
      return r.json();
    });
  }
  function loadError(container) {
    clear(container);
    container.appendChild(el('p', { class: 'empty', text: 'This tool could not load. Check your connection and refresh the page.' }));
  }

  /* ---------- tabs ---------- */
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.tab'));
  function selectTab(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
  }
  tabs.forEach(function (tab, i) {
    tab.addEventListener('click', function () { selectTab(tab, false); });
    tab.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') selectTab(tabs[(i + 1) % tabs.length], true);
      else if (e.key === 'ArrowLeft') selectTab(tabs[(i + tabs.length - 1) % tabs.length], true);
    });
  });
  var hashTab = { '#offer': 'tab-offer', '#days': 'tab-days', '#interview': 'tab-interview' }[location.hash];
  if (hashTab) selectTab(document.getElementById(hashTab), false);

  /* ---------- 01 mock interview ---------- */
  var interviewApp = document.getElementById('interviewApp');
  var IV = { data: null, role: null, idx: 0, answers: [] };

  function ivStart() {
    IV.role = null; IV.idx = 0; IV.answers = [];
    clear(interviewApp);
    interviewApp.appendChild(el('p', { class: 'label', text: 'Choose your interview' }));
    var grid = el('div', { class: 'role-grid' });
    IV.data.roles.forEach(function (role) {
      grid.appendChild(el('button', {
        class: 'role-card', type: 'button',
        onclick: function () { IV.role = role; IV.idx = 0; IV.answers = []; track('desk_interview_start', { role: role.id }); ivQuestion(); }
      },
        el('h3', { text: role.title }),
        el('p', { text: role.blurb }),
        el('p', { text: role.questions.length + ' questions · about 10 minutes' })
      ));
    });
    interviewApp.appendChild(grid);
    interviewApp.appendChild(el('p', { class: 'fineprint', text: 'The answers are examples written for practice. Real interviewers differ, and no script can predict a real result.' }));
  }

  function ivProgress() {
    var bar = el('div', { class: 'progress', 'aria-hidden': 'true' });
    IV.role.questions.forEach(function (_, i) {
      bar.appendChild(el('i', { class: i < IV.idx ? 'done' : '' }));
    });
    return bar;
  }

  function ivQuestion() {
    var q = IV.role.questions[IV.idx];
    var total = IV.role.questions.length;
    clear(interviewApp);
    interviewApp.appendChild(ivProgress());
    var head = el('div', null,
      el('p', { class: 'asker', text: 'Question ' + (IV.idx + 1) + ' of ' + total + ' · ' + IV.role.interviewer }),
      el('p', { class: 'question', tabindex: '-1', text: '“' + q.q + '”' })
    );
    interviewApp.appendChild(head);

    var area = el('div', { class: 'app' });
    interviewApp.appendChild(area);

    var choices = el('div', { class: 'choices', role: 'group', 'aria-label': 'Choose the answer closest to what you would say' });
    var buttons = [];
    shuffle(q.options).forEach(function (opt) {
      var b = el('button', { class: 'choice', type: 'button', text: opt.text });
      b.addEventListener('click', function () {
        buttons.forEach(function (x) { x.disabled = true; });
        b.classList.add('picked');
        ownBtn.disabled = true;
        ivReveal(area, q, { level: opt.level, note: opt.note, typed: false });
      });
      buttons.push(b);
      choices.appendChild(b);
    });
    area.appendChild(el('p', { class: 'label', text: 'Pick the answer closest to what you would say' }));
    area.appendChild(choices);

    var ownBtn = el('button', {
      class: 'btn btn-quiet', type: 'button', text: 'Write my own answer instead',
      onclick: function () {
        buttons.forEach(function (x) { x.disabled = true; });
        ownBtn.disabled = true;
        ivOwnAnswer(area, q);
      }
    });
    area.appendChild(el('div', null, ownBtn));
    head.querySelector('.question').focus({ preventScroll: true });
    window.scrollTo({ top: interviewApp.getBoundingClientRect().top + window.scrollY - 84 });
  }

  function ivOwnAnswer(area, q) {
    var ta = el('textarea', { 'aria-label': 'Your answer', placeholder: 'Type what you would actually say. Nobody else will see this.' });
    var card = el('div', { class: 'card' },
      el('p', { class: 'label', text: 'Your answer' }),
      ta
    );
    var checkBtn = el('button', { class: 'btn btn-primary', type: 'button', text: 'Check my answer' });
    card.appendChild(el('div', { class: 'btn-row' }, checkBtn));
    area.appendChild(card);
    ta.focus();

    checkBtn.addEventListener('click', function () {
      if (!ta.value.trim()) { toast('Write your answer first.'); ta.focus(); return; }
      checkBtn.disabled = true;
      ta.readOnly = true;
      var boxes = [];
      var checks = el('div', { class: 'checks' });
      q.listens.forEach(function (line) {
        var cb = el('input', { type: 'checkbox' });
        boxes.push(cb);
        checks.appendChild(el('label', null, cb, el('span', { text: line })));
      });
      var doneBtn = el('button', { class: 'btn btn-primary', type: 'button', text: 'See the interviewer’s view' });
      var self = el('div', { class: 'card' },
        el('p', { class: 'label', text: 'Be honest: which of these did your answer do?' }),
        checks,
        el('div', { class: 'btn-row' }, doneBtn)
      );
      area.appendChild(self);
      doneBtn.addEventListener('click', function () {
        doneBtn.disabled = true;
        boxes.forEach(function (b) { b.disabled = true; });
        var ticks = boxes.filter(function (b) { return b.checked; }).length;
        var level = ticks >= 3 ? 2 : (ticks === 2 ? 1 : 0);
        var strong = q.options.filter(function (o) { return o.level === 2; })[0];
        ivReveal(area, q, { level: level, typed: true, strong: strong, ticks: ticks });
      });
    });
  }

  function ivReveal(area, q, ans) {
    IV.answers[IV.idx] = ans;
    var note = el('div', { class: 'card card-note', tabindex: '-1' });
    if (ans.typed) {
      note.appendChild(el('p', { class: 'label', text: 'What the interviewer listens for' }));
      note.appendChild(el('p', { class: 'note-text', text: 'You ticked ' + ans.ticks + ' of 3. Here is an answer that does all three, and what the interviewer wrote about it.' }));
      note.appendChild(el('p', { class: 'stronger' }, el('strong', { text: 'A strong answer: ' }), ans.strong.text));
      note.appendChild(el('p', { class: 'stronger' }, el('strong', { text: 'Interviewer’s note: ' }), ans.strong.note));
    } else {
      note.appendChild(el('p', { class: 'label', text: 'Interviewer’s private note' }));
      note.appendChild(el('p', { class: 'note-text', text: ans.note }));
    }
    note.appendChild(el('p', { class: 'stronger' }, el('strong', { text: 'How to answer this well: ' }), q.stronger));
    var last = IV.idx === IV.role.questions.length - 1;
    note.appendChild(el('div', { class: 'btn-row' },
      el('button', {
        class: 'btn btn-primary', type: 'button', text: last ? 'See the verdict' : 'Next question',
        onclick: function () { if (last) ivVerdict(); else { IV.idx++; ivQuestion(); } }
      })
    ));
    area.appendChild(note);
    note.focus({ preventScroll: true });
    note.scrollIntoView({ block: 'nearest' });
  }

  function ivVerdict() {
    var qs = IV.role.questions;
    var max = qs.length * 2;
    var score = IV.answers.reduce(function (s, a) { return s + a.level; }, 0);
    var band = IV.data.bands.filter(function (b) { return score >= b.min; })[0];
    clear(interviewApp);
    track('desk_interview_complete', { role: IV.role.id, score: score, band: band.name });

    interviewApp.appendChild(el('div', { class: 'card card-note verdict', tabindex: '-1' },
      el('p', { class: 'label', text: 'Interviewer’s decision · ' + IV.role.title }),
      el('p', { class: 'verdict-band', text: band.name }),
      el('p', { class: 'verdict-score', text: score + ' / ' + max }),
      el('p', { class: 'note-text', text: '“' + band.line + '”' }),
      el('p', { class: 'stronger', text: band.detail })
    ));

    var recap = el('div', { class: 'card recap' }, el('p', { class: 'label', text: 'Question by question' }));
    qs.forEach(function (q, i) {
      var a = IV.answers[i];
      recap.appendChild(el('div', { class: 'recap-item' },
        el('span', { class: 'dot l' + a.level, 'aria-label': a.level + ' out of 2', text: String(a.level) }),
        el('p', null, el('strong', { text: q.q }), el('br'), q.stronger)
      ));
    });
    interviewApp.appendChild(recap);

    var shareText = 'I sat on the other side of the interview table. Interviewer’s decision: ' + band.name +
      ' (' + score + '/' + max + '). You get to read the interviewer’s notes on every answer. Free, no sign-up: ' + PAGE_URL;
    var share = el('div', { class: 'card' },
      el('p', { class: 'label', text: 'Send this to a friend who has interviews coming' }),
      el('div', { class: 'btn-row' },
        el('a', { class: 'btn btn-primary', target: '_blank', rel: 'noopener', href: 'https://wa.me/?text=' + encodeURIComponent(shareText), text: 'Share on WhatsApp', onclick: function () { track('desk_share', { method: 'whatsapp' }); } }),
        el('a', { class: 'btn', target: '_blank', rel: 'noopener', href: 'https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(PAGE_URL), text: 'Share on LinkedIn', onclick: function () { track('desk_share', { method: 'linkedin' }); } }),
        el('button', { class: 'btn', type: 'button', text: 'Save result card', onclick: function () { track('desk_share', { method: 'card' }); ivCard(band, score, max); } }),
        el('button', { class: 'btn btn-quiet', type: 'button', text: 'Copy link', onclick: function () { track('desk_share', { method: 'copy_link' }); copyText(PAGE_URL, 'Link copied'); } })
      ),
      el('p', { class: 'fineprint', text: 'Sharing is your choice. Your answers are not included, only the result.' })
    );
    interviewApp.appendChild(share);

    interviewApp.appendChild(el('div', { class: 'btn-row' },
      el('button', { class: 'btn', type: 'button', text: 'Try again', onclick: function () { IV.idx = 0; IV.answers = []; ivQuestion(); } }),
      el('button', { class: 'btn btn-quiet', type: 'button', text: 'Choose another interview', onclick: ivStart }),
      el('a', { class: 'btn btn-quiet', href: '#ownAiTitle', text: 'Practise live with your own AI' })
    ));
    interviewApp.querySelector('.verdict').focus({ preventScroll: true });
    window.scrollTo({ top: interviewApp.getBoundingClientRect().top + window.scrollY - 84 });
  }

  /* Result card: a 1080x1080 PNG drawn on a canvas. Brand colours are fixed here
     because the image leaves the site and cannot follow the theme. */
  function ivCard(band, score, max) {
    var c = document.createElement('canvas');
    c.width = 1080; c.height = 1080;
    var x = c.getContext('2d');
    x.fillStyle = '#0D1B2A'; x.fillRect(0, 0, 1080, 1080);
    x.fillStyle = '#F0A500'; x.fillRect(0, 0, 1080, 14);
    x.textBaseline = 'top';
    x.fillStyle = '#A8C0D4';
    x.font = '500 30px "DM Mono", monospace';
    x.fillText('THE OTHER SIDE OF THE TABLE', 90, 110);
    x.fillStyle = '#F2EFE9';
    x.font = '400 44px "DM Sans", sans-serif';
    x.fillText('Interviewer’s decision', 90, 250);
    x.fillStyle = '#F0A500';
    var size = 150;
    do { x.font = '800 ' + size + 'px "Syne", sans-serif'; size -= 6; } while (x.measureText(band.name).width > 900 && size > 60);
    x.fillText(band.name, 84, 320);
    x.fillStyle = '#F2EFE9';
    x.font = '500 64px "DM Mono", monospace';
    x.fillText(score + ' / ' + max, 90, 520);
    x.fillStyle = '#A8C0D4';
    x.font = '400 40px "DM Sans", sans-serif';
    wrap(x, IV.role.title + '. I answered ' + IV.role.questions.length + ' interview questions and read what the interviewer wrote about each one.', 90, 650, 900, 56);
    x.fillStyle = '#F2EFE9';
    x.font = '800 54px "Syne", sans-serif';
    x.fillText('en', 90, 880);
    var w = x.measureText('en').width;
    x.fillStyle = '#F0A500';
    x.fillText('aasan', 90 + w, 880);
    x.fillStyle = '#A8C0D4';
    x.font = '400 32px "DM Sans", sans-serif';
    x.fillText('Free · no sign-up · enaasan.online/skills/first-job/desk', 90, 970);

    c.toBlob(function (blob) {
      if (!blob) { toast('Could not create the card on this device.'); return; }
      var file = new File([blob], 'enaasan-mock-interview.png', { type: 'image/png' });
      if (navigator.canShare && navigator.canShare({ files: [file] })) {
        navigator.share({ files: [file], text: 'Try it free: ' + PAGE_URL }).catch(function () {});
        return;
      }
      var a = el('a', { href: URL.createObjectURL(blob), download: 'enaasan-mock-interview.png' });
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
      toast('Card saved to your downloads');
    }, 'image/png');
  }
  function wrap(ctx, text, x, y, maxW, lineH) {
    var words = text.split(' '), line = '';
    words.forEach(function (word) {
      var test = line ? line + ' ' + word : word;
      if (ctx.measureText(test).width > maxW && line) { ctx.fillText(line, x, y); y += lineH; line = word; }
      else line = test;
    });
    if (line) ctx.fillText(line, x, y);
  }

  loadJSON('data/interviews.json').then(function (d) { IV.data = d; ivStart(); }, function () { loadError(interviewApp); });

  /* ---------- 02 offer letter decoder ---------- */
  var offerApp = document.getElementById('offerApp');
  var OFFER_FIELDS = {
    annual: [
      { id: 'ctc', label: 'Total CTC per year', hint: 'The big number on the first page.' },
      { id: 'employerPf', label: 'Employer’s PF contribution, per year', hint: 'Goes into your PF account, not your bank account.' },
      { id: 'gratuity', label: 'Gratuity, per year', hint: 'Paid only if you complete the qualifying service. Check your letter.' },
      { id: 'insurance', label: 'Insurance and other benefits, per year', hint: 'Premiums the company pays for you. A benefit, not cash.' },
      { id: 'variable', label: 'Variable or performance pay, per year', hint: 'Not guaranteed. Depends on targets or ratings.' },
      { id: 'oneTime', label: 'One-time bonuses', hint: 'Joining or relocation bonus. Paid once, often with conditions.' }
    ],
    monthly: [
      { id: 'employeePf', label: 'Your PF deduction, per month', hint: 'In many letters this equals the employer’s PF figure divided by 12. Check yours.' },
      { id: 'profTax', label: 'Professional tax, per month', hint: 'Depends on your state. Leave blank if your letter does not show it.' },
      { id: 'otherDed', label: 'Other monthly deductions', hint: 'Income tax (TDS) if HR has told you, transport, meal card and so on.' }
    ]
  };
  var CLAUSES = [
    { t: 'Bond or service agreement',
      m: 'You agree to stay for a fixed period, often one or two years. If you leave earlier, the letter says you must pay the company an amount. Some companies also hold original certificates; think carefully before handing over originals.',
      a: 'If I leave before the period ends, exactly how much do I pay, and does the amount reduce with each month I complete?' },
    { t: 'Notice period',
      m: 'The time you must keep working after you resign, or pay for in place of working. It is often shorter during probation and longer after confirmation. A long notice period can make it harder to accept your next offer.',
      a: 'What is the notice period during probation and after confirmation, and can it be bought out?' },
    { t: 'Probation',
      m: 'A trial period at the start. The company can usually end the job, or extend the probation, more easily during this time. Benefits such as leave may also differ until you are confirmed.',
      a: 'How long is probation, what is confirmation based on, and will I get the confirmation in writing?' },
    { t: 'Variable pay',
      m: 'A part of your CTC that is paid only if you, your team or the company meet certain targets. It may be paid monthly, quarterly or once a year, and it may be paid in part or not at all.',
      a: 'What is the variable pay based on, when is it paid, and how much of it did new joiners typically receive last year?' },
    { t: 'Joining or relocation bonus',
      m: 'A one-time payment. Many letters say you must return it if you leave within a set period. It is not part of your monthly salary, so do not plan your monthly budget around it.',
      a: 'When is this paid, and do I have to return it if I leave within a certain time?' },
    { t: 'Work location and shifts',
      m: 'Many letters say the company can move you to another location, project or shift. Read whether the role is office-based, hybrid or remote, and whether night or rotational shifts apply.',
      a: 'Which location and shift will I start in, how much notice is given before a change, and is transport provided for night shifts?' },
    { t: 'Background verification',
      m: 'The offer usually depends on your documents and details checking out: marksheets, identity and earlier employment. Wrong or missing information can lead to the offer being withdrawn, even after you join.',
      a: 'Which documents do you need from me, and by when?' },
    { t: 'Offer validity and joining date',
      m: 'Most offers lapse if you do not accept by a given date, and some state that the joining date can change. Until you have a confirmed joining date, do not resign from anything else or turn down other offers lightly.',
      a: 'Is the joining date confirmed, and how will I be told if it changes?' }
  ];

  function buildOffer() {
    clear(offerApp);
    var inputs = {};
    function field(f) {
      var inp = el('input', { id: 'of-' + f.id, type: 'text', inputmode: 'numeric', autocomplete: 'off', placeholder: '0', 'aria-describedby': 'of-' + f.id + '-h' });
      inp.addEventListener('input', function () {
        var digits = inp.value.replace(/[^\d]/g, '').slice(0, 9);
        inp.value = digits ? Number(digits).toLocaleString('en-IN') : '';
        calc();
      });
      inputs[f.id] = inp;
      return el('label', { class: 'field', for: 'of-' + f.id }, f.label, el('span', { class: 'money' }, inp), el('small', { id: 'of-' + f.id + '-h', text: f.hint }));
    }
    var out = el('div', { class: 'card card-note', 'aria-live': 'polite' });

    offerApp.appendChild(el('div', { class: 'card' },
      el('p', { class: 'label', text: 'Step 1 · From the salary table (yearly figures)' }),
      el('div', { class: 'field-grid' }, OFFER_FIELDS.annual.map(field))
    ));
    offerApp.appendChild(el('div', { class: 'card' },
      el('p', { class: 'label', text: 'Step 2 · Monthly deductions' }),
      el('div', { class: 'field-grid' }, OFFER_FIELDS.monthly.map(field))
    ));
    offerApp.appendChild(out);
    offerApp.appendChild(el('p', { class: 'fineprint', text: 'This is arithmetic on the numbers you type, done on your phone. We do not see or keep them. It is not a tax calculation: income tax depends on your total income and the tax regime you choose, so ask HR for your expected monthly deduction.' }));

    offerApp.appendChild(el('h3', { text: 'What the clauses mean', style: 'margin-top:14px' }));
    CLAUSES.forEach(function (c) {
      offerApp.appendChild(el('details', { class: 'clause' },
        el('summary', { text: c.t }),
        el('div', { class: 'clause-body' },
          el('p', { text: c.m }),
          el('div', { class: 'ask' }, el('p', { class: 'label', text: 'Ask HR' }), el('p', { text: c.a }))
        )
      ));
    });
    offerApp.appendChild(el('div', { class: 'btn-row' },
      el('button', {
        class: 'btn', type: 'button', text: 'Copy all the questions for HR',
        onclick: function () {
          copyText('Questions about my offer letter:\n\n' + CLAUSES.map(function (c, i) { return (i + 1) + '. ' + c.a; }).join('\n'), 'Questions copied');
        }
      })
    ));

    var offerTracked = false;
    function val(id) { return Number(inputs[id].value.replace(/[^\d]/g, '')) || 0; }
    function calc() {
      clear(out);
      var ctc = val('ctc');
      if (!ctc) {
        out.appendChild(el('p', { class: 'label', text: 'Your monthly in-hand' }));
        out.appendChild(el('p', { class: 'result-sub', text: 'Enter your total CTC to begin. Leave any other box blank if your letter does not show it.' }));
        return;
      }
      var notCash = val('employerPf') + val('gratuity') + val('insurance') + val('variable') + val('oneTime');
      var fixed = ctc - notCash;
      if (fixed <= 0) {
        out.appendChild(el('p', { class: 'label', text: 'Check your numbers' }));
        out.appendChild(el('p', { class: 'result-sub', text: 'The parts you entered add up to more than the total CTC. Make sure every figure in step 1 is a yearly amount.' }));
        return;
      }
      var gross = fixed / 12;
      var ded = val('employeePf') + val('profTax') + val('otherDed');
      var hand = gross - ded;
      if (hand <= 0) {
        out.appendChild(el('p', { class: 'label', text: 'Check your numbers' }));
        out.appendChild(el('p', { class: 'result-sub', text: 'The monthly deductions are larger than the monthly pay. Make sure every figure in step 2 is a monthly amount.' }));
        return;
      }
      if (!offerTracked) { offerTracked = true; track('desk_offer_calc'); }
      var naive = ctc / 12;
      out.appendChild(el('p', { class: 'label', text: 'Estimated monthly in-hand' }));
      out.appendChild(el('p', { class: 'result-big', text: rupees(hand) }));
      out.appendChild(el('p', { class: 'result-sub', text: 'CTC divided by 12 would suggest ' + rupees(naive) + '. The difference is ' + rupees(naive - hand) + ' a month.' }));

      var pHand = hand * 12 / ctc * 100, pDed = ded * 12 / ctc * 100, pNot = Math.max(0, 100 - pHand - pDed);
      var bar = el('div', { class: 'bar', role: 'img', 'aria-label': 'Of your yearly CTC, ' + Math.round(pHand) + ' per cent reaches your bank account, ' + Math.round(pDed) + ' per cent is deducted monthly and ' + Math.round(pNot) + ' per cent is not monthly cash.' });
      [['b-hand', pHand], ['b-ded', pDed], ['b-notcash', pNot]].forEach(function (s) {
        var seg = el('span', { class: s[0] }); seg.style.width = s[1] + '%'; bar.appendChild(seg);
      });
      out.appendChild(bar);
      function key(cls, label) { var i = el('i'); i.className = cls; return el('span', null, i, label); }
      out.appendChild(el('div', { class: 'legend' },
        key('b-hand', 'Reaches your bank (' + Math.round(pHand) + '%)'),
        key('b-ded', 'Monthly deductions (' + Math.round(pDed) + '%)'),
        key('b-notcash', 'Not monthly cash (' + Math.round(pNot) + '%)')
      ));
      /* legend swatches need a background; reuse the bar classes */
      Array.prototype.forEach.call(out.querySelectorAll('.legend i'), function (i) {
        i.style.background = getComputedStyle(out.querySelector('.bar .' + i.className)).backgroundColor;
      });

      function row(label, amount, cls) {
        return el('tr', { class: cls || '' }, el('td', { text: label }), el('td', { text: amount }));
      }
      var table = el('table', { class: 'ledger' }, el('tbody', null,
        row('CTC per year', rupees(ctc)),
        row('Minus parts that are not monthly cash', '− ' + rupees(notCash), 'minus'),
        row('Fixed pay per year', rupees(fixed)),
        row('Fixed pay per month (gross)', rupees(gross)),
        row('Minus monthly deductions', '− ' + rupees(ded), 'minus'),
        row('Estimated in-hand per month', rupees(hand), 'total')
      ));
      out.appendChild(table);
      if (!val('otherDed')) {
        out.appendChild(el('p', { class: 'fineprint', text: 'You have not entered income tax. If your yearly income is taxable, your in-hand will be lower than this.' }));
      }
    }
    calc();
  }
  buildOffer();

  /* ---------- 03 first 180 days ---------- */
  var daysApp = document.getElementById('daysApp');
  function buildDays(data) {
    clear(daysApp);
    var tl = el('div', { class: 'timeline' });
    data.plan.forEach(function (p) { tl.appendChild(el('div', { class: 'tl' }, el('b', { text: p.when }), el('span', { text: p.do }))); });
    daysApp.appendChild(el('p', { class: 'label', text: 'A simple plan for six months' }));
    daysApp.appendChild(tl);

    daysApp.appendChild(el('h3', { text: 'Find your situation', style: 'margin-top:14px' }));
    var search = el('input', { class: 'search', type: 'search', placeholder: 'Try: deadline, feedback, resign, mistake', 'aria-label': 'Search situations' });
    daysApp.appendChild(search);
    var phase = 'All';
    var chips = el('div', { class: 'chips', role: 'group', 'aria-label': 'Filter by stage' });
    ['All'].concat(data.phases).forEach(function (p) {
      var chip = el('button', { class: 'chip', type: 'button', 'aria-pressed': p === 'All' ? 'true' : 'false', text: p });
      chip.addEventListener('click', function () {
        phase = p;
        Array.prototype.forEach.call(chips.children, function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
        render();
      });
      chips.appendChild(chip);
    });
    daysApp.appendChild(chips);
    var list = el('div', { class: 'app', 'aria-live': 'polite' });
    daysApp.appendChild(list);

    function render() {
      clear(list);
      var words = search.value.toLowerCase().split(/\s+/).filter(Boolean);
      var hits = data.situations.filter(function (s) {
        if (phase !== 'All' && s.phase !== phase) return false;
        var hay = (s.title + ' ' + s.keywords + ' ' + s.means).toLowerCase();
        return words.every(function (w) { return hay.indexOf(w) !== -1; });
      });
      if (!hits.length) {
        list.appendChild(el('p', { class: 'empty', text: 'Nothing matches yet. Try a simpler word, or talk it through with your own AI using the section below.' }));
        return;
      }
      hits.forEach(function (s) {
        var steps = el('ul', { style: 'padding-left:20px;margin-bottom:10px' });
        s.do.forEach(function (d) { steps.appendChild(el('li', { text: d })); });
        list.appendChild(el('details', { class: 'clause', ontoggle: function (e) { if (e.target.open) track('desk_situation_open', { title: s.title }); } },
          el('summary', null, el('span', { class: 'sit-title' }, el('span', { class: 'sit-phase', text: s.phase }), el('span', { text: s.title }))),
          el('div', { class: 'clause-body' },
            el('p', null, el('strong', { text: 'What it usually means. ' }), s.means),
            el('p', null, el('strong', { text: 'What to do' })),
            steps,
            el('p', null, el('strong', { text: 'What you could say' })),
            el('p', { class: 'say', text: '“' + s.say + '”' }),
            el('p', null, el('strong', { text: 'Avoid. ' }), s.avoid),
            el('div', { class: 'btn-row' },
              el('button', { class: 'btn btn-quiet', type: 'button', text: 'Copy what to say', onclick: function () { copyText(s.say, 'Copied'); } }),
              el('button', {
                class: 'btn btn-quiet', type: 'button', text: 'Talk it through with my AI',
                onclick: function () {
                  document.getElementById('aiTask').value = 'work';
                  AI.situation = s.title;
                  aiUpdate();
                  document.getElementById('ownAiTitle').scrollIntoView();
                }
              })
            )
          )
        ));
      });
    }
    search.addEventListener('input', render);
    render();
  }
  loadJSON('data/situations.json').then(buildDays, function () { loadError(daysApp); });

  /* ---------- continue in your own AI ---------- */
  var AI = { situation: '' };
  var aiTask = document.getElementById('aiTask');
  var aiLang = document.getElementById('aiLang');
  var aiRole = document.getElementById('aiRole');
  var aiRoleWrap = document.getElementById('aiRoleWrap');
  var aiPrompt = document.getElementById('aiPrompt');

  function aiBuild() {
    var lang = aiLang.value;
    var langLine = 'Speak to me in ' + lang + ', in simple everyday words.';
    if (aiTask.value === 'interview') {
      var role = aiRole.value.trim() || 'an entry-level graduate role';
      return [
        'Act as an experienced hiring manager in India interviewing me, a fresh graduate, for this job: ' + role + '.',
        langLine,
        'Rules:',
        '1. Ask one question at a time and wait for my answer. Ask 6 questions in total: a mix of "tell me about yourself", motivation, a real past situation, a weakness, a role-specific scenario, and "any questions for us".',
        '2. Stay in character as the interviewer. Do not coach me during the interview.',
        '3. After my last answer, show me the private notes you would have written about each answer: what worked, what did not, and why, from an employer\'s point of view.',
        '4. Then give a decision (Shortlist, Second look, or Not yet), and rewrite my weakest answer using only facts I actually told you. Do not invent experience for me.',
        '5. Be honest and kind. Do not flatter me.',
        'Start by greeting me and asking the first question.'
      ].join('\n');
    }
    if (aiTask.value === 'offer') {
      return [
        'I am a fresh graduate in India and I have received my first job offer. Help me understand it.',
        langLine,
        'I will paste the offer letter text after this message, with my personal details removed.',
        'Please:',
        '1. Explain the salary table: which parts reach my bank account every month, which are deductions, and which are not monthly cash (employer PF, gratuity, insurance, variable pay, one-time bonuses). Use only the numbers in my letter. If a number is missing, tell me to ask HR; do not assume it.',
        '2. Explain in plain words what each of these means for me, if present: bond or service agreement, notice period, probation, variable pay conditions, bonus recovery, location and shift changes, background verification, offer validity.',
        '3. Point out anything unusual or unclear that I should ask about.',
        '4. Give me a short list of polite questions to send HR before I accept.',
        'You are not my lawyer or tax adviser. Say clearly when something needs professional or official confirmation.',
        'Reply "Ready" and wait for me to paste the letter.'
      ].join('\n');
    }
    return [
      'I am in the first six months of my first job in India. Act as a calm, experienced mentor who has managed many new graduates.',
      langLine,
      AI.situation ? 'My situation: ' + AI.situation + '.' : 'I will describe a situation at work.',
      'Please:',
      '1. First ask me two or three short questions to understand what actually happened. Do not assume.',
      '2. Then tell me what this most likely means, and what else it could mean.',
      '3. Give me two or three practical next steps, and the exact words I could say or write to my manager or colleague.',
      '4. Tell me what to avoid doing.',
      'Be honest, including when I may be the one at fault. Do not tell me to resign as a first step. If it sounds like harassment, a safety problem or a legal matter, tell me to go to HR or the proper authority.',
      AI.situation ? 'Start with your questions.' : 'Start by asking me what happened.'
    ].join('\n');
  }
  function aiUpdate() {
    aiRoleWrap.hidden = aiTask.value !== 'interview';
    var p = aiBuild();
    aiPrompt.textContent = p;
    var q = encodeURIComponent(p);
    document.getElementById('aiChatGPT').href = 'https://chatgpt.com/?q=' + q;
    document.getElementById('aiClaude').href = 'https://claude.ai/new?q=' + q;
  }
  aiTask.addEventListener('change', function () { AI.situation = ''; aiUpdate(); });
  aiLang.addEventListener('change', aiUpdate);
  aiRole.addEventListener('input', aiUpdate);
  document.getElementById('aiCopy').addEventListener('click', function () { copyText(aiBuild(), 'Instructions copied. Paste them into your AI app.'); });
  document.getElementById('aiGemini').addEventListener('click', function () {
    copyText(aiBuild(), 'Copied. Paste it into Gemini.');
    window.open('https://gemini.google.com/app', '_blank', 'noopener');
  });
  ['aiChatGPT', 'aiClaude', 'aiGemini', 'aiCopy'].forEach(function (id) {
    document.getElementById(id).addEventListener('click', function () {
      track('desk_ai_open', { app: id.slice(2).toLowerCase(), task: aiTask.value, language: aiLang.value });
    });
  });
  aiUpdate();
})();
