"""Figures, looping animations, illustrations, demo and diagrams. All text comes from S[lang]."""
import html as _h

S = {}          # filled by build.py: {"en": {...}, "kk": {...}, "ru": {...}}
MISSING = set()

def t(k, lang):
    v = S.get(lang, {}).get(k)
    if v is None:
        if lang != "en":
            MISSING.add((lang, k))
        v = S["en"][k]
    return v

def e(s):  # escape for SVG/HTML text nodes
    return _h.escape(s, quote=False)

def svg_lines(text, x, y, cls, lh=14, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    parts = text.split("\n")
    out = f'<text class="{cls}" x="{x}" y="{y}"{a}>'
    for i, p in enumerate(parts):
        out += f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{e(p)}</tspan>'
    return out + "</text>"

# ---------------------------------------------------------------- icons
IC = {
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "moon": '<path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/>',
 "monitor": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "arrowl": '<path d="M19 12H5M11 6l-6 6 6 6"/>',
 "up": '<path d="M12 19V5M6 11l6-6 6 6"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8h.01"/>',
 "alert": '<path d="M12 3 2.5 20h19z"/><path d="M12 10v4M12 17h.01"/>',
 "check": '<path d="m5 12 4.5 4.5L19 7"/>',
 "shield": '<path d="M12 3 4.5 6v5.5c0 4.6 3.2 8.2 7.5 9.5 4.3-1.3 7.5-4.9 7.5-9.5V6z"/><path d="m9 12 2 2 4-4"/>',
 "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11M4.5 6h.01M4.5 12h.01M4.5 18h.01"/>',
 "compare": '<rect x="3" y="4" width="7" height="16" rx="1.5"/><rect x="14" y="4" width="7" height="16" rx="1.5"/><path d="M5.5 9h2M5.5 13h2M16.5 9h2M16.5 13h2"/>',
 "pen": '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m13.5 6.5 4 4"/>',
 "route": '<circle cx="6" cy="18" r="2.5"/><circle cx="18" cy="6" r="2.5"/><path d="M8.5 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.5"/>',
 "scale": '<path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3.5 3.5 0 0 0 6 0zM19 7l-3 7a3.5 3.5 0 0 0 6 0z"/>',
 "building": '<path d="M3 21h18M5 21V10l7-5 7 5v11M9 21v-6h6v6"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
 "chart": '<path d="M4 20V4M4 20h16M8 16v-4M12 16V8M16 16v-6"/>',
 "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>',
 "text": '<path d="M4 7V5h16v2M12 5v14M9 19h6"/>',
 "ear": '<path d="M7 9a5 5 0 0 1 10 0c0 3-3 4-3 7a3 3 0 0 1-6 0"/><path d="M10 9a2 2 0 0 1 4 0"/>',
 "hand": '<path d="M7 11V5.5a1.5 1.5 0 0 1 3 0V10M10 9V4.5a1.5 1.5 0 0 1 3 0V10M13 9.5V5.5a1.5 1.5 0 0 1 3 0V12M16 10a1.5 1.5 0 0 1 3 0v3a8 8 0 0 1-8 8h-1a6 6 0 0 1-5-3l-2.5-4a1.5 1.5 0 0 1 2.6-1.5L7 15"/>',
 "store": '<path d="M3 9 5 4h14l2 5M4 9v11h16V9M3 9h18M9 20v-6h6v6"/>',
 "play": '<path d="M7 5v14l12-7z" fill="currentColor" stroke="none"/>',
 "pause": '<path d="M7 5h3.5v14H7zM13.5 5H17v14h-3.5z" fill="currentColor" stroke="none"/>',
 "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19 13 11"/>',
 "coins": '<ellipse cx="9" cy="7" rx="6" ry="3"/><path d="M3 7v5c0 1.7 2.7 3 6 3s6-1.3 6-3V7M9 15v3c0 1.7 2.7 3 6 3s6-1.3 6-3v-5c0-1.7-2.7-3-6-3"/>',
 "work": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>',
 "flag": '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
}
def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[name]}</svg>'

LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect x="1" y="1" width="32" height="32" rx="9" fill="var(--accent)"/>'
        '<path d="M9 11.5h11M9 17h16M9 22.5h9" stroke="var(--accent-ink)" stroke-width="2.2" stroke-linecap="round"/>'
        '<circle cx="24.5" cy="11.5" r="2.6" fill="var(--accent-ink)"/></svg>')

def pause_btn(lang):
    return (f'<button class="pause" type="button" aria-pressed="false" aria-label="{e(t("pause",lang))}">'
            f'{icon("pause","i-pause")}{icon("play","i-play")}</button>')

