"""Shared helpers + page templates for the Gwadar Digital static site generator."""
import html as _html
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://www.gwadar.digital"
BRAND = "Gwadar Digital Agency"
PHONE = "+92-300-9019970"
TEL = "+923009019970"
WA = "https://wa.me/923009019970"
EMAIL = "gwadar.digital@gmail.com"
ADDRESS = "K-39 Phase 1, Phase 1 New Town Housing, Gwadar"
MAPS_Q = "https://www.google.com/maps/search/?api=1&query=Gwadar+Digital+Agency+K-39+Phase+1+New+Town+Housing+Gwadar"
MAPS_EMBED = "https://www.google.com/maps?q=K-39+Phase+1+New+Town+Housing+Gwadar&output=embed"
TODAY = "2026-11-11"

PAGES = []  # registry for sitemap: (path, priority)


def _read(name):
    with open(os.path.join(ROOT, "tools", "partials", name), encoding="utf-8") as f:
        return f.read()


SPRITE = _read("sprite.html")
HEADER = _read("header.html")
FOOTER = _read("footer.html")
BOTTOM = _read("bottom.html")
LD_BUSINESS = _read("ld-business.html")
HOME_MAIN = _read("home-main.html")

esc = _html.escape


def icon(i, cls=""):
    return '<svg class="ico %s" aria-hidden="true"><use href="#%s"/></svg>' % (cls, i)


ICON_CYCLE = ["i-chart", "i-search", "i-layout", "i-gear", "i-rocket", "i-users", "i-trend", "i-compass",
              "i-clipboard", "i-nodes", "i-mail", "i-monitor"]


def trim(text, n=158):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= n:
        return text
    cut = text[:n].rsplit(" ", 1)[0]
    return cut.rstrip(",;:") + "..."


# ---------------------------------------------------------------- sections
def sec(kind, inner, id=None, cls=""):
    idattr = ' id="%s"' % id if id else ""
    return '<section class="sec sec-%s %s"%s><div class="container">%s</div></section>' % (kind, cls, idattr, inner)


def sec_head(eyebrow, color, h2, p="", center=False):
    return ('<div class="sec-head%s"><span class="eyebrow p-%s">%s</span><h2>%s</h2>%s</div>'
            % (" is-center" if center else "", color, eyebrow, h2, ("<p>%s</p>" % p) if p else ""))


def cards(items, start=0):
    out = []
    for n, (t, d) in enumerate(items):
        out.append('<article class="fcard"><span class="fico c%d">%s</span><h3>%s</h3><p>%s</p></article>'
                   % (n % 4, icon(ICON_CYCLE[(n + start) % len(ICON_CYCLE)]), t, d))
    return '<div class="fgrid%s">%s</div>' % (" two" if len(items) in (2, 4) else "", "".join(out))


def steps(items):
    li = "".join('<li><span class="pno">%02d</span><h3>%s</h3><p>%s</p></li>' % (i + 1, t, d)
                 for i, (t, d) in enumerate(items))
    return '<ol class="proc">%s</ol>' % li


def rel_cards(items, root):
    """items: (title, desc, href, icon_id, image or None)"""
    out = []
    for t, d, href, ic, img in items:
        media = ('<span class="rc-img" style="background-image:url(%s%s)"></span>' % (root, img)) if img else \
            '<span class="rc-ico">%s</span>' % icon(ic)
        out.append('<a class="rcard" href="%s%s">%s<span class="rc-body"><strong>%s</strong><span>%s</span></span>'
                   '<span class="rc-go" aria-hidden="true">%s</span></a>'
                   % (root, href, media, t, d, icon("i-arrow-up-right")))
    return '<div class="rgrid%s">%s</div>' % (" two" if len(items) in (2, 4) else "", "".join(out))


def faq_section(faqs, title="Frequently asked questions", eyebrow="FAQs", pid="p"):
    items = ""
    for i, (q, a) in enumerate(faqs):
        items += ('<div class="faq-item"><h3><button type="button" class="faq-q" id="%s-q%d" aria-expanded="false" '
                  'aria-controls="%s-a%d"><span>%s</span>%s</button></h3><div class="faq-a" id="%s-a%d" role="region" '
                  'aria-labelledby="%s-q%d"><div><p>%s</p></div></div></div>'
                  % (pid, i, pid, i, esc(q), icon("i-chevron-right"), pid, i, pid, i, esc(a)))
    return ('<section class="faq"><div class="container faq-grid"><div class="faq-title"><span class="eyebrow p-cyan">%s</span>'
            '<h2>%s</h2></div><div class="faq-list">%s</div></div></section>' % (eyebrow, title, items))


