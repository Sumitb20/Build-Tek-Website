# AI-Sec Global Summit 2027: QA Verification Checklist

Use this QA checklist to verify the landing page, partner portal, and registration flows before launching public traffic.

---

## 1. Responsiveness & Cross-Browser Layout
- [ ] **Mobile viewport (360px – 390px):** Test on iPhone SE (375px) and Galaxy S20 (360px). Confirm **zero horizontal scrolling**, text wraps naturally, and touch targets are minimum 44x44px.
- [ ] **Tablet viewport (768px – 1024px):** Verify two-column grid layouts for tracks and pass cards stack gracefully without overlapping.
- [ ] **Desktop viewport (1280px – 1920px):** Verify max-width containers (1140px / 1200px) center properly and high-DPI graphics render sharply.
- [ ] **Browsers:** Test in Chrome, Firefox, Safari (macOS & iOS), and Microsoft Edge. Verify backdrop-filter blur and gradients render consistently.

---

## 2. Credibility & Content Verification
- [ ] **Logo Wall:**
  - Verify that only companies with `confirmed: true` in `config.js` render on `aisecsummit.html`.
  - Verify that unconfirmed logos are completely absent and the verified fallback message appears when all are false.
  - Verify that invented sub-labels (*"Microsoft Enterprise Security"*, etc.) do not appear anywhere on the page.
- [ ] **Claim Wording:**
  - Check hero facts: "50+ CISOs: TARGET ATTENDANCE", "200 DELEGATES: STRICT CAPACITY CAP".
  - Ensure "Zero vendor pitches" has been replaced everywhere by "No product demos. Thought-leadership & technical content only."
  - Ensure "INVITE-ONLY" has been replaced by "Vetted Registration".
  - Ensure CPE status reads: "Digital Certificate of Attendance, CPE credits pending accreditation".
- [ ] **Speakers Section:**
  - Verify 4 staged TBA cards render with session roles (Offensive AI, Prompt Injection, Model Gateways, Autonomous SOC) and silhouette icons.
  - Verify "Apply as a speaker" button opens email client with pre-filled subject: `Speaker Application - AI-Sec Global Summit 2027`.
- [ ] **Agenda:**
  - Verify 11:50 AM ET break reads "Virtual Coffee Break and Interactive Chat Polls" (no "Vendor Spotlight").
  - Verify partner slots (09:50 AM, 10:45 AM, 12:55 PM) are marked "[Reserved for Partner]".
  - Verify 01:25 PM ET CISO roundtable is marked "Executive Pass Only // Chatham House Rule".

---

## 3. Pass Selection & Registration Flow (`ai-sec-register.html`)
- [ ] **Pass Pre-Selection:**
  - Navigate to `ai-sec-register.html?pass=standard` → Verify "Standard Virtual Pass ($199)" is pre-selected.
  - Navigate to `ai-sec-register.html?pass=executive` → Verify "Executive Delegate Pass ($399)" is pre-selected.
  - Navigate to `ai-sec-register.html?pass=provider` → Verify "Solution Provider Pass ($999)" is pre-selected.
- [ ] **Free Email Validation:**
  - Select Executive or Provider Pass and enter a `@gmail.com` or `@yahoo.com` address.
  - Confirm validation warning fires: *"Executive & Solution Provider passes require a corporate work email address."*
- [ ] **Vetted Submission & Post-Registration State:**
  - **Standard Pass Submission:** Fill in required fields and submit. Verify user is shown the post-registration state with the instant Razorpay checkout button (`https://rzp.io/rzp/i0saXC2M`).
  - **Executive / Provider Pass Submission:** Fill in corporate credentials and submit. Verify user is shown the "Application Received — Verification in Progress" 3-step review screen with no public payment button.
- [ ] **Hidden Field Capture:**
  - Visit `ai-sec-register.html?utm_source=linkedin&utm_campaign=ciso_q1`.
  - Confirm hidden inputs `utm_source`, `utm_campaign`, `registration_timestamp`, and `referrer` are populated in the form submission payload.

---

## 4. Timezone Converter & Add to Calendar
- [ ] **Timezone Detection:**
  - Load `aisecsummit.html`. Verify `#user-local-time` displays the summit hours in your local browser timezone.
  - Change the timezone dropdown to "London (GMT/BST)" → Verify time shifts to `13:00 – 19:05 GMT`.
  - Change to "India (IST)" → Verify time shifts to `18:30 – 00:35 IST`.
- [ ] **Add to Calendar Buttons:**
  - Click "+ Google" → Verify Google Calendar opens with event title "AI-Sec Global Summit 2027", date Feb 12 2027, and full summit description.
  - Click "+ .ICS File" → Verify browser downloads `ai-sec-summit-2027.ics`. Open file in Apple Calendar or Outlook to verify event time (13:00 UTC).

---

## 5. Lead Magnet & Modals
- [ ] **Threat Matrix Modal:**
  - Click "DOWNLOAD EXECUTIVE SUMMARY (FREE)". Verify `#threat-matrix-modal` opens with blurred backdrop.
  - Test closing modal via "✕" button, clicking outside the modal box, and pressing the `ESC` key.
  - Submit email and organization → Verify success message appears and form routes to `info@buildtek.in`.

---

## 6. Mobile Sticky CTA & Floating Controls
- [ ] **Sticky Mobile Bar:**
  - View on mobile screen (< 768px). Scroll past hero section.
  - Verify `#mobile-sticky-cta` smoothly slides in at the bottom.
  - Click "GET PASS" → Verify smooth scroll directly to `#passes`.
  - Scroll into footer → Verify sticky bar hides so footer links remain visible.
- [ ] **WhatsApp Button:**
  - Click floating WhatsApp icon → Verify it opens WhatsApp chat to `+91 9226348550` with pre-filled greeting.

---

## 7. Cookie Consent & Pixel Gating
- [ ] **Consent Banner:**
  - Open site in an Incognito / Private window. Verify `#cookie-consent-banner` appears at the bottom.
  - Click "ESSENTIAL ONLY" → Verify banner closes, `ai_sec_cookie_consent=essential` is stored in `localStorage`, and Meta/LinkedIn pixels remain inactive.
  - Click "ACCEPT ALL" → Verify `ai_sec_cookie_consent=all` is stored, and ad pixels are initialized.

---

## 8. Technical SEO & Legal Compliance
- [ ] **Meta Tags:**
  - Verify `<meta name="keywords">` is absent.
  - Verify `<title>` length is < 60 characters: `AI Security Summit 2027 | 12 Feb — Virtual CISO Conference`.
  - Verify `<meta name="description">` length is 154 characters.
- [ ] **Schema.org Structured Data:**
  - Validate with Google Rich Results Test or Schema Markup Validator.
  - Verify `Event` schema has `startDate: 2027-02-12T08:00:00-05:00` and `offers` link to registration page without `rzp.io` URLs.
  - Verify `Organization` and `FAQPage` schemas validate with 0 errors.
- [ ] **Legal Links:**
  - Click footer links: `privacy-policy.html`, `terms.html`, `refund-policy.html`, `code-of-conduct.html`. Verify all pages resolve with HTTP 200 and return clean, updated text.

