/* =========================================================
   Gwadar Digital Agency - header menus, mobile sheet, carousel
   ========================================================= */
(function () {
  'use strict';

  var header = document.getElementById('siteHeader');
  var mq = window.matchMedia('(max-width: 991px)');

  /* ---------- Header: scrolled state ---------- */
  function onScroll() { header.classList.toggle('is-scrolled', window.scrollY > 10); }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* ---------- Desktop mega menu ---------- */
  var navBtns = document.querySelectorAll('.nav-btn[data-panel]');
  var panels = {};
  document.querySelectorAll('.mega .panel').forEach(function (p) {
    panels[p.id.replace('panel-', '')] = p;
  });
  var openKey = null, closeTimer = null;

  function openPanel(key) {
    clearTimeout(closeTimer);
    if (openKey === key) return;
    Object.keys(panels).forEach(function (k) { panels[k].hidden = k !== key; });
    navBtns.forEach(function (b) { b.setAttribute('aria-expanded', String(b.dataset.panel === key)); });
    openKey = key;
  }
  function closePanel() {
    clearTimeout(closeTimer);
    Object.keys(panels).forEach(function (k) { panels[k].hidden = true; });
    navBtns.forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
    openKey = null;
  }
  function scheduleClose() { clearTimeout(closeTimer); closeTimer = setTimeout(closePanel, 160); }

  navBtns.forEach(function (btn) {
    btn.addEventListener('mouseenter', function () { if (!mq.matches) openPanel(btn.dataset.panel); });
    btn.addEventListener('click', function () {
      if (mq.matches) return;
      openKey === btn.dataset.panel ? closePanel() : openPanel(btn.dataset.panel);
    });
  });
  // plain links in the pill close any open panel when hovered
  document.querySelectorAll('.nav-btn:not([data-panel])').forEach(function (a) {
    a.addEventListener('mouseenter', closePanel);
  });
  var navWrap = document.getElementById('mainNav'), mega = document.getElementById('mega');
  [navWrap, mega].forEach(function (el) {
    el.addEventListener('mouseenter', function () { clearTimeout(closeTimer); });
    el.addEventListener('mouseleave', scheduleClose);
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closePanel(); closeSheet(); }
  });
  document.addEventListener('click', function (e) {
    if (openKey && !header.contains(e.target)) closePanel();
  });
  mq.addEventListener('change', function () { closePanel(); closeSheet(); });

  /* ---------- Mobile bottom sheet ---------- */
  var sheet = document.getElementById('sheet');
  var backdrop = document.getElementById('sheetBackdrop');
  var sheetBody = document.getElementById('sheetBody');
  var sheetTitle = document.getElementById('sheetTitle');
  var barBtns = document.querySelectorAll('.bb-item[data-sheet]');
  var sheetKey = null;

  function openSheet(key) {
    sheetBody.innerHTML = '';
    if (key === 'more') {
      sheetTitle.textContent = 'More';
      sheetBody.appendChild(document.getElementById('tpl-more').content.cloneNode(true));
    } else {
      var src = panels[key];
      var clone = src.cloneNode(true);
      clone.removeAttribute('id'); clone.removeAttribute('hidden');
      sheetTitle.textContent = src.dataset.title;
      sheetBody.appendChild(clone);
    }
    sheet.hidden = false; backdrop.hidden = false;
    sheetBody.scrollTop = 0;
    sheetKey = key;
    barBtns.forEach(function (b) { b.setAttribute('aria-expanded', String(b.dataset.sheet === key)); });
  }
  function closeSheet() {
    sheet.hidden = true; backdrop.hidden = true; sheetKey = null;
    barBtns.forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
  }
  barBtns.forEach(function (b) {
    b.addEventListener('click', function () {
      sheetKey === b.dataset.sheet ? closeSheet() : openSheet(b.dataset.sheet);
    });
  });
  document.getElementById('sheetClose').addEventListener('click', closeSheet);
  backdrop.addEventListener('click', closeSheet);
  sheetBody.addEventListener('click', function (e) { if (e.target.closest('a')) closeSheet(); });

  /* ---------- Client carousel (auto-scrolling marquee) ---------- */
  var track = document.getElementById('carouselTrack');
  var viewport = document.getElementById('carouselViewport');
  var clients = window.GWADAR_CLIENTS || [];
  if (!track || !clients.length) return;

  function esc(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }
  function cardHTML(c) {
    var style = [];
    if (c.bg) style.push('--bg:' + c.bg);
    if (c.image) style.push("--img:url('" + String(c.image).replace(/'/g, '%27') + "')");
    var top = c.logo
      ? '<img class="c-logo" src="' + esc(c.logo) + '" alt="' + esc(c.name) + '" loading="lazy">'
      : '<span class="c-name">' + esc(c.name) + '</span>';
    var bottom = (c.stat || c.label)
      ? '<div><div class="c-stat">' + esc(c.stat) + '</div><div class="c-label">' + esc(c.label) + '</div></div>'
      : '<div></div>';
    return '<article class="c-card' + (c.image ? ' has-img' : '') + '" style="' + style.join(';') + '">' + top + bottom + '</article>';
  }

  var setHTML = clients.map(cardHTML).join('');
  track.innerHTML = setHTML;
  var gap = 12;
  var setWidth = 0;

  function measure() {
    // rebuild with enough copies to always cover viewport + one full set
    track.innerHTML = setHTML;
    setWidth = track.scrollWidth + gap;
    var copies = Math.max(2, Math.ceil((viewport.clientWidth * 2) / setWidth) + 1);
    var html = '';
    for (var i = 0; i < copies; i++) html += setHTML;
    track.innerHTML = html;
    track.querySelectorAll('.c-card').forEach(function (el, i) {
      if (i >= clients.length) el.setAttribute('aria-hidden', 'true');
    });
  }
  measure();

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)');
  var pos = 0, kick = 0, hovering = false, last = performance.now();
  var SPEED = 0.045; // px per ms

  function cardStep() { var c = track.querySelector('.c-card'); return c ? c.offsetWidth + gap : 296; }

  function frame(now) {
    var dt = Math.min(now - last, 50); last = now;
    if (!hovering && !reduce.matches) pos += SPEED * dt;
    if (kick !== 0) { var s = kick * 0.14; pos += s; kick -= s; if (Math.abs(kick) < .5) { pos += kick; kick = 0; } }
    pos = ((pos % setWidth) + setWidth) % setWidth;
    track.style.transform = 'translate3d(' + (-pos) + 'px,0,0)';
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  var car = document.getElementById('clientCarousel');
  car.addEventListener('mouseenter', function () { hovering = true; });
  car.addEventListener('mouseleave', function () { hovering = false; });
  car.addEventListener('focusin', function () { hovering = true; });
  car.addEventListener('focusout', function () { hovering = false; });
  document.getElementById('carNext').addEventListener('click', function () { kick += cardStep(); });
  document.getElementById('carPrev').addEventListener('click', function () { kick -= cardStep(); });

  // touch swipe
  var sx = null, spos = 0;
  viewport.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; spos = pos; hovering = true; kick = 0; }, { passive: true });
  viewport.addEventListener('touchmove', function (e) { if (sx !== null) pos = spos + (sx - e.touches[0].clientX); }, { passive: true });
  viewport.addEventListener('touchend', function () { sx = null; hovering = false; });

  var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(measure, 200); });
})();
