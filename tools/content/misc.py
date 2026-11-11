"""About, team, careers, contact, assessment, legal, insights, 404."""
import re
from lib import *
from content.services import SV, pairs

HOME_CRUMB = ("Home", "index.html")


def page(path, title, desc, parts, crumbs, section=None, scripts=None, ld=None, business_ld=False, priority="0.6", noindex=False):
    main = '<main id="main">\n%s\n</main>' % "\n".join(parts)
    render_page(path, title, desc, main, crumbs=crumbs, section=section, scripts=scripts, ld=ld, business_ld=business_ld,
                priority=priority, noindex=noindex)


# ---------------------------------------------------------------- About
def build_about():
    r = ""
    crumbs = [HOME_CRUMB, ("About", "about.html")]
    parts = [hero(r, crumbs, "About us", "purple", "About Gwadar Digital Agency",
                  "A full-service digital marketing agency based in Gwadar, helping local businesses get found, get chosen and grow.", novis=True, trust=False)]
    parts.append(sec("light", '<div class="ov-grid"><div class="prose"><span class="eyebrow p-purple">Our story</span><h2>A local team for a fast-growing city</h2>'
                              '<p>Gwadar is changing quickly. New businesses, new visitors and new investment are arriving every month. Yet many local companies still depend on word of mouth, or on agencies far away that do not understand the city.</p>'
                              '<p>Gwadar Digital Agency exists to change that. We are a team based in Gwadar that brings strategy, marketing, websites, CRM and creative together under one roof, so local businesses can compete online with confidence.</p>'
                              '<p>We measure ourselves by your results: more enquiries, more bookings and more revenue, not by how busy we look.</p></div>'
                              '<aside class="glance"><h3>Quick facts</h3><ul><li><span>Based in</span><strong>%s</strong></li><li><span>Services</span><strong>Marketing, websites, CRM and creative</strong></li>'
                              '<li><span>Reporting</span><strong>Monthly, in plain language</strong></li><li><span>First step</span><strong>Free 30-minute strategy call</strong></li></ul>'
                              '<a class="btn btn-orange" href="contact.html">Get a free quote</a></aside></div>' % ADDRESS))
    vals = pairs(["Local first|We live and work in Gwadar, and we understand how local customers search, buy and trust.",
                  "Honest advice|We tell you what is worth doing, and what is not, even if it means less work for us.",
                  "Measured results|Everything we do is tracked and reported, so decisions use data.",
                  "Built to last|We build foundations that keep working: SEO, tracking, content and systems you own."])
    parts.append(sec("dark", sec_head("What we stand for", "orange", "Our values") + cards(vals)))
    areas = [("Digital Marketing", "SEO, social media, Google Ads and complete packages.", "services/digital-marketing.html", "i-chart", None),
             ("Website Technology", "WordPress, ecommerce, headless and HubSpot CMS.", "services/website-technology.html", "i-monitor", None),
             ("CRM Development", "HubSpot, Salesforce, Zoho and custom CRM systems.", "services/crm-development.html", "i-briefcase", None),
             ("Creative", "Ad creative, branding, design, video and photography.", "services/creative.html", "i-brush", None)]
    parts.append(sec("light", sec_head("What we do", "cyan", "Four service areas, one team") + rel_cards(areas, r)))
    parts.append(local_section("Find us in Gwadar", "Our office is in New Town Housing, Gwadar. We work with businesses across the city and nearby towns, and with clients elsewhere in Pakistan. Call, message or visit us to talk about your goals.", r))
    parts.append(cta_section(r))
    page("about.html", "About Gwadar Digital Agency | Digital Marketing Agency in Gwadar",
         "Gwadar Digital Agency is a full-service digital marketing agency based in Gwadar. Meet the team and learn how we help local businesses grow.",
         parts, crumbs, section="about", business_ld=True, priority="0.7")


def build_team():
    r = ""
    crumbs = [HOME_CRUMB, ("About", "about.html"), ("Our Team", "our-team.html")]
    parts = [hero(r, crumbs, "Our team", "purple", "Meet Your Digital Experts",
                  "Specialists who treat your budget like their own: curious, direct and hard to please until the numbers move.", novis=True, trust=False)]
    parts.append(sec("light", sec_head("The people behind the work", "purple", "Strategists, creatives and developers in one team",
                                       "You will work directly with the specialists doing the work, not a layer of account managers.", center=True) +
                     '<div class="team-grid" id="teamGrid"></div>'))
    parts.append(cta_section(r, h2="Want to work with us?", p="Book a free strategy call and meet the team that would run your marketing."))
    page("our-team.html", "Our Team | Gwadar Digital Agency", "Meet the Gwadar Digital Agency team: strategists, creatives and developers helping Gwadar businesses grow.",
         parts, crumbs, section="about", scripts=["team.js"])


