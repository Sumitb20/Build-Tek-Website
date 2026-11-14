# BuildTek Events — Official Website Repository

**Website:** [buildtek.in](https://buildtek.in) · [www.buildtek.in](https://www.buildtek.in)  
**Hosting:** AWS Amplify (`ap-southeast-2`) & AWS CloudFront CDN  
**Domain Registrar:** GoDaddy (`ns01.domaincontrol.com`, `ns02.domaincontrol.com`)  
**Headquarters:** Pune & Mumbai, India  

---

## 📌 Overview

BuildTek Events produces elite virtual B2B summits, leadership conferences, and executive conclaves for C-suite decision-makers across:
1. **AI Security & Governance** — *AI Security Global Virtual Summit 2027* (Feb 12, 2027)
2. **FinTech Risk & Payments** — *Global Payments & Risk Summit 2027* (June 18, 2027)
3. **Pharma & Life Sciences** — *Pharma Vista Global Summit* (Oct 5, 2026 / 2027)

---

## 🏗️ Architecture & Technology Stack

- **Frontend:** Pure semantic HTML5, modern CSS3 (Custom Properties, Flexbox, Grid), Vanilla ES6+ JavaScript.
- **Third-Party Libraries:**
  - GSAP & ScrollTrigger (Animation)
  - Lenis (Smooth scrolling)
  - FontAwesome 6.4 (Icons)
  - Cloudflare Turnstile (Bot protection on high-value forms)
- **Forms & Backend:** FormSubmit.co (serverless form handling to email).
- **Security:**
  - Subresource Integrity (SRI) on external CDN scripts.
  - Custom HTTP security headers via AWS Amplify (`HSTS`, `X-Frame-Options`, `X-Content-Type-Options`, `Permissions-Policy`, `Referrer-Policy`).
  - Strict DMARC email authentication policy.
- **PWA (Progressive Web App):**
  - Web App Manifest (`site.webmanifest`)
  - Service Worker (`sw.js`) with cache-first asset caching & network-first navigation fallback.
- **SEO & AI Search (GEO / AEO):**
  - Canonical tags and Open Graph meta tags across all 35 pages.
  - JSON-LD structured schemas (`Event`, `Organization`, `FAQPage`, `TechArticle`, `BlogPosting`).
  - Search engine sitemap (`sitemap.xml`) and AI-agent manifest (`llms.txt`, `llms-full.txt`).

---

## 🚀 Deployment & Hosting Workflow

### AWS Amplify
- **App ID:** `d14g7sz0e6oj1v`
- **Region:** `ap-southeast-2` (Sydney)
- **Branch:** `main`
- **CDN Domain:** `dqvl29bopye1a.cloudfront.net`
- **Configuration Files:**
  - `amplify.yml`: Build specifications and custom headers.
  - `customHttp.yml`: Security headers delivery.

### GoDaddy DNS Records
| Type | Name | Value | Purpose |
|------|------|-------|---------|
| `A` | `@` | `15.197.225.128` | AWS Global Accelerator Root |
| `A` | `@` | `3.33.251.168` | AWS Global Accelerator Root |
| `CNAME` | `www` | `dqvl29bopye1a.cloudfront.net` | WWW subdomain pointing to CloudFront |
| `CNAME` | `_3ed5...` | `_15cd...acm-validations.aws.` | ACM SSL Certificate Validation |
| `TXT` | `_dmarc` | `v=DMARC1; p=quarantine; ...` | Email anti-spoofing policy |

---

## 🛠️ Local Development & Validation

To test locally:
```bash
# Start a simple HTTP server
python3 -m http.server 8000

# Open in browser:
# http://localhost:8000
```

To validate SEO and AI Discoverability:
```bash
python3 validate_seo_geo.py
```

---

## 🔒 Security Best Practices
- Never commit AWS access keys or secrets to Git.
- Always include `integrity` and `crossorigin="anonymous"` when referencing third-party scripts.
- Keep `llms.txt` and `robots.txt` synchronized with newly added summits and publications.
