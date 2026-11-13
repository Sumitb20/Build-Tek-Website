import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update <head> up to <style>
head_pattern = r'(<head>).*?(<style>)'
new_head_content = r'''\1
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>BuildTek Events — Where Industry Leaders Meet What's Next | Global B2B Summits &amp; Executive Conclaves</title>
<meta name="description" content="BuildTek Events organizes premier global executive conferences and leadership summits, including the AI Security Global Virtual Summit 2027 and Pharma Vista. Connecting C-suite decision-makers across cybersecurity, AI governance, life sciences, and enterprise technology.">
<meta name="keywords" content="BuildTek Events, AI Security Global Summit 2027, AI security conference 2027, B2B summit organizers, corporate conference organizers, virtual global summits, CISO conference, cybersecurity summit, Pharma Vista Global Summit, enterprise AI risk, B2B event partnerships">
<meta name="author" content="BuildTek Events">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<link rel="canonical" href="https://buildtek.in/">

<!-- Geographic & Regional Metadata -->
<meta name="geo.region" content="IN-MH">
<meta name="geo.placename" content="Mumbai">

<!-- Favicons & Mobile Icons -->
<link rel="icon" type="image/x-icon" href="favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="mask-icon" href="safari-pinned-tab.svg" color="#7C3AED">
<meta name="theme-color" content="#070417">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://buildtek.in/">
<meta property="og:title" content="BuildTek Events — Where Industry Leaders Meet What's Next">
<meta property="og:description" content="Premier executive B2B summits and global conferences. Organizer of the AI Security Global Virtual Summit 2027 and Pharma Vista Global Summit.">
<meta property="og:image" content="https://buildtek.in/buildtek-logo-stacked.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="BuildTek Events">
<meta property="og:locale" content="en_US">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@BuildTekEvents">
<meta name="twitter:creator" content="@BuildTekEvents">
<meta name="twitter:title" content="BuildTek Events — Global B2B Leadership Summits &amp; Executive Conclaves">
<meta name="twitter:description" content="Premier executive B2B summits and global conferences. Organizer of the AI Security Global Virtual Summit 2027 and Pharma Vista Global Summit.">
<meta name="twitter:image" content="https://buildtek.in/buildtek-logo-stacked.png">

<!-- Google Analytics 4 (GA4) with Non-Blocking Async Loading -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-HJL88YELRT"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-HJL88YELRT', {
    'page_title': 'BuildTek Events — Where Industry Leaders Meet What\'s Next',
    'page_location': window.location.href,
    'send_page_view': true
  });
</script>

<!-- Structured Data: Schema.org Knowledge Graph (JSON-LD) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://buildtek.in/#organization",
      "name": "BuildTek Events",
      "legalName": "Build Tek Events",
      "url": "https://buildtek.in/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://buildtek.in/buildtek-logo-header.png",
        "width": 320,
        "height": 70
      },
      "image": "https://buildtek.in/buildtek-logo-stacked.png",
      "description": "BuildTek Events is a premier global B2B conference organizer delivering executive leadership summits, industry summits, and C-level networking assemblies across AI Security, Cyber Defense, Life Sciences, FinTech, and Enterprise Technology.",
      "email": "info@buildtek.in",
      "telephone": "+919226348550",
      "address": {
        "@type": "PostalAddress",
        "addressCountry": "IN",
        "addressRegion": "Maharashtra"
      },
      "sameAs": [
        "https://www.linkedin.com/company/build-tek-events/",
        "https://x.com/BuildTekEvents",
        "https://www.instagram.com/build_tek_events/",
        "https://www.facebook.com/profile.php?id=61587264392058"
      ],
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+919226348550",
          "contactType": "customer service",
          "email": "info@buildtek.in",
          "availableLanguage": ["English", "Hindi"]
        },
        {
          "@type": "ContactPoint",
          "email": "partners@buildtek.in",
          "contactType": "sponsorship inquiries",
          "availableLanguage": ["English"]
        }
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://buildtek.in/#website",
      "url": "https://buildtek.in/",
      "name": "BuildTek Events",
      "description": "Where Industry Leaders Meet What's Next — Executive B2B Summits, Global Conferences & Leadership Conclaves",
      "publisher": {
        "@id": "https://buildtek.in/#organization"
      },
      "inLanguage": "en-US"
    },
    {
      "@type": "WebPage",
      "@id": "https://buildtek.in/#webpage",
      "url": "https://buildtek.in/",
      "name": "BuildTek Events — Where Industry Leaders Meet What's Next",
      "isPartOf": {
        "@id": "https://buildtek.in/#website"
      },
      "about": {
        "@id": "https://buildtek.in/#organization"
      },
      "description": "BuildTek Events organizes executive B2B summits and global conferences connecting C-suite leaders across AI Security, Life Sciences, Payments, and Enterprise Technology.",
      "inLanguage": "en-US"
    },
    {
      "@type": "Event",
      "@id": "https://buildtek.in/aisecsummit.html#event",
      "name": "AI Security Global Virtual Summit 2027",
      "alternateName": ["AI-Sec 2027", "AI Security Summit 2027", "Virtual CISO Conference"],
      "description": "The premier virtual summit convening 200+ CISOs, risk officers, and enterprise cybersecurity leaders to examine adversarial AI attacks, LLM red teaming, autonomous SOC, and AI governance.",
      "startDate": "2027-02-13T08:00:00-05:00",
      "endDate": "2027-02-13T14:05:00-05:00",
      "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
      "eventStatus": "https://schema.org/EventScheduled",
      "location": {
        "@type": "VirtualLocation",
        "url": "https://buildtek.in/aisecsummit.html"
      },
      "image": "https://buildtek.in/event-01-ai-security.png",
      "organizer": {
        "@id": "https://buildtek.in/#organization"
      },
      "offers": [
        {
          "@type": "Offer",
          "name": "Standard Virtual Pass",
          "price": "199",
          "priceCurrency": "USD",
          "url": "https://buildtek.in/ai-sec-register.html",
          "availability": "https://schema.org/InStock",
          "validFrom": "2026-09-01"
        },
        {
          "@type": "Offer",
          "name": "Executive CISO Pass",
          "price": "299",
          "priceCurrency": "USD",
          "url": "https://buildtek.in/ai-sec-register.html?pass=executive",
          "availability": "https://schema.org/InStock",
          "validFrom": "2026-09-01"
        }
      ]
    },
    {
      "@type": "Event",
      "@id": "https://buildtek.in/pharma-vista.html#event",
      "name": "Pharma Vista Global Summit 2026",
      "alternateName": "Pharma Vista 2026",
      "description": "The landmark global virtual assembly of 200+ pharmaceutical and biotechnology executives, CDMO leaders, and regulatory authorities examining AI in drug discovery, data integrity, and supply chain resilience.",
      "startDate": "2026-10-05T08:00:00-04:00",
      "endDate": "2026-10-05T15:05:00-04:00",
      "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
      "eventStatus": "https://schema.org/EventMovedOnline",
      "location": {
        "@type": "VirtualLocation",
        "url": "https://buildtek.in/pharma-vista.html"
      },
      "image": "https://buildtek.in/event-past-pharma-vista-2026.png",
      "organizer": {
        "@id": "https://buildtek.in/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://buildtek.in/"
        }
      ]
    }
  ]
}
</script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
\2'''