def build_careers():
    r = ""
    crumbs = [HOME_CRUMB, ("About", "about.html"), ("Careers", "careers.html")]
    parts = [hero(r, crumbs, "Careers", "purple", "Build Your Career in Digital Marketing",
                  "Join a growing team in Gwadar. We are always interested in talented people who like solving real problems for real businesses.", novis=True, trust=False,
                  extra='<div class="ph-cta"><a class="btn btn-orange btn-lg" href="mailto:%s?subject=Career%%20enquiry">Send your CV</a></div>' % EMAIL)]
    perks = pairs(["Real client work|You will work on live projects from day one and see the results of what you do.",
                   "Learn from specialists|Work alongside people in SEO, paid media, creative and development.",
                   "Local, growing company|Help shape a young team in one of Pakistan's fastest-changing cities.",
                   "Room to grow|We promote people who take ownership and learn quickly."])
    parts.append(sec("dark", sec_head("Why join us", "orange", "A place to learn and grow") + cards(perks)))
    roles = [("SEO Specialist", "Technical and local SEO, content and reporting."), ("Paid Media Specialist", "Google and Meta ads, tracking and optimisation."),
             ("Content Creator & Social Media Executive", "Reels, posts, captions and community management."), ("Graphic Designer", "Ad creative, social media and brand design."),
             ("Video Editor & Photographer", "Shoot and edit for brands in Gwadar."), ("Web Developer", "WordPress, ecommerce and front-end development.")]
    rl = "".join('<div class="role"><div><strong>%s</strong><span>%s</span></div><a class="btn btn-orange" href="mailto:%s?subject=Application%%20-%%20%s">Apply</a></div>'
                 % (t, d, EMAIL, t.replace(" ", "%20").replace("&", "and")) for t, d in roles)
    parts.append(sec("light", sec_head("Roles we hire for", "cyan", "Do not see your role? Send us your CV anyway",
                                       "We hire for these roles as the team grows. Send your CV and a short note about the work you are proud of.") + rl))
    parts.append(cta_section(r, h2="Ready to join the team?", p="Email your CV and portfolio to %s and tell us what you would like to work on." % EMAIL, btn="Contact us"))
    page("careers.html", "Careers | Gwadar Digital Agency", "Careers at Gwadar Digital Agency. Join a growing digital marketing team in Gwadar and work on real client projects.",
         parts, crumbs, section="about")


# ---------------------------------------------------------------- Contact
def contact_card():
    m = re.search(r'<div class="contact-card">.*?</form>\s*</div>', HOME_MAIN, re.S)
    return m.group(0)


def build_contact():
    r = ""
    crumbs = [HOME_CRUMB, ("Contact", "contact.html")]
    parts = [hero(r, crumbs, "Contact", "orange", "Talk to Gwadar Digital Agency",
                  "Book a free 30-minute strategy call, or contact us directly. We reply quickly, usually on the same day.", novis=True, trust=False, ctas=False)]
    info = ('<div class="contact-info"><h2 style="font-size:clamp(2rem,4vw,3rem);font-weight:500;letter-spacing:-1px;line-height:1.1">Visit, call or message us</h2>'
            '<p class="lead">We are based in New Town Housing, Gwadar. Choose whichever way suits you.</p><ul class="contact-list">'
            '<li>%s<div><small>Address</small><a href="%s" target="_blank" rel="noopener">%s</a></div></li>'
            '<li>%s<div><small>Phone</small><a href="tel:%s">%s</a></div></li>'
            '<li>%s<div><small>WhatsApp</small><a href="%s" target="_blank" rel="noopener">Message us on WhatsApp</a></div></li>'
            '<li>%s<div><small>Email</small><a href="mailto:%s">%s</a></div></li></ul></div>'
            % (icon("i-pin"), MAPS_Q, ADDRESS, icon("i-phone"), TEL, PHONE, icon("i-whatsapp"), WA, icon("i-mail"), EMAIL, EMAIL))
    parts.append(sec("dark", '<div class="contact-grid">%s%s</div>' % (info, contact_card()), id="contact"))
    parts.append(sec("light", sec_head("Find us", "cyan", "Our location in Gwadar") +
                     '<div class="map-wrap"><iframe src="%s" title="Gwadar Digital Agency on Google Maps" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>'
                     '<div class="map-actions"><a class="btn btn-orange" href="%s" target="_blank" rel="noopener">Open in Google Maps</a>'
                     '<a class="btn-ghost" href="%s" target="_blank" rel="noopener">Leave us a Google review</a></div>' % (MAPS_EMBED, MAPS_Q, MAPS_Q)))
    page("contact.html", "Contact Gwadar Digital Agency | Digital Marketing in Gwadar",
         "Contact Gwadar Digital Agency in New Town Housing, Gwadar. Call %s, WhatsApp or book a free 30-minute strategy call." % PHONE,
         parts, crumbs, business_ld=True, priority="0.8")


