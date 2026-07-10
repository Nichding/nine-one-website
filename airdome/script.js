/* ════════════════════════════════════════════════
   AIR DOME · minimal vanilla JS
   1) mobile nav toggle
   2) estimator calculation (PLACEHOLDER formula)
   ════════════════════════════════════════════════ */

// ── 1 · mobile nav toggle (site-standard header: .nav / .nav-toggle) ──
const nav = document.getElementById('nav');
const navToggle = document.querySelector('.nav-toggle');
if (nav && navToggle) {
  navToggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(open));
  });
  // close the overlay after tapping any menu link
  document.querySelectorAll('.nav-menu a').forEach((a) =>
    a.addEventListener('click', () => {
      nav.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
    })
  );
}

// ── 1b · product sub-nav scrollspy: light "Tech Specs" once #specs is reached ──
const psOverview = document.querySelector('.psub-links a[href="#hero"]');
const psSpecs = document.querySelector('.psub-links a[href="#specs"]');
const specsSec = document.getElementById('specs');
if (psOverview && psSpecs && specsSec) {
  const spy = () => {
    const atSpecs = (window.scrollY + window.innerHeight * 0.35) >= specsSec.offsetTop;
    psSpecs.classList.toggle('cur', atSpecs);
    psOverview.classList.toggle('cur', !atSpecs);
  };
  addEventListener('scroll', spy, { passive: true });
  addEventListener('resize', spy);
  spy();
}

// ── 2 · hero reel: rotate the three clips with a crossfade ──
// each clip plays once; on 'ended' the next fades in (ended video holds
// its last frame underneath, so the fade is seamless). Cycles forever.
const clips = Array.from(document.querySelectorAll('#hero-reel .heroclip'));
if (clips.length > 1) {
  let cur = 0;
  clips.forEach((v, i) => {
    v.addEventListener('ended', () => {
      const next = (i + 1) % clips.length;
      const nv = clips[next];
      nv.currentTime = 0;
      nv.play();
      nv.classList.add('is-active');
      clips[i].classList.remove('is-active');
      cur = next;
    });
  });
  // if autoplay was blocked (e.g. power saving), start on first interaction
  document.addEventListener('click', () => { if (clips[cur].paused) clips[cur].play(); }, { once: true });
}

// ── 3 · early-stage placeholder estimator ──
// Intentionally public and non-commercial. Do not add supplier pricing,
// margins, CAPEX ranges or operating-cost coefficients to this file.
const PLACEHOLDER_PER_COURT = 1200;

(function initEstimator(){
  const form = document.getElementById('calc-form');
  if (!form) return;
  const $ = (id) => document.getElementById(id);
  const el = {
    sport:$('c-sport'), courts:$('c-courts'), hours:$('c-hours'), rate:$('c-rate'), util:$('c-util'),
    hV:$('c-hours-v'), uV:$('c-util-v'),
    rHours:$('r-hours'), rRev:$('r-rev'), rOp:$('r-op'), rProj:$('r-proj'), rPay:$('r-payback'), rInterp:$('r-interp')
  };
  const nf = new Intl.NumberFormat('en-NZ');                       // NZD locale formatting
  const clamp = (n,lo,hi) => Math.min(hi, Math.max(lo, n));
  const setHidden = (id,v) => { const n=$(id); if(n) n.value=v; };

  function calc(){
    const sport  = el.sport.value;
    const courts = clamp(parseInt(el.courts.value,10)||1, 1, 12);
    const hrsDay = clamp(parseInt(el.hours.value,10)||0, 2, 16);
    const rate   = Math.max(0, parseFloat(el.rate.value)||0);
    const utilPct= clamp(parseInt(el.util.value,10)||0, 20, 85);
    el.hV.textContent = hrsDay + ' hrs/day';
    el.uV.textContent = utilPct + '%';
    const placeholder = courts * PLACEHOLDER_PER_COURT;

    el.rHours.textContent = '[__] hrs / year';
    el.rRev.textContent   = '[__] / year';
    el.rOp.textContent    = 'Confirmed after site review';
    el.rProj.textContent  = nf.format(placeholder) + ' placeholder units';
    el.rPay.textContent   = 'Confirmed after site review';
    el.rPay.classList.add('is-note');

    el.rInterp.textContent = 'This public placeholder demonstrates the interaction only. A site-specific business case is prepared after review.';

    // keep the lead-capture snapshot in sync (submitted with the form for context)
    setHidden('m-sport', sport); setHidden('m-courts', courts); setHidden('m-hpd', hrsDay);
    setHidden('m-rate', rate); setHidden('m-util', utilPct+'%');
    setHidden('m-hpy', '[__]'); setHidden('m-rev', '[__]');
    setHidden('m-pay', el.rPay.textContent);
  }

  el.sport.addEventListener('change', calc);
  form.addEventListener('input', calc);                            // live update on every change
  form.addEventListener('submit', (e) => { e.preventDefault(); calc(); });
  calc();                                                          // show a modelled result on load
})();

// ── 3b · lead capture (Netlify Forms, AJAX → inline thank-you; no backend) ──
(function initLead(){
  const form = document.getElementById('lead-form');
  const thanks = document.getElementById('lead-thanks');
  if (!form || !thanks) return;
  form.addEventListener('submit', (e) => {
    e.preventDefault();                                            // native validation has already passed
    const body = new URLSearchParams(new FormData(form)).toString();
    const done = () => { form.hidden = true; thanks.hidden = false; thanks.scrollIntoView({behavior:'smooth', block:'center'}); };
    fetch('/', { method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body })
      .then(done).catch(done);                                     // Netlify captures it in production; thank the user either way
  });
})();

