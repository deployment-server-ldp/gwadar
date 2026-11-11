"""Our Work: category pages + case studies. Revenue pages."""
from lib import *
from content.services import SV, pairs

# n = case-study number (1-4 are the featured ones in the header menu)
CASES = [
 dict(n=1, name="Joaquin Painting", img="assets/clients/joaquin-painting.webp", industry="Home services", stat="290%", label="Increase in conversions",
      services=["website-design", "seo-aeo", "ppc-sem"], goal="Turn more website visitors into quote requests.",
      actions=["Rebuilt key pages around the services customers ask for most.", "Added clear calls to action and quote forms on every page.", "Tracked calls and form fills to see which pages and campaigns brought customers."]),
 dict(n=2, name="Silver Hammer", img="assets/clients/silver-hammer.webp", industry="Property", stat="40+", label="Listings monthly sold",
      services=["seo-aeo", "ppc-sem", "video-photography"], goal="Reach more qualified buyers and sellers online.",
      actions=["Built property pages and campaigns aimed at buyers searching for homes.", "Added photo and video content that shows each property at its best.", "Tracked enquiries by source to put budget behind what worked."]),
 dict(n=3, name="Alamo", img="assets/clients/alamo.webp", industry="Automotive and rental", stat="190+", label="Online bookings monthly",
      services=["website-design", "seo-aeo", "ppc-sem"], goal="Increase direct online bookings.",
      actions=["Simplified the booking path so customers could reserve in fewer steps.", "Targeted high-intent searches for vehicle rentals with search ads.", "Measured every booking back to its channel."]),
 dict(n=4, name="Tyris Tile and Renovations", img="assets/clients/tyris-tile-renovations.webp", industry="Construction and renovation", stat="172%", label="Increase in organic website traffic",
      services=["seo-aeo", "wordpress", "video-photography"], goal="Grow organic visibility for renovation services.",
      actions=["Created service pages for each type of work the company offers.", "Fixed technical issues so search engines could crawl the site properly.", "Added project photography to build trust with visitors."]),
 dict(n=5, name="Bio-X Weight Loss Center", img="assets/clients/bio-x-weight-loss.webp", industry="Healthcare", stat="+471%", label="Increase in organic leads",
      services=["seo-aeo", "wordpress", "crm-consulting-development"], goal="Bring more enquiries from people searching for weight-loss support.",
      actions=["Structured the website around the treatments patients search for.", "Published helpful content that answers common patient questions.", "Tracked each enquiry source so budget followed what worked."]),
 dict(n=6, name="Junk Patrol", img="assets/clients/junk-patrol.webp", industry="Home services", stat="+179%", label="Organic traffic value",
      services=["seo-aeo", "wordpress"], goal="Win more local searches for junk removal services.",
      actions=["Optimised service and location pages for local searches.", "Improved page speed and mobile usability.", "Strengthened local listings and consistent business details."]),
 dict(n=7, name="Victor Super Premium Pet Food", img="assets/clients/victor.webp", industry="Retail and ecommerce", stat="134%", label="Increase in engagement rate",
      services=["social-media", "ad-creative"], goal="Grow an engaged community of pet owners.",
      actions=["Planned a content calendar around what pet owners care about.", "Designed on-brand creative for posts and ads.", "Reviewed engagement monthly and doubled down on top-performing formats."]),
 dict(n=8, name="Sharkey's Cuts for Kids", img="assets/clients/sharkeys-cuts-for-kids.webp", industry="Kids and family services", stat="4.8x", label="Return on ad spend",
      services=["ppc-sem", "social-media", "ad-creative"], goal="Fill appointment books profitably through paid media.",
      actions=["Built campaigns around parents searching for kids' haircuts nearby.", "Tested creative and offers to find what parents responded to.", "Tracked bookings so spend was tied to revenue."]),
 dict(n=9, name="Bali Family Dental Care", img="assets/clients/bali-family-dental-care.webp", industry="Dental", stat="+811%", label="Social media growth",
      services=["social-media", "video-photography"], goal="Build a trusted local brand on social media.",
      actions=["Shared real team and patient-education content.", "Produced short videos that made the clinic feel friendly and approachable.", "Responded to comments and messages promptly."]),
 dict(n=10, name="Aruni Restoran & Bar", img="assets/clients/aruni-restoran-bar.webp", industry="Hospitality", stat="5.11x", label="ROAS on Meta ads",
      services=["ppc-sem", "social-media", "video-photography"], goal="Drive reservations and visits from Meta ads.",
      actions=["Created appetising photos and short videos of the menu and venue.", "Targeted diners near the restaurant with offer-led ads.", "Measured reservations and visits against ad spend."]),
 dict(n=11, name="Rüyam Gemüse Kebab", img="assets/clients/ruyam-gemuse-kebab.webp", industry="Hospitality", stat="+178%", label="Conversions year on year",
      services=["website-design", "ppc-sem", "social-media"], goal="Increase online orders and conversions.",
      actions=["Made ordering clearer and faster on mobile.", "Ran local ads for people searching for food nearby.", "Compared year-on-year conversion data to guide changes."]),
]
CASE = {c["n"]: c for c in CASES}

