import re

with open('pharma-vista.html', 'r', encoding='utf-8') as f:
    html = f.read()

# =========================================================================
# 1. NAVIGATION UPDATE
# =========================================================================
old_nav_links = """<ul class="nav-links">
<li><a href="#philosophy">About</a></li>
<li><a href="#themes">Themes</a></li>
<li><a href="#discussion-domains">Core Domains</a></li>
<li><a href="#blogs">Insights</a></li>
<li><a href="#agenda">Sample Agenda</a></li>
<li><a href="#sponsorship">Partners</a></li>
</ul>"""

new_nav_links = """<ul class="nav-links">
<li><a href="#philosophy">About</a></li>
<li><a href="#themes">Themes</a></li>
<li><a href="#speakers">Speakers</a></li>
<li><a href="#agenda">Agenda</a></li>
<li><a href="#discussion-domains">Core Domains</a></li>
<li><a href="#blogs">Insights</a></li>
<li><a href="#sponsorship">Partners</a></li>
</ul>"""

if old_nav_links in html:
    html = html.replace(old_nav_links, new_nav_links, 1)
    print("Nav links updated")
else:
    print("WARNING: Nav links not found")

old_mobile_links = """<a class="mobile-link" href="#philosophy">About</a>
<a class="mobile-link" href="#themes">Themes</a>
<a class="mobile-link" href="#discussion-domains">Core Domains</a>
<a class="mobile-link" href="#blogs">Insights</a>
<a class="mobile-link" href="#agenda">Sample Agenda</a>
<a class="mobile-link" href="#sponsorship">Partners</a>"""

new_mobile_links = """<a class="mobile-link" href="#philosophy">About</a>
<a class="mobile-link" href="#themes">Themes</a>
<a class="mobile-link" href="#speakers">Speakers</a>
<a class="mobile-link" href="#agenda">Agenda</a>
<a class="mobile-link" href="#discussion-domains">Core Domains</a>
<a class="mobile-link" href="#blogs">Insights</a>
<a class="mobile-link" href="#sponsorship">Partners</a>"""

if old_mobile_links in html:
    html = html.replace(old_mobile_links, new_mobile_links, 1)
    print("Mobile nav links updated")
else:
    print("WARNING: Mobile nav links not found")


# =========================================================================
# 2. HERO SECTION & STATS UPDATE
# =========================================================================
old_hero_badge = """<div class="hero-badge r">
<span class="dot"></span>
          Invite-Only · Virtual Summit · 5 October 2026
        </div>"""

new_hero_badge = """<div class="hero-badge r">
<span class="dot"></span>
          Invite-Only · Virtual Summit · 5 October 2026 · 11:30 AM – 6:30 PM BST | 6:30 AM – 1:30 PM ET
        </div>"""

if old_hero_badge in html:
    html = html.replace(old_hero_badge, new_hero_badge, 1)
    print("Hero badge updated")
else:
    print("WARNING: Hero badge not found")

html = html.replace('<a class="btn btn-ghost" href="#agenda">View Sample Agenda</a>',
                    '<a class="btn btn-ghost" href="#agenda">View Summit Agenda</a>', 1)

old_hero_urgency = """<p class="hero-urgency r" data-d="4" style="font-size:0.78rem; color:var(--accent-amber); font-weight:500; margin-top:0.25rem; letter-spacing:0.5px; margin-bottom:2rem;">
          ⚠️ Registration closes October 1, 2026. Limited Executive Seats Available (Join 200 Leaders).
        </p>"""

new_hero_urgency = """<p class="hero-urgency r" data-d="4" style="font-size:0.78rem; color:var(--accent-amber); font-weight:500; margin-top:0.25rem; letter-spacing:0.5px; margin-bottom:2rem;">
          ⚠️ Registration closes October 1, 2026. Limited Executive Seats Available (Join 200+ Leaders).
        </p>"""

if old_hero_urgency in html:
    html = html.replace(old_hero_urgency, new_hero_urgency, 1)
    print("Hero urgency updated")

old_hero_stats = """<div aria-label="Event statistics" class="hero-stats r" data-d="5">
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="+" data-target="200">200+</span></div>
<div class="h-stat-label">Global Leaders<br/><span style="font-size:0.62rem; opacity:0.8; font-weight:normal; text-transform:none; letter-spacing:0; display:block; line-height:1.2; margin-top:2px;">From
                top pharma &amp; biotech</span></div>
</div>
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="+" data-target="12">12+</span></div>
<div class="h-stat-label">Interactive Sessions<br/><span style="font-size:0.62rem; opacity:0.8; font-weight:normal; text-transform:none; letter-spacing:0; display:block; line-height:1.2; margin-top:2px;">Panels
                &amp; roundtables</span></div>
</div>
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="" data-target="7">7</span></div>
<div class="h-stat-label">Strategic Tracks</div>
</div>
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="" data-target="1">1</span></div>
<div class="h-stat-label">Day</div>
</div>
</div>"""

new_hero_stats = """<div aria-label="Event statistics" class="hero-stats r" data-d="5">
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="+" data-target="200">200+</span></div>
<div class="h-stat-label">Senior Leaders<br/><span style="font-size:0.62rem; opacity:0.8; font-weight:normal; text-transform:none; letter-spacing:0; display:block; line-height:1.2; margin-top:2px;">Pharma &amp; Life Sciences</span></div>
</div>
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="+" data-target="12">12+</span></div>
<div class="h-stat-label">Countries<br/><span style="font-size:0.62rem; opacity:0.8; font-weight:normal; text-transform:none; letter-spacing:0; display:block; line-height:1.2; margin-top:2px;">Global Representation</span></div>
</div>
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="" data-target="7">7</span></div>
<div class="h-stat-label">Keynote Speakers<br/><span style="font-size:0.62rem; opacity:0.8; font-weight:normal; text-transform:none; letter-spacing:0; display:block; line-height:1.2; margin-top:2px;">Visionary Keynotes</span></div>
</div>
<div class="h-stat">
<div class="h-stat-num"><span class="counter-el" data-suffix="" data-target="2">2</span></div>
<div class="h-stat-label">Executive Panels<br/><span style="font-size:0.62rem; opacity:0.8; font-weight:normal; text-transform:none; letter-spacing:0; display:block; line-height:1.2; margin-top:2px;">High-Impact Debates</span></div>
</div>
</div>"""

if old_hero_stats in html:
    html = html.replace(old_hero_stats, new_hero_stats, 1)
    print("Hero stats updated")
else:
    print("WARNING: Hero stats not found")


