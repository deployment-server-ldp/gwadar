#!/usr/bin/env python3
"""Build the whole Gwadar Digital Agency static site.
Usage:  python3 tools/build.py
Edit content in tools/content/*.py and shared header/footer in tools/partials/*.html, then re-run.
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib
from lib import *
from content import services, industries, work, misc, blog


def build_home():
    render_page("index.html", "Gwadar Digital Agency | Digital Marketing Agency in Gwadar",
                "Gwadar Digital Agency is a full-service digital marketing agency in Gwadar. SEO, social media, PPC, websites, branding and CRM under one roof.",
                HOME_MAIN, home=True, business_ld=True,
                scripts=["clients.js", "services.js", "partners.js", "team.js", "industries.js"], priority="1.0")


def write_sitemap():
    rows = []
    for path, pr in sorted(set(PAGES), key=lambda x: (-float(x[1]), x[0])):
        loc = SITE + "/" + ("" if path == "index.html" else path)
        rows.append("  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (loc, TODAY, pr))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % "\n".join(rows))
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)


def check_links():
    bad = []
    pages = [p for p, _ in PAGES] + ["404.html"]
    for path in pages:
        t = open(os.path.join(ROOT, path), encoding="utf-8").read()
        base = os.path.dirname(os.path.join(ROOT, path))
        for m in re.finditer(r'(?:href|src)="([^"#]+)(?:#[^"]*)?"', t):
            u = m.group(1)
            if re.match(r"(https?:|tel:|mailto:|data:|//)", u) or "{{" in u:
                continue
            target = os.path.normpath(os.path.join(ROOT, u.lstrip("/")) if u.startswith("/") else os.path.join(base, u))
            if u in ("/",):
                continue
            if not os.path.exists(target):
                bad.append((path, u))
    return bad


if __name__ == "__main__":
    build_home()
    services.build()
    industries.build()
    work.build()
    work.build_revenue()
    blog.build()
    misc.build_about(); misc.build_team(); misc.build_careers(); misc.build_contact()
    misc.build_assessment(); misc.build_legal(); misc.build_404()
    write_sitemap()
    bad = check_links()
    print("pages:", len(PAGES), "| broken links:", len(bad))
    for b in bad[:40]:
        print("  BROKEN", b)