WORK_CATS = [
 dict(slug="website-design-development", name="Website Design & Development", icon="i-monitor", cases=[1, 3, 2, 4],
      lead="Websites that load fast, look professional and turn visitors into enquiries and bookings.",
      intro=["A good website is the centre of your marketing. These projects show how we design and build sites around clear goals, with tracking so results can be measured."]),
 dict(slug="crm-development", name="CRM Development", icon="i-users", cases=[5, 2],
      lead="Projects where better lead tracking and follow-up helped teams close more of the enquiries they already had.",
      intro=["Marketing is wasted if leads are lost. These projects show how organising enquiries and follow-up helped businesses turn more of them into customers."]),
 dict(slug="digital-marketing", name="Digital Marketing", icon="i-layout", cases=[5, 6, 9, 4, 7],
      lead="SEO, social media and content projects that grew visibility, engagement and enquiries.",
      intro=["These projects combine search, social and content to build steady, compounding growth."]),
 dict(slug="ecommerce", name="Ecommerce", icon="i-cart", cases=[7, 3],
      lead="Online selling and booking projects, from product brands to online reservations.",
      intro=["These projects focus on making it easy to buy or book online, then bringing the right visitors to do it."]),
 dict(slug="performance-marketing", name="Performance Marketing", icon="i-chart", cases=[10, 8, 11, 1],
      lead="Paid media projects built around return on ad spend, conversions and booked revenue.",
      intro=["In performance marketing, every rupee must earn its place. These projects show how tracking and testing improved return on ad spend."]),
]


def case_card(n):
    c = CASE[n]
    return ("%s: %s %s" % (c["name"], c["stat"], c["label"].lower()), "%s" % c["goal"], "work/case-study-%d.html" % n, "i-chart", c["img"])