# =========================================================================
# 3. MEDIA PARTNERS STRIP (SHOWCASE & FOOTER)
# =========================================================================
old_media_strip = """<!-- Media Partners Strip -->
<div style="display: flex; align-items: center; justify-content: center; gap: 2.5rem; flex-wrap: wrap; padding: 1.25rem 2rem; position: relative; z-index: 3;">
<span style="font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2.5px; color: rgba(255,255,255,0.4); font-weight: 500; margin-right: 0.5rem;">Media Partners</span>
<a href="https://www.bioseedin.com" target="_blank" rel="noopener noreferrer" style="display:flex; align-items:center; opacity:0.8; transition: opacity 0.3s, transform 0.3s; text-decoration:none;" onmouseover="this.style.opacity='1'; this.style.transform='scale(1.08)'" onmouseout="this.style.opacity='0.8'; this.style.transform='scale(1)'" title="BIOSEEDIN">
<img src="assets/bioseedin_logo.svg" alt="BIOSEEDIN — Media Partner" style="height: 34px;" loading="lazy"/>
</a>
<a href="https://www.allex.ai" target="_blank" rel="noopener noreferrer" style="display:flex; align-items:center; opacity:0.8; transition: opacity 0.3s, transform 0.3s; text-decoration:none;" onmouseover="this.style.opacity='1'; this.style.transform='scale(1.08)'" onmouseout="this.style.opacity='0.8'; this.style.transform='scale(1)'" title="Allex.ai">
<img src="assets/allex_ai_logo.png" alt="Allex.ai — Media Partner" style="height: 34px;" loading="lazy"/>
</a>
</div>"""

new_media_strip = """<!-- Media Partners Strip -->
<div class="media-partners-strip">
  <span class="media-partners-label">Official Media Partners</span>
  <div class="media-partners-grid">
    <a href="https://www.bioseedin.com" target="_blank" rel="noopener noreferrer" class="media-partner-card" title="BIOSEEDIN — Official Media Partner">
      <img src="assets/bioseedin_logo_dark.svg" alt="BIOSEEDIN — Official Media Partner" class="media-partner-logo" loading="lazy"/>
    </a>
    <a href="https://www.allex.ai" target="_blank" rel="noopener noreferrer" class="media-partner-card" title="Allex.ai — Official Media Partner">
      <img src="assets/allex_ai_logo.png" alt="Allex.ai — Official Media Partner" class="media-partner-logo" loading="lazy"/>
    </a>
  </div>
</div>"""

if old_media_strip in html:
    html = html.replace(old_media_strip, new_media_strip, 1)
    print("Media partners strip updated")
else:
    print("WARNING: Media partners strip not found")

# Showcase stats
old_showcase_stats = """<div class="cine-stats-col">
<div class="cine-stat-pill">
<div class="cine-stat-pill-num">200+</div>
<div class="cine-stat-pill-label">Global Leaders from Pharma &amp; Biotech</div>
</div>
<div class="cine-stat-pill">
<div class="cine-stat-pill-num">12+</div>
<div class="cine-stat-pill-label">Interactive Sessions &amp; Panels</div>
</div>
<div class="cine-stat-pill">
<div class="cine-stat-pill-num">7</div>
<div class="cine-stat-pill-label">Strategic Tracks</div>
</div>
</div>"""

new_showcase_stats = """<div class="cine-stats-col">
<div class="cine-stat-pill">
<div class="cine-stat-pill-num">200+</div>
<div class="cine-stat-pill-label">Senior Pharma Leaders</div>
</div>
<div class="cine-stat-pill">
<div class="cine-stat-pill-num">7</div>
<div class="cine-stat-pill-label">Keynote Speakers</div>
</div>
<div class="cine-stat-pill">
<div class="cine-stat-pill-num">2</div>
<div class="cine-stat-pill-label">Executive Panels</div>
</div>
</div>"""

if old_showcase_stats in html:
    html = html.replace(old_showcase_stats, new_showcase_stats, 1)
    print("Showcase stats updated")

# Footer media partners
old_footer_partners = """<!-- Footer Media Partners -->
<div style="margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(255,255,255,0.08);">
<p style="font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; color: rgba(255,255,255,0.35); margin-bottom: 0.75rem; font-weight: 500;">Media Partners</p>
<div style="display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;">
<a href="https://www.bioseedin.com" target="_blank" rel="noopener noreferrer" style="display:flex; align-items:center; opacity:0.55; transition: opacity 0.3s; text-decoration:none;" onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='0.55'" title="BIOSEEDIN">
<img src="assets/bioseedin_logo.svg" alt="BIOSEEDIN" style="height: 28px; filter: brightness(0) invert(1);" loading="lazy"/>
</a>
<a href="https://www.allex.ai" target="_blank" rel="noopener noreferrer" style="display:flex; align-items:center; opacity:0.55; transition: opacity 0.3s; text-decoration:none;" onmouseover="this.style.opacity='0.9'" onmouseout="this.style.opacity='0.55'" title="Allex.ai">
<img src="assets/allex_ai_logo.png" alt="Allex.ai" style="height: 28px; filter: brightness(0) invert(1);" loading="lazy"/>
</a>
</div>
</div>"""

new_footer_partners = """<!-- Footer Media Partners -->
<div style="margin-top: 1.5rem; padding-top: 1.25rem; border-top: 1px solid rgba(255,255,255,0.08);">
<p style="font-size: 0.68rem; text-transform: uppercase; letter-spacing: 2px; color: rgba(255,255,255,0.6); margin-bottom: 0.85rem; font-weight: 600;">Official Media Partners</p>
<div style="display: flex; align-items: center; gap: 1.25rem; flex-wrap: wrap;">
<a href="https://www.bioseedin.com" target="_blank" rel="noopener noreferrer" class="media-partner-card" style="background:#ffffff; padding:8px 20px; border-radius:10px; display:inline-flex; align-items:center; justify-content:center; height:46px; text-decoration:none;" title="BIOSEEDIN">
<img src="assets/bioseedin_logo_dark.svg" alt="BIOSEEDIN — Official Media Partner" style="height: 24px; width: auto; max-width: 130px; object-fit: contain;" loading="lazy"/>
</a>
<a href="https://www.allex.ai" target="_blank" rel="noopener noreferrer" class="media-partner-card" style="background:#ffffff; padding:8px 20px; border-radius:10px; display:inline-flex; align-items:center; justify-content:center; height:46px; text-decoration:none;" title="Allex.ai">
<img src="assets/allex_ai_logo.png" alt="Allex.ai — Official Media Partner" style="height: 24px; width: auto; max-width: 130px; object-fit: contain;" loading="lazy"/>
</a>
</div>
</div>"""

if old_footer_partners in html:
    html = html.replace(old_footer_partners, new_footer_partners, 1)
    print("Footer media partners updated")
else:
    print("WARNING: Footer media partners not found")