// ── 4 · engineered-air flow field ──
// Our own animated, CFD-informed airflow — NOT a supplier/Ansys render.
// Field = a symmetric double-cell ventilation pattern (validated to form a
// closed, bounded circulation): fresh air rises at the centre inlet, is guided
// up and over by the arched roof, sinks down the two sides, and returns along
// the floor. Particles advect along the field; colour maps to air velocity
// (deep ink-blue = slow → sky-blue → near-white = fast).
(function initFlow(){
  const cv = document.getElementById('flow');
  if (!cv) return;
  const ctx = cv.getContext('2d');
  const PI = Math.PI;
  const U = (x, y) => -Math.sin(2 * PI * x) * PI * Math.cos(PI * y);
  const V = (x, y) =>  2 * PI * Math.cos(2 * PI * x) * Math.sin(PI * y);
  const SPEED = 0.0013;          // normalized advance per unit field-speed per frame
  const SMIN = 0.5, SMAX = 6.5;  // field-speed range for the colour ramp

  let W = 0, H = 0, DPR = 1, parts = [], geo = {}, raf = 0;

  const ceilY = (nx) => geo.edgeY + (geo.peakY - geo.edgeY) * Math.sin(PI * nx);
  function toPx(nx, ny){
    const px = geo.x0 + nx * (geo.x1 - geo.x0);
    const cy = ceilY(nx);
    return [px, cy + ny * (geo.floor - cy)];
  }
  function domePath(c){
    c.beginPath();
    c.moveTo(geo.x0, geo.floor);
    for (let i = 0; i <= 48; i++){ const nx = i / 48; const p = toPx(nx, 0); c.lineTo(p[0], p[1]); }
    c.lineTo(geo.x1, geo.floor);
    c.closePath();
  }
  function ramp(t){
    t = t < 0 ? 0 : t > 1 ? 1 : t;
    if (t < 0.38) return '#38195C';
    if (t < 0.72) return '#5C2E91';
    return '#F4F4F1';
  }
  function spawn(p){
    if (Math.random() < 0.38){ p.nx = 0.40 + Math.random()*0.20; p.ny = 0.80 + Math.random()*0.18; }
    else { p.nx = Math.random(); p.ny = Math.random(); }
    p.age = 0; p.life = 120 + (Math.random()*260|0);
    const q = toPx(p.nx, p.ny); p.px = q[0]; p.py = q[1];
  }
  function paintBg(){
    const g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, '#38195C'); g.addColorStop(1, '#0B0B0B');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    ctx.save(); domePath(ctx); ctx.clip();
    ctx.strokeStyle = 'rgba(92,46,145,.10)'; ctx.lineWidth = 1;
    ctx.beginPath(); ctx.moveTo(geo.x0, geo.floor); ctx.lineTo(geo.x1, geo.floor); ctx.stroke();
    ctx.restore();
  }
  function build(){
    const r = cv.getBoundingClientRect();
    if (!r.width || !r.height) return;
    DPR = Math.min(2, window.devicePixelRatio || 1);
    W = r.width; H = r.height; cv.width = W * DPR; cv.height = H * DPR;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    geo = { x0: W*0.06, x1: W-W*0.06, floor: H*0.90, edgeY: H*0.80, peakY: H*0.14 };
    paintBg();
    const n = Math.min(1700, Math.round(W * H / 620));
    parts = []; for (let i = 0; i < n; i++){ const p = {}; spawn(p); parts.push(p); }
  }
  function frame(){
    ctx.save(); domePath(ctx); ctx.clip();
    ctx.fillStyle = 'rgba(32,14,56,0.14)'; ctx.fillRect(0, 0, W, H);
    ctx.globalCompositeOperation = 'lighter'; ctx.lineWidth = 1.15; ctx.lineCap = 'round';
    for (const p of parts){
      const u = U(p.nx, p.ny), v = V(p.nx, p.ny); const s = Math.hypot(u, v);
      const t = (s - SMIN) / (SMAX - SMIN);
      const ox = p.px, oy = p.py;
      p.nx += u * SPEED; p.ny += v * SPEED; p.age++;
      if (p.nx<0.002 || p.nx>0.998 || p.ny<0.002 || p.ny>0.998 || p.age>p.life || s<1e-4){ spawn(p); continue; }
      const q = toPx(p.nx, p.ny); p.px = q[0]; p.py = q[1];
      ctx.strokeStyle = ramp(t); ctx.globalAlpha = 0.35 + 0.5 * t;
      ctx.beginPath(); ctx.moveTo(ox, oy); ctx.lineTo(p.px, p.py); ctx.stroke();
    }
    ctx.globalAlpha = 1; ctx.globalCompositeOperation = 'source-over'; ctx.restore();
    // membrane outline + centre inlet glow
    domePath(ctx); ctx.strokeStyle = 'rgba(92,46,145,.55)'; ctx.lineWidth = 1.4; ctx.stroke();
    const ix = geo.x0 + (geo.x1 - geo.x0) * 0.5, iy = geo.floor;
    const gl = ctx.createRadialGradient(ix, iy, 0, ix, iy, 46);
    gl.addColorStop(0, 'rgba(244,244,241,.55)'); gl.addColorStop(1, 'rgba(244,244,241,0)');
    ctx.fillStyle = gl; ctx.beginPath(); ctx.arc(ix, iy, 46, 0, 2*PI); ctx.fill();
    raf = requestAnimationFrame(frame);
  }
  build();
  if (W){ raf = requestAnimationFrame(frame); }
  let rz; window.addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(() => { cancelAnimationFrame(raf); build(); if (W) raf = requestAnimationFrame(frame); }, 180); });
})();
