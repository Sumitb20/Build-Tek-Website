with open('aisecsummit.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update GA4 section
old_ga = """      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-HJL88YELRT', {
        'page_title': 'AI Security Summit 2027',
        'page_location': window.location.href,
        'send_page_view': true
      });"""

new_ga = """      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-HJL88YELRT', {
        'page_title': 'AI Security Summit 2027 | 13 Feb — Virtual CISO Conference',
        'page_location': window.location.href,
        'send_page_view': true
      });

      // Dispatch specific AI Security Summit Page View
      gtag('event', 'aisec_event_page_view', {
        'page_title': 'AI Security Summit 2027',
        'page_location': window.location.href,
        'event_name': 'AI Security Global Summit 2027'
      });"""

if old_ga in c:
    c = c.replace(old_ga, new_ga)
    print("Updated GA4 init in aisecsummit.html")
else:
    print("Warning: old_ga not found exact match")

# 2. Update event listeners in GA4
old_listeners = """        // Registration button clicks
        document.querySelectorAll('.trigger-reg-warp, a[href*="ai-sec-register"]').forEach(function(btn) {
          btn.addEventListener('click', function() {
            gtag('event', 'begin_registration', {
              'event_category': 'conversion',
              'event_label': btn.textContent.trim(),
              'value': 1
            });
          });
        });

        // Partner modal opens
        document.querySelectorAll('[onclick*="togglePartnerModal"]').forEach(function(btn) {
          btn.addEventListener('click', function() {
            gtag('event', 'partner_inquiry_click', {
              'event_category': 'conversion',
              'event_label': 'Partner CTA'
            });
          });
        });"""

new_listeners = """        // Registration button clicks (Standard + aisec_registration_click)
        document.querySelectorAll('.trigger-reg-warp, a[href*="ai-sec-register"]').forEach(function(btn) {
          btn.addEventListener('click', function() {
            gtag('event', 'begin_registration', {
              'event_category': 'conversion',
              'event_label': btn.textContent.trim(),
              'value': 1
            });
            gtag('event', 'aisec_registration_click', {
              'event_category': 'conversion',
              'event_label': btn.textContent.trim(),
              'link_url': btn.getAttribute('href') || 'ai-sec-register.html',
              'page_location': window.location.href
            });
          });
        });

        // Partner modal opens (Standard + aisec_sponsorship_click)
        document.querySelectorAll('[onclick*="togglePartnerModal"]').forEach(function(btn) {
          btn.addEventListener('click', function() {
            gtag('event', 'partner_inquiry_click', {
              'event_category': 'conversion',
              'event_label': 'Partner CTA'
            });
            gtag('event', 'aisec_sponsorship_click', {
              'event_category': 'conversion',
              'event_label': btn.textContent.trim() || 'Partner CTA',
              'page_location': window.location.href
            });
          });
        });

        // Track Meaningful Agenda Engagement (aisec_agenda_view)
        var agendaSection = document.getElementById('agenda');
        if (agendaSection && 'IntersectionObserver' in window) {
          var agendaObserver = new IntersectionObserver(function(entries) {
            if (entries[0].isIntersecting) {
              gtag('event', 'aisec_agenda_view', {
                'event_category': 'engagement',
                'event_label': 'Agenda Section In View'
              });
              agendaObserver.unobserve(agendaSection);
            }
          }, { threshold: 0.2 });
          agendaObserver.observe(agendaSection);
        }

        // Partner Form Interaction & Lead Tracking (aisec_form_start, aisec_form_submit, aisec_sponsorship_lead)
        var partnerForm = document.getElementById('partner-form');
        var pFormStarted = false;
        if (partnerForm) {
          partnerForm.addEventListener('focusin', function() {
            if (!pFormStarted) {
              pFormStarted = true;
              gtag('event', 'aisec_form_start', {
                'form_type': 'sponsorship_inquiry',
                'event_category': 'lead_generation'
              });
            }
          });
          partnerForm.addEventListener('submit', function() {
            gtag('event', 'aisec_form_submit', {
              'form_type': 'sponsorship_inquiry',
              'event_category': 'conversion'
            });
            gtag('event', 'aisec_sponsorship_lead', {
              'form_type': 'sponsorship_inquiry',
              'partnership_tier': document.getElementById('pType') ? document.getElementById('pType').value : 'General',
              'event_category': 'conversion'
            });
          });
        }"""

if old_listeners in c:
    c = c.replace(old_listeners, new_listeners)
    print("Updated event listeners in aisecsummit.html")
else:
    print("Warning: old_listeners not found exact match")

# 3. Add loading="lazy" and decoding="async" to images
c = c.replace(
    '<img src="./assets/ai-sec/buildtek-events-logo.jpg" alt="BuildTek Events" class="organizer-logo-img">',
    '<img src="./assets/ai-sec/buildtek-events-logo.jpg" alt="BuildTek Events" class="organizer-logo-img" loading="lazy" decoding="async">'
)
c = c.replace(
    '<img src="./assets/ai-sec/cybertorch-logo.png" alt="CyberTorch" class="strategic-partner-logo">',
    '<img src="./assets/ai-sec/cybertorch-logo.png" alt="CyberTorch" class="strategic-partner-logo" loading="lazy" decoding="async">'
)
c = c.replace(
    '<img src="./assets/ai-sec/aerotech-logo.png" alt="Aerotech B2B" class="strategic-partner-logo" style="height: 32px;">',
    '<img src="./assets/ai-sec/aerotech-logo.png" alt="Aerotech B2B" class="strategic-partner-logo" style="height: 32px;" loading="lazy" decoding="async">'
)
c = c.replace(
    '<img src="./assets/ai-sec/tasktech-logo.jpg" alt="Task Tech Media" class="strategic-partner-logo" style="height: 36px; border-radius: 3px; object-fit: contain;">',
    '<img src="./assets/ai-sec/tasktech-logo.jpg" alt="Task Tech Media" class="strategic-partner-logo" style="height: 36px; border-radius: 3px; object-fit: contain;" loading="lazy" decoding="async">'
)
c = c.replace(
    '<img src="./assets/ai-sec/cybertorch-logo.png" alt="CyberTorch Strategic Partner" class="sp-showcase-logo">',
    '<img src="./assets/ai-sec/cybertorch-logo.png" alt="CyberTorch Strategic Partner" class="sp-showcase-logo" loading="lazy" decoding="async">'
)
c = c.replace(
    '<img src="./assets/ai-sec/aerotech-logo.png" alt="Aerotech B2B" class="sp-showcase-logo" style="height: 40px;">',
    '<img src="./assets/ai-sec/aerotech-logo.png" alt="Aerotech B2B" class="sp-showcase-logo" style="height: 40px;" loading="lazy" decoding="async">'
)
c = c.replace(
    '<img src="./assets/ai-sec/tasktech-logo.jpg" alt="Task Tech Media" class="sp-showcase-logo" style="height: 60px; object-fit: contain; border-radius: 4px;">',
    '<img src="./assets/ai-sec/tasktech-logo.jpg" alt="Task Tech Media" class="sp-showcase-logo" style="height: 60px; object-fit: contain; border-radius: 4px;" loading="lazy" decoding="async">'
)

with open('aisecsummit.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Saved updated aisecsummit.html successfully!")