# =========================================================================
# 4. COMPANY STATS SECTION (200+, 70+, 12+, 14)
# =========================================================================
old_companies_stats = """<div class="companies-stats-grid">
<div class="company-stat-card r" data-d="3">
<div class="company-stat-num"><span class="counter-el" data-suffix="+" data-target="200">200+</span></div>
<div class="company-stat-label">Executive Delegates</div>
</div>
<div class="company-stat-card r" data-d="4">
<div class="company-stat-num"><span class="counter-el" data-suffix="+" data-target="70">70+</span></div>
<div class="company-stat-label">Global Companies</div>
</div>
<div class="company-stat-card r" data-d="5">
<div class="company-stat-num"><span class="counter-el" data-suffix="+" data-target="25">25+</span></div>
<div class="company-stat-label">Countries</div>
</div>
<div class="company-stat-card r" data-d="6">
<div class="company-stat-num"><span class="counter-el" data-suffix="+" data-target="15">15+</span></div>
<div class="company-stat-label">Industry Speakers</div>
</div>
</div>"""

new_companies_stats = """<div class="companies-stats-grid">
<div class="company-stat-card r" data-d="3">
<div class="company-stat-num"><span class="counter-el" data-suffix="+" data-target="200">200+</span></div>
<div class="company-stat-label">Senior Leaders</div>
</div>
<div class="company-stat-card r" data-d="4">
<div class="company-stat-num"><span class="counter-el" data-suffix="+" data-target="70">70+</span></div>
<div class="company-stat-label">Global Companies</div>
</div>
<div class="company-stat-card r" data-d="5">
<div class="company-stat-num"><span class="counter-el" data-suffix="+" data-target="12">12+</span></div>
<div class="company-stat-label">Countries</div>
</div>
<div class="company-stat-card r" data-d="6">
<div class="company-stat-num"><span class="counter-el" data-suffix="" data-target="14">14</span></div>
<div class="company-stat-label">Named Experts &amp; Moderators</div>
</div>
</div>"""

if old_companies_stats in html:
    html = html.replace(old_companies_stats, new_companies_stats, 1)
    print("Company stats updated")
else:
    print("WARNING: Company stats not found")


# =========================================================================
# 5. SPEAKERS SECTION (7 KEYNOTES, 2 MODERATORS, 5 PANELLISTS)
# =========================================================================
# We will replace from <section aria-labelledby="speakers-title" id="speakers" ... to the end of the panellists section
# Let's find the start of speakers and end of panellists
speakers_start = html.find('<!-- ============================================================\n     SPEAKERS')
if speakers_start == -1:
    speakers_start = html.find('id="speakers"')
    speakers_start = html.rfind('<!--', 0, speakers_start)

philosophy_start = html.find('<!-- ============================================================\n     PHILOSOPHY / ABOUT')
if philosophy_start == -1:
    philosophy_start = html.find('id="philosophy"')
    philosophy_start = html.rfind('<!--', 0, philosophy_start)

print(f"Speakers section range: {speakers_start} to {philosophy_start}")