def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def cta_section(root, h2="Ready to grow in Gwadar?", p=None, btn="Book a free strategy call"):
    p = p or ("Tell us about your business and goals. In a free 30-minute call we will map out what to do first, "
              "what it should cost and what results to expect.")
    return ('<section class="sec sec-white cta2"><div class="container"><div class="cta-card"><div><h2>%s</h2><p>%s</p></div>'
            '<div class="cta-actions"><a class="btn btn-orange btn-lg" href="%scontact.html">%s</a>'
            '<a class="btn-ghost" href="%s" rel="noopener">%s WhatsApp us</a></div></div></div></section>'
            % (h2, p, root, btn, WA, icon("i-whatsapp")))


def crumbs_html(crumbs, root):
    items = []
    for i, (name, path) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            items.append('<li aria-current="page">%s</li>' % esc(name))
        else:
            items.append('<li><a href="%s%s">%s</a></li>' % (root, path, esc(name)))
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>%s</ol></nav>' % "".join(items)


def crumbs_ld(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + p}
                                for i, (n, p) in enumerate(crumbs)]}


def hero(root, crumbs, eyebrow, color, h1, lead, img=None, vis_icon="i-chart", vis_title="", trust=True, ctas=True,
         stat=None, alt="", novis=False, extra=""):
    if novis:
        visual = ""
    elif img:
        portrait = " is-portrait" if "assets/clients/" in img else ""
        visual = '<div class="ph-visual has-img%s"><img src="%s%s" alt="%s" width="1200" height="800" loading="eager"></div>' % (
            portrait, root, img, esc(alt or h1))
    elif stat:
        visual = '<div class="ph-visual stat-vis g-%s"><b>%s</b><span>%s</span></div>' % (color, stat[0], stat[1])
    else:
        visual = ('<div class="ph-visual art-vis g-%s">%s<strong>%s</strong></div>' % (color, icon(vis_icon), vis_title))
    cta = ""
    if ctas:
        cta = ('<div class="ph-cta"><a class="btn btn-orange btn-lg" href="%scontact.html">Get a free quote</a>'
               '<a class="btn-ghost" href="tel:%s">%s Call %s</a></div>' % (root, TEL, icon("i-phone"), PHONE))
    tr = ""
    if trust:
        tr = ('<ul class="ph-trust"><li>%s Local team in Gwadar</li><li>%s Free 30-minute strategy call</li>'
              '<li>%s Clear monthly reporting</li></ul>' % (icon("i-check"), icon("i-check"), icon("i-check")))
    return ('<section class="ph"><div class="hero-glow" aria-hidden="true"></div><div class="container ph-grid%s"><div class="ph-text">%s'
            '<span class="eyebrow p-%s">%s</span><h1>%s</h1><p class="ph-lead">%s</p>%s%s%s</div>%s</div></section>'
            % (" one" if novis else "", crumbs_html(crumbs, root), color, eyebrow, h1, lead, extra, cta, tr, visual))


AREAS = ["Gwadar City", "New Town Housing", "Marine Drive", "Gwadar Port area", "Pasni", "Jiwani", "Ormara"]


def local_section(h2, text, root, eyebrow="Local to Gwadar"):
    chips = "".join("<span>%s</span>" % a for a in AREAS)
    inner = ('<div class="local-grid"><div><span class="eyebrow p-orange">%s</span><h2>%s</h2><p>%s</p>'
             '<div class="area-chips" aria-label="Areas we serve">%s</div></div>'
             '<aside class="visit-card"><h3>Visit or call us</h3><ul><li>%s<span>%s</span></li><li>%s<a href="tel:%s">%s</a></li>'
             '<li>%s<a href="mailto:%s">%s</a></li></ul><a class="btn btn-orange" href="%scontact.html">Contact us</a></aside></div>'
             % (eyebrow, h2, text, chips, icon("i-pin"), ADDRESS, icon("i-phone"), TEL, PHONE, icon("i-mail"), EMAIL, EMAIL, root))
    return sec("dark", inner)


# ---------------------------------------------------------------- page shell
NAV_BTN = {"services": "button", "work": "button", "industries": "button", "about": "button",
           "revenue": "link", "insights": "link"}


