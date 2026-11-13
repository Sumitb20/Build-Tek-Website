# TO BE CONFIRMED: Action Items & Operator Checkpoints

The following items are marked with `[TO BE CONFIRMED]` across the AI-Sec Global Summit codebase. No fabricated data has been entered. You can safely activate or update each item in `assets/ai-sec/config.js` or the corresponding HTML files once confirmed.

---

## 1. Attendee Logos & Brand Approvals
- **File:** `assets/ai-sec/config.js` (Lines 15–185)
- **Status:** All 20 enterprise companies (Microsoft, Google Cloud, AWS, CrowdStrike, Palo Alto, Cisco, Fortinet, Cloudflare, SentinelOne, Snowflake, Datadog, IBM, JPMorgan Chase, Goldman Sachs, Deloitte, Zscaler, Okta, Check Point, Darktrace, Splunk) are currently set to `confirmed: false`.
- **Action Required:**
  1. Obtain written consent (an email confirmation is sufficient) from the security team or corporate marketing before publicly displaying a third-party trademark.
  2. In `assets/ai-sec/config.js`, locate the company object and flip `"confirmed": false` to `"confirmed": true`.
  3. The website will automatically render the verified logo in the logo wall section.

---

## 2. Confirmed CISO Attendance Count
- **File:** `assets/ai-sec/config.js` (Line 192: `cisoConfirmedCount: null`)
- **Status:** Currently set to `null`. The front-end honestly displays `"50+ CISOs: TARGET ATTENDANCE"`.
- **Action Required:**
  - As vetted registrations accumulate, enter the verified count (e.g. `cisoConfirmedCount: 38`).
  - The hero badge and fact grid will automatically update to display `"38 CISOs registered"`.

---

## 3. Staged Keynote Speakers
- **File:** `assets/ai-sec/config.js` (Lines 197–235)
- **Status:** Defaulted to 4 neutral session roles marked with status `"tba"`:
  - Role 1: Keynote Faculty — Offensive AI & Autonomous Agents
  - Role 2: Technical Teardown — Prompt Injection & Tool-Calling Exploits
  - Role 3: Defensive Blueprints — Enterprise Model Gateways & Firewalls
  - Role 4: Executive Roundtable — Autonomous SOC & AI Governance
- **Action Required:**
  - As speakers sign speaker agreements, replace the placeholder object in `config.speakers`:
    ```javascript
    {
      id: "spk-01",
      name: "Jane Doe",
      title: "Chief Information Security Officer",
      organization: "Acme Financial Corp",
      photo: "assets/ai-sec/speakers/jane-doe.jpg",
      linkedin: "https://linkedin.com/in/janedoe",
      topic: "Autonomous AI Agents in Production: Offensive Surface & Defense",
      status: "announced" // Flip from "tba" to "announced"
    }
    ```
  - The speaker card will automatically transition from the TBA silhouette to the full profile card.

---

## 4. CPE Accreditation Status
- **File:** `assets/ai-sec/config.js` (Line 193: `cpeApproved: false`)
- **Status:** Set to `false`. Front-end copy accurately states: *"Digital Certificate of Attendance, CPE credits pending accreditation (details confirmed closer to the event)"*.
- **Action Required:**
  - When accreditation with ISC2 / ISACA is officially confirmed, change `cpeApproved: false` to `cpeApproved: true`.
  - The passes and hero copy will automatically update to verified accredited status.

---

## 5. Agenda Reserved Partner Slots
- **File:** `assets/ai-sec/config.js` (Lines 240–265) & `aisecsummit.html` (Lines 470–540)
- **Status:** Strategic partner speaking slots are marked as reserved:
  - 09:50 AM ET: Strategic Partner Keynote [Reserved for Partner]
  - 10:45 AM ET: Founding Partner Marquee Session [Reserved for Partner]
  - 12:55 PM ET: Strategic Solution Briefing [Reserved for Partner]
- **Action Required:**
  - Once sponsorship contracts are executed, update the partner title, speaker name, and session synopsis in `config.agendaPartnerSlots`.

---

## 6. Commercial Resolution: Gold Sponsor Tier Panel Inventory
- **File:** `aisecsummit-partners.html` (Lines 180–210) & `aisecsummit.html` (Sample Agenda)
- **Status:** Gold Sponsor Tier ($5,999) has 2 available inventory slots and promises a *"Featured Executive Panel Seat"*. The agenda currently features exactly two executive panels:
  - 09:15 AM ET: *Fraud at Machine Speed*
  - 12:20 PM ET: *Governing AI Risk, Shadow LLMs & Board Reporting*
- **Action Required:**
  - If both Gold Tier slots are sold to commercial vendors, both panels will have sponsored speakers.
  - Decide whether to:
    - (Option A) Keep as-is and clarify that each panel contains 1 sponsored seat alongside 3 practitioner CISOs.
    - (Option B) Add a 3rd panel to the defensive track.
    - (Option C) Cap Gold inventory at 1 slot.

---

## 7. Past Events Proof & Testimonials
- **File:** `assets/ai-sec/config.js` (Line 194: `showProof: false`)
- **Status:** Currently hidden (`showProof = false`). No fabricated attendee quotes or stats are rendered.
- **Action Required:**
  - Gather authentic quotes, names, and titles from previous attendees who have granted written permission.
  - Insert them into `config.proofTestimonials` and set `showProof: true`.

---

## 8. Analytics & Ad Pixels Activation
- **File:** `assets/ai-sec/config.js` (Lines 280–290)
- **Status:**
  - Google Analytics: `G-HJL88YELRT` (active).
  - Meta Pixel ID: `YOUR_PIXEL_ID` (placeholder; strictly blocked until consent is given).
  - LinkedIn Partner ID: `YOUR_LINKEDIN_PARTNER_ID` (placeholder; strictly blocked until consent is given).
- **Action Required:**
  - Replace the placeholder IDs with your live Meta and LinkedIn tracking pixel IDs once advertising campaigns are ready to launch.

---

## 9. Legal Policy Sign-Off
- **Files:** `refund-policy.html`, `code-of-conduct.html`, `privacy-policy.html`, `terms.html`
- **Status:** Standard enterprise B2B terms have been implemented.
- **Action Required:**
  - Have corporate legal or financial counsel review the cancellation refund schedule (30+ days = 100% minus fee, 14–29 days = 50%, < 14 days = 0%) to ensure alignment with banking terms in Pune, India.