# ---------------------------------------------------------------- hero art
def art_hero(lang):
    L = lambda k: e(t(k, lang))
    def reg(y, label, cls="", warnline=False):
        return (f'<g class="a-float" style="animation-delay:{y/100:.1f}s">'
                f'<rect class="s-card" x="16" y="{y}" width="168" height="96" rx="14"/>'
                f'<rect class="s-soft" x="16.6" y="{y+.6}" width="166.8" height="28" rx="13.4"/>'
                f'<text class="s-txt2" x="32" y="{y+19}">{label}</text>'
                f'<rect class="s-bar" x="32" y="{y+44}" width="110" height="7" rx="3.5"/>'
                f'<rect class="{"s-warn" if warnline else "s-bar"}" x="32" y="{y+59}" width="78" height="7" rx="3.5"/>'
                f'<rect class="s-bar" x="32" y="{y+74}" width="124" height="7" rx="3.5"/></g>')
    rows = ""
    for i, (w, c) in enumerate([(120, "s-bar2"), (96, "s-bar2"), (132, "s-warn"), (88, "s-bar2"), (110, "s-bar2")]):
        y = 132 + i * 46
        bg = "s-warn-soft" if c == "s-warn" else "s-card"
        rows += (f'<rect class="{bg}" x="330" y="{y}" width="160" height="36" rx="9"/>'
                 f'<circle class="{"s-warn" if c=="s-warn" else "s-soft"}" cx="348" cy="{y+18}" r="7"/>'
                 f'<rect class="{c}" x="362" y="{y+10}" width="{w*.75:.0f}" height="6" rx="3"/>'
                 f'<rect class="s-bar" x="362" y="{y+22}" width="{w*.5:.0f}" height="5" rx="2.5"/>')
    return f'''<svg viewBox="0 0 520 410" role="img" aria-label="{L("art_log")}">
<path class="s-line" d="M184 88 C 250 88, 260 160, 316 160" />
<path class="s-acc-st a-flow" d="M184 88 C 250 88, 260 160, 316 160" />
<path class="s-line" d="M184 218 C 250 218, 262 250, 316 250" />
<path class="s-acc-st a-flow" style="stroke:var(--warn)" d="M184 218 C 250 218, 262 250, 316 250" />
<path class="s-line" d="M184 348 C 250 348, 260 330, 316 330" />
<path class="s-acc-st a-flow" d="M184 348 C 250 348, 260 330, 316 330" />
{reg(40, L("art_civil"))}{reg(170, L("art_addr"), warnline=True)}{reg(300, L("art_med"))}
<rect x="316" y="30" width="188" height="350" rx="28" fill="var(--surface-2)" stroke="var(--line-2)" stroke-width="1.4"/>
<rect x="388" y="42" width="44" height="6" rx="3" class="s-bar"/>
<text x="334" y="88" style="fill:var(--ink);font:600 20px Literata,serif">Kuä</text>
<text class="s-txt3" x="334" y="110">{L("art_log")}</text>
{rows}
<circle class="s-warn a-blink" cx="250" cy="234" r="5"/>
<text class="s-txtw" x="252" y="212" text-anchor="middle">{L("art_mis")}</text>
</svg>'''

def art_small(kind):
    """Minimal page-head illustrations (no text)."""
    A = {
     "problem": '''<rect class="s-card" x="20" y="30" width="80" height="56" rx="10"/><rect class="s-card" x="140" y="18" width="80" height="56" rx="10"/><rect class="s-card" x="90" y="112" width="80" height="56" rx="10"/>
<path class="s-line s-dash" d="M100 58 L140 46M60 86 L100 112M180 74 L150 112"/><circle class="s-warn a-blink" cx="120" cy="52" r="5"/>
<rect class="s-bar" x="32" y="46" width="44" height="6" rx="3"/><rect class="s-bar" x="32" y="60" width="30" height="6" rx="3"/><rect class="s-bar" x="152" y="34" width="44" height="6" rx="3"/><rect class="s-warn" x="152" y="48" width="30" height="6" rx="3"/><rect class="s-bar" x="102" y="128" width="44" height="6" rx="3"/><rect class="s-bar" x="102" y="142" width="30" height="6" rx="3"/>''',
     "data": '''<path class="c-axis" d="M24 160H216M24 160V20"/><rect class="s-soft" x="40" y="100" width="26" height="60" rx="4"/><rect class="s-soft" x="78" y="70" width="26" height="90" rx="4"/><rect class="s-acc" x="116" y="40" width="26" height="120" rx="4"/><rect class="s-soft" x="154" y="118" width="26" height="42" rx="4"/>
<path class="s-acc-st a-flow" d="M40 92 L90 60 L130 30 L190 108"/>''',
     "research": '''<circle cx="92" cy="70" r="50" fill="var(--accent)" fill-opacity=".12" stroke="var(--accent)" stroke-width="1.4"/><circle cx="148" cy="70" r="50" fill="var(--accent)" fill-opacity=".12" stroke="var(--accent)" stroke-width="1.4"/><circle cx="120" cy="118" r="50" fill="var(--accent)" fill-opacity=".12" stroke="var(--accent)" stroke-width="1.4"/><circle class="s-warn a-blink" cx="120" cy="88" r="6"/>''',
     "solution": '''<rect class="s-card" x="70" y="10" width="100" height="160" rx="18"/><rect class="s-bar" x="102" y="20" width="36" height="5" rx="2.5"/>
<rect class="s-soft" x="82" y="40" width="76" height="22" rx="6"/><rect class="s-soft" x="82" y="70" width="76" height="22" rx="6"/><rect class="s-warn-soft" x="82" y="100" width="76" height="22" rx="6"/><rect class="s-acc" x="82" y="134" width="76" height="22" rx="8"/>
<path class="s-line" d="M20 80h40M180 80h40"/><circle class="s-acc" cx="20" cy="80" r="5"/><circle class="s-ok" cx="220" cy="80" r="5"/>''',
     "costs": '''<circle cx="70" cy="90" r="46" class="s-card"/><path d="M70 44 A46 46 0 0 1 112 108 L70 90Z" class="s-acc"/><path d="M70 44 A46 46 0 0 0 30 112 L70 90Z" class="s-soft"/>
<rect class="s-card" x="140" y="40" width="80" height="100" rx="12"/><path class="s-acc-st" d="M156 112 l14-22 14 10 20-32"/><circle class="s-warn a-blink" cx="204" cy="68" r="4.5"/>''',
     "verdict": '''<rect class="s-card" x="44" y="16" width="152" height="150" rx="14"/>
<g><rect class="s-soft" x="60" y="34" width="18" height="18" rx="5"/><path d="m64 43 3.5 3.5L74 39" stroke="var(--accent)" stroke-width="2" fill="none"/><rect class="s-bar" x="88" y="40" width="90" height="6" rx="3"/></g>
<g><rect class="s-soft" x="60" y="64" width="18" height="18" rx="5"/><path d="m64 73 3.5 3.5L74 69" stroke="var(--accent)" stroke-width="2" fill="none"/><rect class="s-bar" x="88" y="70" width="70" height="6" rx="3"/></g>
<g><rect class="s-soft" x="60" y="94" width="18" height="18" rx="5"/><path d="m64 103 3.5 3.5L74 99" stroke="var(--accent)" stroke-width="2" fill="none"/><rect class="s-bar" x="88" y="100" width="84" height="6" rx="3"/></g>
<g><rect class="s-warn-soft" x="60" y="124" width="18" height="18" rx="5"/><rect class="s-bar" x="88" y="130" width="60" height="6" rx="3"/></g>''',
     "about": '''<rect class="s-card" x="40" y="20" width="110" height="140" rx="12"/><rect class="s-bar" x="56" y="40" width="70" height="7" rx="3.5"/><rect class="s-bar" x="56" y="56" width="80" height="6" rx="3"/><rect class="s-bar" x="56" y="70" width="60" height="6" rx="3"/><rect class="s-bar" x="56" y="84" width="76" height="6" rx="3"/>
<circle cx="168" cy="110" r="34" class="s-soft"/><circle cx="168" cy="100" r="10" class="s-acc"/><path d="M148 130a20 18 0 0 1 40 0" class="s-acc"/>''',
     "sources": '''<rect class="s-soft" x="40" y="120" width="160" height="22" rx="5"/><rect class="s-card" x="52" y="96" width="140" height="22" rx="5"/><rect class="s-acc" x="46" y="72" width="150" height="22" rx="5"/><rect class="s-card" x="60" y="48" width="124" height="22" rx="5"/>
<path class="s-acc-st" d="M200 40 l10 -10 M210 30 v14 M210 30 h-14"/>''',
    }
    return f'<svg viewBox="0 0 240 180" aria-hidden="true">{A[kind]}</svg>'

