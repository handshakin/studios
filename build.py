#!/usr/bin/env python3
"""Generates the Studios at Parkway static rebuild from real site content."""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("Home", "/index.html"),
    ("Forms", "/forms.html"),
    ("Operating Documents", "/operating-documents.html"),
    ("Businesses", "/businesses.html"),
    ("Blog", "/blog/index.html"),
    ("Contact", "/contact.html"),
]

SOCIAL = [
    ("Facebook", "https://www.facebook.com/studiosatparkway"),
    ("Instagram", "https://www.instagram.com/studiosatparkway/"),
    ("LinkedIn", "https://www.linkedin.com/company/75636040/"),
    ("Twitter", "https://twitter.com/StudiosAtPrkway"),
    ("YouTube", "https://www.youtube.com/channel/UCmFkUtBozY_A_7D_-g3DsVw/featured"),
]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600;700;800&family=Public+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">'


def nav_html(active_href, base_prefix):
    items = []
    for label, href in NAV:
        cur = ' aria-current="page"' if href == active_href else ""
        items.append(f'<a href="{base_prefix}{href}"{cur}>{label}</a>')
    return "\n      ".join(items)


def page(title, meta_desc, active_href, content, base_prefix=".", canonical=""):
    # rewrite any root-relative href="/..." or src="/..." in the body content
    # so the site works both on a real host and inside the Artifact preview
    # (which does not serve root-relative paths).
    content = re.sub(r'(href|src)="/', rf'\1="{base_prefix}/', content)
    css = f"{base_prefix}/assets/style.css"
    header = f"""<header class="site-header">
    <div class="wrap">
      <a class="brand" href="{base_prefix}/index.html"><span class="mark">&#9633;</span> Studios at Parkway</a>
      <nav class="primary" aria-label="Primary">
      {nav_html(active_href, base_prefix)}
      </nav>
      <a class="callbar" href="tel:+15056052060">Call (505) 605-2060</a>
    </div>
  </header>"""

    social_links = "\n        ".join(f'<a href="{u}" rel="noopener">{n}</a>' for n, u in SOCIAL)

    footer = f"""<footer class="site">
    <div class="wrap">
      <div class="col">
        <h4>Studios at Parkway</h4>
        <div>1189 Parkway Drive</div>
        <div>Santa Fe, NM</div>
      </div>
      <div class="col">
        <h4>Listing Broker</h4>
        <div>Leslie Giorgetti, Owner Broker</div>
        <div>Keller Williams Realty</div>
        <div>130 Lincoln Ave Suite K, Santa Fe, NM 87501</div>
      </div>
      <div class="col">
        <h4>Contact</h4>
        <a href="tel:+15056052060">(505) 605-2060</a>
        <a href="mailto:studiosatparkway@gmail.com">studiosatparkway@gmail.com</a>
      </div>
      <div class="col">
        <h4>Follow</h4>
        <div class="social">
        {social_links}
        </div>
      </div>
      <div class="legal">&copy; Studios at Parkway. Rebuilt {os.environ.get('BUILD_DATE','2026')} &mdash; draft in progress, content pending owner review.</div>
    </div>
  </footer>"""

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{meta_desc}">
{FONTS}
<link rel="stylesheet" href="{css}">
</head>
<body>
{header}
{content}
{footer}
</body>
</html>
"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", path)


def frame(caption):
    return f'<div class="frame"><div class="cap">{caption}</div><div class="c2"></div></div>'


