/* Kuä prototype — site behaviour. No tracking, no external requests. */
(function () {
  "use strict";
  var root = document.documentElement;
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Language ---------- */
  function setLang(l, save) {
    if (["en", "kk", "ru"].indexOf(l) < 0) l = "en";
    root.setAttribute("data-lang", l);
    root.setAttribute("lang", l);
    document.querySelectorAll("[data-set-lang]").forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-set-lang") === l ? "true" : "false");
    });
    var t = document.querySelector('meta[name="title-' + l + '"]');
    if (t) document.title = t.getAttribute("content");
    if (save) store.set("kua-lang", l);
    // re-run reveals for newly visible blocks
    setTimeout(observeAll, 30);
    document.dispatchEvent(new CustomEvent("kua:lang", { detail: l }));
  }
  document.querySelectorAll("[data-set-lang]").forEach(function (b) {
    b.addEventListener("click", function () { setLang(b.getAttribute("data-set-lang"), true); });
  });
  setLang(root.getAttribute("data-lang") || "en", false);

  /* ---------- Theme ---------- */
  function setTheme(t, save) {
    if (["system", "light", "dark"].indexOf(t) < 0) t = "system";
    root.setAttribute("data-theme", t);
    document.querySelectorAll("[data-set-theme]").forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-set-theme") === t ? "true" : "false");
    });
    if (save) store.set("kua-theme", t);
  }
  document.querySelectorAll("[data-set-theme]").forEach(function (b) {
    b.addEventListener("click", function () { setTheme(b.getAttribute("data-set-theme"), true); });
  });
  setTheme(root.getAttribute("data-theme") || "system", false);

  /* ---------- Banner disclosure & translation note ---------- */
  document.querySelectorAll("[data-disclose]").forEach(function (b) {
    var p = document.getElementById(b.getAttribute("aria-controls"));
    b.addEventListener("click", function () {
      var open = b.getAttribute("aria-expanded") === "true";
      b.setAttribute("aria-expanded", open ? "false" : "true");
      if (p) p.hidden = open;
      measureHeader();
    });
  });
  document.querySelectorAll("[data-show-en]").forEach(function (b) {
    b.addEventListener("click", function () { setLang("en", true); });
  });

  /* ---------- Mobile menu ---------- */
  var nav = document.querySelector(".navbar"), mb = document.querySelector(".menu-btn");
  function measureHeader() {
    var h = document.querySelector(".site-header");
    if (h) root.style.setProperty("--hdr", (h.getBoundingClientRect().bottom) + "px");
  }
  if (mb && nav) {
    mb.addEventListener("click", function () {
      measureHeader();
      var open = nav.classList.toggle("open");
      mb.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); mb.setAttribute("aria-expanded", "false"); mb.focus(); }
    });
    nav.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { nav.classList.remove("open"); mb.setAttribute("aria-expanded", "false"); }); });
  }
  window.addEventListener("resize", measureHeader);

  /* ---------- Scroll reveal & chart triggers ---------- */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (es) {
    es.forEach(function (e) {
      if (e.isIntersecting) {
        e.target.classList.add("in");
        if (e.target.hasAttribute("data-count")) countUp(e.target);
        if (!e.target.classList.contains("loop")) io.unobserve(e.target);
      } else if (e.target.classList.contains("loop")) {
        e.target.classList.remove("in"); // pause loops off-screen
      }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }) : null;
  function observeAll() {
    document.querySelectorAll(".rv:not(.in), .fig:not(.in), .loop, [data-count]:not(.done)").forEach(function (el) {
      if (!el.offsetParent && el.getClientRects().length === 0) return; // hidden language block
      if (io) io.observe(el); else el.classList.add("in");
    });
  }
  observeAll();

  /* ---------- Count-up numbers ---------- */
  function countUp(el) {
    if (el.classList.contains("done")) return;
    el.classList.add("done");
    var end = parseFloat(el.getAttribute("data-count")), dec = parseInt(el.getAttribute("data-dec") || "0", 10);
    var pre = el.getAttribute("data-pre") || "", suf = el.getAttribute("data-suf") || "";
    var loc = { en: "en-GB", kk: "kk-KZ", ru: "ru-RU" }[root.getAttribute("data-lang")] || "en-GB";
    var comma = root.getAttribute("data-lang") !== "en";
    function fmt(v) { var x = v.toFixed(dec); if (comma) x = x.replace(".", ","); return pre + x + suf; }
    if (reduce) { el.textContent = fmt(end); return; }
    var t0 = null, dur = 1400;
    function step(ts) {
      if (!t0) t0 = ts;
      var p = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(end * e);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  /* ---------- Looping animations: pause / reduced motion ---------- */
  document.querySelectorAll(".loop").forEach(function (lp) {
    if (reduce) lp.classList.add("paused", "static");
    var b = lp.querySelector(".pause");
    if (!b) return;
    function sync() {
      var p = lp.classList.contains("paused");
      b.setAttribute("aria-pressed", p ? "true" : "false");
    }
    b.addEventListener("click", function () { lp.classList.toggle("paused"); lp.classList.remove("static"); sync(); });
    sync();
  });

  /* ---------- Figure toggles (e.g., Figure 1 regroup) ---------- */
  document.querySelectorAll("[data-toggle-group]").forEach(function (g) {
    var fig = g.closest(".fig");
    g.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        g.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        fig.querySelectorAll(".view").forEach(function (v) { v.classList.toggle("on", v.getAttribute("data-view") === b.getAttribute("data-show")); });
        fig.classList.remove("in"); void fig.offsetWidth; fig.classList.add("in");
      });
    });
  });

  /* ---------- Scripted demo ---------- */
  document.querySelectorAll(".demo").forEach(function (d) {
    var steps = d.querySelectorAll(".demo-steps button"), screens = d.querySelectorAll(".ph-screen");
    var prev = d.querySelector("[data-prev]"), next = d.querySelector("[data-next]"), live = d.querySelector("[aria-live]");
    var i = 0, n = screens.length;
    function go(k) {
      i = Math.max(0, Math.min(n - 1, k));
      steps.forEach(function (s, j) { s.toggleAttribute("aria-current", j === i); if (j === i) s.setAttribute("aria-current", "step"); s.classList.toggle("done", j < i); });
      screens.forEach(function (s, j) { s.classList.toggle("on", j === i); });
      if (prev) prev.disabled = i === 0;
      if (next) {
        next.querySelectorAll("[data-last]").forEach(function (x) { x.hidden = i !== n - 1; });
        next.querySelectorAll("[data-notlast]").forEach(function (x) { x.hidden = i === n - 1; });
      }
      if (live) live.textContent = (steps[i] ? steps[i].querySelector("b").textContent : "");
      var body = d.querySelector(".ph-body"); if (body) body.scrollTop = 0;
    }
    steps.forEach(function (s, j) { s.addEventListener("click", function () { go(j); }); });
    if (prev) prev.addEventListener("click", function () { go(i - 1); });
    if (next) next.addEventListener("click", function () { go(i === n - 1 ? 0 : i + 1); });
    go(0);
  });

  /* ---------- Energy calculator ---------- */
  document.querySelectorAll(".calc").forEach(function (c) {
    var users = c.querySelector("[name=users]"), reqs = c.querySelector("[name=reqs]");
    var wh = 0.34, GRID = 603, PER = 13.94;
    var oUsers = c.querySelector("[data-o=users]"), oReqs = c.querySelector("[data-o=reqs]");
    var oCalls = c.querySelector("[data-o=calls]"), oMwh = c.querySelector("[data-o=mwh]"), oT = c.querySelector("[data-o=t]"), oP = c.querySelector("[data-o=p]"), ppl = c.querySelector(".people");
    function loc() { return { en: "en-GB", kk: "kk-KZ", ru: "ru-RU" }[root.getAttribute("data-lang")] || "en-GB"; }
    function f(v, d) { return v.toLocaleString(loc(), { minimumFractionDigits: d, maximumFractionDigits: d }); }
    var person = '<svg viewBox="0 0 20 24" aria-hidden="true"><circle cx="10" cy="6" r="4.2" fill="currentColor"/><path d="M2.5 23c0-5.2 3.4-9 7.5-9s7.5 3.8 7.5 9z" fill="currentColor"/></svg>';
    function run() {
      var u = parseFloat(users.value), r = parseFloat(reqs.value);
      var calls = u * 1e6 * r * 12;            // requests per year
      var kwh = calls * wh / 1000;             // Wh -> kWh
      var t = kwh * GRID / 1e6;                // g -> tonnes
      var p = t / PER;
      oUsers.textContent = f(u, 1); oReqs.textContent = f(r, 0);
      oCalls.textContent = f(calls / 1e6, 0); oMwh.textContent = f(kwh / 1000, 1); oT.textContent = f(t, 1); oP.textContent = f(p, 1);
      var whole = Math.floor(p), part = p - whole, html = "";
      var cap = Math.min(whole, 40);
      for (var k = 0; k < cap; k++) html += person;
      if (whole < 40 && part > 0.05) html += person.replace("<svg", '<svg class="part"');
      ppl.innerHTML = html;
    }
    c.querySelectorAll("[data-wh]").forEach(function (b) {
      b.addEventListener("click", function () {
        wh = parseFloat(b.getAttribute("data-wh"));
        c.querySelectorAll("[data-wh]").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        run();
      });
    });
    users.addEventListener("input", run); reqs.addEventListener("input", run);
    document.addEventListener("kua:lang", run);
    run();
  });

  /* ---------- On-this-page highlighting ---------- */
  var toc = document.querySelector(".toc");
  if (toc && io) {
    var links = toc.querySelectorAll("a");
    var tio = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.toggle("on", a.getAttribute("href") === "#" + e.target.id); });
        }
      });
    }, { rootMargin: "-30% 0px -60% 0px" });
    document.querySelectorAll(".prose > section[id]").forEach(function (s) { tio.observe(s); });
  }

  /* ---------- Reading progress & back to top ---------- */
  var bar = document.querySelector(".progress"), top = document.querySelector(".totop");
  function onScroll() {
    var h = document.documentElement, max = h.scrollHeight - h.clientHeight;
    if (bar) bar.style.width = (max > 0 ? (h.scrollTop / max) * 100 : 0) + "%";
    if (top) top.classList.toggle("show", h.scrollTop > 900);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  if (top) top.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" }); });
  onScroll();

  /* ---------- Reference filter ---------- */
  var rf = document.querySelector("[data-ref-filter]");
  if (rf) rf.addEventListener("input", function () {
    var q = rf.value.toLowerCase();
    document.querySelectorAll(".refs li").forEach(function (li) { li.hidden = q && li.textContent.toLowerCase().indexOf(q) < 0; });
  });

  measureHeader();
})();