# ---------------------------------------------------------------- loops
def loop_view(lang):
    L = lambda k: e(t(k, lang))
    rows = ""
    data = [("l1_r1", "l1_r1m", "l1_r1d", "s-soft", False), ("l1_r2", "l1_r2m", "l1_r2d", "s-soft", False),
            ("l1_r3", "l1_r3m", "l1_r3d", "s-soft", False), ("l1_r4", "l1_r4m", "l1_r4d", "s-warn", True)]
    for i, (a, b, d, c, ex) in enumerate(data):
        y = 94 + i * 44
        box = (f'<rect x="54" y="{y}" width="372" height="38" rx="9" fill="none" stroke="var(--warn-line)" stroke-width="1.2" stroke-dasharray="5 4"/>'
               if ex else f'<rect x="54" y="{y}" width="372" height="38" rx="9" fill="var(--bg)"/>')
        extra = f'<text class="s-txtw" x="412" y="{y+31}" text-anchor="end">{L("l1_r4a")}</text>' if ex else ""
        rows += (f'<g class="lp a-row" style="animation-delay:{i*0.55:.2f}s">{box}'
                 f'<circle class="{c}" cx="74" cy="{y+19}" r="8"/>'
                 f'<text class="s-txt2" x="92" y="{y+16}" style="font-weight:600;fill:var(--ink)">{L(a)}</text>'
                 f'<text class="s-txt3" x="92" y="{y+31}">{L(b)}</text>'
                 f'<text class="s-txt3" x="412" y="{y+16}" text-anchor="end">{L(d)}</text>{extra}</g>')
    return f'''<div class="loop"><svg viewBox="0 0 480 300" role="img" aria-label="{L("l1_title")}">
<rect class="s-card" x="38" y="24" width="404" height="262" rx="16"/>
<text class="s-txt" x="58" y="56">{L("l1_title")}</text>
<text class="s-txt3" x="58" y="75">{L("l1_sub")}</text>
<g transform="translate(398 42)"><path d="M12 2 5 5v5c0 4.2 3 7.5 7 8.7 4-1.2 7-4.5 7-8.7V5z" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.4"/><path d="m9 10 2 2 4-4" stroke="var(--accent)" stroke-width="1.6" fill="none"/></g>
{rows}</svg>{pause_btn(lang)}</div>'''

def loop_check(lang):
    L = lambda k: e(t(k, lang))
    def card(x, title, v3, side):
        out = (f'<rect class="s-card" x="{x}" y="34" width="196" height="200" rx="14"/>'
               f'<text class="s-txt" x="{x+16}" y="62">{title}</text>')
        vals = [("l2_f1", t("p_name", lang)), ("l2_f2", "14.03.1992"), ("l2_f3", v3)]
        for i, (lab, val) in enumerate(vals):
            y = 84 + i * 46
            if i == 2:
                out += f'<rect class="lp a-flag s-warn-soft" x="{x+8}" y="{y-6}" width="180" height="42" rx="8"/>'
            out += (f'<text class="s-txt3" x="{x+16}" y="{y+10}">{L(lab)}</text>'
                    f'<text class="s-txt2" x="{x+16}" y="{y+27}" style="fill:var(--ink)">{e(val)}</text>')
            if i < 2:
                out += (f'<g class="lp a-ok" style="animation-delay:{0.35*i:.2f}s"><circle class="s-ok-soft" cx="{x+176}" cy="{y+18}" r="9"/>'
                        f'<path d="m{x+172} {y+18} 3 3 6-6" stroke="var(--ok)" stroke-width="1.8" fill="none"/></g>')
        return out
    return f'''<div class="loop"><svg viewBox="0 0 480 300" role="img" aria-label="{L("l2_rule")}">
{card(28, L("l2_a"), t("l2_v3a",lang), 0)}{card(256, L("l2_b"), t("l2_v3b",lang), 1)}
<rect class="lp a-scan" x="28" y="72" width="424" height="2" fill="var(--accent)" opacity=".7"/>
<path class="lp a-draw" style="--len:36" d="M224 194 H256" stroke="var(--warn)" stroke-width="2" fill="none"/>
<g class="lp a-flag"><circle cx="240" cy="194" r="12" fill="var(--warn)"/><text x="240" y="199" text-anchor="middle" style="fill:var(--surface-2);font:700 14px Inter">≠</text></g>
<text class="s-txta" x="28" y="268">{L("l2_rule")}</text>
<text class="lp a-late s-txtw" x="452" y="268" text-anchor="end">{L("l2_found")}</text>
</svg>{pause_btn(lang)}</div>'''

