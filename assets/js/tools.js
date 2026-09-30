/* 360Comm — interactive calculators */
(function () {
  'use strict';
  var $ = function (id) { return document.getElementById(id); };
  var money = function (n) { return '$' + Math.round(n).toLocaleString(); };
  function bind(ids, fn) { ids.forEach(function (id) { var el = $(id); if (el) el.addEventListener('input', fn); }); fn(); }

  /* 1. VoIP savings calculator */
  if ($('sv-bill')) bind(['sv-bill', 'sv-users', 'sv-price', 'sv-fees', 'sv-hw'], function () {
    var bill = +$('sv-bill').value || 0, users = +$('sv-users').value || 0, price = +$('sv-price').value || 0,
      fees = (+$('sv-fees').value || 0) / 100, hw = +$('sv-hw').value || 0;
    var voip = users * price * (1 + fees);
    var monthly = bill - voip, year1 = monthly * 12 - hw * users, year3 = monthly * 36 - hw * users;
    $('sv-voip').textContent = money(voip) + '/mo';
    $('sv-month').textContent = money(monthly) + '/mo';
    $('sv-y1').textContent = money(year1);
    $('sv-y3').textContent = money(year3);
    $('sv-pct').textContent = bill > 0 ? Math.round(monthly / bill * 100) + '%' : '—';
  });

  /* 2. True cost of ownership */
  if ($('tc-seats')) bind(['tc-seats', 'tc-base', 'tc-addons', 'tc-numbers', 'tc-numprice', 'tc-fees', 'tc-hw', 'tc-setup', 'tc-min'], function () {
    var seats = Math.max(+$('tc-seats').value || 0, +$('tc-min').value || 0), base = +$('tc-base').value || 0,
      add = +$('tc-addons').value || 0, nums = +$('tc-numbers').value || 0, np = +$('tc-numprice').value || 0,
      fees = (+$('tc-fees').value || 0) / 100, hw = +$('tc-hw').value || 0, setup = +$('tc-setup').value || 0;
    var sub = seats * (base + add) + nums * np, monthly = sub * (1 + fees);
    var y1 = monthly * 12 + hw + setup, y3 = monthly * 36 + hw + setup;
    $('tc-month').textContent = money(monthly) + '/mo';
    $('tc-seat').textContent = seats ? '$' + (monthly / seats).toFixed(2) + ' per seat' : '—';
    $('tc-y1').textContent = money(y1); $('tc-y3').textContent = money(y3);
    $('tc-gap').textContent = base ? Math.round((monthly / seats / base - 1) * 100) + '% above advertised price' : '—';
  });

  /* 3. Erlang C contact-center staffing */
  function erlangC(A, N) {
    if (N <= A) return 1;
    var sum = 0, term = 1;
    for (var k = 0; k < N; k++) { if (k > 0) term = term * A / k; sum += term; }
    var top = term * A / N * (N / (N - A));
    return top / (sum + top);
  }
  if ($('er-calls')) bind(['er-calls', 'er-aht', 'er-sl', 'er-target', 'er-shrink'], function () {
    var calls = +$('er-calls').value || 0, aht = +$('er-aht').value || 1, sl = (+$('er-sl').value || 80) / 100,
      T = +$('er-target').value || 20, shrink = (+$('er-shrink').value || 0) / 100;
    var A = calls * aht / 3600; // traffic intensity in Erlangs (calls per hour × AHT seconds)
    var N = Math.max(1, Math.ceil(A)), pw, svc, guard = 0;
    while (guard++ < 500) {
      pw = erlangC(A, N);
      svc = 1 - pw * Math.exp(-(N - A) * T / aht);
      if (svc >= sl && N > A) break;
      N++;
    }
    var asa = pw * aht / (N - A), occ = A / N;
    $('er-agents').textContent = N;
    $('er-sched').textContent = Math.ceil(N / (1 - shrink));
    $('er-svc').textContent = (svc * 100).toFixed(1) + '%';
    $('er-asa').textContent = asa.toFixed(1) + ' sec';
    $('er-occ').textContent = (occ * 100).toFixed(1) + '%';
    $('er-traffic').textContent = A.toFixed(2) + ' Erlangs';
  });

  /* 4. Bandwidth calculator */
  if ($('bw-calls')) bind(['bw-calls', 'bw-codec', 'bw-video', 'bw-vq', 'bw-users', 'bw-head'], function () {
    var calls = +$('bw-calls').value || 0, codec = +$('bw-codec').value || 100, vids = +$('bw-video').value || 0,
      vq = +$('bw-vq').value || 2.5, users = +$('bw-users').value || 0, head = (+$('bw-head').value || 0) / 100;
    var voice = calls * codec / 1000, video = vids * vq, data = users * 1.5;
    var total = (voice + video + data) * (1 + head);
    $('bw-voice').textContent = voice.toFixed(2) + ' Mbps';
    $('bw-vid').textContent = video.toFixed(1) + ' Mbps';
    $('bw-total').textContent = Math.ceil(total) + ' Mbps up & down';
    var tier = total < 25 ? '25/25 Mbps fiber or cable business plan' : total < 100 ? '100/100 Mbps symmetrical fiber' : total < 300 ? '300/300 Mbps fiber' : '500 Mbps–1 Gbps dedicated fiber (DIA)';
    $('bw-tier').textContent = tier;
  });

  /* 5. SMS campaign cost estimator */
  if ($('sm-contacts')) bind(['sm-contacts', 'sm-per', 'sm-rate', 'sm-carrier', 'sm-segments'], function () {
    var c = +$('sm-contacts').value || 0, per = +$('sm-per').value || 0, rate = +$('sm-rate').value || 0,
      carrier = +$('sm-carrier').value || 0, seg = +$('sm-segments').value || 1;
    var msgs = c * per * seg, cost = msgs * (rate + carrier);
    $('sm-msgs').textContent = msgs.toLocaleString() + ' segments/mo';
    $('sm-cost').textContent = money(cost) + '/mo';
    $('sm-year').textContent = money(cost * 12) + '/yr';
  });

  /* 6. Provider matcher quiz */
  var quiz = $('quiz');
  if (quiz && window.C360_PROVIDERS) {
    quiz.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(quiz), size = f.get('size'), budget = +f.get('budget'), must = f.getAll('must');
      var ranked = window.C360_PROVIDERS.map(function (p) {
        var s = p.score * 2;
        if (p.from && p.from <= budget) s += 4; else if (p.from) s -= 3;
        must.forEach(function (m) { if (p[m]) s += 3; else s -= 4; });
        if (size === 'solo' && /solo|freelanc|startup|small/i.test(p.bestFor)) s += 3;
        if (size === 'large' && /enterprise|large|global|contact/i.test(p.bestFor)) s += 3;
        if (size === 'mid' && /growing|mid|sales|team/i.test(p.bestFor)) s += 2;
        if (p.min > 1 && size === 'solo') s -= 5;
        return { p: p, s: s };
      }).sort(function (a, b) { return b.s - a.s; }).slice(0, 3);
      var root = document.body.getAttribute('data-root') || '';
      $('quiz-out').innerHTML = '<h3>Your top 3 matches</h3>' + ranked.map(function (r, i) {
        return '<div class="card" style="margin-bottom:12px;display:flex;gap:14px;align-items:center;flex-wrap:wrap"><span class="score">' + r.p.score + '<small>Score</small></span><div style="flex:1;min-width:180px"><b>' + (i + 1) + '. ' + r.p.name + '</b><br><span class="small muted">' + r.p.bestFor + ' · from ' + r.p.price + '</span></div><a class="btn btn-sm btn-ghost" href="' + root + 'providers/' + r.p.slug + '.html">Review</a><a class="btn btn-sm btn-cta" href="' + root + 'quotes.html?users=' + encodeURIComponent(f.get('users') || '') + '">Get quotes</a></div>';
      }).join('') + '<p class="small muted">Matches are generated from our published scoring data and your answers — not paid placement.</p>';
      $('quiz-out').scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  }

  /* 7. Latency / jitter quick check (browser-side estimate) */
  var lt = $('lt-run');
  if (lt) lt.addEventListener('click', function () {
    var out = $('lt-out'), samples = [], n = 0, url = 'https://www.google.com/favicon.ico';
    lt.disabled = true; out.textContent = 'Testing…';
    (function ping() {
      var t0 = performance.now();
      fetch(url + '?r=' + Math.random(), { mode: 'no-cors', cache: 'no-store' }).then(function () {
        samples.push(performance.now() - t0);
      }).catch(function () { }).then(function () {
        if (++n < 12) return setTimeout(ping, 150);
        samples.shift();
        if (!samples.length) { out.textContent = 'Test blocked by your browser or network.'; lt.disabled = false; return; }
        var avg = samples.reduce(function (a, b) { return a + b; }, 0) / samples.length, jit = 0;
        for (var i = 1; i < samples.length; i++) jit += Math.abs(samples[i] - samples[i - 1]);
        jit = jit / Math.max(1, samples.length - 1);
        var verdict = avg < 100 && jit < 30 ? '✅ Looks VoIP-ready' : avg < 150 && jit < 50 ? '⚠️ Borderline — test at peak hours' : '❌ Likely call-quality issues';
        out.innerHTML = '<b class="big">' + verdict + '</b>Round-trip ≈ ' + avg.toFixed(0) + ' ms · jitter ≈ ' + jit.toFixed(0) + ' ms<br><span class="small muted">Browser HTTP timing overstates true network latency; treat as a rough screen. VoIP targets: &lt;150 ms one-way latency, &lt;30 ms jitter, &lt;1% packet loss.</span>';
        lt.disabled = false;
      });
    })();
  });
})();
