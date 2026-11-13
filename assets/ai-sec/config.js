/**
 * AI-SEC GLOBAL SUMMIT 2027 — CENTRAL CONFIGURATION ENGINE
 * 
 * Non-developer editable configuration block for all event parameters,
 * dates, speaker data, attendance claims, partner tiers, and tracking.
 * Edit this file to update event details across the site.
 */

window.AI_SEC_CONFIG = {
    // --------------------------------------------------------------------------
    // 1. EVENT CORE METADATA
    // --------------------------------------------------------------------------
    event: {
        name: "AI-Sec Global Summit 2027",
        edition: "Inaugural Global Virtual Assembly",
        dateISO: "2027-02-12",
        startDateTimeISO: "2027-02-12T08:00:00-05:00",
        endDateTimeISO: "2027-02-12T14:05:00-05:00",
        dateDisplay: "12 February 2027",
        timeDisplayET: "08:00 AM – 02:05 PM ET",
        durationHours: 6,
        format: "100% Virtual / Global Live Stream & Replay",
        locationUrl: "https://buildtek.in/aisecsummit.html",
        organizerName: "Build Tek Events",
        organizerUrl: "https://buildtek.in/",
        contactEmail: "info@buildtek.in",
        partnersEmail: "partners@buildtek.in", // [TO BE CONFIRMED: Dedicated partners email or info@buildtek.in]
        whatsappNumber: "+91 9226348550",
        whatsappLink: "https://wa.me/919226348550?text=Hi%20BuildTek!%20I'm%20inquiring%20about%20the%20AI-Sec%20Global%20Summit%202027.",
        linkedinUrl: "https://www.linkedin.com/company/build-tek-events/"
    },

    // --------------------------------------------------------------------------
    // 2. CREDIBILITY & ATTENDANCE CLAIMS (TASK 1.2)
    // --------------------------------------------------------------------------
    claims: {
        targetCapacity: 200, // True capacity cap
        targetCISOs: 50,     // Target CISO attendance
        
        // Confirmed speakers & participating leaders from Microsoft & AWS
        cisoConfirmedCount: "2 Confirmed Faculty (Microsoft & AWS)",
        seatsRegistered: null,
        
        // Set to true only when Fortune 500 company permissions are signed
        showFortune500Claim: true,
        
        // CPE accreditation status (Task 2.3)
        // Set to true once official accreditation body confirms 6 CPE credits
        cpeApproved: false,
        
        // Proof & testimonials visibility (Task 1.4)
        showProof: true
    },

    // --------------------------------------------------------------------------
    // 3. PRICING & EARLY-BIRD CONFIG (TASK 4.6)
    // --------------------------------------------------------------------------
    pricing: {
        currency: "USD",
        passes: {
            standard: {
                id: "standard",
                name: "Standard Virtual Pass",
                tagline: "For security analysts, architects, engineers & researchers",
                regularPrice: 199,
                earlyBirdPrice: 149, // Active only when earlyBird.active = true
                popular: false,
                recommendedFor: "Practitioners & Technical Leads"
            },
            executive: {
                id: "executive",
                name: "Executive Delegate Pass",
                tagline: "For enterprise CISOs, CIOs, CTOs, VPs & Security Heads",
                regularPrice: 399,
                earlyBirdPrice: 299,
                popular: true,
                recommendedFor: "CISOs & Security Executives"
            },
            provider: {
                id: "provider",
                name: "Solution Provider Pass",
                tagline: "For cybersecurity vendors, technology providers & consultants",
                regularPrice: 999,
                earlyBirdPrice: 799,
                popular: false,
                recommendedFor: "Vendors & Solution Providers"
            }
        },
        earlyBird: {
            active: false, // Set to true to activate early-bird pricing
            endDateISO: "2026-12-31T23:59:59-05:00", // [TO BE CONFIRMED: Early bird deadline]
            label: "Early-Bird Registration Window"
        }
    },

    // --------------------------------------------------------------------------
    // 4. CONFIRMED ATTENDEE COMPANIES LOGO WALL (TASK 1.1)
    // --------------------------------------------------------------------------
    // IMPORTANT: Per legal guidelines, ensure written permission (email is enough)
    // before setting confirmed: true for any third-party logo.
    // Flip confirmed: true once permission is secured.
    attendeeCompanies: [
        { name: "Microsoft", logoKey: "microsoft", confirmed: true },
        { name: "Amazon AWS", logoKey: "amazon-aws", confirmed: true },
        { name: "Google Cloud", logoKey: "google-cloud", confirmed: false },
        { name: "CrowdStrike", logoKey: "crowdstrike", confirmed: false },
        { name: "Palo Alto Networks", logoKey: "palo-alto-networks", confirmed: false },
        { name: "Cisco", logoKey: "cisco", confirmed: false },
        { name: "Fortinet", logoKey: "fortinet", confirmed: false },
        { name: "Cloudflare", logoKey: "cloudflare", confirmed: false },
        { name: "SentinelOne", logoKey: "sentinelone", confirmed: false },
        { name: "Snowflake", logoKey: "snowflake", confirmed: false },
        { name: "Datadog", logoKey: "datadog", confirmed: false },
        { name: "IBM", logoKey: "ibm", confirmed: false },
        { name: "JPMorgan Chase", logoKey: "jpmorgan-chase", confirmed: false },
        { name: "Goldman Sachs", logoKey: "goldman-sachs", confirmed: false },
        { name: "Deloitte", logoKey: "deloitte", confirmed: false },
        { name: "Okta", logoKey: "okta", confirmed: false }
    ],

    // --------------------------------------------------------------------------
    // 5. STAGED-REVEAL SPEAKERS GRID (TASK 1.3)
    // --------------------------------------------------------------------------
    // status: "announced" | "tba"
    // When "announced": supply name, title, organization, photo, linkedin, topic
    // When "tba": displays honest session role and silhouette
    speakers: [
        {
            id: "sp-1",
            status: "announced",
            sessionRole: "Featured Keynote Speaker",
            topic: "Securing the Agentic Enterprise: Identity, Data, and Runtime Controls for AI Agents",
            name: "Siva Sundaramoorthy",
            title: "Field CISO / Security Cloud Solutions Architect",
            organization: "Microsoft",
            photo: "./assets/ai-sec/siva_sundaramoorthy.jpg",
            banner: "./assets/ai-sec/siva_sundaramoorthy_poster.jpg",
            linkedin: "https://www.linkedin.com/in/siva-sundaramoorthy/"
        },
        {
            id: "sp-2",
            status: "announced",
            sessionRole: "Executive Panel Speaker",
            topic: "Fraud at Machine Speed: Threat Intelligence from the Frontlines of Financial Crime & Digital Commerce",
            name: "James Daniel Ferguson",
            title: "Executive Security Engagement Leader",
            organization: "AWS (Amazon Web Services)",
            photo: "./assets/ai-sec/james_daniel_ferguson.jpg",
            banner: "./assets/ai-sec/james_daniel_ferguson_poster.jpg",
            linkedin: "https://www.linkedin.com/in/james-daniel-ferguson/"
        },
        {
            id: "sp-3",
            status: "tba",
            sessionRole: "Panel: Governing AI Risk",
            topic: "Governing AI Risk Without Slowing Innovation: Boardroom Reporting & SEC Mandates",
            name: "[Speaker to be announced]",
            title: "Chief Information Security Officer",
            organization: "Global Enterprise",
            photo: "",
            linkedin: ""
        },
        {
            id: "sp-4",
            status: "tba",
            sessionRole: "Technical Session: SOC Automation",
            topic: "The AI-Powered SOC: Sub-Second Alert Triage and Autonomous Incident Response",
            name: "[Speaker to be announced]",
            title: "Head of Threat Intelligence",
            organization: "Enterprise Defense Labs",
            photo: "",
            linkedin: ""
        }
    ],

    // --------------------------------------------------------------------------
    // 6. AGENDA STRATEGIC PARTNER SLOTS (TASK 1.5)
    // --------------------------------------------------------------------------
    agendaPartnerSlots: {
        slot1: {
            time: "08:30 – 08:50 AM ET",
            title: "How Adversaries Exploit Identity at Scale",
            confirmed: false,
            partnerName: "Reserved for Strategic / Platinum Partner",
            speakerName: "Speaker to be announced"
        },
        marqueeFounding: {
            time: "10:45 – 11:05 AM ET",
            title: "From Detection to Trust: Rethinking Identity Verification for the AI Era",
            confirmed: false,
            partnerName: "Reserved for Founding Partner",
            speakerName: "Speaker to be announced"
        },
        slot3: {
            time: "12:00 – 12:20 PM ET",
            title: "Operationalizing AI Governance: Lessons from the Field",
            confirmed: false,
            partnerName: "Reserved for Strategic / Platinum Partner",
            speakerName: "Speaker to be announced"
        }
    },

    // --------------------------------------------------------------------------
    // 7. INTERNAL PAYMENT LINKS (TASK 3)
    // --------------------------------------------------------------------------
    // NOTE: Executive and Solution Provider links are for internal manual emailing only.
    // They are NOT printed on public landing pages.
    paymentLinks: {
        standard: "https://rzp.io/rzp/i0saXC2M",
        executive: "https://rzp.io/rzp/0WlrjSCw",
        provider: "https://rzp.io/rzp/lsBnDSki"
    },

    // --------------------------------------------------------------------------
    // 8. FORM ENDPOINTS (TASK 3.2)
    // --------------------------------------------------------------------------
    forms: {
        // [TO BE CONFIRMED: Backend form handler URL (e.g. FormSubmit, Formspree, Google Apps Script, CRM Webhook)]
        registrationEndpoint: "https://formsubmit.co/info@buildtek.in",
        partnerEndpoint: "https://formsubmit.co/info@buildtek.in",
        leadMagnetEndpoint: "https://formsubmit.co/info@buildtek.in"
    },

    // --------------------------------------------------------------------------
    // 9. LEAD MAGNET FILES (TASK 4.5)
    // --------------------------------------------------------------------------
    leadMagnets: {
        // [TO BE CONFIRMED: Upload actual PDF files to /assets/ai-sec/docs/]
        freeSummaryPdf: "assets/ai-sec/docs/AI-Threat-Matrix-2027-Executive-Summary.pdf",
        fullReportPdf: "assets/ai-sec/docs/AI-Threat-Matrix-2027-Full-Benchmark-Report.pdf",
        prospectusPdf: "assets/ai-sec/AI-Sec-2027-Sponsor-Prospectus.pdf"
    },

    // --------------------------------------------------------------------------
    // 10. TRACKING & ANALYTICS CONFIG (TASK 6.4)
    // --------------------------------------------------------------------------
    tracking: {
        ga4Id: "G-HJL88YELRT",
        // [TO BE CONFIRMED: Supply Meta Pixel ID and LinkedIn Partner ID]
        metaPixelId: "",        // e.g. "123456789012345"
        linkedInPartnerId: "",  // e.g. "5432109"
        cookieConsentCookieName: "aisec_cookie_consent_v1"
    }
};

