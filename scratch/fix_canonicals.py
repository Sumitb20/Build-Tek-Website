import re

# 1. speaker-kit.html
with open('speaker-kit.html', 'r', encoding='utf-8') as f:
    c = f.read()
if 'rel="canonical"' not in c:
    c = c.replace('<meta name="description"', '<link rel="canonical" href="https://buildtek.in/speaker-kit.html">\n  <meta name="description"')
    with open('speaker-kit.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed canonical in speaker-kit.html")

# 2. delegate-registration.html
with open('delegate-registration.html', 'r', encoding='utf-8') as f:
    c = f.read()
if 'rel="canonical"' not in c:
    c = c.replace('<meta name="description"', '<link rel="canonical" href="https://buildtek.in/delegate-registration.html">\n  <meta name="description"')
    with open('delegate-registration.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed canonical in delegate-registration.html")

# 3. registration.html
with open('registration.html', 'r', encoding='utf-8') as f:
    c = f.read()
if 'rel="canonical"' not in c:
    c = c.replace('<meta name="description"', '<link rel="canonical" href="https://buildtek.in/delegate-registration.html">\n  <meta name="description"')
    with open('registration.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed canonical in registration.html")

# 4. pharma-vista.html
with open('pharma-vista.html', 'r', encoding='utf-8') as f:
    c = f.read()
if 'https://pharmavistaglobal.com/' in c and 'rel="canonical"' in c:
    c = c.replace('href="https://pharmavistaglobal.com/" rel="canonical"', 'href="https://buildtek.in/pharma-vista.html" rel="canonical"')
    with open('pharma-vista.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Fixed canonical in pharma-vista.html to https://buildtek.in/pharma-vista.html")