# ---------------------------------------------------------------- HOME
home_content = f"""
  <section class="hero">
    <div class="wrap">
      <div class="eyebrow">Santa Fe, New Mexico &mdash; Warehouse/Art &amp; Innovation District</div>
      <h1>Distinctive spaces for work and play in the heart of Santa Fe.</h1>
      <p class="lede">29 newly built industrial flex-use condominiums &mdash; for sale or lease &mdash; in a Federal Opportunity Zone one block off Cerrillos Road.</p>
      <div class="actions">
        <a class="btn primary" href="tel:+15056052060">Call (505) 605-2060</a>
        <a class="btn ghost" href="/contact.html">Ask about availability</a>
      </div>
    </div>
  </section>

  <div class="specs wrap" style="padding-inline:0;">
    <dl><dt>Units</dt><dd>29</dd></dl>
    <dl><dt>Unit size</dt><dd>~1,500 SF</dd></dl>
    <dl><dt>Zoning</dt><dd>I&#8209;1</dd></dl>
    <dl><dt>Status</dt><dd>Move&#8209;in ready</dd></dl>
  </div>

  <section class="block wrap">
    <div class="grid-2">
      <div>
        <div class="eyebrow">The development</div>
        <h2>Built for makers, not cubicles.</h2>
        <div class="prose">
          <p>Studios at Parkway is Santa Fe's newest commercial, industrial, flex-use development, with units available for sale or lease. Each roughly 1,500&nbsp;square&#8209;foot unit spans a ground floor and mezzanine level, with tall ceilings, roll&#8209;up garage doors, expansive storefront windows, LED lighting, and finished concrete floors. Units can be combined for larger footprints, and each comes with kitchenette provisions and separately metered utilities.</p>
          <p>The 29 move&#8209;in ready condominiums sit within Santa Fe's Warehouse/Art and Innovation District, next to the Richards Avenue Business Park and its roughly 85 established businesses &mdash; minutes from Meow Wolf, local galleries, restaurants, and breweries. The property also falls within a Federal Opportunity Zone, which can offer tax advantages to qualifying investors and business owners.</p>
          <p>Designed and built by Palo Santo Designs, Santa Fe's award&#8209;winning architecture and construction firm, with an emphasis on craftsmanship and energy efficiency.</p>
        </div>
      </div>
      {frame("Photo: exterior &mdash; roll-up garage doors and storefront glazing")}
    </div>
  </section>

  <section class="block wrap">
    <div class="grid-2">
      {frame("Photo: interior &mdash; mezzanine, steel stair, concrete floor")}
      <div>
        <div class="eyebrow">Inside a unit</div>
        <h2>Ground floor and mezzanine.</h2>
        <div class="prose">
          <p>Finished concrete floors and warm LED lighting set an industrial&#8209;chic tone at street level. Handcrafted steel staircases with wood treads lead to a second&#8209;story mezzanine &mdash; a private retreat, a second workstation, or extra storage, depending on how you run your business.</p>
          <p>Zoned I&#8209;1, the units suit a wide range of uses: studios, galleries, light industrial, design and fabrication shops, wellness practices, and office or showroom space.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="block wrap">
    <div class="eyebrow">Location</div>
    <h2>1189 Parkway Drive</h2>
    <p class="lede">Near the streets of Parkway, Rufina, and Calle Marie &mdash; one block off Cerrillos Road and minutes from anywhere in Santa Fe.</p>
    <div class="mapframe" style="margin-top:24px;">
      <iframe loading="lazy" title="Map to 1189 Parkway Drive, Santa Fe, NM" src="https://www.google.com/maps?q=1189+Parkway+Drive,+Santa+Fe,+NM&output=embed"></iframe>
    </div>
  </section>
"""

write("index.html", page(
    "Studios at Parkway | Call us @ (505) 605-2060",
    "Santa Fe's newest commercial, industrial, flex-use development with units available for sale or lease.",
    "/index.html", home_content))

# ---------------------------------------------------------------- FORMS
forms_content = f"""
  <section class="block wrap" style="padding-block-start:48px;">
    <div class="eyebrow">Leasing &amp; ownership</div>
    <h2>Forms</h2>
    <p class="lede">Documents needed to apply or transact at Studios at Parkway.</p>
    <ul class="doclist">
      <li><a href="https://docs.google.com/document/d/1Ykea1B37pAZYIloDWVQZaEmrNljlCu8_/edit?usp=sharing" rel="noopener"><span class="name">Sign Application</span><span class="meta">Google&nbsp;Doc</span></a></li>
    </ul>
    <p class="note" style="margin-top:16px;">Have a question about a specific form, or need something not listed here? <a href="/contact.html">Contact the listing broker</a> or call (505) 605-2060.</p>
  </section>
"""
write("forms.html", page(
    "Forms | Studios at Parkway",
    "Sign application and other forms for tenants and owners at Studios at Parkway, Santa Fe.",
    "/forms.html", forms_content))