new_speakers_section = """<!-- ============================================================
     SPEAKERS & LEADERSHIP FACULTY
     ============================================================ -->
<section aria-labelledby="speakers-title" id="speakers" style="background: var(--bg-primary);">
<div class="section-pad">
<div class="container">
<div style="max-width: var(--max-w); margin: 0 auto 3.5rem; text-align: center;">
<div class="sec-label r" style="justify-content: center;">Summit Leadership Faculty</div>
<h2 class="section-title r" data-d="1" id="speakers-title">Hear from the <span class="teal">Industry's</span> Brightest Minds</h2>
<p class="r" data-d="2" style="font-size: 1rem; color: var(--text-secondary); max-width: 680px; margin: 1.5rem auto 0; line-height: 1.75;">
  A distinguished faculty of 14 confirmed keynote speakers, executive panel moderators, and panellists shaping the next decade of pharmaceutical innovation, commercial excellence, and global supply chain resilience.
</p>
</div>

<!-- ==========================================
     SUBSECTION 1: FEATURED KEYNOTE SPEAKERS (7)
     ========================================== -->
<div class="speaker-category-block">
  <div style="margin-bottom: 2rem;">
    <div class="speaker-cat-title">
      Featured Keynote Speakers
      <span class="speaker-cat-badge badge-keynote-cat">7 Keynotes</span>
    </div>
    <p class="speaker-cat-desc">Visionary keynote addresses addressing clinician education, water dynamics in cellular metabolism, omnichannel commercialization, trust infrastructure, patient support programs, medical affairs, and GTM transformation.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 2rem; max-width: var(--max-w); margin: 0 auto;">

    <!-- Keynote 1: Dr. Aridita Mukherjee -->
    <div class="r" data-d="1" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-teal); color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Keynote</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Dr. Aridita Mukherjee" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.06)'" src="assets/aridita_mukherjee.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Dr. Aridita Mukherjee</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Founder Director, Inside Health Communications</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Session:</strong> Can AI Personalize Clinician Education Without Dehumanizing Medicine?</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Humanizing medical education through responsible AI integration."
        </div>
      </div>
    </div>

    <!-- Keynote 2: In Sang Lee -->
    <div class="r" data-d="2" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-teal); color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Keynote</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="In Sang Lee" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.06)'" src="assets/in_sang_lee.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">In Sang Lee</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">CEO, Divine Labs</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Session:</strong> Beyond pH: Exploring Hydronium Ion Dynamics in Cellular Metabolism &amp; Pharmaceutical Research</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Exploring emerging research at the intersection of water chemistry &amp; biomedical science."
        </div>
      </div>
    </div>

    <!-- Keynote 3: Andres von der Walde -->
    <div class="r" data-d="3" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-teal); color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Keynote</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Andres von der Walde" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.06)'" src="assets/andres_von_der_walde.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Andres von der Walde</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Senior Director, Novo Nordisk</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Session:</strong> AI-Powered Omnichannel Commercial Excellence</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Connecting AI intelligence with human-centred engagement for commercial impact."
        </div>
      </div>
    </div>

    <!-- Keynote 4: Varun Sharma -->
    <div class="r" data-d="4" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-teal); color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Keynote</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Varun Sharma" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.06)'" src="assets/varun_sharma_portrait_1785845304931.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Varun Sharma</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Founder &amp; CEO, NEUVIOR</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Session:</strong> Beyond Discovery: Building Trust Infrastructure for Pharma AI Deployment</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Innovation today creates healthier tomorrows."
        </div>
      </div>
    </div>

    <!-- Keynote 5: Robin Hunter -->
    <div class="r" data-d="5" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-teal); color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Keynote</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Robin Hunter" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.06)'" src="assets/robin_hunter.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Robin Hunter</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">President, Ribicon Group Canada</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Session:</strong> How Patient Support Programs Create Measurable Patient Impact</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Delivering equitable patient access and measurable real-world outcomes."
        </div>
      </div>
    </div>

    <!-- Keynote 6: Dr. Harshad Malve -->
    <div class="r" data-d="6" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-teal); color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Keynote</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Dr. Harshad Malve" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.06)'" src="assets/harshad_malve_portrait_1785845325472.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Dr. Harshad Malve</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Medical Head, Kenvue</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Session:</strong> The Evolving Role of Medical Affairs in Driving Innovation</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Science saves lives. Innovation scales it."
        </div>
      </div>
    </div>

    <!-- Keynote 7: Zara Baker -->
    <div class="r" data-d="7" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-teal); color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Keynote</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Zara Baker" onmouseout="this.style.transform='scale(1)'" onmouseover="this.style.transform='scale(1.06)'" src="assets/zara_baker.jpg" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Zara Baker</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Interim Chief Marketing &amp; Growth Officer, Executive Advisor</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Session:</strong> AI-Enabled Commercialization: Transforming Go-to-Market Strategies in Life Sciences</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Transforming commercial go-to-market strategies with AI-driven precision."
        </div>
      </div>
    </div>

  </div>
</div>

<div aria-hidden="true" class="sec-divider" style="margin: 3.5rem 0;"></div>

<!-- ==========================================
     SUBSECTION 2: EXECUTIVE PANEL MODERATORS (2)
     ========================================== -->
<div class="speaker-category-block">
  <div style="margin-bottom: 2rem;">
    <div class="speaker-cat-title">
      Executive Panel Moderators
      <span class="speaker-cat-badge badge-mod-cat">2 Moderators</span>
    </div>
    <p class="speaker-cat-desc">Distinguished editorial directors and life sciences strategists steering high-impact dialogue and debate across our two summit executive panels.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap: 2.5rem; max-width: 820px; margin: 0 auto;">

    <!-- Moderator 1: Andrea Charles (Panel 1) -->
    <div class="r" data-d="1" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: #6366f1; color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Moderator</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Andrea Charles" src="assets/andrea_charles.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Andrea Charles</h3>
        <p style="font-size: 0.85rem; color: #6366f1; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Editorial Director, European Medical Journal</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Moderating:</strong> Executive Panel 1 — Manufacturing as Geopolitics: API Resilience, China+One &amp; the Supply-Chain Digital Twin</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Guiding conversations. Driving impact."
        </div>
      </div>
    </div>

    <!-- Moderator 2: Michelle Stewart (Panel 2) -->
    <div class="r" data-d="2" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: #6366f1; color: #fff; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Moderator</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Michelle Stewart" src="assets/michelle_stewart.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Michelle Stewart</h3>
        <p style="font-size: 0.85rem; color: #6366f1; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Director, The Pangea Group</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Moderating:</strong> Executive Panel 2 — AI: Hype vs. Pipeline — What's Actually Deployed?</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Challenging hype to uncover real-world deployment in the pharma pipeline."
        </div>
      </div>
    </div>

  </div>
</div>

<div aria-hidden="true" class="sec-divider" style="margin: 3.5rem 0;"></div>

<!-- ==========================================
     SUBSECTION 3: EXECUTIVE PANELISTS (5)
     ========================================== -->
<div class="speaker-category-block">
  <div style="margin-bottom: 2rem;">
    <div class="speaker-cat-title">
      Executive Panelists
      <span class="speaker-cat-badge badge-panel-cat">5 Panellists</span>
    </div>
    <p class="speaker-cat-desc">Senior manufacturing, operational excellence, quality, consulting, and AI executives sharing operational ground truth across our executive panels.</p>
  </div>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 280px), 1fr)); gap: 2rem; max-width: var(--max-w); margin: 0 auto;">

    <!-- Panellist 1: Dr. Deep Upadhyay -->
    <div class="r" data-d="1" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-amber); color: #14251f; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Panel 1</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Dr. Deep Upadhyay" src="assets/deep_upadhyay.jpeg" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Dr. Deep Upadhyay</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Chief Quality Officer, Vasudha Pharma Chem Ltd</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Panel:</strong> Manufacturing as Geopolitics: API Resilience, China+One &amp; the Supply-Chain Digital Twin</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Quality is a culture that defines every molecule we deliver."
        </div>
      </div>
    </div>

    <!-- Panellist 2: Dr. Saurabh Pandey -->
    <div class="r" data-d="2" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-amber); color: #14251f; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Panel 1</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Dr. Saurabh Pandey" src="assets/saurabh_pandey.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Dr. Saurabh Pandey</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Cluster Lead – API Manufacturing – Toansa, Punjab, Sun Pharmaceutical Industries Limited</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Panel:</strong> Manufacturing as Geopolitics: API Resilience, China+One &amp; the Supply-Chain Digital Twin</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Scale without compromise — the mandate of modern API manufacturing."
        </div>
      </div>
    </div>

    <!-- Panellist 3: Tushar Maradwar -->
    <div class="r" data-d="3" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-amber); color: #14251f; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Panel 1</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Tushar Maradwar" src="assets/tushar_maradwar.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Tushar Maradwar</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Head – Operational Excellence, Dr. Reddy's Laboratories</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Panel:</strong> Manufacturing as Geopolitics: API Resilience, China+One &amp; the Supply-Chain Digital Twin</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Operational excellence powers resilient global supply chains."
        </div>
      </div>
    </div>

    <!-- Panellist 4: Dr. Richa Goyal -->
    <div class="r" data-d="4" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-amber); color: #14251f; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Panel 2</div>
      <div style="height: 320px; overflow: hidden; position: relative; background: #eef2f6;">
        <img alt="Dr. Richa Goyal" src="assets/richa_goyal.png" style="width: 100%; height: 100%; object-fit: cover; object-position: center top; transition: transform 0.6s ease;" onmouseover="this.style.transform='scale(1.06)'" onmouseout="this.style.transform='scale(1)'" loading="lazy"/>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Dr. Richa Goyal</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">Founder &amp; CEO, Dual Sphere Consulting</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Panel:</strong> AI: Hype vs. Pipeline — What's Actually Deployed?</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Bridging strategy and technology deployment for measurable pharmaceutical value."
        </div>
      </div>
    </div>

    <!-- Panellist 5: Srinivas Yelleka -->
    <div class="r" data-d="5" onmouseover="this.style.transform='translateY(-6px)'; this.style.boxShadow='0 20px 40px rgba(0,0,0,0.08)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';" style="background: #fff; border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden; transition: transform 0.3s ease, box-shadow 0.3s ease; text-align: center; position: relative;">
      <div style="position: absolute; top: 1rem; right: 1rem; background: var(--accent-amber); color: #14251f; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 0.3rem 0.75rem; border-radius: 20px; z-index: 2;">Panel 2</div>
      <div style="height: 320px; overflow: hidden; position: relative;">
        <div class="avatar-protofine">
          <div class="avatar-initials">SY</div>
          <div style="font-family: var(--font-sans); font-size: 0.8rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--accent-teal);">Protofine AI</div>
          <div style="font-size: 0.72rem; opacity: 0.75; margin-top: 4px;">Technology Leadership</div>
        </div>
      </div>
      <div style="padding: 1.5rem;">
        <h3 style="font-family: 'Cormorant Garamond', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.3rem;">Srinivas Yelleka</h3>
        <p style="font-size: 0.85rem; color: var(--accent-teal); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.8rem;">CTO, Protofine AI</p>
        <p style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.55; margin-bottom: 1rem;"><strong>Panel:</strong> AI: Hype vs. Pipeline — What's Actually Deployed?</p>
        <div style="font-size: 0.85rem; font-style: italic; color: var(--accent-amber); padding-top: 1rem; border-top: 1px solid var(--border);">
          "Deploying resilient enterprise AI architectures across real-world workflows."
        </div>
      </div>
    </div>

  </div>
</div>

</div>
</div>
</section>
<div aria-hidden="true" class="sec-divider"></div>
"""