def loop_correct(lang):
    L = lambda k: e(t(k, lang))
    lines = ""
    for i, w in enumerate([196, 172, 204, 150, 188, 120]):
        lines += f'<rect class="lp a-type s-bar2" style="animation-delay:{0.25*i:.2f}s" x="58" y="{106+i*16}" width="{w}" height="6" rx="3"/>'
    return f'''<div class="loop"><svg viewBox="0 0 480 300" role="img" aria-label="{L("l3_head")}">
<g class="lp a-fly">
<rect class="s-card" x="40" y="34" width="244" height="232" rx="14" style="stroke:var(--accent)"/>
<g transform="translate(56 50)"><path d="M0 14h4L13 5l-4-4L0 10z" fill="none" stroke="var(--accent)" stroke-width="1.5"/></g>
<text class="s-txta" x="76" y="62">{L("l3_head")}</text>
<text class="s-txt3" x="58" y="88">{L("l3_to")}</text>
{lines}
<rect x="58" y="222" width="80" height="28" rx="8" fill="none" stroke="var(--line-2)"/>
<text class="s-txt2" x="98" y="240" text-anchor="middle">{L("l3_edit")}</text>
<g class="lp a-press"><rect x="148" y="222" width="118" height="28" rx="8" class="s-acc"/>
<text x="207" y="240" text-anchor="middle" style="fill:var(--accent-ink);font:600 12px Inter">{L("l3_send")}</text></g>
</g>
<g transform="translate(350 92)">
<path d="M0 34 45 8 90 34Z" fill="var(--accent-soft)" stroke="var(--line-2)" stroke-width="1.2"/>
<rect x="6" y="38" width="78" height="62" rx="4" class="s-card"/>
<path d="M22 46v46M38 46v46M54 46v46M70 46v46" class="s-line"/>
<rect x="0" y="100" width="90" height="8" rx="3" class="s-bar2"/>
</g>
{svg_lines(t("l3_body",lang), 395, 222, "s-txt3", anchor="middle")}
<g class="lp a-arrive"><rect x="330" y="236" width="130" height="28" rx="14" class="s-ok-soft"/>
<text class="s-txto" x="395" y="254" text-anchor="middle">{L("l3_ok")}</text></g>
</svg>{pause_btn(lang)}</div>'''

def loop_escalate(lang):
    L = lambda k: e(t(k, lang))
    nodes = ""
    for i, (x, k, ic) in enumerate([(90, "l4_n1", "users"), (240, "l4_n2", "scale"), (390, "l4_n3", "chart")]):
        nodes += (f'<g class="lp a-node" style="animation-delay:{0.25*i:.2f}s"><circle cx="{x}" cy="206" r="22" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="1.4"/>'
                  f'<g transform="translate({x-10} 196) scale(.84)" stroke="var(--accent)" fill="none" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{IC[ic]}</g>'
                  f'{svg_lines(t(k,lang), x, 246, "s-txt2", lh=14, anchor="middle")}</g>')
    paths = [("M240 132 V160 H90 V184", 266), ("M240 132 V184", 52), ("M240 132 V160 H390 V184", 266)]
    p = "".join(f'<path class="lp a-branch" style="--len:{l};animation-delay:{0.2*i:.1f}s" d="{d}" stroke="var(--accent)" stroke-width="2" fill="none"/>' for i, (d, l) in enumerate(paths))
    pb = "".join(f'<path d="{d}" class="s-line s-dash"/>' for d, _ in paths)
    return f'''<div class="loop"><svg viewBox="0 0 480 300" role="img" aria-label="{L("l4_req")}">
<rect x="30" y="28" width="420" height="104" rx="14" class="s-card"/>
<text class="s-txt" x="48" y="56">{L("l4_req")}</text>
<rect x="48" y="76" width="384" height="10" rx="5" class="s-bar"/>
<rect class="lp a-fill" x="48" y="76" width="384" height="10" rx="5" fill="var(--warn)"/>
<circle cx="48" cy="81" r="6" class="s-acc"/>
<text class="s-txt3" x="48" y="110">{L("l4_sent")}</text>
<g transform="translate(424 66)"><path d="M0 0v28M0 0h12l-3 4 3 4H0" stroke="var(--ink-2)" stroke-width="1.4" fill="none"/></g>
<text class="s-txt3" x="432" y="110" text-anchor="end">{L("l4_dead")}</text>
<text class="lp a-flag s-txtw" x="432" y="56" text-anchor="end">{L("l4_none")}</text>
{pb}{p}
<text class="lp a-node s-txta" x="252" y="172">{L("l4_auto")}</text>
{nodes}
</svg>{pause_btn(lang)}</div>'''

LOOPS = {"view": loop_view, "check": loop_check, "correct": loop_correct, "escalate": loop_escalate}

# ---------------------------------------------------------------- figures
def fig_wrap(k, title, body, cap, lang, extra_head="", table=""):
    tb = f'<details><summary>{e(t("show_data",lang))}</summary>{table}</details>' if table else ""
    return (f'<figure class="fig"><div class="fig-head"><div><span class="k">{e(k)}</span><h4>{e(title)}</h4></div>{extra_head}</div>'
            f'{body}<figcaption>{cap}</figcaption>{tb}</figure>')