# ---------------------------------------------------------------- OPERATING DOCUMENTS
docs_content = f"""
  <section class="block wrap" style="padding-block-start:48px;">
    <div class="eyebrow">Governance</div>
    <h2>Operating Documents</h2>
    <p class="lede">Governing documents for the Studios at Parkway condominium association.</p>
    <ul class="doclist">
      <li><a href="/documents/Studios-ByLaws.pdf"><span class="name">Bylaws</span><span class="meta">PDF</span></a></li>
      <li><a href="/documents/Studios-CRs-w-Exhibits-AB.pdf"><span class="name">Declaration of Covenants &amp; Restrictions</span><span class="meta">PDF &middot; with Exhibits A&#8211;B</span></a></li>
      <li><a href="/documents/Amendment-Studios-CRs-2024-11-27.pdf"><span class="name">Amendment to Declaration</span><span class="meta">PDF &middot; signed Nov 27, 2024</span></a></li>
    </ul>
    <p class="note" style="margin-top:16px;">These PDFs are placeholders in this draft &mdash; Jason will provide the current, clean source files to publish here directly, independent of the old hosting.</p>
  </section>
"""
write("operating-documents.html", page(
    "Operating Documents | Studios at Parkway",
    "Bylaws, declaration of covenants and restrictions, and amendments for Studios at Parkway, Santa Fe.",
    "/operating-documents.html", docs_content))

# ---------------------------------------------------------------- BUSINESSES
biz_content = f"""
  <section class="block wrap" style="padding-block-start:48px;">
    <div class="eyebrow">Directory</div>
    <h2>Businesses in the Studios at Parkway</h2>
    <p class="lede">This directory is still filling in as units are occupied &mdash; here's who's listed so far.</p>
    <div class="cards" style="margin-top:24px;">
      <div class="card">
        <div class="eyebrow">Listing Broker</div>
        <h3>Keller Williams Realty</h3>
        <p>Leslie Giorgetti, Owner Broker<br>130 Lincoln Ave Suite K, Santa Fe, NM 87501<br>(505) 605-2060</p>
      </div>
    </div>
    <p class="note" style="margin-top:20px;">Own or lease a unit at Studios at Parkway? <a href="/contact.html">Get in touch</a> to be added to this page.</p>
  </section>
"""
write("businesses.html", page(
    "Businesses in the Studios at Parkway",
    "Directory of businesses located at Studios at Parkway, Santa Fe.",
    "/businesses.html", biz_content))

# ---------------------------------------------------------------- CONTACT
contact_content = f"""
  <section class="block wrap" style="padding-block-start:48px;">
    <div class="grid-2">
      <div>
        <div class="eyebrow">Get in touch</div>
        <h2>Contact</h2>
        <p class="lede">Centrally located in the geographic heart of Santa Fe, near Parkway, Rufina, and Calle Marie &mdash; one block off Cerrillos Road and minutes from anywhere in the city.</p>
        <form class="contact" action="#" method="post" style="margin-top:28px;">
          <div class="field"><label for="c-name">Name</label><input id="c-name" name="name" type="text" required></div>
          <div class="field"><label for="c-phone">Phone number</label><input id="c-phone" name="phone" type="tel"></div>
          <div class="field"><label for="c-email">Email</label><input id="c-email" name="email" type="email" required></div>
          <div class="field"><label for="c-message">Message</label><textarea id="c-message" name="message" required></textarea></div>
          <button class="submit" type="submit">Send message</button>
          <p class="note">This draft form isn't wired to send yet &mdash; we'll connect it to a form service before this goes live.</p>
        </form>
      </div>
      <div style="display:grid; gap:20px;">
        <div class="infopanel">
          <h3>Leslie Giorgetti</h3>
          <div class="row"><span>Title</span><span>Owner Broker, Keller Williams Realty</span></div>
          <div class="row"><span>Phone</span><span><a href="tel:+15056052060">(505) 605-2060</a></span></div>
          <div class="row"><span>Email</span><span><a href="mailto:studiosatparkway@gmail.com">studiosatparkway@gmail.com</a></span></div>
          <div class="row"><span>Address</span><span>130 Lincoln Ave Suite K, Santa Fe, NM 87501</span></div>
        </div>
        <div class="mapframe">
          <iframe loading="lazy" title="Map to 1189 Parkway Drive, Santa Fe, NM" src="https://www.google.com/maps?q=1189+Parkway+Drive,+Santa+Fe,+NM&output=embed"></iframe>
        </div>
      </div>
    </div>
  </section>
"""
write("contact.html", page(
    "Contact | Studios at Parkway",
    "Contact Studios at Parkway and listing broker Leslie Giorgetti of Keller Williams Realty.",
    "/contact.html", contact_content))