if speakers_start != -1 and philosophy_start != -1:
    html = html[:speakers_start] + new_speakers_section + html[philosophy_start:]
    print("Speakers section replaced successfully")
else:
    print("ERROR: Could not locate speakers section bounds")


# =========================================================================
# 6. FIVE PILLARS SECTION (THEMES)
# =========================================================================
themes_start = html.find('<!-- ============================================================\n     THEMES / TRACKS')
if themes_start == -1:
    themes_start = html.find('id="themes"')
    themes_start = html.rfind('<!--', 0, themes_start)

domains_start = html.find('<!-- ============================================================\n     DISCUSSION DOMAINS')
if domains_start == -1:
    domains_start = html.find('id="discussion-domains"')
    domains_start = html.rfind('<!--', 0, domains_start)

print(f"Themes section range: {themes_start} to {domains_start}")

new_themes_section = """<!-- ============================================================
     THEMES / FIVE PILLARS
     ============================================================ -->
<section aria-labelledby="themes-title" id="themes">
<div class="section-pad">
<div class="themes-head">
<div class="sec-label r">Five Core Pillars</div>
<h2 class="section-title r" data-d="1" id="themes-title">Five Pillars of Pharma's <span class="teal">Future</span></h2>
<p class="r" data-d="2" style="font-size: 1rem; color: var(--text-secondary); max-width: 720px; margin: 1rem auto 0; line-height: 1.7; text-align: center;">
  Strategic focus areas defining the executive agenda at Pharma Vista Global Summit 2026.
</p>
</div>
<div class="themes-mosaic">
<!-- Pillar 01 — Market Access (LARGE) -->
<div class="theme-card large r" data-cursor="hover" data-d="1">
<div class="theme-img-wrap">
<img alt="Market Access & Global Reimbursement — Pharma Vista 2026" class="theme-card-img" decoding="async" height="534" loading="lazy" src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&q=80&fit=crop" width="800"/>
</div>
<div class="theme-icon-wrap">
<svg class="theme-svg-icon" fill="none" height="28" stroke="var(--accent-teal)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewbox="0 0 24 24" width="28">
<circle cx="12" cy="12" r="10"></circle>
<path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
<path d="M2 12h20"></path>
</svg>
</div>
<div class="theme-card-large-inner">
<div>
<div class="theme-num">Pillar 01</div>
<h3 class="theme-title">Market Access &amp; Global Reimbursement</h3>
<p class="theme-desc">Navigating evolving global payer landscapes, complex value-based pricing agreements, and accelerated patient access frameworks across mature and emerging biopharma markets to secure sustainable product adoption.</p>
</div>
<div aria-hidden="true" class="theme-mol-art">ACCESS</div>
</div>
<div aria-hidden="true" class="theme-bg-word">ACCESS</div>
</div>

<!-- Pillar 02 — HEOR -->
<div class="theme-card r" data-cursor="hover" data-d="2">
<div class="theme-img-wrap">
<img alt="Health Economics and Outcomes Research (HEOR) — Pharma Vista 2026" class="theme-card-img" decoding="async" height="534" loading="lazy" src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80&fit=crop" width="800"/>
</div>
<div class="theme-icon-wrap">
<svg class="theme-svg-icon" fill="none" height="28" stroke="var(--accent-teal)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewbox="0 0 24 24" width="28">
<path d="M18 3a3 3 0 0 0-3 3v12a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3zM9 9a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0v-6a3 3 0 0 0-3-3z"></path>
<path d="M3 15h2a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1v-2a1 1 0 0 1 1-1z"></path>
</svg>
</div>
<div class="theme-num">Pillar 02</div>
<h3 class="theme-title">Health Economics &amp; Outcomes Research (HEOR)</h3>
<p class="theme-desc">Leveraging real-world evidence (RWE), patient-reported outcomes, and comparative effectiveness analysis to demonstrate undeniable clinical differentiation, economic value, and payer alignment.</p>
<div aria-hidden="true" class="theme-bg-word">HEOR</div>
</div>

<!-- Pillar 03 — Pricing -->
<div class="theme-card r" data-cursor="hover" data-d="2">
<div class="theme-img-wrap">
<img alt="Pharmaceutical Pricing Strategy & Net Revenue Management — Pharma Vista 2026" class="theme-card-img" decoding="async" height="534" loading="lazy" src="https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=800&q=80&fit=crop" width="800"/>
</div>
<div class="theme-icon-wrap">
<svg class="theme-svg-icon" fill="none" height="28" stroke="var(--accent-teal)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewbox="0 0 24 24" width="28">
<path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
</svg>
</div>
<div class="theme-num">Pillar 03</div>
<h3 class="theme-title">Pharmaceutical Pricing &amp; Net Revenue Management</h3>
<p class="theme-desc">Building resilient pricing architectures amidst international reference pricing pressures, IRA implications, dynamic discounting models, and global launch sequencing challenges.</p>
<div aria-hidden="true" class="theme-bg-word">PRICE</div>
</div>

<!-- Pillar 04 — Commercial Strategy -->
<div class="theme-card r" data-cursor="hover" data-d="3">
<div class="theme-img-wrap">
<img alt="Commercial Strategy & Omnichannel Execution — Pharma Vista 2026" class="theme-card-img" decoding="async" height="534" loading="lazy" src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&q=80&fit=crop" width="800"/>
</div>
<div class="theme-icon-wrap">
<svg class="theme-svg-icon" fill="none" height="28" stroke="var(--accent-teal)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewbox="0 0 24 24" width="28">
<path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
</svg>
</div>
<div class="theme-num">Pillar 04</div>
<h3 class="theme-title">Commercial Strategy &amp; Omnichannel Execution</h3>
<p class="theme-desc">Reinventing go-to-market models with AI-driven physician segmentation, omnichannel customer engagement, hybrid sales force enablement, and targeted patient support programs.</p>
<div aria-hidden="true" class="theme-bg-word">STRAT</div>
</div>

<!-- Pillar 05 — AI in Healthcare -->
<div class="theme-card r" data-cursor="hover" data-d="3">
<div class="theme-img-wrap">
<img alt="AI in Healthcare & Life Sciences — Pharma Vista 2026" class="theme-card-img" decoding="async" height="450" loading="lazy" src="https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=800&q=80&fit=crop" width="800"/>
</div>
<div class="theme-icon-wrap">
<svg class="theme-svg-icon" fill="none" height="28" stroke="var(--accent-teal)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewbox="0 0 24 24" width="28">
<rect height="20" rx="4" width="20" x="2" y="2"></rect>
<path d="M9 9h6v6H9z"></path>
<path d="M9 1v1M15 1v1M9 22v1M15 22v1M1 9h1M1 15h1M22 9h1M22 15h1"></path>
</svg>
</div>
<div class="theme-num">Pillar 05</div>
<h3 class="theme-title">AI in Healthcare &amp; Life Sciences</h3>
<p class="theme-desc">Operationalizing generative AI, machine intelligence, and predictive modeling across clinical trial protocols, regulatory intelligence, R&amp;D acceleration, and automated evidence generation.</p>
<div aria-hidden="true" class="theme-bg-word">AI</div>
</div>
</div>
</div>
</section>
<div aria-hidden="true" class="sec-divider"></div>
"""