F1 = [("f1_c1", 23.29, 1), ("f1_c2", 15.24, 2), ("f1_c3", 14.45, 3), ("f1_c4", 12.05, 2), ("f1_c5", 9.37, 2),
      ("f1_c6", 6.46, 2), ("f1_c7", 6.20, 1), ("f1_c8", 5.30, 1), ("f1_c9", 4.27, 1), ("f1_c10", 3.38, 4)]
G = {1: ("f1_grp1", 39.06), 2: ("f1_grp2", 43.12), 3: ("f1_grp3", 14.45), 4: ("f1_grp4", 3.38)}
LOC = {"en": ("en", "."), "kk": ("kk", ","), "ru": ("ru", ",")}
def num(v, lang, d=2):
    s = f"{v:.{d}f}"
    return s.replace(".", LOC[lang][1])

def fig1(lang):
    L = lambda k: e(t(k, lang))
    legend = '<div class="legend">' + "".join(f'<span><i style="background:var(--g{g})"></i>{L(G[g][0])}</span>' for g in (1, 2, 3, 4)) + "</div>"
    mx = 28.0
    cat = '<div class="bars">' + "".join(
        f'<div class="bar g{g}" style="--i:{i}"><div class="lb">{L(k)}</div><div class="tr"><div class="fl" style="--w:{v/mx*100:.2f}%"></div>'
        f'<span class="vl" style="--w:{v/mx*100:.2f}%">{num(v,lang)}%</span></div></div>' for i, (k, v, g) in enumerate(F1)) + "</div>"
    mx2 = 48.0
    org = '<div class="bars">'
    for i, g in enumerate((1, 2, 3, 4)):
        k, tot = G[g]
        segs = "".join(f'<i style="flex:{v}" title="{L(kk)}: {num(v,lang)}%"></i>' for kk, v, gg in F1 if gg == g)
        org += (f'<div class="bar tall g{g}" style="--i:{i}"><div class="lb"><b>{L(k)}</b></div><div class="tr"><div class="fl seg-row" style="--w:{tot/mx2*100:.2f}%">{segs}</div>'
                f'<span class="vl" style="--w:{tot/mx2*100:.2f}%">{num(tot,lang)}%</span></div></div>')
    org += "</div>"
    toggle = (f'<div class="toggle" data-toggle-group role="group" aria-label="{L("f1_t")}">'
              f'<button type="button" aria-pressed="true" data-show="cat">{L("f1_by_cat")}</button>'
              f'<button type="button" aria-pressed="false" data-show="org">{L("f1_by_org")}</button></div>')
    body = legend + f'<div class="view on" data-view="cat">{cat}</div><div class="view" data-view="org">{org}</div>'
    table = (f'<table><thead><tr><th>{L("f1_th1")}</th><th>{L("f1_th2")}</th><th class="n">{L("f1_th3")}</th></tr></thead><tbody>'
             + "".join(f'<tr><td>{L(k)}</td><td>{L(G[g][0])}</td><td class="n">{num(v,lang)}%</td></tr>' for k, v, g in F1)
             + "".join(f'<tr><td><b>{L(G[g][0])}</b></td><td></td><td class="n"><b>{num(G[g][1],lang)}%</b></td></tr>' for g in (1, 2, 3, 4))
             + "</tbody></table>")
    cap = L("f1_cap") + ' <a href="https://doi.org/10.3389/fpos.2025.1679601">Amirova (2025)</a>'
    return fig_wrap(t("f1_k", lang), t("f1_t", lang), body, cap, lang, toggle, table)

def fig2(lang):
    L = lambda k: e(t(k, lang))
    cols = (f'<div class="vcols"><div class="vcol open"><span class="v">40+</span><div class="c" style="--h:{40/44*100:.1f}%"></div></div>'
            f'<div class="vcol warn"><span class="v">5</span><div class="c" style="--h:{5/44*100:.1f}%"></div></div>'
            f'<div class="vcol warn"><span class="v">2</span><div class="c" style="--h:{2/44*100:.1f}%"></div></div></div>'
            f'<div class="vcol-lbls"><span>{L("f2_a")}</span><span>{L("f2_b")}</span><span>{L("f2_c")}</span></div>')
    cap = (L("f2_cap") + ' <a href="https://en.tengrinews.kz/kazakhstan_news/Weakest-link-interior-ministry-names-main-cause-of-Kazakh-269405/">Tengrinews</a>; '
           '<a href="https://bes.media/amp/utechka-est-podrobnostey-net-kak-kazahstantsam-budut-soobschat-o-krazhe-dannyh/">BES.media</a>')
    return fig_wrap(t("f2_k", lang), t("f2_t", lang), cols, cap, lang)

EGDI = [(2003, .38661), (2004, .43437), (2005, .48125), (2008, .47430), (2010, .55782), (2012, .68438), (2014, .72827),
        (2016, .72499), (2018, .75970), (2020, .83750), (2022, .86280), (2024, .90093), (2026, .9363)]