# ---------------------------------------------------------------- BLOG
POSTS = [
    dict(
        slug="work-and-play-in-perfect-harmony",
        title="Work and Play in Perfect Harmony: Studios at Parkway in the Heart of Santa Fe",
        date="2023-09-23", date_h="September 23, 2023",
        excerpt="Studios at Parkway breaks from the traditional office, offering a workspace that inspires and energizes &mdash; right in Santa Fe's Warehouse/Art and Innovation District.",
        body="""
<p>Studios at Parkway is a premier workspace solution in Santa Fe's Warehouse/Art and Innovation District, built to break from the traditional office environment. It offers, in short, a workspace that inspires and energizes you, with contemporary design throughout.</p>
<p>Each unit spans approximately 1,500 square feet across a ground floor and mezzanine level. Features include tall ceilings, roll-up garage doors, expansive windows, LED lighting, and concrete floors. Units can be combined for larger spaces and include kitchenette provisions and separately metered utilities.</p>
<p>The location offers significant advantages, positioned near Meow Wolf, local galleries, restaurants, and breweries. The surrounding Siler/Rufina district hosts artists and entrepreneurs, creating networking opportunities. Palo Santo Designs, an award-winning Santa Fe architecture firm, developed the property with an emphasis on craftsmanship and energy efficiency.</p>
<p>Ready to learn about available units? Call (505) 605-2060 or <a href="/contact.html">get in touch</a> to secure your workspace in this creative community hub.</p>
""".strip()),
    dict(
        slug="opportunity-knocks-federal-opportunity-zones",
        title="Opportunity Knocks: Federal Opportunity Zones and Tax Incentives at Studios at Parkway",
        date="2023-08-22", date_h="August 22, 2023",
        excerpt="Studios at Parkway sits within a Federal Opportunity Zone &mdash; here's what that can mean for investors and business owners.",
        body="""
<p>Studios at Parkway, a commercial development in Santa Fe, is located within a Federal Opportunity Zone. These zones provide significant tax incentives to investors and business owners, making them an attractive option for those seeking to maximize their returns.</p>
<p>Key tax benefits include the ability to defer capital gains taxes when reinvesting proceeds into the development, and potential reductions in capital gains tax liability for longer-term holdings. Business operators may also access tax credits for hiring employees from within the Opportunity Zone, as well as tax deductions for investing in qualified assets.</p>
<p>Beyond the tax advantages, Studios at Parkway sits in Santa Fe's Warehouse/Art and Innovation District, near the Richards Avenue Business Park and its roughly 85 established businesses. Proximity to Meow Wolf, galleries, restaurants, and breweries brings both networking and customer access.</p>
<p>The development's architecture and construction is by Palo Santo Designs, Santa Fe's award-winning firm, with an emphasis on energy-efficient design and quality construction.</p>
<p><em>This is general information, not tax advice &mdash; talk with a qualified tax professional about your specific situation.</em> For more on investment opportunities, contact listing agent Leslie Giorgetti at Keller Williams Realty, (505) 605-2060.</p>
""".strip()),
    dict(
        slug="unleash-your-creativity",
        title="Unleash Your Creativity: Inspiring Workspaces at Studios at Parkway in Santa Fe",
        date="2023-07-13", date_h="July 13, 2023", modified_h="August 30, 2023",
        excerpt="Industrial aesthetics meet contemporary design in flexible-use spaces drenched in natural light.",
        body="""
<p>In the heart of Santa Fe, amidst rich cultural heritage and breathtaking landscapes, lies a haven for creative minds and innovative businesses. Studios at Parkway, Santa Fe's newest commercial development, is where work and play harmoniously coexist &mdash; an inspiring workspace built to fuel creativity.</p>
<p>Imagine walking into a space that instantly ignites your imagination, where industrial aesthetics meet contemporary design to create an atmosphere of boundless possibility. Studios at Parkway offers flexible-use spaces drenched in natural light, so your ideas have room to flourish.</p>
<p>Each unit spans nearly 1,500 square feet, with room for your business to grow and evolve. Spaces can be customized to suit your needs, with the ability to combine units for even greater square footage. Tall ceilings lend a sense of grandeur, while generous roll-up aluminum-glass garage doors and expansive storefront windows connect the indoor and outdoor environments.</p>
<p>Step inside and you're greeted by finished concrete floors with an industrial-chic feel, warmed by LED lighting. Handcrafted steel staircases with wood treads lead up to a second-story mezzanine &mdash; a private retreat or additional workspace. Whether you're an artist seeking a studio, a tech startup in need of an office, or a creative entrepreneur with a vision, Studios at Parkway has a space to bring it to life.</p>
<p>The development sits within the Warehouse/Art and Innovation District of Siler/Rufina, adjacent to the thriving Richards Avenue Business Park &mdash; a vibrant mix of local talent and entrepreneurial spirit. Nearby, Meow Wolf's internationally acclaimed immersive art and music venue adds inspiration and entertainment to the workday, alongside galleries, playhouses, and local favorites like Rufina Taproom, Kakawa Chocolate House, and Leaf and Hive.</p>
<p>Growth nearby &mdash; including the luxury apartments at Markana de Santa Fe and the artist rental housing at Siler Yards &mdash; is bringing more residents to the area, expanding the customer base for businesses based here.</p>
<p>Studios at Parkway is zoned I-1, accommodating a diverse range of businesses and industries: designers, startups, wellness professionals, and artisans alike. The 29 newly built condominiums are professional, state-of-the-art, and move-in ready.</p>
<p>Designed and built by Palo Santo Designs, Santa Fe's award-winning architecture and construction firm, with more than 20 years of experience creating unique commercial spaces and custom homes.</p>
<p>Ready to secure your space? Call (505) 605-2060 or <a href="/contact.html">get in touch</a> to learn more about available units.</p>
""".strip()),
    dict(
        slug="discover-the-studios-at-parkway",
        title="Discover the Studios at Parkway: Santa Fe's Premier Industrial Flex-Use Spaces",
        date="2023-06-30", date_h="June 30, 2023", modified_h="August 30, 2023",
        excerpt="29 move-in ready, I-1 zoned units at 1189 Parkway Drive &mdash; for sale or lease.",
        body="""
<p>Business owners seeking distinctive workspace in Santa Fe should consider Studios at Parkway &mdash; Santa Fe's newest commercial, industrial, flex-use development, with units available for purchase or lease.</p>
<p>The complex sits in the Warehouse/Art and Innovation District, within a Federal Opportunity Zone that can offer tax and investment incentives. Each studio spans approximately 1,500 square feet and features tall ceilings, roll-up glass garage doors, storefront windows, finished concrete floors, LED lighting, and steel staircases with wood treads. Units include ground floor and mezzanine space, kitchenette provisions, and separately metered utilities.</p>
<p>Located at 1189 Parkway Drive, adjacent to the Richards Avenue Business Park, the 29 fully finished, move-in ready units are zoned I-1 for diverse commercial use &mdash; offices, galleries, light industrial, warehousing, or wellness centers. The neighborhood includes Meow Wolf, plus galleries, restaurants, and breweries, and recent residential development like Markana de Santa Fe has expanded the area's customer base.</p>
<p>Palo Santo Designs, a Santa Fe architecture and construction firm, designed the development with an emphasis on craftsmanship and energy efficiency.</p>
<p>Contact Leslie Giorgetti, Owner Broker at Keller Williams Realty, at (505) 605-2060, or <a href="/contact.html">reach out here</a>.</p>
""".strip()),
]