if themes_start != -1 and domains_start != -1:
    html = html[:themes_start] + new_themes_section + html[domains_start:]
    print("Themes/Pillars section replaced successfully")
else:
    print("ERROR: Could not locate themes section bounds")


# =========================================================================
# 7. SUMMIT AGENDA SECTION (EXACT CONFIRMED AGENDA WITH BST + ET)
# =========================================================================
agenda_start = html.find('<!-- ============================================================\n     SAMPLE AGENDA')
if agenda_start == -1:
    agenda_start = html.find('id="agenda"')
    agenda_start = html.rfind('<!--', 0, agenda_start)

sponsorship_start = html.find('<!-- ============================================================\n     SPONSORSHIP')
if sponsorship_start == -1:
    sponsorship_start = html.find('id="sponsorship"')
    sponsorship_start = html.rfind('<!--', 0, sponsorship_start)

print(f"Agenda section range: {agenda_start} to {sponsorship_start}")

new_agenda_section = """<!-- ============================================================
     SUMMIT AGENDA (BST & ET TIMINGS)
     ============================================================ -->
<section aria-labelledby="agenda-title" id="agenda">
<div class="section-pad">
<div style="max-width:var(--max-w);margin:0 auto 3rem; text-align:center;">
<div class="sec-label r" style="display:inline-flex;align-items:center;gap:8px; justify-content:center;">
  <span>Confirmed Programme</span>
  <span style="background:rgba(0,201,167,0.15);color:var(--teal);border:1px solid rgba(0,201,167,0.35);padding:2px 10px;border-radius:4px;font-size:0.7rem;letter-spacing:0.8px;font-weight:700;">OCTOBER 5, 2026</span>
</div>
<h2 class="section-title r" data-d="1" id="agenda-title">SUMMIT AGENDA<br/><span class="teal">BST &amp; ET TIMINGS</span></h2>
<p class="sp-subtitle r" data-d="2" style="margin-top:1rem; font-size:1.05rem;">
  <strong>BST = UK Time | ET = Eastern Time</strong><br/>
  <span style="font-size:0.88rem; color:var(--text-muted); display:inline-block; margin-top:0.4rem;">
    All timings are shown in BST (UK Time) and ET (Eastern Time). Virtual Summit | October 5, 2026.
  </span>
</p>
</div>

<div class="agenda-inner">
<div aria-label="Event agenda" class="timeline" role="list">

  <!-- Session 1: Welcome Address -->
  <div class="tl-item r" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">11:30 – 11:50 AM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">6:30 – 6:50 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-open">WELCOME ADDRESS</span>
      <h3 class="tl-title">Welcome Address &amp; Framing</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-role">Speaker / Host:</span> <span class="tl-speaker-name">Build Tek Events</span>
      </div>
    </div>
  </div>

  <!-- Session 2: Keynote 1 - Dr. Aridita Mukherjee -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">11:50 AM – 12:15 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">6:50 – 7:15 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-keynote">KEYNOTE</span>
      <h3 class="tl-title">Can AI Personalize Clinician Education Without Dehumanizing Medicine?</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-name">Dr. Aridita Mukherjee</span> — <span class="tl-speaker-role">Founder Director, Inside Health Communications</span>
      </div>
    </div>
  </div>

  <!-- Session 3: Keynote 2 - In Sang Lee -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">12:15 – 12:40 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">7:15 – 7:40 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-keynote">KEYNOTE</span>
      <h3 class="tl-title">Beyond pH: Exploring Hydronium Ion Dynamics in Cellular Metabolism &amp; Pharmaceutical Research</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-name">In Sang Lee</span> — <span class="tl-speaker-role">CEO, Divine Labs</span>
      </div>
    </div>
  </div>

  <!-- Session 4: Keynote 3 - Andres von der Walde -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">12:40 – 1:05 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">7:40 – 8:05 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-keynote">KEYNOTE</span>
      <h3 class="tl-title">AI-Powered Omnichannel Commercial Excellence</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-name">Andres von der Walde</span> — <span class="tl-speaker-role">Senior Director, Novo Nordisk</span>
      </div>
    </div>
  </div>

  <!-- Session 5: Keynote 4 - Varun Sharma -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">1:05 – 1:30 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">8:05 – 8:30 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-keynote">KEYNOTE</span>
      <h3 class="tl-title">Beyond Discovery: Building Trust Infrastructure for Pharma AI Deployment</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-name">Varun Sharma</span> — <span class="tl-speaker-role">Founder &amp; CEO, NEUVIOR</span>
      </div>
    </div>
  </div>

  <!-- Session 6: Executive Panel 1 -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">1:30 – 2:20 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">8:30 – 9:20 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-panel">EXECUTIVE PANEL</span>
      <h3 class="tl-title">Manufacturing as Geopolitics: API Resilience, China+One &amp; the Supply-Chain Digital Twin</h3>
      <div class="tl-panel-structure">
        <div class="tl-panel-mod">
          <span class="tl-role-tag">MODERATOR</span>
          <div><strong>Andrea Charles</strong> — Editorial Director, European Medical Journal</div>
        </div>
        <div class="tl-panel-panellists">
          <span class="tl-role-tag">PANELLISTS</span>
          <ul class="tl-panellist-list">
            <li><strong>Dr. Deep Upadhyay</strong> — Chief Quality Officer, Vasudha Pharma Chem Ltd</li>
            <li><strong>Dr. Saurabh Pandey</strong> — Cluster Lead – API Manufacturing – Toansa, Punjab, Sun Pharmaceutical Industries Limited</li>
            <li><strong>Tushar Maradwar</strong> — Head – Operational Excellence, Dr. Reddy's Laboratories</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Session 7: Networking Break -->
  <div class="tl-break-item r" data-d="1" role="separator">
    <div class="tl-time-box">
      <div class="tl-time-bst">2:20 – 2:45 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">9:20 – 9:45 AM <span class="tz-label">ET</span></div>
    </div>
    <div class="tl-break-content">
      <span class="tl-tag tl-tag-net">NETWORKING BREAK</span>
      <h3 class="tl-title" style="margin-bottom:0.2rem;">Virtual Networking Break</h3>
      <p class="tl-desc">Connect 1-on-1 with attending executives and visit digital partner showcases.</p>
    </div>
  </div>

  <!-- Session 8: Keynote 5 - Robin Hunter -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">2:45 – 3:10 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">9:45 – 10:10 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-keynote">KEYNOTE</span>
      <h3 class="tl-title">How Patient Support Programs Create Measurable Patient Impact</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-name">Robin Hunter</span> — <span class="tl-speaker-role">President, Ribicon Group Canada</span>
      </div>
    </div>
  </div>

  <!-- Session 9: Networking Break -->
  <div class="tl-break-item r" data-d="1" role="separator">
    <div class="tl-time-box">
      <div class="tl-time-bst">3:10 – 3:35 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">10:10 – 10:35 AM <span class="tz-label">ET</span></div>
    </div>
    <div class="tl-break-content">
      <span class="tl-tag tl-tag-net">NETWORKING BREAK</span>
      <h3 class="tl-title" style="margin-bottom:0.2rem;">Virtual Networking Break</h3>
      <p class="tl-desc">Informal peer exchanges, interactive roundtable rooms, and private 1:1 meetings.</p>
    </div>
  </div>

  <!-- Session 10: Keynote 6 - Dr. Harshad Malve -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">3:35 – 4:00 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">10:35 – 11:00 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-keynote">KEYNOTE</span>
      <h3 class="tl-title">The Evolving Role of Medical Affairs in Driving Innovation</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-name">Dr. Harshad Malve</span> — <span class="tl-speaker-role">Medical Head, Kenvue</span>
      </div>
    </div>
  </div>

  <!-- Session 11: Networking / Transition Break -->
  <div class="tl-break-item r" data-d="1" role="separator">
    <div class="tl-time-box">
      <div class="tl-time-bst">4:00 – 4:30 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">11:00 – 11:30 AM <span class="tz-label">ET</span></div>
    </div>
    <div class="tl-break-content">
      <span class="tl-tag tl-tag-net">TRANSITION BREAK</span>
      <h3 class="tl-title" style="margin-bottom:0.2rem;">Networking / Transition Break</h3>
      <p class="tl-desc">Pre-panel networking, partner consultations, and thematic lounge transitions.</p>
    </div>
  </div>

  <!-- Session 12: Keynote 7 - Zara Baker -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">4:30 – 4:55 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">11:30 – 11:55 AM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-keynote">KEYNOTE</span>
      <h3 class="tl-title">AI-Enabled Commercialization: Transforming Go-to-Market Strategies in Life Sciences</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-name">Zara Baker</span> — <span class="tl-speaker-role">Interim Chief Marketing &amp; Growth Officer, Executive Advisor</span>
      </div>
    </div>
  </div>

  <!-- Session 13: Executive Panel 2 -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">4:55 – 5:45 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">11:55 AM – 12:45 PM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-panel">EXECUTIVE PANEL</span>
      <h3 class="tl-title">AI: Hype vs. Pipeline — What's Actually Deployed?</h3>
      <div class="tl-panel-structure">
        <div class="tl-panel-mod">
          <span class="tl-role-tag">MODERATOR</span>
          <div><strong>Michelle Stewart</strong> — Director, The Pangea Group</div>
        </div>
        <div class="tl-panel-panellists">
          <span class="tl-role-tag">PANELLISTS</span>
          <ul class="tl-panellist-list">
            <li><strong>Dr. Richa Goyal</strong> — Founder &amp; CEO, Dual Sphere Consulting</li>
            <li><strong>Srinivas Yelleka</strong> — CTO, Protofine AI</li>
          </ul>
        </div>
      </div>
    </div>
  </div>

  <!-- Session 14: Closing Remarks -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">5:45 – 6:00 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">12:45 – 1:00 PM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-close">CLOSING REMARKS</span>
      <h3 class="tl-title">Closing Remarks — A Letter from the Conveners to the Industry</h3>
      <div class="tl-speaker-info">
        <span class="tl-speaker-role">Speaker / Host:</span> <span class="tl-speaker-name">Build Tek Events</span>
      </div>
    </div>
  </div>

  <!-- Session 15: Virtual Networking Open Lounges -->
  <div class="tl-item r" data-d="1" role="listitem">
    <div class="tl-time-box">
      <div class="tl-time-bst">6:00 – 6:30 PM <span class="tz-label">BST</span></div>
      <div class="tl-time-et">1:00 – 1:30 PM <span class="tz-label">ET</span></div>
    </div>
    <div>
      <span class="tl-tag tl-tag-net">VIRTUAL NETWORKING</span>
      <h3 class="tl-title">Virtual Networking — Open Lounges</h3>
      <p class="tl-desc">Dedicated virtual breakout lounges, private discussion rooms, and open peer networking.</p>
    </div>
  </div>

</div>
</div>
</div>
</section>
<div aria-hidden="true" class="sec-divider"></div>
"""