def build():
    for w in WORK_CATS:
        children = [(CASE[n]["name"], "%s %s" % (CASE[n]["stat"], CASE[n]["label"].lower()), "work/case-study-%d.html" % n, "i-chart", CASE[n]["img"]) for n in w["cases"]]
        hub_page(dict(path="work/%s.html" % w["slug"], crumbs=[("Home", "index.html"), ("Our Work", "work/index.html"), (w["name"], "work/%s.html" % w["slug"])],
                      eyebrow="Our Work", color="cyan", h1="%s Work" % w["name"], title="%s Case Studies | Gwadar Digital Agency" % w["name"],
                      lead=w["lead"], name=w["name"], icon=w["icon"], intro_h2="%s projects" % w["name"], intro=w["intro"],
                      grid_eyebrow="Case studies", grid_h2="Selected %s projects" % w["name"].lower(), children=children, section="work"))
    all_kids = [(CASE[c["n"]]["name"], "%s %s" % (c["stat"], c["label"].lower()), "work/case-study-%d.html" % c["n"], "i-chart", c["img"]) for c in CASES]
    hub_page(dict(path="work/index.html", crumbs=[("Home", "index.html"), ("Our Work", "work/index.html")], eyebrow="Our Work", color="cyan",
                  h1="Our Work: Results We Have Delivered", title="Our Work and Case Studies | Gwadar Digital Agency",
                  lead="Real projects, clear numbers. See how our team has helped businesses grow with websites, SEO, social media and paid media.",
                  name="Our Work", icon="i-monitor", intro_h2="Results that can be measured",
                  intro=["We judge our work by outcomes: more enquiries, more bookings and better return on ad spend. These case studies show what we did and what changed.",
                         "Browse by service below, or open any project to see the goal, our approach and the result."],
                  grid_eyebrow="Case studies", grid_h2="All projects", children=all_kids, section="work",
                  faqs=[("Can I see results relevant to my industry?", "Yes. Tell us your industry on a call and we will share the most relevant examples."),
                        ("Are the results guaranteed?", "Every business is different, so past results are not a promise. We set realistic targets and explain our approach before we start.")]))
    for c in CASES:
        others = [n for n in CASE if n != c["n"]]
        idx = [x["n"] for x in CASES].index(c["n"])
        near = [CASES[(idx + k) % len(CASES)]["n"] for k in (1, 2, 3)]
        related = [(CASE[n]["name"], "%s %s" % (CASE[n]["stat"], CASE[n]["label"].lower()), "work/case-study-%d.html" % n, "i-chart", CASE[n]["img"]) for n in near]
        root = "../"
        crumbs = [("Home", "index.html"), ("Our Work", "work/index.html"), (c["name"], "work/case-study-%d.html" % c["n"])]
        svc = "".join('<li><a href="%sservices/%s.html">%s</a></li>' % (root, s, SV[s]["name"]) for s in c["services"])
        snap = ('<div class="cs-snap"><div><span>Client</span><strong>%s</strong></div><div><span>Industry</span><strong>%s</strong></div>'
                '<div><span>Services</span><strong>%s</strong></div></div>' % (c["name"], c["industry"], ", ".join(SV[s]["name"] for s in c["services"])))
        actions = "".join("<li>%s%s</li>" % (icon("i-check"), a) for a in c["actions"])
        body = [hero(root, crumbs, "Case study", "cyan", "%s: %s %s" % (c["name"], c["stat"], c["label"].lower()),
                     "How we helped %s. %s" % (c["name"], c["goal"]), img=c["img"], alt=c["name"], trust=False)]
        body.append(sec("light", snap))
        body.append(sec("soft", '<div class="cs-body"><div><span class="eyebrow p-purple">The goal</span><h2 class="cs-h2">%s</h2>'
                                '<h3 class="cs-h3">What we did</h3><ul class="cs-list">%s</ul></div>'
                                '<div class="cs-result g-cyan"><b>%s</b><span>%s</span></div></div>' % (c["goal"], actions, c["stat"], c["label"])))
        body.append(sec("white", sec_head("Related work", "orange", "More case studies") + rel_cards(related, root)))
        body.append(cta_section(root, h2="Want results like these?", p="Book a free 30-minute strategy call. We will review your business and show you what we would do first."))
        main = '<main id="main">\n%s\n</main>' % "\n".join(body)
        render_page("work/case-study-%d.html" % c["n"], "%s Case Study | Gwadar Digital Agency" % c["name"],
                    "%s: %s %s. See the goal, our approach and the result." % (c["name"], c["stat"], c["label"].lower()), main,
                    crumbs=crumbs, section="work", og_image=c["img"], priority="0.6")