def egdi_svg(lang, W, H, fs, every):
    L = lambda k: e(t(k, lang))
    ml, mr, mt, mb = 44, 24, 24, 34
    x = lambda yr: ml + (yr - 2003) / 23 * (W - ml - mr)
    y = lambda v: mt + (1.0 - v) / 0.7 * (H - mt - mb)
    g = ""
    for v in (0.3, 0.5, 0.7, 0.9):
        g += f'<line class="c-grid" x1="{ml}" x2="{W-mr}" y1="{y(v):.1f}" y2="{y(v):.1f}"/><text class="c-lbl" style="font-size:{fs}px" x="{ml-8}" y="{y(v)+4:.1f}" text-anchor="end">{num(v,lang,1)}</text>'
    yrs = [a for a, _ in EGDI] if every == 1 else [2003, 2010, 2018, 2026]
    for yr in yrs:
        g += f'<text class="c-lbl" style="font-size:{fs}px" x="{x(yr):.1f}" y="{H-10}" text-anchor="middle">{yr}</text>'
    pts = " ".join(f"{x(a):.1f},{y(b):.1f}" for a, b in EGDI)
    area = f"M{x(2003):.1f},{y(.3):.1f} L" + pts.replace(" ", " L") + f" L{x(2026):.1f},{y(.3):.1f}Z"
    dots = "".join(f'<circle class="c-dot fadein" style="--i:{i}" cx="{x(a):.1f}" cy="{y(b):.1f}" r="4"><title>{a}: {num(b,lang,4)}</title></circle>' for i, (a, b) in enumerate(EGDI))
    lx, ly = x(2026), y(.9363)
    lab = (f'<text class="c-val fadein" style="--i:14;font-size:{fs+1}px" x="{lx-8:.1f}" y="{ly-14:.1f}" text-anchor="end">{L("f3_rank")}</text>'
           )
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{L("f3_t")}">{g}<path class="c-area fadein" d="{area}"/>'
            f'<polyline class="c-line drawline" style="--len:1400" points="{pts}"/>{dots}{lab}</svg>')

def fig3(lang):
    L = lambda k: e(t(k, lang))
    chart = f'<div class="sv-wide">{egdi_svg(lang, 640, 300, 12, 1)}</div><div class="sv-narrow">{egdi_svg(lang, 360, 260, 12, 4)}</div>'
    fh = (f'<div class="fh-box"><span class="k" style="font:600 .72rem Inter;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)">{L("f3_fh_t")}</span>'
          f'<span class="big">23<small style="font-size:.5em;color:var(--muted)">/100</small></span><div class="meter"><i></i></div><p>{L("f3_fh")}</p>'
          f'<a href="https://freedomhouse.org/fr/node/8120" style="font-size:.8rem">Freedom House</a></div>')
    body = f'<div class="fig-split"><div>{chart}</div>{fh}</div>'
    table = (f'<table><thead><tr><th>{L("f3_th1")}</th><th class="n">{L("f3_th2")}</th></tr></thead><tbody>'
             + "".join(f'<tr><td>{a}</td><td class="n">{num(b,lang,4)}</td></tr>' for a, b in EGDI) + "</tbody></table>")
    cap = (L("f3_cap") + ' <a href="https://desapublications.un.org/sites/default/files/publications/2026-11/EGOV_TEC_26_EN_V15_WEB.pdf">UN DESA (2026)</a>; '
           '<a href="https://publicadministration.un.org/egovkb/en-us/Data/Country-Information/id/87-Kazakhstan/dataYear/2020">UN DESA country data</a>')
    return fig_wrap(t("f3_k", lang), t("f3_t", lang), body, cap, lang, table=table)

def fig_timeline(lang):
    L = lambda k: e(t(k, lang))
    items = [("tl1d", "tl1", "tl1p", "w", "tl1m", 2 / 16.6 * 100,
              "https://timesca.com/kazakhstan-data-leak-supreme-court/"),
             ("tl2d", "tl2", "tl2p", "", None, 0, "https://kazpravda.kz/n/sotrudnitsu-tsona-osudili-v-astane-za-lozhnye-dannye-v-sisteme/"),
             ("tl3d", "tl3", "tl3p", "w", "tl3m", 16.3 / 16.6 * 100,
              "https://en.tengrinews.kz/kazakhstan_news/personal-data-of-almost-all-kazakhstan-residents-leaked-into-268316"),
             ("tl4d", "tl4", "tl4p", "s", None, 0, "https://www.lada.kz/kazakhstan-news/154341-kto-za-vami-podsmatrivaet-kazakhstantsy-uvidiat-vse-skrytye-zaprosy-k-lichnym-dannym-cherez-egov.html"),
             ("tl5d", "tl5", "tl5p", "w", "tl5m", 100, "https://timesca.com/kazakhstan-data-leak-supreme-court/")]
    li = ""
    for d, h, p, c, m, w, u in items:
        mag = f'<div class="mag" style="--w:{w:.0f}%"></div><small>{L(m)}</small>' if m else ""
        li += f'<li class="{c}"><time>{L(d)}</time><b>{L(h)}</b><p>{L(p)} <a class="src" href="{u}">[{L("source")}]</a></p>{mag}</li>'
    return fig_wrap(t("tl_k", lang), t("tl_t", lang), f'<ol class="tline">{li}</ol>', "", lang)

def fig_survey(lang):
    L = lambda k: e(t(k, lang))
    body = ('<div class="bars">'
            f'<div class="bar warn tall"><div class="lb">{L("sv1")}</div><div class="tr"><div class="fl" style="--w:53%"></div><span class="vl" style="--w:53%">~53%</span></div></div>'
            f'<div class="bar g1 tall" style="--i:1"><div class="lb">{L("sv2")}</div><div class="tr"><div class="fl" style="--w:18%"></div><span class="vl" style="--w:18%">18%</span></div></div></div>')
    cap = L("sv_cap") + ' <a href="https://egov.kz/cms/en/news/Service_available">egov.kz</a>'
    return fig_wrap(t("sv_k", lang), t("sv_t", lang), body, cap, lang)