if agenda_start != -1 and sponsorship_start != -1:
    html = html[:agenda_start] + new_agenda_section + html[sponsorship_start:]
    print("Agenda section replaced successfully")
else:
    print("ERROR: Could not locate agenda section bounds")


# =========================================================================
# 8. STRUCTURED DATA & FAQ CONSISTENCY
# =========================================================================
# Update FAQ Question 1
html = html.replace(
    'taking place on 5 October 2026 (08:00–15:05 EDT / 13:00–20:05 BST). It brings together 200 senior leaders across R&D, smart manufacturing, quality, regulatory affairs, and digital transformation to address AI in drug discovery, Pharma 4.0, FDA 2026 regulatory changes, biosimilars, and API supply chain resilience.',
    'taking place on 5 October 2026 (11:30 AM – 6:30 PM BST | 6:30 AM – 1:30 PM ET). It brings together 200+ senior leaders across Market Access, HEOR, Pricing, Commercial Strategy, and AI in Healthcare.'
)

# Update FAQ Question 4 (Who are the speakers)
html = html.replace(
    'Distinguished speakers and panelists include Andrés von der Walde (Sr. Director, Novo Nordisk), Dr. Harshad Malve (Medical Head, Kenvue), Dr. Saurabh Pandey (Cluster Lead API, Sun Pharma), Dr. Deep Upadhyay (Chief Quality Officer, Vasudha Pharma Chem), Varun Sharma (CEO, NEUVIOR), Zara Baker (Healthcare Growth Executive), Robin Hunter (President, Ribicon Group Canada), Michelle Stewart (Director, The Pangea Group), and Andrea Charles (Editorial Director, European Medical Journal).',
    'The summit faculty features 14 confirmed keynote speakers, panel moderators, and panellists: Dr. Aridita Mukherjee (Founder Director, Inside Health Communications), In Sang Lee (CEO, Divine Labs), Andres von der Walde (Senior Director, Novo Nordisk), Varun Sharma (Founder & CEO, NEUVIOR), Robin Hunter (President, Ribicon Group Canada), Dr. Harshad Malve (Medical Head, Kenvue), Zara Baker (Interim Chief Marketing & Growth Officer / Executive Advisor), Andrea Charles (Editorial Director, European Medical Journal), Michelle Stewart (Director, The Pangea Group), Dr. Deep Upadhyay (Chief Quality Officer, Vasudha Pharma Chem Ltd), Dr. Saurabh Pandey (Cluster Lead – API Manufacturing, Sun Pharmaceutical Industries Limited), Tushar Maradwar (Head – Operational Excellence, Dr. Reddy\'s Laboratories), Dr. Richa Goyal (Founder & CEO, Dual Sphere Consulting), and Srinivas Yelleka (CTO, Protofine AI).'
)