content = re.sub(head_pattern, new_head_content, content, count=1, flags=re.DOTALL)

# 2. Update hero background image to WebP
content = content.replace("url('hero-summit-bg.jpg')", "url('hero-summit-bg.webp')")

# 3. Update events images in DATA to WebP
content = content.replace("img:'event-01-ai-security.png'", "img:'event-01-ai-security.webp'")
content = content.replace("img:'event-02-payments-fraud.png'", "img:'event-02-payments-fraud.webp'")
content = content.replace("img:'event-03-pharma-vista.png'", "img:'event-03-pharma-vista.webp'")
content = content.replace('"img": "event-past-pharma-vista-2026.png"', '"img": "event-past-pharma-vista-2026.webp"')

# 4. Add GA4 event tracking listeners in script
ga_listeners = '''
/* ===== ANALYTICS EVENT TRACKING (GA4) ===== */
(function(){
  // Track clicks on AI-Sec Summit exploration & registration
  document.querySelectorAll('a[href*="aisecsummit"], a[href*="ai-sec-register"]').forEach(function(el){
    el.addEventListener('click',function(){
      if(typeof gtag==='function'){
        gtag('event','aisec_registration_click',{
          'event_category':'conversion',
          'event_label':el.textContent.trim()||'AI-Sec Explore',
          'link_url':el.href,
          'page_location':window.location.href
        });
      }
    });
  });

  // Track Partner / Sponsorship inquiries
  document.querySelectorAll('a[href="#partner"], a[href*="partners@buildtek.in"]').forEach(function(el){
    el.addEventListener('click',function(){
      if(typeof gtag==='function'){
        gtag('event','aisec_sponsorship_click',{
          'event_category':'lead_generation',
          'event_label':'Partner CTA',
          'page_location':window.location.href
        });
      }
    });
  });

  // Track WhatsApp desk
  document.querySelectorAll('a[href*="wa.me"]').forEach(function(el){
    el.addEventListener('click',function(){
      if(typeof gtag==='function'){
        gtag('event','contact_whatsapp',{
          'event_category':'engagement',
          'event_label':'WhatsApp Contact Desk'
        });
      }
    });
  });

  // Track Telephone clicks
  document.querySelectorAll('a[href^="tel:"]').forEach(function(el){
    el.addEventListener('click',function(){
      if(typeof gtag==='function'){
        gtag('event','contact_call',{
          'event_category':'engagement',
          'event_label':el.href
        });
      }
    });
  });

  // Scroll depth tracking
  var scrollMarks={25:false,50:false,75:false,90:false};
  window.addEventListener('scroll',function(){
    var docH=document.body.scrollHeight-window.innerHeight;
    if(docH<=0)return;
    var scrollPct=Math.round((window.scrollY/docH)*100);
    [25,50,75,90].forEach(function(mark){
      if(scrollPct>=mark&&!scrollMarks[mark]){
        scrollMarks[mark]=true;
        if(typeof gtag==='function'){
          gtag('event','scroll_depth',{
            'event_category':'engagement',
            'value':mark,
            'event_label':mark+'% scrolled'
          });
        }
      }
    });
  },{passive:true});
})();
'''

# Place ga_listeners inside the existing main script before closing
content = content.replace('/* painted scene */', ga_listeners + '\n/* painted scene */')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully!")
