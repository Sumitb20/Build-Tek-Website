/**
 * AI-SEC GLOBAL SUMMIT 2027 — CORE CLIENT ENGINE & CONVERSION MODULES
 * Modules:
 * 1. Global UTM & Referral Capture
 * 2. Robust Countdown Timer (Timezone-Aware)
 * 3. Dynamic Local Timezone Converter (Intl API)
 * 4. Add to Calendar (Google, Outlook, Apple .ics)
 * 5. Dynamic Staged-Reveal Speaker Grid
 * 6. Confirmed Companies Logo Wall
 * 7. FAQ Accordion Engine (Accessible ARIA)
 * 8. 2-Tier Threat Matrix Lead Magnet Engine
 * 9. Sticky Mobile CTA Bar
 * 10. Lightweight Cookie Consent & Tag Manager
 * 11. Warp Transition & Modal Controls
 * 12. Ambient Cyber Particles Background
 * 13. Metric Counter & Scroll Animations
 */

(function () {
    'use strict';

    // ==========================================================================
    // 01 — GLOBAL UTM & REFERRER CAPTURE (TASK 6.4)
    // ==========================================================================
    function captureTrafficData() {
        try {
            const urlParams = new URLSearchParams(window.location.search);
            const utmKeys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'];
            const trafficData = {};

            utmKeys.forEach(key => {
                if (urlParams.has(key)) {
                    trafficData[key] = urlParams.get(key);
                }
            });

            // Store in sessionStorage if new UTMs detected
            if (Object.keys(trafficData).length > 0) {
                sessionStorage.setItem('aisec_utm_params', JSON.stringify(trafficData));
            }

            // Capture referrer if external
            if (document.referrer && !document.referrer.includes(window.location.hostname)) {
                sessionStorage.setItem('aisec_initial_referrer', document.referrer);
            }
        } catch (e) {
            console.warn('Traffic capture error:', e);
        }
    }
    captureTrafficData();

    // ==========================================================================
    // 02 — TRACKING DISPATCHER (TASK 6.4)
    // ==========================================================================
    window.aiSecTrack = function (eventName, eventParams) {
        eventParams = eventParams || {};
        eventParams.page_location = window.location.href;
        eventParams.page_title = document.title;

        // Attach stored UTMs if present
        try {
            const savedUtms = JSON.parse(sessionStorage.getItem('aisec_utm_params') || '{}');
            Object.assign(eventParams, savedUtms);
        } catch (e) {}

        // Google Analytics 4
        if (typeof window.gtag === 'function') {
            window.gtag('event', eventName, eventParams);
        }

        // Meta Pixel (if consent granted and ID configured)
        if (typeof window.fbq === 'function' && window.hasAdConsent) {
            window.fbq('trackCustom', eventName, eventParams);
        }

        // LinkedIn Insight (if consent granted and ID configured)
        if (typeof window.lintrk === 'function' && window.hasAdConsent) {
            window.lintrk('track', { conversion_id: eventName });
        }
    };

    function initSummit() {
        const CFG = window.AI_SEC_CONFIG || {};
        const eventDateTarget = new Date('2027-02-12T13:00:00Z').getTime(); // 08:00 AM ET in UTC

        // ==========================================================================
        // 03 — ROBUST COUNTDOWN TIMER (TASK 6.3)
        // ==========================================================================
        const elDays = document.getElementById('cd-days');
        const elHours = document.getElementById('cd-hours');
        const elMins = document.getElementById('cd-mins');
        const elSecs = document.getElementById('cd-secs');
        const cdLabel = document.querySelector('.countdown-label');

        function updateCountdown() {
            const now = Date.now();
            const distance = eventDateTarget - now;
            const eventEnd = eventDateTarget + (6 * 60 + 5) * 60 * 1000; // 6h 5m duration

            if (distance > 0) {
                const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const mins = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                const secs = Math.floor((distance % (1000 * 60)) / 1000);

                if (elDays) elDays.textContent = String(days).padStart(2, '0');
                if (elHours) elHours.textContent = String(hours).padStart(2, '0');
                if (elMins) elMins.textContent = String(mins).padStart(2, '0');
                if (elSecs) elSecs.textContent = String(secs).padStart(2, '0');
            } else if (now <= eventEnd) {
                if (cdLabel) cdLabel.textContent = "SUMMIT IS NOW LIVE // JOIN ONLINE:";
                if (elDays) elDays.textContent = "00";
                if (elHours) elHours.textContent = "00";
                if (elMins) elMins.textContent = "LIVE";
                if (elSecs) elSecs.textContent = "NOW";
            } else {
                if (cdLabel) cdLabel.textContent = "SUMMIT CONCLUDED // ON-DEMAND REPLAY:";
                if (elDays) elDays.textContent = "00";
                if (elHours) elHours.textContent = "00";
                if (elMins) elMins.textContent = "00";
                if (elSecs) elSecs.textContent = "00";
            }
        }
        setInterval(updateCountdown, 1000);
        updateCountdown();

        // ==========================================================================
        // 04 — DYNAMIC GLOBAL TIMEZONE CONVERTER & AGENDA SYNC (TASK 4.4)
        // ==========================================================================
        const localTimeDisplay = document.getElementById('user-local-time');
        const heroTzSelect = document.getElementById('tz-selector');
        const agendaTzSelect = document.getElementById('agenda-tz-selector');
        const agendaTzLabel = document.getElementById('agenda-current-tz-label');
        const factSummitHours = document.getElementById('fact-summit-hours');
        const phase1Hours = document.getElementById('phase-1-hours');
        const phase2Hours = document.getElementById('phase-2-hours');
        const phaseRtHours = document.getElementById('phase-roundtable-hours');
        const breakHours = document.getElementById('agenda-break-hours');

        function formatInTimezone(tzInput) {
            try {
                let targetZone = 'America/New_York';
                let labelText = 'New York (ET)';

                if (!tzInput || tzInput === 'LOCAL') {
                    try {
                        targetZone = Intl.DateTimeFormat().resolvedOptions().timeZone || 'America/New_York';
                        labelText = targetZone.replace('_', ' ') + ' (Local)';
                    } catch (err) {
                        targetZone = 'America/New_York';
                        labelText = 'New York (ET)';
                    }
                } else if (tzInput === 'America/New_York' || tzInput === 'ET') {
                    targetZone = 'America/New_York';
                    labelText = 'New York (ET)';
                } else if (tzInput === 'America/Los_Angeles' || tzInput === 'PT') {
                    targetZone = 'America/Los_Angeles';
                    labelText = 'San Francisco (PT)';
                } else if (tzInput === 'Europe/London' || tzInput === 'GMT' || tzInput === 'BST') {
                    targetZone = 'Europe/London';
                    labelText = 'London (GMT)';
                } else if (tzInput === 'Europe/Paris' || tzInput === 'CET') {
                    targetZone = 'Europe/Paris';
                    labelText = 'Paris / Berlin (CET)';
                } else if (tzInput === 'Asia/Kolkata' || tzInput === 'IST') {
                    targetZone = 'Asia/Kolkata';
                    labelText = 'India (IST)';
                } else if (tzInput === 'Asia/Singapore' || tzInput === 'SGT') {
                    targetZone = 'Asia/Singapore';
                    labelText = 'Singapore / HK (SGT)';
                } else if (tzInput === 'Australia/Sydney' || tzInput === 'AEDT') {
                    targetZone = 'Australia/Sydney';
                    labelText = 'Sydney (AEDT)';
                } else if (tzInput === 'UTC') {
                    targetZone = 'UTC';
                    labelText = 'UTC / Coordinated';
                } else {
                    targetZone = tzInput;
                    labelText = tzInput;
                }

                // Formatters
                const timeFormatterWithTz = new Intl.DateTimeFormat('en-US', {
                    timeZone: targetZone,
                    hour: '2-digit',
                    minute: '2-digit',
                    hour12: true,
                    timeZoneName: 'short'
                });

                const timeFormatter = new Intl.DateTimeFormat('en-US', {
                    timeZone: targetZone,
                    hour: '2-digit',
                    minute: '2-digit',
                    hour12: true
                });

                const dateFormatter = new Intl.DateTimeFormat('en-US', {
                    timeZone: targetZone,
                    weekday: 'short',
                    month: 'short',
                    day: 'numeric'
                });

                // Summit Overall Times (13:00 UTC - 19:05 UTC)
                const startDate = new Date('2027-02-12T13:00:00Z');
                const endDate = new Date('2027-02-12T19:05:00Z');
                const startStr = timeFormatter.format(startDate);
                const endStr = timeFormatterWithTz.format(endDate);
                const dateStr = dateFormatter.format(startDate);

                // 1. Hero local time badge
                if (localTimeDisplay) {
                    localTimeDisplay.innerHTML = `<span class="tz-date">${dateStr}</span> &nbsp;·&nbsp; <strong class="tz-hours" style="color:#00f0ff;">${startStr} – ${endStr}</strong>`;
                }

                // 2. Agenda current timezone indicator
                if (agendaTzLabel) {
                    agendaTzLabel.textContent = labelText;
                }

                // 3. Hero Fact Card (Summit Hours)
                if (factSummitHours) {
                    factSummitHours.textContent = `${startStr} - ${endStr}`;
                }

                // 4. Agenda Phase I (13:00 UTC - 15:45 UTC)
                if (phase1Hours) {
                    const p1End = new Date('2027-02-12T15:45:00Z');
                    phase1Hours.textContent = `${startStr} – ${timeFormatterWithTz.format(p1End)}`;
                }

                // 5. Agenda Phase II (15:45 UTC - 18:25 UTC)
                if (phase2Hours) {
                    const p2Start = new Date('2027-02-12T15:45:00Z');
                    const p2End = new Date('2027-02-12T18:25:00Z');
                    phase2Hours.textContent = `${timeFormatter.format(p2Start)} – ${timeFormatterWithTz.format(p2End)}`;
                }

                // 6. Agenda Roundtable (18:25 UTC - 19:05 UTC)
                if (phaseRtHours) {
                    const rtStart = new Date('2027-02-12T18:25:00Z');
                    phaseRtHours.textContent = `${timeFormatter.format(rtStart)} – ${endStr}`;
                }

                // 7. Networking Break (16:50 UTC - 17:20 UTC)
                if (breakHours) {
                    const bStart = new Date('2027-02-12T16:50:00Z');
                    const bEnd = new Date('2027-02-12T17:20:00Z');
                    breakHours.textContent = `${timeFormatter.format(bStart)} – ${timeFormatterWithTz.format(bEnd)} (30 Mins):`;
                }

                // 8. Individual Session Cards with [data-start] and [data-end]
                document.querySelectorAll('.agenda-card[data-start][data-end]').forEach(card => {
                    const sStart = new Date(card.getAttribute('data-start'));
                    const sEnd = new Date(card.getAttribute('data-end'));
                    const timeSpan = card.querySelector('.agenda-time-val');
                    if (timeSpan && !isNaN(sStart.getTime()) && !isNaN(sEnd.getTime())) {
                        const svgIcon = `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>`;
                        timeSpan.innerHTML = `${svgIcon} ${timeFormatter.format(sStart)} – ${timeFormatter.format(sEnd)}`;
                    }
                });

            } catch (e) {
                console.warn('Timezone conversion error:', e);
            }
        }

        function syncTimezoneSelectors(selectedVal) {
            if (heroTzSelect && heroTzSelect.value !== selectedVal) {
                heroTzSelect.value = selectedVal;
            }
            if (agendaTzSelect && agendaTzSelect.value !== selectedVal) {
                agendaTzSelect.value = selectedVal;
            }
            formatInTimezone(selectedVal);
        }

        // Initialize with auto-detected local timezone
        formatInTimezone('LOCAL');

        // Setup dropdown listeners
        [heroTzSelect, agendaTzSelect].forEach(selectEl => {
            if (!selectEl) return;
            try {
                const detected = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
                for (let opt of selectEl.options) {
                    if (opt.value === detected || (detected.includes('Calcutta') && opt.value === 'Asia/Kolkata')) {
                        opt.selected = true;
                        break;
                    }
                }
            } catch (e) {}

            selectEl.addEventListener('change', (e) => {
                syncTimezoneSelectors(e.target.value);
                if (typeof window.aiSecTrack === 'function') {
                    window.aiSecTrack('timezone_changed', { selected_timezone: e.target.value });
                }
            });
        });

        // ==========================================================================
        // 05 — ADD TO CALENDAR CONTROL (TASK 4.4)
        // ==========================================================================
        const calTitle = encodeURIComponent("AI-Sec Global Summit 2027");
        const calDesc = encodeURIComponent("AI-Sec Global Summit 2027 — Premier virtual summit for CISOs and security architects examining adversarial AI exploitation, LLM red teaming, and autonomous SOC defense.\n\nVirtual Summit Portal: https://buildtek.in/aisecsummit.html\nAccess Credentials: Sent upon registration verification.");
        const calLoc = encodeURIComponent("Virtual Global Broadcast (https://buildtek.in/aisecsummit.html)");
        
        // 2027-02-12 13:00:00 UTC to 2027-02-12 19:05:00 UTC
        const calStartISO = "20270212T130000Z";
        const calEndISO = "20270212T190500Z";

        const btnGoogleCal = document.querySelectorAll('.cal-link-google');
        btnGoogleCal.forEach(btn => {
            btn.href = `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${calTitle}&dates=${calStartISO}/${calEndISO}&details=${calDesc}&location=${calLoc}`;
            btn.target = "_blank";
            btn.rel = "noopener noreferrer";
            btn.addEventListener('click', () => {
                window.aiSecTrack('add_to_calendar_click', { calendar_type: 'google' });
            });
        });

        const btnOutlookCal = document.querySelectorAll('.cal-link-outlook');
        btnOutlookCal.forEach(btn => {
            btn.href = `https://outlook.live.com/calendar/0/deeplink/compose?subject=${calTitle}&startdt=2027-02-12T13:00:00Z&enddt=2027-02-12T19:05:00Z&body=${calDesc}&location=${calLoc}`;
            btn.target = "_blank";
            btn.rel = "noopener noreferrer";
            btn.addEventListener('click', () => {
                window.aiSecTrack('add_to_calendar_click', { calendar_type: 'outlook' });
            });
        });

        const btnIcsCal = document.querySelectorAll('.cal-link-ics');
        btnIcsCal.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                window.aiSecTrack('add_to_calendar_click', { calendar_type: 'ics_download' });
                
                const icsContent = [
                    'BEGIN:VCALENDAR',
                    'VERSION:2.0',
                    'PRODID:-//BuildTek Events//AI-Sec Global Summit 2027//EN',
                    'CALSCALE:GREGORIAN',
                    'METHOD:PUBLISH',
                    'BEGIN:VEVENT',
                    'UID:aisec2027-' + Date.now() + '@buildtek.in',
                    'DTSTAMP:' + calStartISO,
                    'DTSTART:' + calStartISO,
                    'DTEND:' + calEndISO,
                    'SUMMARY:AI-Sec Global Summit 2027',
                    'DESCRIPTION:Premier virtual summit for CISOs and cybersecurity leaders examining adversarial AI, prompt injection defenses, LLM firewalls, and model governance.\\n\\nPortal: https://buildtek.in/aisecsummit.html',
                    'LOCATION:Virtual Global Broadcast (https://buildtek.in/aisecsummit.html)',
                    'STATUS:CONFIRMED',
                    'END:VEVENT',
                    'END:VCALENDAR'
                ].join('\r\n');

                const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' });
                const link = document.createElement('a');
                link.href = window.URL.createObjectURL(blob);
                link.setAttribute('download', 'AI-Sec-Global-Summit-2027.ics');
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            });
        });

        // ==========================================================================
        // 06 — STAGED-REVEAL SPEAKER GRID (TASK 1.3)
        // ==========================================================================
        const speakersContainer = document.getElementById('speakers-dynamic-grid');
        if (speakersContainer && CFG.speakers && CFG.speakers.length > 0) {
            speakersContainer.innerHTML = CFG.speakers.map(sp => {
                if (sp.status === 'announced' && sp.name) {
                    const tagStyle = sp.organization && sp.organization.includes('Microsoft') 
                        ? 'background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.4);'
                        : 'background: rgba(0, 240, 255, 0.15); color: #00f0ff; border: 1px solid rgba(0, 240, 255, 0.4);';
                    return `
                        <div class="speaker-card speaker-announced">
                            <div class="speaker-avatar">
                                ${sp.photo ? `<img src="${sp.photo}" alt="${sp.name}" loading="lazy" decoding="async">` : `<div class="avatar-placeholder">${sp.name.charAt(0)}</div>`}
                            </div>
                            <span class="speaker-announced-tag" style="${tagStyle}">${sp.sessionRole || 'CONFIRMED FACULTY'}</span>
                            <h4 style="font-size: 1.25rem; margin: 0.5rem 0 0.2rem; color: #fff;">${sp.name}</h4>
                            <span class="speaker-role" style="color: #00f0ff; font-weight: 500;">${sp.title}, <strong>${sp.organization}</strong></span>
                            <p class="speaker-topic" style="margin-top: 0.6rem; font-size: 0.88rem; color: #cbd5e1;"><strong>Topic:</strong> ${sp.topic}</p>
                            ${sp.linkedin ? `
                                <a href="${sp.linkedin}" target="_blank" rel="noopener noreferrer" class="speaker-li-link" aria-label="${sp.name} LinkedIn Profile" style="margin-top: 0.5rem; display: inline-flex; align-items: center; gap: 4px; color: #00f0ff; font-size: 0.8rem;">
                                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                                    <span>LinkedIn</span>
                                </a>` : ''}
                        </div>
                    `;
                } else {
                    return `
                        <div class="speaker-card speaker-tba">
                            <div class="speaker-avatar avatar-silhouette">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
                            </div>
                            <span class="speaker-tba-tag">CONFIRMATION PENDING</span>
                            <h4>${sp.sessionRole}</h4>
                            <span class="speaker-role">Speaker announcing soon</span>
                            <p class="speaker-topic"><em>${sp.topic}</em></p>
                        </div>
                    `;
                }
            }).join('');
        }

        // ==========================================================================
        // 07 — CONFIRMED ATTENDEE COMPANIES LOGO WALL (TASK 1.1)
        // ==========================================================================
        const logoWallContainer = document.getElementById('confirmed-logos-grid');
        const logoWallSection = document.getElementById('delegates-logo-section');
        if (logoWallContainer && CFG.attendeeCompanies) {
            const confirmedCompanies = CFG.attendeeCompanies.filter(c => c.confirmed === true);
            
            if (confirmedCompanies.length > 0) {
                logoWallContainer.innerHTML = confirmedCompanies.map(c => `
                    <div class="company-logo-card" title="${c.name}" style="padding: 12px 24px; background: rgba(255,255,255,0.04); border: 1px solid rgba(0,240,255,0.25); border-radius: 8px; display: inline-flex; align-items: center; gap: 10px;">
                        ${c.logoKey ? `<img src="./assets/ai-sec/brands/${c.logoKey}.png" alt="${c.name}" style="height: 22px; width: auto; object-fit: contain; filter: brightness(0) invert(1);" onerror="this.style.display='none'">` : ''}
                        <span class="logo-name" style="font-weight: 600; color: #fff; font-size: 0.95rem;">${c.name}</span>
                    </div>
                `).join('');
                if (logoWallSection) logoWallSection.style.display = 'block';
            } else {
                // If zero companies confirmed with written permission, hide wall or show honest invitation note
                if (logoWallSection) {
                    logoWallSection.innerHTML = `
                        <div class="container text-center py-3">
                            <div class="section-tag" style="justify-content:center;">// TARGET PARTICIPATION</div>
                            <h3 class="section-heading" style="font-size:1.4rem;">Confirmed Attendees Include Teams From</h3>
                            <p class="section-sub" style="max-width:640px; margin:0.5rem auto 1.5rem;">Security delegations from leading cloud, financial, and enterprise infrastructures are currently confirming attendance. Organization names will appear here once written permissions are confirmed.</p>
                            <a href="ai-sec-register.html" class="btn-cyber-cyan">APPLY FOR VETTED DELEGATE SEAT</a>
                        </div>
                    `;
                }
            }
        }

        // ==========================================================================
        // 08 — METRIC CLAIMS HONESTY ADAPTATION (TASK 1.2)
        // ==========================================================================
        const cisoMetricVal = document.getElementById('metric-ciso-val');
        const cisoMetricLbl = document.getElementById('metric-ciso-lbl');
        const cisoMetricDesc = document.getElementById('metric-ciso-desc');

        if (CFG.claims) {
            if (CFG.claims.cisoConfirmedCount) {
                if (cisoMetricVal) cisoMetricVal.textContent = CFG.claims.cisoConfirmedCount;
                if (cisoMetricLbl) cisoMetricLbl.textContent = "REGISTERED CISOs & C-SUITE";
                if (cisoMetricDesc) cisoMetricDesc.textContent = "Confirmed enterprise Chief Information Security Officers.";
            } else {
                if (cisoMetricVal) cisoMetricVal.textContent = (CFG.claims.targetCISOs || 50) + "+";
                if (cisoMetricLbl) cisoMetricLbl.textContent = "TARGET CISO ATTENDANCE";
                if (cisoMetricDesc) cisoMetricDesc.textContent = "Targeted executive quorum across banking, tech, and healthcare.";
            }
        }

        // ==========================================================================
        // 09 — 2-TIER THREAT MATRIX LEAD MAGNET (TASK 4.5)
        // ==========================================================================
        const magnetModal = document.getElementById('threat-matrix-modal');
        const triggerMagnet = document.querySelectorAll('.trigger-threat-matrix-download');
        const closeMagnet = document.getElementById('close-threat-matrix-modal');
        const magnetForm = document.getElementById('threat-matrix-download-form');
        const magnetSuccess = document.getElementById('threat-matrix-success');

        if (triggerMagnet.length > 0 && magnetModal) {
            triggerMagnet.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    magnetModal.classList.add('active');
                    window.aiSecTrack('report_download_modal_opened');
                });
            });
        }

        if (closeMagnet && magnetModal) {
            closeMagnet.addEventListener('click', () => {
                magnetModal.classList.remove('active');
            });
        }

        if (magnetForm) {
            magnetForm.addEventListener('submit', (e) => {
                e.preventDefault();
                const emailInput = magnetForm.querySelector('input[type="email"]');
                const workEmail = emailInput ? emailInput.value.trim() : '';

                if (!workEmail) return;

                window.aiSecTrack('report_download', {
                    report_tier: 'free_summary',
                    email: workEmail
                });

                // Simulate/submit to endpoint
                const endpoint = (CFG.forms && CFG.forms.leadMagnetEndpoint) || 'https://formsubmit.co/info@buildtek.in';
                const formData = new FormData(magnetForm);
                formData.append('Lead_Magnet', '2027 AI Threat Matrix Executive Summary');

                fetch(endpoint, {
                    method: 'POST',
                    body: formData,
                    headers: { 'Accept': 'application/json' }
                }).catch(() => {});

                if (magnetSuccess) {
                    magnetForm.style.display = 'none';
                    magnetSuccess.style.display = 'block';
                }
            });
        }

        // ==========================================================================
        // 10 — STICKY MOBILE CTA BAR (TASK 4.7)
        // ==========================================================================
        const mobileStickyBar = document.getElementById('mobile-sticky-cta');
        const heroSection = document.querySelector('.event-hero');
        const footerSection = document.querySelector('.event-footer');

        if (mobileStickyBar && heroSection) {
            window.addEventListener('scroll', () => {
                const heroBottom = heroSection.getBoundingClientRect().bottom;
                const footerTop = footerSection ? footerSection.getBoundingClientRect().top : Infinity;
                const windowHeight = window.innerHeight;

                // Show after hero is scrolled past, hide if footer comes into view
                if (heroBottom < 0 && footerTop > windowHeight) {
                    mobileStickyBar.classList.add('visible');
                } else {
                    mobileStickyBar.classList.remove('visible');
                }
            }, { passive: true });
        }

        // ==========================================================================
        // 11 — LIGHTWEIGHT COOKIE / TRACKING CONSENT BANNER (TASK 5)
        // ==========================================================================
        const consentBanner = document.getElementById('cookie-consent-banner');
        const btnAcceptConsent = document.getElementById('btn-consent-accept');
        const btnDeclineConsent = document.getElementById('btn-consent-decline');
        const consentKey = (CFG.tracking && CFG.tracking.cookieConsentCookieName) || 'aisec_cookie_consent_v1';

        function checkConsent() {
            try {
                const consent = localStorage.getItem(consentKey);
                if (!consent) {
                    if (consentBanner) consentBanner.style.display = 'flex';
                } else if (consent === 'granted') {
                    activatePixels();
                }
            } catch (e) {}
        }

        function activatePixels() {
            window.hasAdConsent = true;
            // Activate Meta Pixel if ID provided
            if (CFG.tracking && CFG.tracking.metaPixelId && !window.metaPixelActive) {
                window.metaPixelActive = true;
                /* Meta Pixel Snippet */
                !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
                n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
                n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
                t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
                document,'script','https://connect.facebook.net/en_US/fbevents.js');
                window.fbq('init', CFG.tracking.metaPixelId);
                window.fbq('track', 'PageView');
            }
            // Activate LinkedIn Insight if ID provided
            if (CFG.tracking && CFG.tracking.linkedInPartnerId && !window.liPixelActive) {
                window.liPixelActive = true;
                window._linkedin_data_partner_ids = window._linkedin_data_partner_ids || [];
                window._linkedin_data_partner_ids.push(CFG.tracking.linkedInPartnerId);
                (function(l) {
                if (!l){window.lintrk = function(a,b){window.lintrk.q.push([a,b])};
                window.lintrk.q=[]}
                var s = document.getElementsByTagName("script")[0];
                var b = document.createElement("script");
                b.type = "text/javascript";b.async = true;
                b.src = "https://snap.licdn.com/li.lms-analytics/insight.min.js";
                s.parentNode.insertBefore(b, s);})(window.lintrk);
            }
        }

        if (btnAcceptConsent) {
            btnAcceptConsent.addEventListener('click', () => {
                try { localStorage.setItem(consentKey, 'granted'); } catch (e) {}
                if (consentBanner) consentBanner.style.display = 'none';
                activatePixels();
                window.aiSecTrack('cookie_consent_granted');
            });
        }

        if (btnDeclineConsent) {
            btnDeclineConsent.addEventListener('click', () => {
                try { localStorage.setItem(consentKey, 'declined'); } catch (e) {}
                if (consentBanner) consentBanner.style.display = 'none';
                window.hasAdConsent = false;
                window.aiSecTrack('cookie_consent_declined');
            });
        }

        checkConsent();

        // ==========================================================================
        // 12 — SCROLL DEPTH TRACKING (TASK 6.4)
        // ==========================================================================
        let tracked50 = false;
        let tracked90 = false;

        window.addEventListener('scroll', () => {
            const scrollTotal = document.documentElement.scrollHeight - window.innerHeight;
            if (scrollTotal <= 0) return;
            const scrollPct = (window.scrollY / scrollTotal) * 100;

            if (scrollPct >= 50 && !tracked50) {
                tracked50 = true;
                window.aiSecTrack('scroll_depth_50');
            }
            if (scrollPct >= 90 && !tracked90) {
                tracked90 = true;
                window.aiSecTrack('scroll_depth_90');
            }
        }, { passive: true });

        // ==========================================================================
        // 13 — OUTBOUND & CTA CLICKS TRACKING (TASK 6.4)
        // ==========================================================================
        document.querySelectorAll('a[href*="wa.me"]').forEach(link => {
            link.addEventListener('click', () => {
                window.aiSecTrack('whatsapp_click');
            });
        });

        document.querySelectorAll('a[href*="mailto:"]').forEach(link => {
            if (link.href.includes('Speaker')) {
                link.addEventListener('click', () => {
                    window.aiSecTrack('speaker_apply_click');
                });
            }
        });

        document.querySelectorAll('a[href*="ai-sec-register.html"]').forEach(link => {
            link.addEventListener('click', () => {
                let passParam = 'general';
                if (link.href.includes('pass=standard')) passParam = 'standard';
                else if (link.href.includes('pass=executive')) passParam = 'executive';
                else if (link.href.includes('pass=provider')) passParam = 'provider';
                window.aiSecTrack('register_click', { pass_type: passParam });
            });
        });

        // ==========================================================================
        // 14 — FAQ ACCORDION ENGINE (ACCESSIBLE ARIA)
        // ==========================================================================
        const faqItems = document.querySelectorAll('.faq-item');
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            const answer = item.querySelector('.faq-answer');

            if (question && answer) {
                question.setAttribute('aria-expanded', 'false');
                answer.setAttribute('role', 'region');

                question.addEventListener('click', () => {
                    const isActive = item.classList.contains('active');

                    // Close other items
                    faqItems.forEach(i => {
                        i.classList.remove('active');
                        const q = i.querySelector('.faq-question');
                        const a = i.querySelector('.faq-answer');
                        if (q) q.setAttribute('aria-expanded', 'false');
                        if (a) a.style.maxHeight = null;
                    });

                    if (!isActive) {
                        item.classList.add('active');
                        question.setAttribute('aria-expanded', 'true');
                        answer.style.maxHeight = answer.scrollHeight + 'px';
                    }
                });
            }
        });

        // ==========================================================================
        // 15 — NUMBER COUNT-UP ANIMATION
        // ==========================================================================
        const countElements = document.querySelectorAll('.d-val, .fact-num');
        const countObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    // Skip time elements or non-numeric cards
                    if (target.id === 'fact-summit-hours' || target.innerText.includes(':') || target.innerText.includes('AM') || target.innerText.includes('PM') || target.innerText.includes('FEB')) {
                        observer.unobserve(target);
                        return;
                    }
                    const finalValueText = target.innerText;
                    const isPlus = finalValueText.includes('+');
                    const finalValue = parseInt(finalValueText.replace(/[^0-9]/g, ''), 10);

                    if (!isNaN(finalValue)) {
                        let startValue = 0;
                        const duration = 1600;
                        const startTime = performance.now();

                        function updateCounter(currentTime) {
                            const elapsed = currentTime - startTime;
                            const progress = Math.min(elapsed / duration, 1);
                            const easeProgress = progress * (2 - progress);
                            const currentVal = Math.floor(easeProgress * finalValue);
                            target.innerText = currentVal + (isPlus ? '+' : '');

                            if (progress < 1) {
                                requestAnimationFrame(updateCounter);
                            } else {
                                target.innerText = finalValueText;
                            }
                        }
                        requestAnimationFrame(updateCounter);
                    }
                    observer.unobserve(target);
                }
            });
        }, { threshold: 0.5 });
        countElements.forEach(el => countObserver.observe(el));

        // ==========================================================================
        // 16 — SMOOTH ANCHOR NAVIGATION
        // ==========================================================================
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const href = this.getAttribute('href');
                if (!href || href === '#') return;
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });

        // ==========================================================================
        // 17 — CANVAS PARTICLES AMBIENT BACKGROUND
        // ==========================================================================
        const canvas = document.getElementById('cyber-bg-canvas');
        if (canvas && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            const ctx = canvas.getContext('2d');
            let width, height;

            function resize() {
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            class Particle {
                constructor() { this.reset(); }
                reset() {
                    this.x = Math.random() * width;
                    this.y = Math.random() * height;
                    this.vx = (Math.random() - 0.5) * 0.25;
                    this.vy = (Math.random() - 0.5) * 0.25;
                    this.size = Math.random() * 1.4 + 0.6;
                    this.alpha = Math.random() * 0.35 + 0.1;
                    this.color = Math.random() > 0.4 ? '#00f0ff' : '#ff3333';
                }
                update() {
                    this.x += this.vx;
                    this.y += this.vy;
                    if (this.x < 0 || this.x > width || this.y < 0 || this.y > height) this.reset();
                }
                draw() {
                    ctx.save();
                    ctx.globalAlpha = this.alpha;
                    ctx.fillStyle = this.color;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.restore();
                }
            }

            const particleList = Array.from({ length: 70 }, () => new Particle());
            let animId = null;

            function render() {
                if (document.hidden) return;
                ctx.clearRect(0, 0, width, height);
                particleList.forEach(p => {
                    p.update();
                    p.draw();
                });
                animId = requestAnimationFrame(render);
            }
            render();

            document.addEventListener('visibilitychange', () => {
                if (document.hidden && animId) {
                    cancelAnimationFrame(animId);
                    animId = null;
                } else if (!animId) {
                    render();
                }
            });
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSummit);
    } else {
        initSummit();
    }
})();