# In FAQ accordion body (around line 2417 and 2443)
html = html.replace(
    '(08:00–15:05 EDT / 13:00–20:05 BST)',
    '(11:30 AM – 6:30 PM BST | 6:30 AM – 1:30 PM ET)'
)

# Update Event Schema dates and performers
old_event_dates = '"startDate": "2026-10-05T08:00:00-04:00",\n    "endDate": "2026-10-05T15:05:00-04:00",'
new_event_dates = '"startDate": "2026-10-05T11:30:00+01:00",\n    "endDate": "2026-10-05T18:30:00+01:00",'
if old_event_dates in html:
    html = html.replace(old_event_dates, new_event_dates, 1)
    print("Event schema dates updated")

new_performers_json = """    "performer": [
      {
        "@type": "Person",
        "name": "Dr. Aridita Mukherjee",
        "jobTitle": "Founder Director",
        "worksFor": { "@type": "Organization", "name": "Inside Health Communications" }
      },
      {
        "@type": "Person",
        "name": "In Sang Lee",
        "jobTitle": "CEO",
        "worksFor": { "@type": "Organization", "name": "Divine Labs" }
      },
      {
        "@type": "Person",
        "name": "Andres von der Walde",
        "jobTitle": "Senior Director",
        "worksFor": { "@type": "Organization", "name": "Novo Nordisk", "sameAs": "https://www.novonordisk.com" }
      },
      {
        "@type": "Person",
        "name": "Varun Sharma",
        "jobTitle": "Founder & CEO",
        "worksFor": { "@type": "Organization", "name": "NEUVIOR" }
      },
      {
        "@type": "Person",
        "name": "Robin Hunter",
        "jobTitle": "President",
        "worksFor": { "@type": "Organization", "name": "Ribicon Group Canada" }
      },
      {
        "@type": "Person",
        "name": "Dr. Harshad Malve",
        "jobTitle": "Medical Head",
        "worksFor": { "@type": "Organization", "name": "Kenvue", "sameAs": "https://www.kenvue.com" }
      },
      {
        "@type": "Person",
        "name": "Zara Baker",
        "jobTitle": "Interim Chief Marketing & Growth Officer, Executive Advisor"
      },
      {
        "@type": "Person",
        "name": "Andrea Charles",
        "jobTitle": "Editorial Director",
        "worksFor": { "@type": "Organization", "name": "European Medical Journal", "sameAs": "https://www.emjreviews.com" }
      },
      {
        "@type": "Person",
        "name": "Michelle Stewart",
        "jobTitle": "Director",
        "worksFor": { "@type": "Organization", "name": "The Pangea Group" }
      },
      {
        "@type": "Person",
        "name": "Dr. Deep Upadhyay",
        "jobTitle": "Chief Quality Officer",
        "worksFor": { "@type": "Organization", "name": "Vasudha Pharma Chem Ltd", "sameAs": "https://www.vasudhapharma.com" }
      },
      {
        "@type": "Person",
        "name": "Dr. Saurabh Pandey",
        "jobTitle": "Cluster Lead – API Manufacturing – Toansa, Punjab",
        "worksFor": { "@type": "Organization", "name": "Sun Pharmaceutical Industries Limited", "sameAs": "https://www.sunpharma.com" }
      },
      {
        "@type": "Person",
        "name": "Tushar Maradwar",
        "jobTitle": "Head – Operational Excellence",
        "worksFor": { "@type": "Organization", "name": "Dr. Reddy's Laboratories", "sameAs": "https://www.drreddys.com" }
      },
      {
        "@type": "Person",
        "name": "Dr. Richa Goyal",
        "jobTitle": "Founder & CEO",
        "worksFor": { "@type": "Organization", "name": "Dual Sphere Consulting" }
      },
      {
        "@type": "Person",
        "name": "Srinivas Yelleka",
        "jobTitle": "CTO",
        "worksFor": { "@type": "Organization", "name": "Protofine AI" }
      }
    ],"""

performer_start = html.find('"performer": [')
if performer_start != -1:
    performer_end = html.find('"subEvent": [', performer_start)
    if performer_end != -1:
        html = html[:performer_start] + new_performers_json + '\n' + html[performer_end:]
        print("Schema performers updated")

with open('pharma-vista.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("ALL UPDATES COMPLETED SUCCESSFULLY!")