def render_page(path, title, desc, main, crumbs=None, section=None, ld=None, scripts=None, home=False,
                business_ld=False, og_image="assets/logo-full.png", noindex=False, priority="0.7"):
    depth = path.count("/")
    root = "../" * depth
    canonical = SITE + "/" + ("" if path == "index.html" else path)
    cta = "#contact" if home else root + "contact.html"

    header = HEADER
    if section in NAV_BTN:
        if NAV_BTN[section] == "button":
            header = header.replace('class="nav-btn" type="button" data-panel="%s"' % section,
                                    'class="nav-btn is-current" type="button" data-panel="%s"' % section, 1)
        else:
            header = header.replace('<a class="nav-btn" href="{{root}}%s.html">' % section,
                                    '<a class="nav-btn is-current" href="{{root}}%s.html" aria-current="page">' % section, 1)
    bottom = BOTTOM.replace("{{home_active}}", " is-active" if home else "").replace(
        "{{home_current}}", ' aria-current="page"' if home else "")

    def fill(t):
        return t.replace("{{root}}", root).replace("{{cta}}", cta)

    lds = []
    if business_ld:
        lds.append(LD_BUSINESS.strip())
    if crumbs and not home:
        lds.append('<script type="application/ld+json">%s</script>' % json.dumps(crumbs_ld(crumbs), ensure_ascii=False))
    for item in (ld or []):
        lds.append('<script type="application/ld+json">%s</script>' % json.dumps(item, ensure_ascii=False))

    scripts = scripts or []
    script_tags = "".join('<script src="%sjs/%s"></script>\n' % (root, s) for s in scripts + ["main.js"])
    desc = trim(desc)
    out = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>%(title)s</title>
  <meta name="description" content="%(desc)s">
  <meta name="theme-color" content="#070a2e">
  <meta name="robots" content="%(robots)s">
  <link rel="canonical" href="%(canonical)s">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="%(brand)s">
  <meta property="og:title" content="%(title)s">
  <meta property="og:description" content="%(desc)s">
  <meta property="og:url" content="%(canonical)s">
  <meta property="og:image" content="%(site)s/%(og)s">
  <meta property="og:locale" content="en_PK">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" type="image/png" href="%(root)sassets/logo-mark.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="%(root)scss/style.css">
  <link rel="stylesheet" href="%(root)scss/pages.css">
  %(lds)s
</head>
<body>

%(sprite)s<a class="skip-link" href="#main">Skip to content</a>

%(header)s
%(main)s

