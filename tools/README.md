# Site generator

All HTML pages are generated. Do not edit the .html files by hand: your changes will be overwritten.

    python3 tools/build.py

- Page text: `tools/content/*.py` (services, industries, work, blog, misc)
- Header, mega menu, footer, mobile bar: `tools/partials/*.html`
- Templates and section helpers: `tools/lib.py`
- Styles: `css/style.css` (global) and `css/pages.css` (inner pages)
- Sitemap and robots.txt are regenerated on every build.