listing_items = []
for p in POSTS:
    listing_items.append(f"""<article>
        <time datetime="{p['date']}">{p['date_h']}</time>
        <div>
          <h3><a href="/blog/{p['slug']}.html">{p['title']}</a></h3>
          <p>{p['excerpt']}</p>
        </div>
      </article>""")

blog_index_content = f"""
  <section class="block wrap" style="padding-block-start:48px;">
    <div class="eyebrow">Notes from Studios at Parkway</div>
    <h2>Blog</h2>
    <div class="postlist">
      {''.join(listing_items)}
    </div>
  </section>
"""
write("blog/index.html", page(
    "Blog | Studios at Parkway",
    "News and notes from Studios at Parkway, Santa Fe's newest commercial, industrial, flex-use development.",
    "/blog/index.html", blog_index_content, base_prefix=".."))

for p in POSTS:
    modified_line = f' &middot; updated {p["modified_h"]}' if p.get("modified_h") else ""
    post_content = f"""
  <section class="block wrap" style="padding-block-start:48px;">
    <a class="backlink" href="/blog/index.html">&larr; Back to blog</a>
    <div class="eyebrow">Studios at Parkway</div>
    <h1 style="font-size:clamp(1.9rem,4.4vw,2.8rem); margin-bottom:6px;">{p['title']}</h1>
    <div class="postmeta">
      <time class="eyebrow" datetime="{p['date']}">{p['date_h']}{modified_line}</time>
    </div>
    <div class="prose" style="margin-top:28px;">
      {p['body']}
    </div>
  </section>
"""
    write(f"blog/{p['slug']}.html", page(
        f"{p['title']} | Studios at Parkway",
        p['excerpt'].replace("&mdash;", "-"),
        "/blog/index.html", post_content, base_prefix=".."))