# ---------------------------------------------------------------- Revenue
REV = [
 dict(slug="marketing-that-drives-sales", name="Marketing That Drives Sales", icon="i-trend",
  h1="Marketing That Drives Sales", title="Marketing That Drives Sales | Gwadar Digital Agency",
  lead="Move from marketing activity to marketing revenue. A sales-first approach to digital marketing for businesses in Gwadar.",
  intro=["Likes, views and clicks are not sales. Revenue-focused marketing starts with the number that matters to you, such as bookings, enquiries or orders, and works backwards to the channels that deliver it.",
         "We connect your marketing to your sales process, so you can see what is working, what is not and where to invest next."],
  best="Businesses that want marketing judged by sales", time="Clear picture within 60 to 90 days",
  items=pairs(["Revenue Goals|We agree the target in rupees, enquiries or bookings before we start.", "Funnel Mapping|We map the path from first search to paid customer.",
               "Channel Selection|We back the channels that suit your buyers and budget.", "Tracking & CRM|Calls, forms and WhatsApp tracked into one place.",
               "Sales Follow-up|Faster responses and simple processes so leads convert.", "Monthly Revenue Reports|You see leads, cost per lead and revenue by channel."]),
  faqs=[("How do you tie marketing to sales?", "We track every call, form and WhatsApp click, connect it to your CRM and review which channels produce paying customers."),
        ("What if I do not track sales today?", "We set up simple tracking first, so you can see results within weeks."),
        ("Do you focus only on ads?", "No. We look at the whole path, including SEO, content, website and follow-up.")],
  local="Gwadar businesses often rely on phone calls and WhatsApp, which are easy to lose track of. We make those channels measurable, so you know which marketing brings customers.",
  services=["digital-marketing-packages", "seo-aeo", "ppc-sem"]),
 dict(slug="marketing-roi", name="See Which Marketing Makes Money", icon="i-chart",
  h1="See Which Marketing Makes Money", title="Marketing ROI Tracking | Gwadar Digital Agency",
  lead="Know exactly what each channel costs and what it earns. Marketing ROI tracking and reporting for Gwadar businesses.",
  intro=["Most businesses cannot say which marketing brings customers. They know they spend on ads, social media and SEO, but not what each one earns. That makes it hard to decide where to put the next rupee.",
         "We set up tracking and reporting so every channel has a cost, a lead count and a revenue figure. Then you can invest with confidence."],
  best="Businesses spending on several channels", time="Reporting live within 2 to 4 weeks",
  items=pairs(["Conversion Tracking|Calls, forms, WhatsApp clicks and bookings tracked correctly.", "Source Attribution|See which channel and campaign each lead came from.",
               "Cost per Lead & Customer|Know what each lead and customer really costs.", "Return on Ad Spend|Revenue earned for every rupee spent on ads.",
               "Dashboards|A simple view of the numbers that matter.", "Recommendations|Clear actions: what to scale, fix or stop."]),
  faqs=[("What tools do you use?", "We use Google Analytics, Google Tag Manager, platform dashboards and a CRM, depending on your needs."),
        ("Can you track phone calls?", "Yes. We can track calls from ads and your website, and log WhatsApp enquiries."),
        ("How often will I get reports?", "Monthly, with a live dashboard if you want one.")],
  local="In Gwadar, a lot of business is closed by phone or in person. We show you how to link those sales back to the marketing that started them.",
  services=["seo-aeo", "ppc-sem", "crm-consulting-development"]),
 dict(slug="ad-budget", name="Plan Your Ad Budget Around Profit", icon="i-coin",
  h1="Plan Your Ad Budget Around Profit", title="Ad Budget Planning | Gwadar Digital Agency",
  lead="Set an ad budget that makes sense for your margins. Budget planning for Google and Meta ads in Gwadar, built around profit.",
  intro=["Setting a budget by guesswork is expensive. Too low and you never learn what works. Too high and you waste money before you know the return.",
         "We start with your margins and what a customer is worth, then work out what you can afford to pay for a lead or a sale. That sets a sensible budget and a clear target."],
  best="Businesses starting or scaling paid advertising", time="Plan ready in 1 week",
  items=pairs(["Margin & Value Analysis|What is a customer worth to you, and what can you afford to pay to win one?", "Test Budget|A starting budget designed to learn quickly without waste.",
               "Channel Split|How to divide spend across search, social and other channels.", "Scaling Rules|Clear rules for when to increase spend.",
               "Seasonal Planning|Adjust for peaks such as holidays and tourist seasons.", "Budget Reviews|Monthly reviews to move money to what works."]),
  faqs=[("How much should I spend on ads?", "It depends on your margins and goals. We calculate an affordable cost per lead and set a test budget around it."),
        ("Can I start with a small budget?", "Yes. A small, well-tracked test often teaches more than a large, unfocused spend."),
        ("When should I increase my budget?", "When results are stable and profitable. We give you clear rules.")],
  local="Costs and competition in Gwadar differ from big cities, so budgets should too. We plan around your local market and margins.",
  services=["ppc-sem", "social-media", "ad-creative"]),
 dict(slug="funnel-audit", name="Find Where You Are Losing Sales", icon="i-compass",
  h1="Find Where You Are Losing Sales", title="Sales Funnel Audit | Gwadar Digital Agency",
  lead="A sales funnel audit that shows where leads drop off, from first click to paid customer. Practical fixes for Gwadar businesses.",
  intro=["Often the problem is not getting more traffic. It is what happens after. Slow replies, confusing pages or missing follow-up can lose most of your leads.",
         "Our funnel audit reviews your website, ads, forms, WhatsApp handling and follow-up, then gives you a ranked list of fixes with the biggest wins first."],
  best="Businesses getting traffic or enquiries that do not convert", time="Audit delivered in 1 to 2 weeks",
  items=pairs(["Website Review|Pages, speed, trust signals and calls to action.", "Ads & Landing Pages|Message match, tracking and conversion paths.",
               "Enquiry Handling|Response time, scripts and WhatsApp processes.", "Follow-up Process|What happens to leads after the first contact.",
               "Data & Tracking Check|Whether your numbers can be trusted.", "Priority Action Plan|A ranked list of fixes with expected impact."]),
  faqs=[("What do I receive from the audit?", "A clear report with findings, screenshots and a prioritised action plan, plus a walkthrough call."),
        ("Do I need to implement the fixes with you?", "No. You can use the plan with your own team. We are happy to help if you want."),
        ("Is the audit free?", "We offer a free initial review on the strategy call. A full audit is scoped after that.")],
  local="Many Gwadar businesses lose leads because messages go unanswered for hours. Fixing that alone can lift sales without spending more on marketing.",
  services=["crm-consulting-development", "website-design", "ppc-sem"]),
]


