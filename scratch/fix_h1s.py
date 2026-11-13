with open('ai-sec-register.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h2>REGISTRATION & CLEARANCE PORTAL</h2>', '<h1>REGISTRATION & CLEARANCE PORTAL</h1>')
with open('ai-sec-register.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('delegate-registration.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h1 class="text-gradient" style="text-align: center; font-size: 2.8rem; font-weight: 800; margin-bottom: 16px;">Application Submitted</h1>', '<h2 class="text-gradient" style="text-align: center; font-size: 2.8rem; font-weight: 800; margin-bottom: 16px;">Application Submitted</h2>')
with open('delegate-registration.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('registration.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<h1 class="text-gradient" style="text-align: center; font-size: 2.8rem; font-weight: 800; margin-bottom: 16px;">Application Submitted</h1>', '<h2 class="text-gradient" style="text-align: center; font-size: 2.8rem; font-weight: 800; margin-bottom: 16px;">Application Submitted</h2>')
with open('registration.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("H1 headings normalized successfully!")