# ---------------------------------------------------------------- ARTIFACT ENTRY (content-only, no doctype/html/head/body — Artifact tool wraps this itself)
home_content_relative = re.sub(r'(href|src)="/', r'\1="./', home_content)
artifact_entry = f"""<title>Studios at Parkway | Call us @ (505) 605-2060</title>
{FONTS}
<link rel="stylesheet" href="./assets/style.css">
<header class="site-header">
    <div class="wrap">
      <a class="brand" href="./index.html"><span class="mark">&#9633;</span> Studios at Parkway</a>
      <nav class="primary" aria-label="Primary">
      <a href="./index.html" aria-current="page">Home</a>
      <a href="./forms.html">Forms</a>
      <a href="./operating-documents.html">Operating Documents</a>
      <a href="./businesses.html">Businesses</a>
      <a href="./blog/index.html">Blog</a>
      <a href="./contact.html">Contact</a>
      </nav>
      <a class="callbar" href="tel:+15056052060">Call (505) 605-2060</a>
    </div>
  </header>
{home_content_relative}
<footer class="site">
    <div class="wrap">
      <div class="col">
        <h4>Studios at Parkway</h4>
        <div>1189 Parkway Drive</div>
        <div>Santa Fe, NM</div>
      </div>
      <div class="col">
        <h4>Listing Broker</h4>
        <div>Leslie Giorgetti, Owner Broker</div>
        <div>Keller Williams Realty</div>
      </div>
      <div class="col">
        <h4>Contact</h4>
        <a href="tel:+15056052060">(505) 605-2060</a>
        <a href="mailto:studiosatparkway@gmail.com">studiosatparkway@gmail.com</a>
      </div>
      <div class="legal">Draft rebuild &mdash; navigate the menu above to review every page. Photo frames mark where real photography goes.</div>
    </div>
</footer>
"""
write("artifact_entry.html", artifact_entry)

print("done")