# ---------------------------------------------------------------- Assessment
QUIZ = [
 ("Website", "Is your website fast and easy to use on a phone?"),
 ("Google", "Do you have a verified, complete Google Business Profile with photos?"),
 ("Reviews", "Do you regularly ask customers for Google reviews?"),
 ("Tracking", "Do you track calls, forms and WhatsApp enquiries by source?"),
 ("SEO", "Does your website appear on page one for your main services?"),
 ("Social", "Do you post on social media at least once a week?"),
 ("Ads", "Do you run ads with a clear target cost per lead?"),
 ("Follow-up", "Do you reply to new enquiries within an hour?"),
]


def build_assessment():
    r = ""
    crumbs = [HOME_CRUMB, ("Marketing Assessment", "marketing-assessment.html")]
    parts = [hero(r, crumbs, "Free tool", "purple", "Score Your Marketing in Minutes",
                  "Answer 8 quick questions to see where your marketing stands and what to fix first. It takes about two minutes.", novis=True, trust=False, ctas=False)]
    qs = ""
    for i, (k, q) in enumerate(QUIZ):
        qs += ('<fieldset class="q"><h3><small>%s</small>%s</h3><div class="opts">'
               '<label><input type="radio" name="q%d" value="2"><span>Yes</span></label>'
               '<label><input type="radio" name="q%d" value="1"><span>Partly</span></label>'
               '<label><input type="radio" name="q%d" value="0"><span>No</span></label></div></fieldset>' % (k, q, i, i, i))
    quiz = ('<form class="quiz" id="quiz" novalidate>%s<div class="quiz-bar"><button type="submit" class="btn btn-orange btn-lg">See my score</button>'
            '<span id="quizMsg" class="sr-note" role="status"></span></div>'
            '<div class="quiz-result" id="quizResult" hidden><b id="qScore"></b><h3 id="qTitle"></h3><p id="qText"></p>'
            '<a class="btn btn-orange btn-lg" href="contact.html">Book a free strategy call</a></div></form>' % qs)
    parts.append(sec("light", quiz))
    page("marketing-assessment.html", "Free Marketing Assessment | Gwadar Digital Agency",
         "Take our free 2-minute marketing assessment and see where your business stands on website, Google, reviews, tracking, social media and follow-up.",
         parts, crumbs, scripts=["assessment.js"])


# ---------------------------------------------------------------- Legal
def legal(path, title, h1, intro, blocks):
    r = ""
    crumbs = [HOME_CRUMB, (h1, path)]
    body = '<div class="legal"><p class="updated">Last updated: 11 November 2026</p><p>%s</p>%s</div>' % (intro, "".join(blocks))
    parts = [hero(r, crumbs, "Legal", "cyan", h1, "How we handle information and the terms on which we work.", novis=True, trust=False, ctas=False),
             sec("light", body)]
    page(path, title, "%s for %s. Learn how we collect, use and protect information, and the terms that apply to our digital marketing services." % (h1, BRAND), parts, crumbs, priority="0.3")


