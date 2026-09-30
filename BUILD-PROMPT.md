# 360Comm.com — Idea Validation & Phase-Wise Build Prompt

## 1. The winning idea

**360Comm = "the 360° Business Communications Hub"**: independent comparisons, free calculators, guides and videos, plus a no-obligation **quote marketplace** for business phone/VoIP (UCaaS), contact centers (CCaaS), video conferencing, team chat, business SMS/CPaaS and business internet.

### Why this beats the alternatives

| Candidate concept for "360 Comm" | AdSense CPC tier | Lead value | Affiliate programs | Verdict |
|---|---|---|---|---|
| **B2B comms comparison + quote marketplace** | High (B2B VoIP/UCaaS/contact-center terms are among the pricier SaaS keywords) | $30–$150+ per qualified lead in the category | Many UCaaS vendors run partner/affiliate programs | ✅ **Chosen** |
| Communications/PR agency | Medium | One-off projects | Few | ❌ Service business, not a scalable site |
| Communications degree/careers portal | Medium | Education leads (competitive, regulated) | Some | ❌ Weak brand fit |
| Consumer phone/mobile plans | Low–medium | Low | Carrier affiliates | ❌ Crowded, low B2B value |

**Revenue stack (in order of expected impact):** (1) pay-per-lead / referral fees from quote requests → (2) affiliate commissions on "Visit site" clicks → (3) sponsored listings & featured-partner boxes → (4) AdSense on high-intent pages → (5) YouTube + sponsored video reviews → (6) newsletter sponsorship → (7) donations and contest sponsors.

### Competitive audit summary (38 sites reviewed)
G2, Capterra, TrustRadius, Software Advice, GetApp, Forbes Advisor, TechRadar, Fit Small Business, Business.com (+ paid LP), Business News Daily, GetVoIP, UC Today, No Jitter, Top10.com, TechnologyAdvice, TopConsumerReviews, Expert Market, Zapier blog, Merchant Maverick, Cloudwards, WhichVoIP, VoipReview, TechRepublic, ConsumersAdvocate, Business.org, Crozdesk, VoIP-Info, HighSpeedInternet, Quo calculator, Ooma savings calculator, PeerSpot, WPBeginner, SaaSworthy, Wirefly, ISPReports, ConsumerVoice, Nextiva/CloudTalk/Vibe pricing blogs.

**Patterns adopted:** one-click first form step (Expert Market), quote button beside every provider (Business.com/Top10), published scoring weights (Forbes/Merchant Maverick), "prices verified [date]" stamps (TechnologyAdvice/Cloudwards), hidden-cost pricing content feeding calculators (CloudTalk/Quo/Ooma), quiz matcher (Fit Small Business), labeled featured-partner modules (Forbes/TechRepublic), exit-intent offer (ConsumerVoice), clear advertiser disclosure (Software Advice).

---

## 2. Phase-wise master prompt

> Use these phases in order with any AI coding assistant or developer. Each phase is self-contained and testable.

### Phase 0: Global rules (apply to every phase)
- Static site (HTML/CSS/vanilla JS), deployable on the **free GitHub Pages** plan. No server, no build step required at runtime; relative links only.
- Brand: **360Comm**. Palette navy `#0b1b3f`, blue `#2563eb`, CTA orange `#f97316`. Font: Inter. Light and dark mode.
- **Top banner on every page:** "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership", linking to `https://web.works/contact`.
- **One inbox for every form:** all submissions go to a single hidden email address via FormSubmit AJAX. The address is stored obfuscated in JS and is **never printed in HTML**. mailto and PayPal links are assembled only on click.
- Trademark safety: no third-party logos (use colored initial badges); a nominative-fair-use notice; a clear "not affiliated with any '360 Comm/360 Communications' entity" statement on every footer and on `/legal.html`.
- Accessibility: WCAG AA contrast, labels on all inputs, keyboard support, `prefers-reduced-motion`.
- SEO: unique title/description, canonical, OG/Twitter tags, JSON-LD (Organization, WebSite, FAQPage, Review, Article, JobPosting, WebApplication, DefinedTermSet), sitemap.xml, robots.txt.

### Phase 1: Foundation & design system
Build `assets/css/style.css` (tokens, grid, cards, buttons, tables, forms, wizard, modals, dark mode) and `assets/js/main.js` (theme toggle, mobile mega-menu, form engine, wizard, sortable/filterable tables, lazy YouTube, AdSense loader with house-ad fallback, cookie consent, exit-intent, site search (`/` or Ctrl-K), counters, back-to-top). Header: logo, mega-menus (Compare, Free Tools, Community), Guides, Videos, search, theme, "Get Free Quotes" CTA. Footer: newsletter, 4 link columns, legal disclosure, sticky mobile CTA.

