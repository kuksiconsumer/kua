#!/usr/bin/env python3
"""Builds the static Kuä site from src/content/<page>.<lang>.html into the repository root.
Usage:  python3 src/build.py      (no dependencies beyond Python 3.8+)"""
import os, re, html, importlib.util, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import components as C

LANGS = ["en", "kk", "ru"]
def load_strings(lang):
    p = os.path.join(HERE, f"strings_{lang}.py")
    if not os.path.exists(p):
        return {}
    spec = importlib.util.spec_from_file_location(f"s_{lang}", p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m.S
C.S = {l: load_strings(l) for l in LANGS}
t = C.t; e = C.e; icon = C.icon

PAGES = [("index", "nav_home"), ("problem", "nav_problem"), ("data", "nav_data"), ("research", "nav_research"),
         ("solution", "nav_solution"), ("costs", "nav_costs"), ("verdict", "nav_verdict"), ("about", "nav_about"), ("sources", "nav_sources")]
SEQ = ["problem", "data", "research", "solution", "costs", "verdict"]

def tri(key, fmt=None):
    out = ""
    for l in LANGS:
        v = t(key, l)
        if fmt: v = fmt(v, l)
        out += f'<span class="l-{l}" lang="{l}">{v}</span>'
    return out

def tri_attr(key):  # for aria-labels: use English (visible text is translated)
    return e(t(key, "en"))

def read_content(page, lang):
    p = os.path.join(HERE, "content", f"{page}.{lang}.html")
    if not os.path.exists(p):
        if lang == "en":
            raise SystemExit(f"missing {p}")
        C.MISSING.add((lang, f"content:{page}"))
        p = os.path.join(HERE, "content", f"{page}.en.html")
    raw = open(p, encoding="utf-8").read()
    meta, body = {}, raw
    if "\n---\n" in raw:
        head, body = raw.split("\n---\n", 1)
        for line in head.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip()
    return meta, body

def expand(body, lang):
    def rep(m):
        kind, _, arg = m.group(1).partition(":")
        if kind == "loop": return C.LOOPS[arg](lang)
        if kind == "icon": return icon(arg)
        if kind == "art": return C.art_small(arg)
        return C.COMP[kind](lang)
    return re.sub(r"\{\{([a-z0-9_:]+)\}\}", rep, body)

def words(s):
    return len(re.sub(r"<[^>]+>", " ", s).split())

THEME_BTNS = lambda: "".join(
    f'<button type="button" data-set-theme="{k}" aria-pressed="false" aria-label="{tri_attr("th_"+k)}" title="{tri_attr("th_"+k)}">{icon(ic)}<span class="t">{tri("th_"+k)}</span></button>'
    for k, ic in (("system", "monitor"), ("light", "sun"), ("dark", "moon")))

def chrome_top(page):
    nav = ""
    for slug, key in PAGES:
        href = "index.html" if slug == "index" else f"{slug}.html"
        cur = ' aria-current="page"' if slug == page else ""
        nav += f'<a href="{href}"{cur}>{tri(key)}</a>'
    langs = "".join(f'<button type="button" data-set-lang="{l}" aria-pressed="false" lang="{l}" aria-label="{n}">{a}</button>'
                    for l, a, n in (("kk", "ҚАЗ", "Қазақша"), ("ru", "РУС", "Русский"), ("en", "ENG", "English")))
    return f'''<a class="skip" href="#main">{tri("skip")}</a>
<div class="progress" aria-hidden="true"></div>
<div class="proto"><div class="wrap"><span class="mark" aria-hidden="true"></span><span>{tri("banner")}</span>
<button type="button" data-disclose aria-expanded="false" aria-controls="proto-more">{tri("banner_how")}{icon("chev")}</button></div></div>
<div class="proto-more" id="proto-more" hidden><div class="wrap grid">
<div><span class="ic">{icon("doc")}</span><b>{tri("bm1_t")}</b>{tri("bm1")}</div>
<div><span class="ic">{icon("lock")}</span><b>{tri("bm2_t")}</b>{tri("bm2")}</div></div></div>
<header class="site-header"><div class="wrap">
<a class="brand" href="index.html">{C.LOGO}<span><b>Kuä</b><small>{tri("tagline")}</small></span></a>
<div class="controls">
<div class="seg" role="group" aria-label="Language">{langs}</div>
<div class="seg theme" role="group" aria-label="Theme">{THEME_BTNS()}</div>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Menu">{icon("menu")}</button>
</div></div></header>
<div class="xnote" role="note"><div class="wrap">{icon("alert")}<span>{tri("xnote")}</span><button type="button" data-show-en>{tri("xnote_btn")}</button></div></div>
<nav class="navbar" id="site-nav" aria-label="Main"><div class="wrap">{nav}
<a class="demo-link" href="index.html#demo">{tri("nav_demo")} →</a>
<div class="drawer-only"><span class="muted">{tri("theme_label")}</span><div class="seg" role="group" aria-label="Theme">{THEME_BTNS()}</div></div>
</div></nav>'''

def footer():
    links = lambda keys: "".join(f'<li><a href="{s}.html">{tri(k)}</a></li>' for s, k in keys)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="cols">
<div><a class="brand" href="index.html" style="margin-bottom:12px">{C.LOGO}<span><b>Kuä</b></span></a><p class="muted" style="margin:0">{tri("f_about")}</p></div>
<div><h4>{tri("f_prop")}</h4><ul>{links([(s, "nav_"+s) for s in SEQ])}</ul></div>
<div><h4>{tri("f_more")}</h4><ul>{links([("about","nav_about"),("sources","nav_sources")])}<li><a href="index.html#demo">{tri("nav_demo")}</a></li><li><a href="about.html#translation">{tri("f_xnote")}</a></li></ul></div>
<div><h4>{tri("f_off")}</h4><ul><li><a href="https://egov.kz">{tri("f_egov")}</a></li></ul><p class="muted" style="font-size:.84rem;margin-top:10px">{tri("f_nodata")}</p></div>
</div>
<div class="fine"><span>{tri("f_course")}</span><span>{tri("f_lang")}</span></div>
</div></footer>
<button class="totop" type="button" aria-label="{tri_attr("totop")}">{icon("up")}</button>'''

def page_head(page, metas, bodies):
    blocks = ""
    for l in LANGS:
        m = metas[l]
        mins = max(1, round(words(bodies[l]) / 200))
        crumbs = f'<div class="crumbs"><a href="index.html">{e(t("home",l))}</a> / {e(t("nav_"+page,l))}</div>'
        meta = (f'<div class="meta"><span>{icon("clock")}{e(t("read_min",l).format(n=mins))}</span>'
                f'<span>{icon("doc")}{e(t("updated",l))}</span>'
                + (f'<span>{icon("globe")}{e(t("orig_en",l))}</span>' if l != "en" else "") + "</div>")
        blocks += (f'<div class="l-{l}" lang="{l}">{crumbs}<p class="eyebrow">{m.get("eyebrow","")}</p><h1>{m.get("title","")}</h1>'
                   f'<p class="lede">{m.get("lede","")}</p>{meta}</div>')
    art = metas["en"].get("art", page)
    return f'<div class="page-head"><div class="wrap"><div>{blocks}</div><div class="art" aria-hidden="true">{C.art_small(art)}</div></div></div>'

def toc(bodies):
    out = ""
    for l in LANGS:
        items = re.findall(r'<section id="([^"]+)" data-toc="([^"]+)"', bodies[l])
        if not items: continue
        lis = "".join(f'<li><a href="#{i}">{lab}</a></li>' for i, lab in items)
        out += f'<div class="l-{l}" lang="{l}"><b>{e(t("toc",l))}</b><ol>{lis}</ol></div>'
    return f'<aside class="toc" aria-label="On this page">{out}</aside>' if out else ""

def pager(page):
    if page not in SEQ: return ""
    i = SEQ.index(page); out = '<nav class="pager" aria-label="Pages">'
    if i > 0:
        p = SEQ[i-1]; out += f'<a class="prev" href="{p}.html"><small>← {tri("prev")}</small><b>{tri("nav_"+p)}</b></a>'
    if i < len(SEQ) - 1:
        n = SEQ[i+1]; out += f'<a class="next" href="{n}.html"><small>{tri("next")} →</small><b>{tri("nav_"+n)}</b></a>'
    return out + "</nav>"

def build_page(page):
    metas, bodies = {}, {}
    for l in LANGS:
        m, b = read_content(page, l)
        metas[l] = m; bodies[l] = expand(b, l)
    titles = {l: (metas[l].get("meta_title") or f'{re.sub("<[^>]+>","",metas[l].get("title",""))} · Kuä') for l in LANGS}
    desc = e(metas["en"].get("desc", t("f_about", "en")))
    langblocks = lambda inner: "".join(f'<div class="l-{l}" lang="{l}">{inner(l)}</div>' for l in LANGS)
    if page == "index":
        main = langblocks(lambda l: bodies[l])
    else:
        main = (page_head(page, metas, bodies) + f'<div class="wrap"><div class="article">{toc(bodies)}<div class="prose">'
                + langblocks(lambda l: bodies[l]) + pager(page) + "</div></div></div>")
    head_meta = "".join(f'<meta name="title-{l}" content="{e(titles[l])}">' for l in LANGS)
    doc = f'''<!doctype html>
<html lang="en" data-lang="en" data-theme="system">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titles["en"])}</title>
{head_meta}
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0b1830" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#e4eefb" media="(prefers-color-scheme: light)">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/Inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/Literata.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
<script>(function(){{var d=document.documentElement;d.classList.add("js");try{{var q=new URLSearchParams(location.search).get("lang");var l=q||localStorage.getItem("kua-lang");if(l&&/^(en|kk|ru)$/.test(l)){{d.setAttribute("data-lang",l);d.setAttribute("lang",l)}}var t=localStorage.getItem("kua-theme");if(t)d.setAttribute("data-theme",t)}}catch(e){{}}}})();</script>
</head>
<body>
{chrome_top(page)}
<main id="main">{main}</main>
{footer()}
<script src="assets/js/site.js" defer></script>
</body>
</html>
'''
    out = "index.html" if page == "index" else f"{page}.html"
    open(os.path.join(ROOT, out), "w", encoding="utf-8").write(doc)
    return out, {l: words(bodies[l]) for l in LANGS}

if __name__ == "__main__":
    for slug, _ in PAGES:
        if os.path.exists(os.path.join(HERE, "content", f"{slug}.en.html")):
            o, w = build_page(slug); print(f"built {o:16s} words {w}")
    miss = sorted(C.MISSING)
    if miss:
        print(f"\n{len(miss)} untranslated items fell back to English, e.g.:", miss[:8])
