with open('ai-sec-register.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Add canonical and JSON-LD
old_head = '<link rel="icon" type="image/svg+xml" href="./assets/ai-sec/favicon.svg">'
new_head = '''<link rel="icon" type="image/svg+xml" href="./assets/ai-sec/favicon.svg">
    <link rel="canonical" href="https://buildtek.in/ai-sec-register.html">
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "AI-Sec Summit 2027 — Official Registration Portal",
      "url": "https://buildtek.in/ai-sec-register.html",
      "description": "Official registration and credentialing portal for the AI-Sec Global Summit 2027.",
      "isPartOf": {
        "@type": "WebSite",
        "name": "BuildTek Events",
        "url": "https://buildtek.in/"
      }
    }
    </script>'''

if old_head in c:
    c = c.replace(old_head, new_head)
    print("Added canonical and JSON-LD to ai-sec-register.html")

# Update GA4 events
old_ga_init = """      gtag('config', 'G-HJL88YELRT', {
        'page_title': 'AI-Sec Summit 2027 Registration Portal',
        'send_page_view': true
      });"""

new_ga_init = """      gtag('config', 'G-HJL88YELRT', {
        'page_title': 'AI-Sec Summit 2027 Registration Portal',
        'send_page_view': true
      });
      gtag('event', 'aisec_event_page_view', {
        'page_title': 'AI-Sec Summit 2027 Registration Portal',
        'page_location': window.location.href,
        'event_name': 'AI Security Summit Registration Portal'
      });"""

if old_ga_init in c:
    c = c.replace(old_ga_init, new_ga_init)
    print("Added aisec_event_page_view to ai-sec-register.html")

# Add form_start and form_submit + registration_complete
old_fetch = """            fetch(form.action, {
                method: "POST",
                body: new FormData(form),
                headers: { 'Accept': 'application/json' }
            }).then(response => {
                if (response.ok) {
                    if (typeof gtag === 'function') {
                        gtag('event', 'sign_up', {
                            method: isCisoPass ? 'ciso_executive_pass' : 'standard_virtual_pass',
                            event_category: 'registration',
                            event_label: 'AI-Sec Summit 2027'
                        });
                        gtag('event', 'generate_lead', {
                            currency: 'USD',
                            value: isCisoPass ? 299.0 : 199.0
                        });
                    }"""

new_fetch = """            if (typeof gtag === 'function') {
                gtag('event', 'aisec_form_submit', {
                    'form_type': 'delegate_registration',
                    'pass_type': isCisoPass ? 'Executive CISO Pass' : 'Standard Virtual Pass'
                });
            }

            fetch(form.action, {
                method: "POST",
                body: new FormData(form),
                headers: { 'Accept': 'application/json' }
            }).then(response => {
                if (response.ok) {
                    if (typeof gtag === 'function') {
                        gtag('event', 'sign_up', {
                            method: isCisoPass ? 'ciso_executive_pass' : 'standard_virtual_pass',
                            event_category: 'registration',
                            event_label: 'AI-Sec Summit 2027'
                        });
                        gtag('event', 'generate_lead', {
                            currency: 'USD',
                            value: isCisoPass ? 299.0 : 199.0
                        });
                        gtag('event', 'aisec_registration_complete', {
                            'form_type': 'delegate_registration',
                            'pass_type': isCisoPass ? 'Executive CISO Pass' : 'Standard Virtual Pass',
                            'value': isCisoPass ? 299.0 : 199.0,
                            'currency': 'USD'
                        });
                    }"""

if old_fetch in c:
    c = c.replace(old_fetch, new_fetch)
    print("Updated form submission & conversion events in ai-sec-register.html")

# Add focusin listener for form start
form_start_listener = """
        // Track Form Start
        document.addEventListener('DOMContentLoaded', () => {
            let regFormStarted = false;
            const regForm = document.getElementById('summit-reg-form');
            if (regForm) {
                regForm.addEventListener('focusin', () => {
                    if (!regFormStarted) {
                        regFormStarted = true;
                        if (typeof gtag === 'function') {
                            gtag('event', 'aisec_form_start', {
                                'form_type': 'delegate_registration',
                                'event_category': 'registration'
                            });
                        }
                    }
                });
            }
        });
"""

c = c.replace('window.addEventListener(\'DOMContentLoaded\', () => {', form_start_listener + '\n        window.addEventListener(\'DOMContentLoaded\', () => {')

with open('ai-sec-register.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Saved updated ai-sec-register.html successfully!")