def fig_venn(lang):
    L = lambda k: e(t(k, lang))
    svg = f'''<svg viewBox="0 0 520 340" role="img" aria-label="{L("vn_t")}" style="max-width:560px;margin-inline:auto">
<rect x="6" y="6" width="508" height="328" rx="16" fill="none" stroke="var(--line-2)" stroke-dasharray="5 5"/>
<text class="c-lbl" x="24" y="30">{L("vn_bg")}</text>
<circle class="fadein" style="--i:0" cx="200" cy="140" r="92" fill="var(--g1)" fill-opacity=".16" stroke="var(--g1)" stroke-width="1.5"/>
<circle class="fadein" style="--i:2" cx="320" cy="140" r="92" fill="var(--g2)" fill-opacity=".16" stroke="var(--g2)" stroke-width="1.5"/>
<circle class="fadein" style="--i:4" cx="260" cy="236" r="92" fill="var(--g3)" fill-opacity=".2" stroke="var(--g3)" stroke-width="1.5"/>
<text class="c-lbl2 fadein" style="--i:1;font-weight:600;fill:var(--ink)" x="160" y="118" text-anchor="middle">{L("vn_a")}</text>
<text class="c-lbl fadein" style="--i:1" x="160" y="136" text-anchor="middle">{L("vn_an")}</text>
<text class="c-lbl2 fadein" style="--i:3;font-weight:600;fill:var(--ink)" x="360" y="118" text-anchor="middle">{L("vn_b")}</text>
<text class="c-lbl fadein" style="--i:3" x="360" y="136" text-anchor="middle">{L("vn_bn")}</text>
<text class="c-lbl2 fadein" style="--i:5;font-weight:600;fill:var(--ink)" x="260" y="284" text-anchor="middle">{L("vn_c")}</text>
<text class="c-lbl fadein" style="--i:5" x="260" y="302" text-anchor="middle">{L("vn_cn")}</text>
<circle class="fadein a-blink" style="--i:7" cx="260" cy="178" r="7" fill="var(--warn)"/>
<text class="c-val fadein" style="--i:8;font-size:12px" x="260" y="200" text-anchor="middle">{L("vn_gap")}</text>
<text class="c-val fadein" style="--i:8;font-size:12px" x="260" y="215" text-anchor="middle">{L("vn_gap2")}</text>
</svg>'''
    return fig_wrap(t("vn_k", lang), t("vn_t", lang), svg, L("vn_cap"), lang)

def fig_energy(lang):
    L = lambda k: e(t(k, lang))
    sc = lambda v: f"{v/30*100:.2f}%"
    ticks = "".join(f'<span class="tick" style="left:{sc(v)}">{v} t</span>' for v in (0, 10, 20, 30))
    body = (f'<div class="range" style="--a:{sc(6.5)};--b:{sc(24.2)};--x:{sc(13.94)}"><div class="axis"></div><div class="band"></div>'
            f'<div class="mk"><span>{L("en_mk")}</span></div>{ticks}</div>'
            f'<p style="margin:0;font-weight:600;color:var(--accent)">{L("en_band")}</p>')
    return fig_wrap(t("en_k", lang), t("en_t", lang), body, L("en_cap"), lang)

def calc(lang):
    L = lambda k: e(t(k, lang))
    return f'''<figure class="fig"><div class="fig-head"><div><span class="k">{L("calc_k")}</span><h4>{L("calc_t")}</h4></div></div>
<div class="calc"><div>
<div class="f"><label for="u-{lang}">{L("calc_users")}: <output data-o="users">1.0</output></label><input id="u-{lang}" name="users" type="range" min="0.1" max="5" step="0.1" value="1"></div>
<div class="f"><label for="r-{lang}">{L("calc_reqs")}: <output data-o="reqs">5</output></label><input id="r-{lang}" name="reqs" type="range" min="1" max="20" step="1" value="5"></div>
<div class="f"><label>{L("calc_wh")}</label><div class="opts">
<button type="button" data-wh="0.18" aria-pressed="false">{L("calc_low")}</button>
<button type="button" data-wh="0.34" aria-pressed="true">{L("calc_mid")}</button>
<button type="button" data-wh="0.67" aria-pressed="false">{L("calc_high")}</button></div></div>
<p class="muted" style="font-size:.86rem;margin:0">{L("calc_grid")}</p>
</div><div class="res" aria-live="polite">
<div class="row"><span>{L("calc_calls")}</span><b data-o="calls"></b></div>
<div class="row"><span>{L("calc_mwh")}</span><b data-o="mwh"></b></div>
<div class="row"><span>{L("calc_t2")}</span><b class="big" data-o="t"></b></div>
<div class="row"><span>{L("calc_p")}</span><b data-o="p"></b></div>
<div class="people" aria-hidden="true"></div>
</div></div><figcaption>{L("calc_note")}</figcaption></figure>'''

def gov(lang):
    L = lambda k: e(t(k, lang))
    ic = ["lock", "users", "scale", "coins", "chart", "book"]
    ring = "".join(f'<div class="rv" data-d="{i%3+1}">{icon(ic[i])}<b>{L("g"+str(i+1))}</b>{L("g"+str(i+1)+"d")}</div>' for i in range(6))
    return (f'<div class="gov"><div class="core rv">{icon("building")}<div><b>{L("g_core")}</b><span>{L("g_cored")}</span></div></div>'
            f'<div class="link">{L("g_link")}</div><div class="ring">{ring}</div></div>')

def stats(lang):
    L = lambda k: e(t(k, lang))
    items = [('data-count="16.3" data-dec="1" data-suf="' + e(t("st1_suf", lang)) + '"', num(16.3, lang, 1) + t("st1_suf", lang), "st1",
              "https://en.tengrinews.kz/kazakhstan_news/personal-data-of-almost-all-kazakhstan-residents-leaked-into-268316", "Tengrinews"),
             ('data-count="40" data-suf="+"', "40+", "st2", "data.html#gap", t("f2_k", lang)),
             ('data-count="39" data-suf="%"', "39%", "st3", "data.html#figure-1", t("f1_k", lang)),
             ('data-count="53" data-suf="%"', "53%", "st4", "https://egov.kz/cms/en/news/Service_available", "egov.kz")]
    out = '<div class="stats">'
    for i, (attrs, final, k, u, s) in enumerate(items):
        out += f'<div class="stat rv" data-d="{i}"><span class="num" {attrs}>{e(final)}</span><p>{L(k)}</p><a href="{u}">{e(s)}</a></div>'
    return out + "</div>"

