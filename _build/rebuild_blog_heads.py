import sys, os, re, json, html
sys.path.insert(0, os.path.dirname(__file__))
from articles import ARTICLES, SITE, ORG, PUBLISHED

TODAY = "2026-08-30"

def head_for(a, prev, nxt):
    url  = f"{SITE}/{a['slug']}.html"
    ogimg= f"{SITE}/assets/og/{a['slug']}.jpg"
    title= a['title'] if len(a['title'])>62 else a['title']+" | BuildTek"
    esc  = lambda s: html.escape(s, quote=True)

    graph = [
      {"@type":"Organization","@id":f"{SITE}/#organization","name":ORG,"url":SITE,
       "logo":{"@type":"ImageObject","url":f"{SITE}/assets/opt/logo.jpg","width":600,"height":245},
       "email":"registers@buildtek.in",
       "contactPoint":[{"@type":"ContactPoint","telephone":"+91-9226348550",
                        "email":"registers@buildtek.in","contactType":"customer support",
                        "areaServed":["IN","AE"],"availableLanguage":"en"}],
       "sameAs":["https://www.linkedin.com/company/build-tek-events/",
                 "https://x.com/BuildTekEvents",
                 "https://www.instagram.com/build_tek_events/",
                 "https://www.facebook.com/profile.php?id=61587264392058"]},
      {"@type":"WebSite","@id":f"{SITE}/#website","url":SITE,"name":ORG,
       "publisher":{"@id":f"{SITE}/#organization"},"inLanguage":"en"},
      {"@type":"BlogPosting","@id":url+"#article",
       "isPartOf":{"@id":f"{SITE}/#website"},
       "headline":a['h1'][:110],"name":a['h1'],"description":a['desc'],
       "articleSection":a['cat'],"keywords":", ".join(a['kw']),
       "wordCount":a.get('words',1200),
       "datePublished":PUBLISHED,"dateModified":TODAY,
       "inLanguage":"en",
       "mainEntityOfPage":{"@type":"WebPage","@id":url},
       "url":url,
       "image":{"@type":"ImageObject","url":ogimg,"width":1200,"height":630},
       "author":{"@type":"Organization","@id":f"{SITE}/#organization","name":ORG,"url":SITE},
       "publisher":{"@id":f"{SITE}/#organization"},
       "timeRequired":f"PT{a['mins']}M"},
      {"@type":"BreadcrumbList","@id":url+"#breadcrumb","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Insights","item":f"{SITE}/blog.html"},
        {"@type":"ListItem","position":3,"name":a['h1']}]},
    ]
    ld = json.dumps({"@context":"https://schema.org","@graph":graph},
                    ensure_ascii=False, separators=(',',':'))

    rel = ""
    if prev: rel += f'\n  <link rel="prev" href="{SITE}/{prev["slug"]}.html" />'
    if nxt:  rel += f'\n  <link rel="next" href="{SITE}/{nxt["slug"]}.html" />'

    return f'''<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' https: data: 'unsafe-inline'; font-src 'self' https://fonts.gstatic.com https://fonts.googleapis.com; img-src 'self' https: data: blob:; connect-src 'self' https:; frame-src 'self' https://challenges.cloudflare.com;" />
  <meta name="referrer" content="strict-origin-when-cross-origin" />

  <title>{esc(title)}</title>
  <meta name="description" content="{esc(a['desc'])}" />
  <link rel="canonical" href="{url}" />{rel}
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
  <meta name="author" content="{ORG}" />

  <!-- Open Graph -->
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{esc(a['h1'])}" />
  <meta property="og:description" content="{esc(a['desc'])}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{ogimg}" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:image:alt" content="{esc(a['h1'])}" />
  <meta property="og:site_name" content="{ORG}" />
  <meta property="og:locale" content="en_US" />
  <meta property="article:published_time" content="{PUBLISHED}" />
  <meta property="article:modified_time" content="{TODAY}" />
  <meta property="article:section" content="{esc(a['cat'])}" />
  {chr(10).join(f'  <meta property="article:tag" content="{esc(k)}" />' for k in a['kw'])}

  <!-- Twitter / X -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:site" content="@BuildTekEvents" />
  <meta name="twitter:title" content="{esc(a['h1'])}" />
  <meta name="twitter:description" content="{esc(a['desc'])}" />
  <meta name="twitter:image" content="{ogimg}" />
  <meta name="twitter:image:alt" content="{esc(a['h1'])}" />

  <!-- Icons -->
  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
  <link rel="mask-icon" href="/safari-pinned-tab.svg" color="#D4AF37" />
  <meta name="theme-color" content="#050409" />

  <link rel="sitemap" type="application/xml" href="{SITE}/sitemap.xml" />

  <script type="application/ld+json">{ld}</script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="dns-prefetch" href="//formsubmit.co" />
  <link rel="dns-prefetch" href="//www.googletagmanager.com" />
  <link rel="stylesheet" href="assets/css/style.min.css" />

  <script async src="https://www.googletagmanager.com/gtag/js?id=G-HJL88YELRT"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-HJL88YELRT');
  </script>
</head>'''

changed = 0
for i, a in enumerate(ARTICLES):
    path = a['slug'] + '.html'
    if not os.path.exists(path):
        print("SKIP (missing)", path); continue
    src = open(path, encoding='utf-8').read()
    # count real words to feed schema
    body = re.sub(r'(?s)<(script|style).*?</\1>', ' ', src)
    a['words'] = len(re.sub(r'(?s)<[^>]+>', ' ', body).split())
    prev = ARTICLES[i-1] if i > 0 else None
    nxt  = ARTICLES[i+1] if i < len(ARTICLES)-1 else None
    out = re.sub(r'(?s)<head>.*?</head>', lambda m: head_for(a, prev, nxt), src, count=1)
    if out != src:
        open(path, 'w', encoding='utf-8').write(out)
        changed += 1
        print(f"  ✓ {a['words']:>5}w  {path[:62]}")
print(f"\nrebuilt {changed} blog heads")