### Phase 2: Lead-generation engine (highest priority)
- `/quotes.html`: a 6-step wizard with a progress bar. (1) users, as a one-click choice that auto-advances; (2) needs, multi-select; (3) timeline, auto-advances; (4) current setup + hardware + budget; (5) country, postal code, industry; (6) first/last name, business, phone, work email, notes, plus a separate TCPA/CASL consent checkbox.
- The home hero card with a one-click user-count choice deep-links into step 2 (`?users=`).
- A quote CTA sits beside every provider row, in every sidebar, in the exit-intent modal and in the sticky mobile bar.
- `/thank-you.html` gives next steps and asks for a donation or share.
- A honeypot field for anti-spam; a `generate_lead` analytics event.

### Phase 3: Comparison engine
- The data model lives in `src/data.py` with slug, score, price, source URL, best-for, feature flags, minimum seats, categories, pros and cons.
- `/compare.html`: a sortable table with category filter pills and a text filter, a sticky first column, and "Get Quote" + "Review" buttons.
- `/head-to-head.html?a=&b=`: a side-by-side comparison with a shareable URL.
- `/providers/*.html` (15 pages): score card, pricing with source and date, strengths, considerations, feature table, FAQ with schema, alternatives and vs-links.
- `/categories/*.html` (6 pages): intro, filtered table, other notable platforms, what to look for, typical pricing, FAQ.

### Phase 4: Free tools (link magnets + lead feeders)
The tools are a VoIP savings calculator, true-cost calculator, Erlang C staffing calculator, bandwidth calculator, SMS cost estimator, provider-matcher quiz and VoIP readiness (latency/jitter) check. Each page puts the result next to a "Turn these numbers into real offers" quote CTA.

### Phase 5: Content & video
- Eight guides: how to choose, hidden costs, UCaaS vs CCaaS vs CPaaS, number porting, 10DLC, HIPAA checklist, contact-center KPIs, remote stack. Each has an author box, an updated date, a mid-article ad, a sidebar quote card and related guides.
- A filterable video library (privacy-enhanced lazy embeds).
- A 45-term glossary with live filter and DefinedTermSet schema.

### Phase 6: Monetization & community
- **Donate:** $10/$50/$250 tiers; any-amount PayPal (built from the hidden address), GitHub Sponsors, Ko-fi and Buy Me a Coffee (configurable); a spend-allocation chart (operations, testing, promotion, hiring, contests); a pledge/in-kind form; a supporters wall.
- **Contests:** 3 contests with live countdowns, prizes, an entry form and official-rules FAQ (no purchase necessary, 18+, skill-judged).
- **Careers:** 6 remote roles with JobPosting schema and an application form.
- **Advertise:** 8 packages with launch rates, an editorial-independence notice, a domain/website acquisition CTA and an inquiry form.
- **Partners:** get listed, buy leads, affiliate program; partner application form.
- **AdSense:** set `ADSENSE_CLIENT` in `main.js` and every `.ad-slot` activates. Until then the slots show house ads that sell advertising.

### Phase 7: Trust, legal, compliance
About, Methodology (published weights), How We Make Money, Privacy (GDPR/CCPA/PIPEDA/Law 25, SMS clause, Google ads cookies), Terms, Trademark & Copyright disclosure, cookie consent, 404, HTML sitemap.

### Phase 8: Deploy & grow
1. Push to `github.com/WEBWORKSA1/360comm-com` and enable **Settings → Pages → Deploy from branch → main / (root)**.
2. **Custom domain:** add `CNAME` containing `360comm.com`. At the registrar, add A records 185.199.108.153, .109.153, .110.153 and .111.153, plus `www` CNAME → `webworksa1.github.io`. Enable "Enforce HTTPS". Set `SITE_URL` in `src/build.py` to `https://360comm.com`, change the 404 `<base>` to `/`, and rebuild.
3. **FormSubmit:** submit any form once and click the activation email. Optionally paste the random alias into `FORM_ALIAS`.
4. Apply for AdSense and add the publisher line to `ads.txt`. Add GA4/Search Console. Submit `sitemap.xml`.
5. **Growth loop:** re-verify prices monthly and update `PRICE_DATE`; add "X pricing" and "X vs Y" pages; publish 2 guides a week; add a YouTube review for each provider page; sell leads to resellers; recruit contest sponsors.