# ---------------------------------------------------------------- demo
def demo(lang):
    L = lambda k: e(t(k, lang))
    steps = "".join(f'<li><button type="button"><span class="n">{i+1}</span><span><b>{L("d_s"+str(i+1))}</b><span class="d">{L("d_s"+str(i+1)+"d")}</span></span></button></li>' for i in range(6))
    safe = f'<p class="safe">{icon("shield")}{L("d_safe")}</p>'
    def row(t1, meta, date, cls=""):
        return f'<div class="row {cls}"><div class="meta"><span>{meta}</span><span>{date}</span></div><b>{t1}</b></div>'
    s1 = (f'<div class="ph-screen"><h5>{L("d_p1h")}</h5><p>{L("d_p1p")}</p>'
          f'<div class="row ok"><b>{L("d_p1r")}</b>{L("d_p1rm")}</div><p style="margin-top:14px;font-weight:600;color:var(--ink)">{L("d_p1q")}</p>'
          f'<div class="row"><b>{L("d_p1o1")}</b></div><div class="row"><b>{L("d_p1o2")}</b></div>{safe}</div>')
    s2 = (f'<div class="ph-screen"><h5>{L("d_p2h")}</h5><p>{L("d_p2p")}</p>'
          + row(L("l1_r1"), L("l1_r1m"), L("l1_r1d")) + row(L("l1_r2"), L("l1_r2m"), L("l1_r2d")) + row(L("l1_r3"), L("l1_r3m"), L("l1_r3d"))
          + f'<div class="row exempt"><div class="meta"><span>{L("l1_r4m")}</span><span>{L("l1_r4d")}</span></div><b>{L("l1_r4")}</b>'
          f'<span style="display:block;margin:4px 0;color:var(--ink-2)">{L("d_p2e")}</span><span style="color:var(--accent);font-weight:600">{L("d_p2a")}</span></div>{safe}</div>')
    s3 = (f'<div class="ph-screen"><h5>{L("d_p3h")}</h5><p>{L("d_p3p")}</p><p style="font-weight:600;color:var(--ink);margin-bottom:6px">{L("d_p3f")}</p>'
          f'<div class="cmp"><div><small>{L("l2_a")}</small>{L("d_p3v1")}</div><div class="bad"><small>{L("l2_b")}</small>{L("d_p3v2")}</div></div>'
          f'<div class="row ok">{L("d_p3ok")}</div><p><span class="tag plain">{L("l2_rule")}</span></p><p>{L("d_p3n")}</p></div>')
    s4 = (f'<div class="ph-screen"><h5>{L("d_p4h")}</h5><div class="draft"><div class="who"><span>{L("d_p4who")}</span><span>{L("d_p4chk")}</span></div>'
          f'<p style="margin:0 0 8px">{L("d_p4x")}</p><p style="margin:0 0 6px;color:var(--muted)">{L("d_p4to")}</p><p style="margin:0;color:var(--ink)">{L("d_p4l")}</p></div>'
          f'<div style="display:flex;gap:6px;margin:10px 0"><span class="btn btn-ghost" style="padding:9px 12px;font-size:.8rem">{L("d_p4b1")}</span>'
          f'<span class="btn btn-primary" style="padding:9px 12px;font-size:.8rem">{L("d_p4b2")}</span></div><p>{L("d_p4n")}</p></div>')
    s5 = (f'<div class="ph-screen"><h5>{L("d_p5h")}</h5><ul class="tl">'
          f'<li class="on"><b>{L("d_p5a")}</b><br><small>{L("d_p5ad")}</small></li>'
          f'<li class="on"><b>{L("d_p5b")}</b><br><small>{L("d_p5bd")}</small></li>'
          f'<li class="w"><b>{L("d_p5c")}</b><br><small>{L("d_p5cd")}</small></li>'
          f'<li class="on"><b>{L("d_p5d")}</b><br><small>{L("d_p5dd")}</small></li>'
          f'<li class="on"><b>{L("d_p5e")}</b><br><small>{L("d_p5ed")}</small></li></ul><p>{L("d_p5n")}</p></div>')
    s6 = (f'<div class="ph-screen"><h5>{L("d_p6h")}</h5><p>{L("d_p6p")}</p><div class="kpi">'
          + "".join(f'<div><b>—</b><small>{L("d_p6k"+str(i))}</small></div>' for i in range(1, 5))
          + f'</div><p style="margin-top:10px">{L("d_p6n")}</p></div>')
    return f'''<div class="demo">
<div><ol class="demo-steps">{steps}</ol><p class="demo-flag">{icon("info")}<span>{L("d_flag")}</span></p></div>
<div class="phone rv"><div class="phone-in ph">
<div class="ph-top"><span>{L("d_time")}</span><span>eGov · Kuä</span></div>
<div class="ph-bar">{LOGO.replace('<svg ', '<svg width="24" height="24" ')}<b>Kuä</b><span class="tag warn">{L("illus")}</span></div>
<div class="ph-body">{s1}{s2}{s3}{s4}{s5}{s6}</div>
<div class="ph-nav"><button type="button" data-prev>{L("d_back")}</button><button type="button" class="primary" data-next><span data-notlast>{L("d_next")}</span><span data-last hidden>{L("d_again")}</span></button></div>
<p class="vh" aria-live="polite"></p>
</div></div></div>'''

COMP = {"fig1": fig1, "fig2": fig2, "fig3": fig3, "timeline": fig_timeline, "survey": fig_survey, "venn": fig_venn,
        "energy": fig_energy, "calc": calc, "gov": gov, "stats": stats, "demo": demo, "hero": art_hero}