%(footer)s
%(bottom)s%(scripts)s</body>
</html>
""" % dict(title=esc(title), desc=esc(desc), robots="noindex, follow" if noindex else "index, follow, max-image-preview:large",
           canonical=canonical, brand=BRAND, site=SITE, og=og_image, root=root, lds="\n  ".join(lds),
           sprite=SPRITE, header=fill(header), main=fill(main), footer=fill(FOOTER), bottom=fill(bottom),
           scripts=script_tags)
    out = out.replace("{{root}}", root)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(out)
    if not noindex:
        PAGES.append((path, priority))
    return out


# ---------------------------------------------------------------- generic detail page (service/industry/solution)
STEPS = {
    "service": lambda n: [
        ("Discover", "We learn your business, your customers and your competitors in Gwadar, then agree what success looks like for %s." % n),
        ("Plan", "We turn that into a clear plan with priorities, timelines and the numbers we will report on, so you know what happens each month."),
        ("Launch", "We build and publish the work, set up tracking and check everything before it goes live."),
        ("Improve", "We review results every month, keep what works, fix what does not and share a plain-language report."),
    ],
    "industry": lambda n: [
        ("Understand", "We study how %s customers in Gwadar search, compare and decide, and what makes them trust a business." % n.lower()),
        ("Plan", "We choose the channels and offers that fit your budget, and set targets you can measure."),
        ("Launch", "We build the website, listings and campaigns, with tracking on every call, form and WhatsApp click."),
        ("Improve", "We read the results every month and move budget to what brings real enquiries."),
    ],
    "solution": lambda n: [
        ("Diagnose", "We look at where %s is leaking today: traffic, enquiries, follow-up and sales." % n.lower()),
        ("Design", "We design a simple plan across the right channels, with clear owners and targets."),
        ("Deliver", "We build, launch and connect the tools so everything is tracked in one place."),
        ("Grow", "We review monthly, fix bottlenecks and scale the parts that perform."),
    ],
}


def detail_page(p):
    """p: dict describing a service / industry / solution page. Returns html and writes file."""
    path = p["path"]
    root = "../" * path.count("/")
    kind = p.get("kind", "service")
    name = p["name"]
    color = p.get("color", "purple")
    crumbs = p["crumbs"]

    related = rel_cards(p.get("related", []), root) if p.get("related") else ""

    parts = [hero(root, crumbs, p["eyebrow"], color, p["h1"], p["lead"], img=p.get("img"), vis_icon=p.get("icon", "i-chart"),
                  vis_title=name, alt=p.get("alt", ""))]

    facts = "".join("<li><span>%s</span><strong>%s</strong></li>" % (k, v) for k, v in p["facts"])
    intro = "".join("<p>%s</p>" % t for t in p["intro"])
    parts.append(sec("light", '<div class="ov-grid"><div class="prose"><span class="eyebrow p-%s">Overview</span><h2>%s</h2>%s</div>'
                              '<aside class="glance"><h3>At a glance</h3><ul>%s</ul><a class="btn btn-orange" href="%scontact.html">Get a free quote</a></aside></div>'
                     % (color, p.get("overview_h2", "%s in Gwadar" % name), intro, facts, root)))

    parts.append(sec("dark", sec_head(p.get("items_eyebrow", "What is included"), color, p.get("items_h2", "What you get with %s" % name),
                                      p.get("items_p", "")) + cards(p["items"], start=p.get("icon_start", 0))))

    if p.get("help"):
        rows = "".join('<a class="hrow" href="%s%s"><span class="hico">%s</span><span><strong>%s</strong><em>%s</em></span>%s</a>'
                       % (root, href, icon(ic), t, d, icon("i-chevron-right")) for href, ic, t, d in p["help"])
        parts.append(sec("light", sec_head("How we help", color, p.get("help_h2", "Services that work best for %s" % name.lower())) +
                         '<div class="hlist">%s</div>' % rows))
        step_kind = "soft"
    else:
        step_kind = "light"

    parts.append(sec(step_kind, sec_head("How we work", "cyan", "A simple process, no surprises") + steps(STEPS[kind](name))))
    parts.append(local_section(p.get("local_h2", "%s in Gwadar: why a local team matters" % name), p["local"], root))
    parts.append(faq_section(p["faqs"], pid="f"))
    if related:
        parts.append(sec("white", sec_head(p.get("related_eyebrow", "Related"), "orange", p.get("related_h2", "You may also need")) + related))
    parts.append(cta_section(root))

    ld = [faq_ld(p["faqs"])]
    if kind == "service":
        ld.append({"@context": "https://schema.org", "@type": "Service", "name": name + " in Gwadar", "serviceType": name,
                   "description": p["lead"], "provider": {"@type": "ProfessionalService", "name": BRAND, "url": SITE + "/"},
                   "areaServed": {"@type": "City", "name": "Gwadar"}, "url": SITE + "/" + path})
    main = '<main id="main">\n%s\n</main>' % "\n".join(parts)
    render_page(path, p["title"], p["lead"], main, crumbs=crumbs, section=p.get("section"), ld=ld, priority=p.get("priority", "0.8"),
                og_image=(p["img"] if p.get("img") else "assets/logo-full.png"))


def hub_page(p):
    """Category / index pages: hero, intro, grid of child cards, optional items, faq, cta."""
    path = p["path"]
    root = "../" * path.count("/")
    color = p.get("color", "purple")
    parts = [hero(root, p["crumbs"], p["eyebrow"], color, p["h1"], p["lead"], img=p.get("img"), vis_icon=p.get("icon", "i-grid"),
                  vis_title=p.get("name", ""), trust=p.get("trust", True))]
    intro = "".join("<p>%s</p>" % t for t in p["intro"])
    parts.append(sec("light", '<div class="hub-intro"><div class="prose"><span class="eyebrow p-%s">Overview</span><h2>%s</h2>%s</div></div>'
                     % (color, p["intro_h2"], intro)))
    parts.append(sec("dark", sec_head(p.get("grid_eyebrow", "Explore"), color, p["grid_h2"], p.get("grid_p", "")) +
                     rel_cards(p["children"], root), cls="hub-grid"))
    if p.get("items"):
        parts.append(sec("light", sec_head("Why choose us", "cyan", p.get("items_h2", "Why businesses in Gwadar choose us")) + cards(p["items"])))
    if p.get("faqs"):
        parts.append(faq_section(p["faqs"], pid="h"))
    parts.append(cta_section(root))
    ld = [faq_ld(p["faqs"])] if p.get("faqs") else []
    main = '<main id="main">\n%s\n</main>' % "\n".join(parts)
    render_page(path, p["title"], p["lead"], main, crumbs=p["crumbs"], section=p.get("section"), ld=ld, priority=p.get("priority", "0.8"))
