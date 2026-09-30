/* 360Comm — core site script (no dependencies) */
(function () {
  'use strict';

  /* =========================================================
     SITE CONFIG — edit here only.
     The contact address is stored obfuscated and is never
     written into the page. All forms post through FormSubmit.
     After the first submission FormSubmit sends a one-time
     activation email; once activated you may paste the random
     alias it gives you into FORM_ALIAS to hide it completely.
     ========================================================= */
  var CONFIG = {
    _k: [122, 120, 116, 57, 123, 126, 118, 122, 112, 87, 38, 118, 100, 124, 101, 120, 96, 117, 114, 96],
    FORM_ALIAS: '',                         // e.g. 'a1b2c3d4e5...' from FormSubmit after activation
    ADSENSE_CLIENT: '',                     // e.g. 'ca-pub-1234567890123456' — leave blank until approved
    DONATE: {
      paypal: true,                         // PayPal donate link built from hidden address
      kofi: '',                             // e.g. 'https://ko-fi.com/yourname'
      bmc: '',                              // e.g. 'https://buymeacoffee.com/yourname'
      github: 'https://github.com/sponsors/WEBWORKSA1'
    },
    YT_CHANNEL: 'https://www.youtube.com/results?search_query=business+phone+system+voip+review'
  };
  function addr() { return CONFIG._k.slice().reverse().map(function (c) { return String.fromCharCode(c ^ 23); }).join(''); }
  function endpoint() { return 'https://formsubmit.co/ajax/' + (CONFIG.FORM_ALIAS || addr()); }
  window.C360 = { config: CONFIG };

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- Theme ---------- */
  var saved = store('c360-theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
  $$('[data-theme-toggle]').forEach(function (b) {
    b.addEventListener('click', function () {
      var cur = document.documentElement.getAttribute('data-theme') ||
        (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      var next = cur === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      store('c360-theme', next);
    });
  });

  /* ---------- Mobile menu ---------- */
  var burger = $('.burger'), menu = $('.menu');
  if (burger && menu) burger.addEventListener('click', function () {
    var o = menu.classList.toggle('open'); burger.setAttribute('aria-expanded', o);
  });

  /* ---------- Hidden-address links (mailto / PayPal) ---------- */
  $$('[data-mail]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var subj = a.getAttribute('data-mail') || 'Inquiry from 360Comm';
      location.href = 'mai' + 'lto:' + addr() + '?subject=' + encodeURIComponent(subj);
    });
  });
  $$('[data-paypal]').forEach(function (a) {
    if (!CONFIG.DONATE.paypal) { a.style.display = 'none'; return; }
    a.addEventListener('click', function (e) {
      e.preventDefault();
      var purpose = a.getAttribute('data-paypal') || 'Support 360Comm';
      var amt = a.getAttribute('data-amount') || '';
      var url = 'https://www.paypal.com/donate/?business=' + encodeURIComponent(addr()) +
        '&item_name=' + encodeURIComponent(purpose) + '&currency_code=USD' + (amt ? '&amount=' + amt : '');
      window.open(url, '_blank', 'noopener');
    });
  });
  ['kofi', 'bmc', 'github'].forEach(function (k) {
    $$('[data-donate="' + k + '"]').forEach(function (a) {
      if (CONFIG.DONATE[k]) { a.href = CONFIG.DONATE[k]; a.target = '_blank'; a.rel = 'noopener'; }
      else a.style.display = 'none';
    });
  });

  /* ---------- Forms (all go to the single hidden inbox) ---------- */
  function serialize(form) {
    var data = {};
    new FormData(form).forEach(function (v, k) {
      if (data[k]) data[k] = [].concat(data[k], v); else data[k] = v;
    });
    Object.keys(data).forEach(function (k) { if (Array.isArray(data[k])) data[k] = data[k].join(', '); });
    data._subject = '[360Comm] ' + (form.getAttribute('data-form') || 'Form') + ' submission';
    data._template = 'table';
    data._captcha = 'false';
    data.page = location.href;
    data.submitted_at = new Date().toISOString();
    return data;
  }
  function msg(form, ok, text) {
    var m = $('.form-msg', form);
    if (!m) { m = document.createElement('div'); m.className = 'form-msg'; form.appendChild(m); }
    m.className = 'form-msg ' + (ok ? 'ok' : 'err'); m.textContent = text;
    m.setAttribute('role', 'status');
  }
  function submitForm(form) {
    var hp = form.querySelector('[name="_honey"]');
    if (hp && hp.value) return Promise.resolve(true);
    var btn = form.querySelector('[type="submit"]');
    if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = 'Sending…'; }
    return fetch(endpoint(), {
      method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify(serialize(form))
    }).then(function (r) { return r.ok; }).catch(function () { return false; })
      .then(function (ok) {
        if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; }
        return ok;
      });
  }
  window.C360.submitForm = submitForm;
  $$('form[data-form]').forEach(function (form) {
    if (form.hasAttribute('data-wizard')) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      submitForm(form).then(function (ok) {
        if (ok) {
          msg(form, true, form.getAttribute('data-success') || 'Thank you! Your message has been received. We will reply within 1–2 business days.');
          form.reset();
          if (window.gtag) gtag('event', 'generate_lead', { form: form.getAttribute('data-form') });
        } else msg(form, false, 'Sorry — the message could not be sent right now. Please try again in a minute.');
      });
    });
  });

  /* ---------- Multi-step lead wizard ---------- */
  $$('form[data-wizard]').forEach(function (form) {
    var steps = $$('.step', form), i = 0, bar = $('.progress i', form), label = $('[data-step-label]', form);
    // prefill from query (?users=2-5 from home one-click card)
    var q = new URLSearchParams(location.search);
    ['users', 'need'].forEach(function (k) {
      var v = q.get(k); if (!v) return;
      $$('input[name="' + k + '"]', form).forEach(function (inp) { if (inp.value === v) inp.checked = true; });
    });
    function show(n) {
      steps.forEach(function (s, idx) { s.classList.toggle('active', idx === n); });
      i = n; if (bar) bar.style.width = Math.round((n + 1) / steps.length * 100) + '%';
      if (label) label.textContent = 'Step ' + (n + 1) + ' of ' + steps.length;
      var f = steps[n].querySelector('input:not([type=hidden]),select,textarea'); if (f && n > 0 && f.type !== 'radio' && f.type !== 'checkbox') f.focus();
    }
    function valid(n) {
      var s = steps[n], ok = true;
      $$('[required]', s).forEach(function (el) { if (!el.checkValidity()) { ok = false; el.reportValidity(); } });
      var groups = {};
      $$('input[type=radio][data-req],input[type=checkbox][data-req]', s).forEach(function (el) { groups[el.name] = groups[el.name] || $$('input[name="' + el.name + '"]:checked', s).length > 0; });
      Object.keys(groups).forEach(function (g) { if (!groups[g]) { ok = false; var box = $('[data-group="' + g + '"]', s); if (box) { box.style.outline = '2px solid #dc2626'; setTimeout(function () { box.style.outline = ''; }, 1400); } } });
      return ok;
    }
    $$('[data-next]', form).forEach(function (b) { b.addEventListener('click', function () { if (valid(i)) show(Math.min(i + 1, steps.length - 1)); }); });
    $$('[data-prev]', form).forEach(function (b) { b.addEventListener('click', function () { show(Math.max(i - 1, 0)); }); });
    // auto-advance on single-choice radio steps
    $$('.step[data-auto] input[type=radio]', form).forEach(function (r) { r.addEventListener('change', function () { setTimeout(function () { if (valid(i)) show(Math.min(i + 1, steps.length - 1)); }, 220); }); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!valid(i)) return;
      submitForm(form).then(function (ok) {
        if (ok) { location.href = form.getAttribute('data-thanks') || 'thank-you.html'; }
        else msg(form, false, 'We could not submit your request. Please check your connection and try again.');
      });
    });
    show(0);
    if (q.get('users') && $$('input[name="users"]:checked', form).length) show(1);
  });

  /* ---------- Home one-click quick quote ---------- */
  $$('[data-quick]').forEach(function (b) {
    b.addEventListener('click', function () { location.href = b.getAttribute('data-href') + '?users=' + encodeURIComponent(b.getAttribute('data-quick')); });
  });

  /* ---------- Sortable / filterable comparison table ---------- */
  $$('table.cmp').forEach(function (t) {
    $$('th[data-sort]', t).forEach(function (th, idx) {
      var dir = 1;
      th.addEventListener('click', function () {
        var col = Array.prototype.indexOf.call(th.parentNode.children, th);
        var rows = $$('tbody tr', t);
        rows.sort(function (a, b) {
          var x = a.children[col].getAttribute('data-v') || a.children[col].textContent;
          var y = b.children[col].getAttribute('data-v') || b.children[col].textContent;
          var nx = parseFloat(x), ny = parseFloat(y);
          if (!isNaN(nx) && !isNaN(ny)) return (nx - ny) * dir;
          return x.localeCompare(y) * dir;
        });
        dir = -dir; rows.forEach(function (r) { t.tBodies[0].appendChild(r); });
      });
    });
  });
  $$('[data-filter-group]').forEach(function (g) {
    var target = $(g.getAttribute('data-filter-group'));
    $$('[data-filter]', g).forEach(function (b) {
      b.addEventListener('click', function () {
        $$('[data-filter]', g).forEach(function (x) { x.classList.remove('active'); }); b.classList.add('active');
        var f = b.getAttribute('data-filter');
        $$('[data-cats]', target).forEach(function (r) { r.style.display = (f === 'all' || r.getAttribute('data-cats').indexOf(f) > -1) ? '' : 'none'; });
      });
    });
  });
  var tsearch = $('[data-table-search]');
  if (tsearch) tsearch.addEventListener('input', function () {
    var q = tsearch.value.toLowerCase(), t = $(tsearch.getAttribute('data-table-search'));
    $$('tbody tr', t).forEach(function (r) { r.style.display = r.textContent.toLowerCase().indexOf(q) > -1 ? '' : 'none'; });
  });

  /* ---------- Head-to-head compare (compare.html?a=x&b=y) ---------- */
  var h2h = $('#h2h');
  if (h2h && window.C360_PROVIDERS) {
    var P = window.C360_PROVIDERS, sa = $('#h2h-a'), sb = $('#h2h-b'), out = $('#h2h-out');
    P.forEach(function (p) { sa.add(new Option(p.name, p.slug)); sb.add(new Option(p.name, p.slug)); });
    var qs = new URLSearchParams(location.search);
    sa.value = qs.get('a') || P[0].slug; sb.value = qs.get('b') || P[1].slug;
    function row(k, a, b) { return '<tr><th>' + k + '</th><td>' + a + '</td><td>' + b + '</td></tr>'; }
    function render() {
      var a = P.find(function (p) { return p.slug === sa.value; }), b = P.find(function (p) { return p.slug === sb.value; });
      var yn = function (v) { return v ? '<span class="yes">✓</span>' : '<span class="no">✗</span>'; };
      out.innerHTML = '<div class="table-wrap"><table class="cmp" style="min-width:560px"><thead><tr><th>Feature</th><th>' + a.name + '</th><th>' + b.name + '</th></tr></thead><tbody>' +
        row('360 Score', a.score.toFixed(1) + '/10', b.score.toFixed(1) + '/10') + row('Starting price', a.price, b.price) + row('Best for', a.bestFor, b.bestFor) +
        row('Video meetings', yn(a.video), yn(b.video)) + row('Business SMS', yn(a.sms), yn(b.sms)) +
        row('Contact center add-on', yn(a.cc), yn(b.cc)) + row('AI features', yn(a.ai), yn(b.ai)) + row('Minimum seats', a.min, b.min) +
        row('Price source', '<a href="' + a.src + '" rel="nofollow noopener" target="_blank">vendor/3rd-party</a>', '<a href="' + b.src + '" rel="nofollow noopener" target="_blank">vendor/3rd-party</a>') +
        '</tbody></table></div><p class="small muted" style="margin-top:10px">Prices checked ' + window.C360_PRICE_DATE + '. Always confirm on the vendor site — taxes and regulatory fees typically add 15–25%.</p>';
      history.replaceState(null, '', '?a=' + sa.value + '&b=' + sb.value);
    }
    sa.addEventListener('change', render); sb.addEventListener('change', render); render();
  }

  /* ---------- Lazy YouTube (privacy-enhanced) ---------- */
  $$('.video[data-yt]').forEach(function (v) {
    var id = v.getAttribute('data-yt');
    v.innerHTML = '<img loading="lazy" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg" alt="' + (v.getAttribute('data-title') || 'Video') + '"><span class="play" aria-hidden="true"></span>';
    v.setAttribute('role', 'button'); v.setAttribute('tabindex', '0'); v.setAttribute('aria-label', 'Play video: ' + (v.getAttribute('data-title') || ''));
    function play() { v.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (v.getAttribute('data-title') || 'Video') + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'; }
    v.addEventListener('click', play); v.addEventListener('keydown', function (e) { if (e.key === 'Enter') play(); });
  });

  /* ---------- AdSense (auto-activates when client ID is set) ---------- */
  var slots = $$('.ad-slot');
  if (CONFIG.ADSENSE_CLIENT) {
    var s = document.createElement('script'); s.async = true; s.crossOrigin = 'anonymous';
    s.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + CONFIG.ADSENSE_CLIENT;
    document.head.appendChild(s);
    slots.forEach(function (el) {
      el.innerHTML = '<span class="ad-label">Advertisement</span><ins class="adsbygoogle" style="display:block;width:100%" data-ad-client="' + CONFIG.ADSENSE_CLIENT + '" data-ad-slot="' + (el.getAttribute('data-slot') || '') + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    });
  } else {
    var root = document.body.getAttribute('data-root') || '';
    slots.forEach(function (el) { el.innerHTML = '<div><span class="ad-label">Advertisement</span>Reach IT buyers comparing phone, video &amp; contact-center tools. <a href="' + root + 'advertise.html">Advertise on 360Comm →</a></div>'; });
  }

  /* ---------- Cookie consent ---------- */
  var ck = $('.cookie');
  if (ck && !store('c360-consent')) ck.classList.add('show');
  $$('[data-consent]').forEach(function (b) { b.addEventListener('click', function () { store('c360-consent', b.getAttribute('data-consent')); ck.classList.remove('show'); }); });

  /* ---------- Modals ---------- */
  function openModal(id) { var m = document.getElementById(id); if (m) { m.classList.add('open'); var f = m.querySelector('input,button'); if (f) f.focus(); } }
  function closeModals() { $$('.modal.open').forEach(function (m) { m.classList.remove('open'); }); }
  $$('[data-open]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); openModal(b.getAttribute('data-open')); }); });
  $$('.modal').forEach(function (m) { m.addEventListener('click', function (e) { if (e.target === m || e.target.closest('.modal-close')) closeModals(); }); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModals();
    if ((e.key === 'k' && (e.metaKey || e.ctrlKey)) || (e.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName))) { e.preventDefault(); openModal('search-modal'); }
  });

  /* ---------- Exit-intent (once per session, not on quote pages) ---------- */
  if (!document.body.hasAttribute('data-no-exit')) {
    var shown = false;
    try { shown = sessionStorage.getItem('c360-exit') === '1'; } catch (e) { }
    document.addEventListener('mouseout', function (e) {
      if (shown || e.clientY > 8 || e.relatedTarget) return;
      shown = true; try { sessionStorage.setItem('c360-exit', '1'); } catch (x) { }
      openModal('exit-modal');
    });
  }

  /* ---------- Site search ---------- */
  var si = $('#site-search'), sr = $('#search-results'), idx = null;
  if (si) si.addEventListener('input', function () {
    var root = document.body.getAttribute('data-root') || '';
    function run() {
      var q = si.value.trim().toLowerCase();
      if (!q) { sr.innerHTML = ''; return; }
      var hits = idx.filter(function (p) { return (p.t + ' ' + p.d + ' ' + p.k).toLowerCase().indexOf(q) > -1; }).slice(0, 12);
      sr.innerHTML = hits.length ? hits.map(function (h) { return '<a href="' + root + h.u + '"><b>' + h.t + '</b><br><span class="small muted">' + h.d + '</span></a>'; }).join('') : '<p class="muted">No results. Try “VoIP”, “calculator” or “contact center”.</p>';
    }
    if (idx) run(); else fetch(root + 'search-index.json').then(function (r) { return r.json(); }).then(function (j) { idx = j; run(); }).catch(function () { });
  });

  /* ---------- Reveal + counters + back-to-top ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('in');
        var c = en.target.querySelector('[data-count]') || (en.target.hasAttribute('data-count') ? en.target : null);
        if (c && !c.dataset.done) {
          c.dataset.done = 1; var end = +c.getAttribute('data-count'), t0 = null, suf = c.getAttribute('data-suffix') || '';
          (function step(ts) { t0 = t0 || ts; var p = Math.min((ts - t0) / 1200, 1); c.textContent = Math.round(end * p).toLocaleString() + suf; if (p < 1) requestAnimationFrame(step); })(performance.now());
        }
        io.unobserve(en.target);
      });
    }, { threshold: .15 });
    $$('.reveal,[data-count]').forEach(function (el) { io.observe(el); });
  } else $$('.reveal').forEach(function (el) { el.classList.add('in'); });
  var tt = $('.to-top');
  if (tt) { addEventListener('scroll', function () { tt.classList.toggle('show', scrollY > 700); }, { passive: true }); tt.addEventListener('click', function () { scrollTo({ top: 0 }); }); }
  var yr = $('[data-year]'); if (yr) yr.textContent = new Date().getFullYear();
})();
