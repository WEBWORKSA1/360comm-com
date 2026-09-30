# 360Comm.com — The 360° Business Communications Hub

Static site with independent comparisons, free calculators, guides, videos and a no-obligation quote marketplace for business phone/VoIP, contact center, video, team chat, business SMS and business internet.

- **Live (GitHub Pages):** https://webworksa1.github.io/360comm-com/
- **Build prompt and strategy:** [BUILD-PROMPT.md](BUILD-PROMPT.md)

## Structure
```
index.html, quotes.html (lead wizard), compare.html, head-to-head.html
providers/ (15)  categories/ (6)  tools/ (7)  guides/ (8)
videos, glossary, donate, contests, careers, advertise, partners, contact
about, methodology, disclosure, privacy, terms, legal, 404, sitemap
assets/css/style.css  assets/js/main.js  assets/js/tools.js
src/data.py (content + provider data)  src/build.py (generator)
```

## Edit and rebuild
```bash
python3 src/build.py      # regenerates every HTML page, sitemap.xml and search-index.json
```

## Configuration (`assets/js/main.js` → `CONFIG`)
| Key | Purpose |
|---|---|
| `FORM_ALIAS` | Optional FormSubmit alias. The single inbox address is stored obfuscated and never appears in the HTML. |
| `ADSENSE_CLIENT` | `ca-pub-…` ID. Once set, every `.ad-slot` becomes a responsive AdSense unit. |
| `DONATE.kofi / bmc / github` | Donation platform URLs. Empty ones are hidden automatically. |

**First form submission:** FormSubmit sends a one-time activation email to the inbox. Click it to start receiving submissions.

## Custom domain (360comm.com)
1. Add a file named `CNAME` containing `360comm.com`.
2. At the DNS provider, add A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153` and `185.199.111.153`, plus `www` CNAME → `webworksa1.github.io`.
3. Go to Settings → Pages → Custom domain and turn on Enforce HTTPS.
4. In `src/build.py`, set `SITE_URL = "https://360comm.com"` and change the 404 `<base href>` to `/`. Then rebuild.

## Legal
© 2026 360Comm. All rights reserved. 360Comm is an independent publication, not affiliated with any entity named "360 Comm", "360 Communications" or similar. Third-party trademarks belong to their owners and are used for identification only. See `legal.html`.