def build_legal():
    def b(h, *ps):
        return "<h2>%s</h2>%s" % (h, "".join(p if p.startswith("<ul") else "<p>%s</p>" % p for p in ps))
    legal("privacy-policy.html", "Privacy Policy | Gwadar Digital Agency", "Privacy Policy",
          "Gwadar Digital Agency (we, us) respects your privacy. This policy explains what information we collect through www.gwadar.digital, how we use it and the choices you have.",
          [b("Information we collect", "We collect information you give us, such as your name, email address, phone number and message when you fill in a form, email us, call us or message us on WhatsApp. We may also collect basic technical data such as your browser, device and pages visited, through cookies and analytics tools."),
           b("How we use information", "<ul><li>To reply to your enquiry and provide a quote or service.</li><li>To improve our website, services and marketing.</li><li>To send updates you have asked for. You can opt out at any time.</li><li>To meet legal and accounting obligations.</li></ul>"),
           b("Sharing information", "We do not sell your personal information. We share it only with service providers who help us run our business (for example hosting, email and analytics) and only as needed, or when the law requires it."),
           b("Cookies and analytics", "We may use cookies and tools such as Google Analytics to understand how visitors use the site. You can control cookies through your browser settings."),
           b("Data retention and security", "We keep information only as long as needed for the purposes above and take reasonable steps to protect it. No online system is perfectly secure, so we cannot guarantee absolute security."),
           b("Your choices", "You can ask us to access, correct or delete your personal information, or to stop contacting you, by emailing %s." % EMAIL),
           b("Third-party links", "Our site may link to other websites. We are not responsible for their privacy practices."),
           b("Contact", "Questions about this policy? Email %s, call %s or write to %s." % (EMAIL, PHONE, ADDRESS))])
    legal("terms.html", "Terms of Service | Gwadar Digital Agency", "Terms of Service",
          "These terms apply to your use of www.gwadar.digital and to services provided by Gwadar Digital Agency. Specific projects are governed by a written proposal or agreement, which takes priority where it differs.",
          [b("Services and proposals", "We provide digital marketing, website, CRM and creative services. The scope, deliverables, fees and timelines for each project are set out in a written proposal. Work outside that scope may be quoted separately."),
           b("Fees and payment", "Fees and payment terms are stated in your proposal. Late payment may pause work until accounts are settled."),
           b("Client responsibilities", "You agree to provide accurate information, timely feedback and access to accounts and assets we need to do the work. Delays on your side may affect timelines."),
           b("Performance guarantee", "Our performance guarantee applies only to eligible clients and only on the conditions confirmed in writing before work begins. Marketing results depend on many factors, so apart from any written guarantee we do not promise specific rankings, leads or revenue."),
           b("Intellectual property", "Once fees are paid in full, you own the final deliverables created for you. We may use completed work in our portfolio unless you ask us not to. Third-party assets and software remain subject to their own licences."),
           b("Accounts and data", "Advertising and analytics accounts should be set up in your name. You keep ownership of your data."),
           b("Limitation of liability", "To the extent permitted by law, we are not liable for indirect or consequential losses, and our total liability is limited to the fees you paid for the relevant service."),
           b("Changes and termination", "Either party may end an engagement as set out in the proposal. We may update these terms from time to time, and changes apply from the date posted."),
           b("Governing law", "These terms are governed by the laws of Pakistan, and the courts of Balochistan have jurisdiction."),
           b("Contact", "Questions about these terms? Email %s or call %s." % (EMAIL, PHONE))])


# ---------------------------------------------------------------- 404
def build_404():
    r = ""
    parts = ['<section class="ph"><div class="hero-glow" aria-hidden="true"></div><div class="container ph-grid one"><div class="ph-text">'
             '<span class="eyebrow p-orange">Error 404</span><h1>We could not find that page</h1>'
             '<p class="ph-lead">The page may have moved or the link may be wrong. Try one of these instead.</p>'
             '<div class="ph-cta"><a class="btn btn-orange btn-lg" href="/">Go to homepage</a><a class="btn-ghost" href="/services/index.html">Our services</a>'
             '<a class="btn-ghost" href="/contact.html">Contact us</a></div></div></div></section>']
    main = '<main id="main">\n%s\n</main>' % "\n".join(parts)
    render_page("404.html", "Page not found | Gwadar Digital Agency", "The page you were looking for could not be found. Visit the Gwadar Digital Agency homepage, services or contact page instead.", main, noindex=True)
    # 404 can be served from any depth: use absolute asset paths
    full = os.path.join(ROOT, "404.html")
    t = open(full, encoding="utf-8").read()
    t = re.sub(r'(href|src)="(?!https?:|/|#|tel:|mailto:|data:)([^"]+)"', r'\1="/\2"', t)
    open(full, "w", encoding="utf-8").write(t)