def build_revenue():
    kids = [(r["name"], trim(r["lead"], 110), "revenue/%s.html" % r["slug"], r["icon"], None) for r in REV]
    hub_page(dict(path="revenue.html", crumbs=[("Home", "index.html"), ("Revenue", "revenue.html")], eyebrow="Revenue", color="orange",
                  h1="Marketing Built Around Revenue", title="Revenue-Focused Digital Marketing | Gwadar Digital Agency",
                  lead="Stop guessing which marketing works. Track it, budget around profit and fix the leaks that lose you sales.",
                  name="Revenue", icon="i-trend", intro_h2="From activity to revenue",
                  intro=["Revenue marketing means every decision is tied to money in and money out. We help you see which channels pay, set budgets that protect profit and find where sales are being lost.",
                         "Start with any of the four topics below."],
                  grid_eyebrow="Revenue", grid_h2="Where do you want to start?", children=kids, section="revenue"))
    for r in REV:
        related = [(SV[v]["name"], trim(SV[v]["lead"], 110), "services/%s.html" % v, SV[v]["icon"], None) for v in r["services"]]
        detail_page(dict(path="revenue/%s.html" % r["slug"], kind="solution", name=r["name"], eyebrow="Revenue", color="orange",
                         crumbs=[("Home", "index.html"), ("Revenue", "revenue.html"), (r["name"], "revenue/%s.html" % r["slug"])],
                         h1=r["h1"], lead=r["lead"], title=r["title"], icon=r["icon"], intro=r["intro"], overview_h2=r["name"],
                         facts=[("Best for", r["best"]), ("Typical timeline", r["time"]), ("Reporting", "Monthly, in plain language"), ("Based in", "Gwadar, Balochistan")],
                         items_h2="What is included", items=r["items"], faqs=r["faqs"], local=r["local"], local_h2="%s in Gwadar" % r["name"],
                         related=related, related_eyebrow="Services", related_h2="Services that help", section="revenue"))
