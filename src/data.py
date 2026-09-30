# -*- coding: utf-8 -*-
"""360Comm content data. Edit here, then run: python3 src/build.py"""

PRICE_DATE = "Sep 30, 2026"

# Editorial 360 Score (0-10) per /methodology.html. Prices = public starting price, USD unless noted.
PROVIDERS = [
  dict(slug="ringcentral", name="RingCentral", color="#f58220", score=9.2, price="$20/user/mo (annual)", frm=20,
       src="https://www.cloudtalk.io/blog/ringcentral-pricing/", bestFor="Growing teams that want an all-in-one UCaaS platform",
       video=True, sms=True, cc=True, ai=True, mn=1, cats="phone video chat cc sms",
       summary="One of the most complete cloud phone + messaging + video platforms, with a very large integration catalog and global calling coverage.",
       pros=["Phone, SMS, team messaging and video in one app","Large app/CRM integration marketplace","Scales from small offices to multi-site enterprises","Contact-center and AI add-ons available"],
       cons=["Advanced features sit in higher tiers","Taxes/regulatory fees add to advertised price","Monthly (non-annual) billing costs noticeably more"]),
  dict(slug="nextiva", name="Nextiva", color="#005fec", score=9.0, price="$15/user/mo (annual)", frm=15,
       src="https://www.nextiva.com/blog/how-much-does-nextiva-cost.html", bestFor="Small and mid-size businesses that value support",
       video=True, sms=True, cc=True, ai=True, mn=1, cats="phone video cc sms",
       summary="Business phone and customer-experience platform known for its onboarding and support focus.",
       pros=["Low entry price on annual plans","Unified inbox for calls, SMS and chat on upper tiers","Contact-center capabilities in the same vendor","Strong onboarding resources"],
       cons=["Best features require higher tiers","Pricing varies by seat count","SMS may require 10DLC registration fees"]),
  dict(slug="ooma", name="Ooma Office", color="#00a0d6", score=8.6, price="$19.95/user/mo (no contract)", frm=19.95,
       src="https://www.ooma.com/small-business-phone-systems/plans/", bestFor="Small businesses and storefronts wanting simplicity",
       video=True, sms=True, cc=False, ai=False, mn=1, cats="phone sms",
       summary="Straightforward small-business phone service with no annual contract and plug-and-play hardware options.",
       pros=["No contract required","Simple setup; desk-phone and base-station options","Virtual receptionist included","Transparent plan structure"],
       cons=["Fewer enterprise features","Video and advanced features on higher plans","Limited contact-center depth"]),
  dict(slug="dialpad", name="Dialpad", color="#7c52ff", score=8.9, price="$15/user/mo (annual)", frm=15,
       src="https://www.cloudtalk.io/blog/dialpad-pricing/", bestFor="Sales and support teams wanting built-in AI",
       video=True, sms=True, cc=True, ai=True, mn=1, cats="phone video cc sms",
       summary="AI-first cloud communications platform with real-time transcription and call summaries.",
       pros=["Native AI transcription and summaries","Clean, modern apps","Contact-center product on same platform","Good for distributed teams"],
       cons=["Some integrations need higher tiers","Monthly billing costs more","Price shown from third-party source — verify"]),
  dict(slug="vonage", name="Vonage Business", color="#871fff", score=8.4, price="$17.99/line/mo (annual)", frm=17.99,
       src="https://www.vonage.com/unified-communications/pricing/", bestFor="Businesses wanting flexible APIs plus UCaaS",
       video=True, sms=True, cc=True, ai=True, mn=1, cats="phone video cc sms",
       summary="Unified communications with a strong communications-API (CPaaS) heritage for custom workflows.",
       pros=["APIs for custom call/SMS flows","Mobile-first plan available","Contact-center options","Online promos often available"],
       cons=["Add-ons can raise cost","Plan names change frequently","Some features are paid extras"]),
  dict(slug="8x8", name="8x8", color="#e4002b", score=8.5, price="Quote-based", frm=0,
       src="https://www.8x8.com/products/plans-and-pricing", bestFor="Multi-national companies needing global calling",
       video=True, sms=True, cc=True, ai=True, mn=1, cats="phone video cc sms",
       summary="Enterprise-grade UCaaS + CCaaS platform with broad international calling coverage.",
       pros=["Integrated UCaaS and contact center","International calling coverage","Enterprise analytics","Uptime-focused architecture"],
       cons=["No public list pricing","Better fit for mid-market/enterprise","Sales-led buying process"]),
  dict(slug="zoom-phone", name="Zoom Phone", color="#0b5cff", score=8.7, price="$10.50/user/mo metered (annual)", frm=10.5,
       src="https://www.cloudtalk.io/blog/zoom-phone-pricing/", bestFor="Teams already using Zoom meetings",
       video=True, sms=True, cc=True, ai=True, mn=1, cats="phone video chat cc sms",
       summary="Cloud phone system inside the Zoom Workplace app — familiar interface for existing Zoom users.",
       pros=["Same app as Zoom Meetings","Metered and unlimited plan options","AI Companion features","Contact-center product available"],
       cons=["Metered plan charges per minute for outbound","Best value when bundled","Price from third-party source — verify"]),
  dict(slug="grasshopper", name="Grasshopper", color="#29b34a", score=7.8, price="$14/mo (annual, 1 user)", frm=14,
       src="https://www.quo.com/blog/grasshopper-pricing/", bestFor="Solopreneurs needing a virtual business number",
       video=False, sms=True, cc=False, ai=False, mn=1, cats="phone sms",
       summary="Virtual phone number service that runs on your existing mobile phone — no hardware needed.",
       pros=["Very simple setup","Uses your existing cell phone","Business texting","Good for solo operators"],
       cons=["No video meetings","Limited team/call-center features","Plan pricing differs across sources"]),
  dict(slug="aircall", name="Aircall", color="#00b388", score=8.3, price="$30/license/mo (min 3)", frm=30,
       src="https://aircall.io/pricing/", bestFor="Sales and support call teams on a CRM",
       video=False, sms=True, cc=True, ai=True, mn=3, cats="phone cc sms",
       summary="Cloud call-center phone system built around CRM and helpdesk integrations.",
       pros=["Deep CRM/helpdesk integrations","Call-center style routing and analytics","Quick deployment","AI add-ons"],
       cons=["3-license minimum","No native video meetings","Costs rise with add-ons"]),
  dict(slug="goto-connect", name="GoTo Connect", color="#ff6a13", score=8.2, price="Quote-based", frm=0,
       src="https://www.goto.com/pricing/connect", bestFor="SMBs wanting phone + meetings + visual call flows",
       video=True, sms=True, cc=True, ai=True, mn=1, cats="phone video cc sms",
       summary="Phone system with GoTo Meeting heritage and a drag-and-drop call-flow editor.",
       pros=["Visual dial-plan editor","Meetings included in bundles","Contact-center tier","Hardware options"],
       cons=["Pricing is quote-based","Interface less modern than newer rivals","Bundles can be confusing"]),
  dict(slug="teams-phone", name="Microsoft Teams Phone", color="#5b5fc7", score=8.5, price="$10/user/mo + base license", frm=10,
       src="https://www.cloudtalk.io/blog/microsoft-teams-phone-system-pricing/", bestFor="Organizations standardized on Microsoft 365",
       video=True, sms=False, cc=True, ai=True, mn=1, cats="phone video chat cc",
       summary="Adds PSTN calling to Microsoft Teams — ideal when your company already lives in Microsoft 365.",
       pros=["Lives inside Teams","Enterprise security/compliance stack","Copilot AI ecosystem","Contact center via partners/Dynamics"],
       cons=["Requires qualifying Microsoft 365 license","Calling plan billed separately","Native business SMS limited"]),
  dict(slug="google-voice", name="Google Voice", color="#1a73e8", score=8.0, price="$10/user/mo + Workspace", frm=10,
       src="https://www.cloudtalk.io/blog/google-voice-pricing/", bestFor="Google Workspace teams wanting basic calling",
       video=True, sms=True, cc=False, ai=True, mn=1, cats="phone video chat sms",
       summary="Simple cloud calling for Google Workspace customers, managed from the Google Admin console.",
       pros=["Inexpensive add-on to Workspace","Simple admin","Voicemail transcription","Google Meet for video"],
       cons=["Requires Google Workspace","Limited advanced call-center features","SMS availability varies by country"]),
  dict(slug="quo", name="Quo (formerly OpenPhone)", color="#6f42f5", score=8.7, price="$15/user/mo (annual)", frm=15,
       src="https://www.quo.com/pricing", bestFor="Startups and small teams sharing numbers",
       video=False, sms=True, cc=False, ai=True, mn=1, cats="phone sms",
       summary="Modern business phone app with shared numbers, shared inboxes and AI call summaries.",
       pros=["Shared numbers and shared SMS inbox","Beautiful, fast apps","AI summaries","Friendly pricing"],
       cons=["No native video","Not a full contact center","US/Canada focus"]),
  dict(slug="cloudtalk", name="CloudTalk", color="#2f80ed", score=8.1, price="€19/user/mo (annual)", frm=21,
       src="https://www.cloudtalk.io/pricing/", bestFor="Outbound sales teams and EU-based call centers",
       video=False, sms=True, cc=True, ai=True, mn=1, cats="cc phone sms",
       summary="Cloud call-center software focused on sales productivity, with power dialers and international numbers.",
       pros=["Power/smart dialers","Numbers in many countries","CRM integrations","AI conversation insights"],
       cons=["Priced in EUR","No video meetings","Advanced dialers on higher tiers"]),
  dict(slug="justcall", name="JustCall", color="#1cb5e0", score=8.0, price="$29/user/mo (annual, min 2)", frm=29,
       src="https://justcall.io/pricing/", bestFor="SMB sales teams that text and call from a CRM",
       video=False, sms=True, cc=True, ai=True, mn=2, cats="cc phone sms",
       summary="Cloud phone + SMS platform for sales and support teams with bulk SMS and CRM sync.",
       pros=["Bulk and automated SMS","CRM integrations","AI coaching add-ons","Fast onboarding"],
       cons=["2-seat minimum on team plans","No native video","Costs rise with AI add-ons"]),
]

CATEGORIES = [
  dict(slug="business-phone", ico="📞", name="Business Phone & VoIP", short="Cloud PBX, virtual numbers, UCaaS",
       intro="A cloud business phone system (VoIP / UCaaS) replaces the office PBX with an app-based service: numbers, extensions, auto-attendants, call routing, voicemail-to-email and mobile apps — billed per user per month.",
       lookfor=["Total monthly cost after taxes & fees (typically 15–25% above list)","Number porting support and timeline","Auto-attendant / IVR and ring-group flexibility","Mobile and desktop app quality","CRM and helpdesk integrations","Uptime SLA (look for 99.99%+)","Business SMS and 10DLC registration help","E911 and compliance (HIPAA, PCI) if needed"],
       pricing="Most small-business plans start between $10 and $30 per user per month on annual billing; monthly billing usually costs 20–40% more. Desk phones cost roughly $80–$300 each if you want hardware.",
       filt="phone"),
  dict(slug="contact-center", ico="🎧", name="Contact Center (CCaaS)", short="Omnichannel queues, IVR, dialers, QA",
       intro="Contact Center as a Service (CCaaS) handles high-volume customer conversations: skills-based routing, IVR, queue callbacks, outbound dialers, call recording, quality management, workforce management and real-time analytics across voice, chat, email and SMS.",
       lookfor=["Omnichannel routing (voice, chat, email, SMS, social)","IVR builder and callback-in-queue","Predictive / power dialers for outbound","Workforce management & forecasting (Erlang)","Quality management, recording and AI scoring","Supervisor wallboards and real-time analytics","CRM integrations (Salesforce, HubSpot, Zendesk)","PCI-compliant payment handling"],
       pricing="CCaaS seats commonly range from about $30 to $200+ per agent per month depending on channels, AI and WFM. Many enterprise vendors are quote-based.",
       filt="cc"),
  dict(slug="video-conferencing", ico="🎥", name="Video Conferencing", short="Meetings, webinars, rooms",
       intro="Video conferencing platforms power meetings, webinars and conference rooms. Most modern UCaaS suites include meetings; standalone tools remain popular for webinars, large events and cross-company collaboration.",
       lookfor=["Participant limits and meeting duration caps","Recording, transcription and AI summaries","Webinar and large-event options","Room-system hardware compatibility","Calendar integration (Google, Outlook)","End-to-end encryption and admin controls","Breakout rooms, whiteboards and polls","Bandwidth efficiency on weak connections"],
       pricing="Free tiers exist for short meetings; paid business plans typically cost about $10–$25 per host per month; webinar add-ons and room licenses are extra.",
       filt="video"),
  dict(slug="team-chat", ico="💬", name="Team Chat & Collaboration", short="Channels, DMs, huddles, file sharing",
       intro="Team chat apps organize internal communication into channels and direct messages with file sharing, quick audio/video huddles, integrations and searchable history — reducing internal email dramatically.",
       lookfor=["Message history and search limits on free plans","Guest/external collaboration (shared channels)","Integrations and workflow automation","Huddles / quick calls","Data retention and eDiscovery","SSO and security controls","Mobile app quality","Pricing per active user"],
       pricing="Common business plans run about $4–$15 per user per month; many teams get chat bundled in their UCaaS or productivity suite.",
       filt="chat"),
  dict(slug="business-sms", ico="✉️", name="Business SMS & CPaaS", short="Texting, 10DLC, APIs, campaigns",
       intro="Business texting and Communications Platform as a Service (CPaaS) let you send SMS/MMS, WhatsApp and voice from apps, CRMs and workflows — from two-way customer texting to automated alerts, reminders and marketing campaigns.",
       lookfor=["10DLC / toll-free verification support","Two-way shared inboxes","Opt-in / opt-out (STOP) compliance tooling","APIs and webhooks","Per-segment pricing and carrier fees","Delivery reporting","Templates, scheduling and automations","WhatsApp / RCS readiness"],
       pricing="API SMS in the US commonly costs a fraction of a cent to about 1–2 cents per segment plus carrier pass-through fees; campaign platforms charge monthly plans plus usage. See our SMS cost estimator.",
       filt="sms"),
  dict(slug="business-internet", ico="🌐", name="Business Internet & Connectivity", short="Fiber, DIA, 5G backup, SD-WAN",
       intro="Every cloud communications tool depends on the connection underneath it. Business internet options include cable, fiber, dedicated internet access (DIA), fixed wireless and 5G/LTE backup, often combined with SD-WAN for failover.",
       lookfor=["Symmetrical upload speed (critical for video)","Service-level agreement and repair times","Static IP availability","Failover / backup (5G, second ISP)","Latency and jitter under load","Contract length and installation fees","QoS support on your router","Local availability by address"],
       pricing="Small-business cable/fiber plans commonly run about $50–$250 per month; dedicated fiber (DIA) typically runs several hundred dollars per month and up, depending on location.",
       filt="none"),
]

TOOLS = [
  dict(slug="voip-savings-calculator", ico="💰", name="VoIP Savings Calculator", d="See what you could save by switching from landlines or a legacy PBX."),
  dict(slug="true-cost-calculator", ico="🧾", name="True Cost Calculator", d="Advertised price vs real bill: seats, add-ons, numbers, taxes & hardware."),
  dict(slug="call-center-staffing-calculator", ico="👥", name="Erlang C Staffing Calculator", d="How many agents you need to hit your service level."),
  dict(slug="bandwidth-calculator", ico="📶", name="VoIP & Video Bandwidth Calculator", d="Size your internet connection for calls, meetings and data."),
  dict(slug="sms-cost-calculator", ico="✉️", name="SMS Campaign Cost Estimator", d="Estimate monthly texting costs including carrier fees."),
  dict(slug="provider-matcher", ico="🎯", name="Provider Matcher Quiz", d="Answer 5 questions, get your top 3 platform matches."),
  dict(slug="voip-readiness-test", ico="⚡", name="VoIP Readiness Check", d="Quick browser-based latency & jitter screen."),
]

VIDEOS = [
  ("jxTMZ22K0zE", "What is VoIP? (VoIP explained)", "Basics"),
  ("uyxw-8pSdp0", "What is VoIP and how does it work? (for business)", "Basics"),
  ("UB6nxN3SRP0", "How does VoIP work? Voice over Internet Protocol", "Basics"),
  ("I-zksmn9CKg", "VoIP phone systems explained: pros and cons", "Buying"),
  ("7GwKX7dt3mM", "UCaaS vs CCaaS — what's the difference?", "Contact Center"),
  ("f23enA-9xmU", "UCaaS vs CPaaS vs CCaaS", "Contact Center"),
  ("ULZQcnEgW80", "UCaaS vs CCaaS: which should you use?", "Contact Center"),
  ("kgPx6__zQJc", "What is SIP trunking?", "Technical"),
  ("CYinuGgtDKI", "SIP trunks explained for business", "Technical"),
  ("C9y7PgGnALM", "How modern phone systems work: PBX & SIP trunking", "Technical"),
]

GLOSSARY = [
  ("ACD","Automatic Call Distributor — routes inbound calls to the right agent or queue."),
  ("AHT","Average Handle Time — talk + hold + after-call work per interaction."),
  ("ASA","Average Speed of Answer — mean time callers wait before an agent answers."),
  ("Auto-attendant","A virtual receptionist menu (\"Press 1 for sales\") that routes callers."),
  ("BYOD","Bring Your Own Device — employees use personal phones/computers with business apps."),
  ("CCaaS","Contact Center as a Service — cloud-hosted contact-center software."),
  ("CPaaS","Communications Platform as a Service — APIs to embed voice, SMS and video in apps."),
  ("Codec","Algorithm that compresses audio/video (e.g., G.711, G.729, Opus)."),
  ("CSAT","Customer Satisfaction score, usually from a post-interaction survey."),
  ("DID","Direct Inward Dialing — a phone number that rings a specific user or device directly."),
  ("DIA","Dedicated Internet Access — uncontended, SLA-backed business fiber."),
  ("E911","Enhanced 911 — sends a caller's registered address to emergency services."),
  ("Erlang","Unit of telephone traffic: one Erlang = one line continuously busy for an hour."),
  ("FCR","First Contact Resolution — issues resolved in the first interaction."),
  ("Hunt group","A set of phones that ring in a pattern until someone answers."),
  ("IVR","Interactive Voice Response — automated menus using keypad or speech input."),
  ("Jitter","Variation in packet arrival time; high jitter causes choppy audio."),
  ("KPI","Key Performance Indicator — a metric tracked against a goal."),
  ("Latency","Delay for data to travel between endpoints; under 150 ms one-way is recommended for voice."),
  ("LNP","Local Number Portability — moving your existing number to a new carrier."),
  ("MOS","Mean Opinion Score — 1–5 rating of perceived call quality."),
  ("Occupancy","Share of logged-in time agents spend handling contacts."),
  ("Omnichannel","Unified handling of voice, chat, email, SMS and social in one queue and history."),
  ("Packet loss","Data packets that never arrive; over 1% degrades call quality."),
  ("PBX","Private Branch Exchange — the switching system behind business phone extensions."),
  ("Porting","The process of transferring a phone number between carriers."),
  ("Predictive dialer","Outbound dialer that calls multiple numbers per agent and connects answered calls."),
  ("PSTN","Public Switched Telephone Network — the traditional global phone network."),
  ("QoS","Quality of Service — router rules that prioritize voice/video traffic."),
  ("Ring group","Several extensions that ring together for one number."),
  ("SBC","Session Border Controller — secures and manages SIP traffic at the network edge."),
  ("SD-WAN","Software-defined WAN — intelligently routes traffic across multiple internet links."),
  ("Service level","Percent of calls answered within a target time (e.g., 80/20)."),
  ("Shrinkage","Paid agent time not available for contacts (breaks, training, absence)."),
  ("SIP","Session Initiation Protocol — the signaling standard behind most VoIP calls."),
  ("SIP trunk","A virtual line connecting a PBX to the PSTN over the internet."),
  ("SLA","Service Level Agreement — contractual uptime/support commitments."),
  ("Softphone","A software app that makes calls from a computer or mobile device."),
  ("10DLC","10-digit long code — US system for registering businesses that send A2P SMS from local numbers."),
  ("Toll-free verification","Carrier approval process required to send SMS from toll-free numbers."),
  ("UCaaS","Unified Communications as a Service — cloud phone, messaging, video in one platform."),
  ("Voicemail-to-email","Delivers voicemail audio/transcripts to your inbox."),
  ("VoIP","Voice over Internet Protocol — phone calls carried over data networks."),
  ("WebRTC","Browser standard for real-time voice/video without plugins."),
  ("WFM","Workforce Management — forecasting, scheduling and adherence for agents."),
]

# Guides: (slug, title, description, category tag, minutes, html body)
GUIDES = [
("how-to-choose-a-business-phone-system", "How to Choose a Business Phone System in 2026: A 9-Step Framework",
 "A practical, vendor-neutral framework to pick the right VoIP/UCaaS platform — requirements, pricing traps, demos and rollout.", "Buying Guide", 9, """
<p>Choosing a business phone system is a 3–5 year decision that touches every customer conversation. The good news: cloud platforms have made switching cheaper and faster than ever. The bad news: dozens of near-identical plans make it easy to overpay. Use this framework to decide in days, not months.</p>
<h2>1. Map how you actually communicate</h2>
<p>Before looking at vendors, count <strong>users</strong> (people who need a number or extension), <strong>shared lines</strong> (sales, support, front desk), <strong>locations</strong> and <strong>call volume</strong>. Pull the last three months of your phone bill and note inbound vs outbound minutes, international calls and text usage.</p>
<h2>2. Decide what category you are buying</h2>
<ul><li><strong>Virtual number</strong> — solo operators who just need a business line on their cell.</li><li><strong>UCaaS</strong> — phone + SMS + video + chat for a whole team.</li><li><strong>CCaaS</strong> — queues, IVR, dialers and analytics for dedicated agents.</li></ul>
<p>Many businesses need UCaaS now and a contact-center add-on later — pick a vendor that offers both so you avoid a second migration.</p>
<h2>3. Write your must-have list (max 8 items)</h2>
<p>Typical must-haves: auto-attendant, ring groups, mobile app, voicemail transcription, CRM integration, call recording, business SMS, and a 99.99% uptime SLA. Everything else is a nice-to-have. A short list prevents feature-shopping into a higher tier you don't need.</p>
<h2>4. Price the <em>real</em> bill, not the headline</h2>
<p>Advertised prices usually assume annual billing and exclude taxes and regulatory recovery fees (commonly 15–25% extra). Add: extra numbers, toll-free minutes, SMS registration, recording storage, AI add-ons and hardware. Our <a href="../tools/true-cost-calculator.html">True Cost Calculator</a> does this in one minute.</p>
<h2>5. Shortlist three vendors</h2>
<p>Use our <a href="../compare.html">comparison table</a> or the <a href="../tools/provider-matcher.html">Provider Matcher</a>. Three is the magic number — enough to create price competition, few enough to demo properly.</p>
<h2>6. Run scripted demos</h2>
<p>Give every vendor the same script: build our main-line call flow, show the mobile app transferring a call, show the admin portal adding a user, show reporting. Record each demo and score it on the same sheet.</p>
<h2>7. Test call quality on your network</h2>
<p>Run a <a href="../tools/voip-readiness-test.html">readiness check</a>, then request a trial and make real calls at peak hours. If quality suffers, enable QoS on your router or size your bandwidth with our <a href="../tools/bandwidth-calculator.html">bandwidth calculator</a>.</p>
<h2>8. Negotiate</h2>
<ul><li>Ask for the annual price on a monthly contract (or vice-versa for a bigger discount).</li><li>Ask for free porting, free onboarding and a price-lock for the full term.</li><li>Ask for a 30–60 day out clause tied to call quality.</li></ul>
<h2>9. Plan the cutover</h2>
<p>Port numbers last. Build call flows, train staff and test with temporary numbers first, then schedule the port for a quiet day. Read our <a href="number-porting-guide.html">number porting guide</a> for the exact steps.</p>
<div class="callout"><strong>Shortcut:</strong> Tell us your requirements once and receive up to five tailored quotes — free, no obligation. <a href="../quotes.html">Get free quotes →</a></div>
"""),
("voip-hidden-costs", "The Hidden Costs of VoIP: 11 Fees That Inflate Your Phone Bill",
 "Why your VoIP invoice is higher than the advertised price — taxes, regulatory fees, add-ons, minimum seats — and how to avoid each.", "Pricing", 7, """
<p>A $20/user plan rarely costs $20. Industry pricing guides consistently show that taxes, regulatory fees and add-ons push real invoices 15–25% above the headline — sometimes much more once hardware and extra numbers are included. Here is every line item to budget for.</p>
<h2>Taxes and government fees</h2>
<ol><li><strong>Federal Universal Service Fund (USF)</strong> — a percentage of the interstate portion of your bill, set quarterly.</li><li><strong>State and local taxes</strong> — sales and telecom taxes vary widely by address.</li><li><strong>E911 fees</strong> — per-line fees that fund emergency services.</li><li><strong>Regulatory recovery fees</strong> — a provider-set charge to recover compliance costs.</li></ol>
<h2>Plan and usage add-ons</h2>
<ol start="5"><li><strong>Monthly vs annual billing</strong> — month-to-month often costs 20–40% more.</li><li><strong>Minimum seats</strong> — some plans require 2–3 licenses minimum.</li><li><strong>Extra numbers and toll-free minutes</strong> — additional DIDs and toll-free usage are frequently billed separately.</li><li><strong>SMS registration (10DLC)</strong> — brand and campaign registration fees plus per-message carrier fees.</li><li><strong>Call recording storage and AI</strong> — transcription, summaries and analytics are often paid add-ons.</li></ol>
<h2>One-time costs</h2>
<ol start="10"><li><strong>Hardware</strong> — desk phones and headsets ($80–$300+ per phone for business-grade models).</li><li><strong>Porting and setup</strong> — some carriers charge to port or for professional onboarding.</li></ol>
<table><thead><tr><th>Line item</th><th>Typical impact</th><th>How to reduce</th></tr></thead><tbody>
<tr><td>Taxes & regulatory fees</td><td>+15–25%</td><td>Budget for it; ask for an all-in quote</td></tr>
<tr><td>Monthly billing</td><td>+20–40%</td><td>Commit annually once trial succeeds</td></tr>
<tr><td>Add-ons (AI, recording)</td><td>+$5–$30/user</td><td>Buy only for roles that need it</td></tr>
<tr><td>Hardware</td><td>One-time</td><td>Use softphones and headsets instead</td></tr></tbody></table>
<div class="callout">Run your own numbers with the <a href="../tools/true-cost-calculator.html">True Cost Calculator</a>, then <a href="../quotes.html">get all-in quotes</a> so vendors compete on the total, not the headline.</div>
"""),
("ucaas-vs-ccaas-vs-cpaas", "UCaaS vs CCaaS vs CPaaS: What's the Difference and Which Do You Need?",
 "Plain-English explanation of the three cloud communications categories, with a decision table.", "Explainer", 6, """
<p>Vendors use three overlapping acronyms. Understanding them prevents buying the wrong product — or two products when one would do.</p>
<h2>UCaaS — Unified Communications as a Service</h2>
<p>Internal and external collaboration for <strong>every employee</strong>: phone numbers and extensions, voicemail, SMS, team chat and video meetings in one app. Priced per user.</p>
<h2>CCaaS — Contact Center as a Service</h2>
<p>Tools for <strong>dedicated agents</strong> handling high volumes: queues, IVR, skills-based routing, dialers, recording, quality management, workforce management and real-time dashboards. Priced per agent, usually higher than UCaaS.</p>
<h2>CPaaS — Communications Platform as a Service</h2>
<p><strong>APIs for developers</strong> to embed SMS, voice, video, WhatsApp and verification into apps and workflows. Priced per usage (per message, per minute).</p>
<table><thead><tr><th>You need…</th><th>Choose</th></tr></thead><tbody>
<tr><td>A phone system for the whole team</td><td>UCaaS</td></tr>
<tr><td>5+ people answering customer calls all day</td><td>CCaaS (or UCaaS with CC add-on)</td></tr>
<tr><td>Automated texts, OTP codes, app calling</td><td>CPaaS</td></tr>
<tr><td>All of the above</td><td>A vendor offering UCaaS + CCaaS with APIs</td></tr></tbody></table>
<p>Most growing businesses start with UCaaS and add CCaaS once call volume justifies dedicated agents. Size that moment with our <a href="../tools/call-center-staffing-calculator.html">Erlang C staffing calculator</a>.</p>
"""),
("number-porting-guide", "How to Port Your Business Phone Number Without Downtime",
 "Step-by-step number porting checklist: LOA, CSR, timing, and the mistakes that cause rejections.", "How-To", 6, """
<p>Porting (Local Number Portability) moves your existing number to a new provider. Done right, customers never notice. Done wrong, your main line goes dark. Follow this checklist.</p>
<h2>Before you start</h2>
<ul><li><strong>Do not cancel your old service</strong> — cancelling can release the number.</li><li>Request a <strong>Customer Service Record (CSR)</strong> from your current carrier; the name, address and account number must match exactly.</li><li>Get your <strong>account PIN / port-out passcode</strong> (mobile carriers require it).</li><li>List every number: main lines, fax, toll-free, DIDs.</li></ul>
<h2>The porting process</h2>
<ol><li>Set up users and call flows on the new platform using temporary numbers.</li><li>Submit a <strong>Letter of Authorization (LOA)</strong> and a recent bill copy to the new provider.</li><li>Wait for the <strong>Firm Order Commitment (FOC)</strong> date — typically days to a few weeks.</li><li>On port day, test inbound calls, SMS and voicemail immediately.</li><li>Cancel the old service only after all numbers are confirmed working.</li></ol>
<h2>Top reasons ports get rejected</h2>
<ul><li>Name or address mismatch with the CSR</li><li>Wrong account number or missing PIN</li><li>Partial port of a hunt group without specifying the billing telephone number</li><li>Numbers under contract or with a pending order</li></ul>
<div class="callout">Tip: Schedule the port mid-week in the morning so support teams are available if anything goes wrong.</div>
"""),
("10dlc-sms-registration", "10DLC Registration Explained: How to Get Your Business Texts Delivered",
 "Why US carriers require 10DLC brand and campaign registration, what it costs, and how to pass on the first try.", "Compliance", 6, """
<p>If you send business (A2P) text messages from a regular 10-digit US number, carriers require <strong>10DLC registration</strong>. Unregistered traffic is heavily filtered or blocked.</p>
<h2>The two registrations</h2>
<ol><li><strong>Brand</strong> — your legal business identity (legal name, EIN/tax ID, address, website).</li><li><strong>Campaign</strong> — what you send (use case, sample messages, opt-in method, opt-out language).</li></ol>
<h2>How to pass on the first attempt</h2>
<ul><li>Legal name and tax ID must match government records exactly.</li><li>Your website should be live with a privacy policy that mentions SMS and says phone numbers are not shared for marketing.</li><li>Show a clear opt-in: a checkbox or keyword with consent language.</li><li>Sample messages must include your brand name and "Reply STOP to opt out".</li></ul>
<h2>Costs to expect</h2>
<p>Expect one-time brand/vetting fees, a monthly campaign fee and per-message carrier surcharges on top of your provider's message rate. Estimate yours with the <a href="../tools/sms-cost-calculator.html">SMS Cost Estimator</a>.</p>
<h2>Alternatives</h2>
<p>Toll-free numbers require <strong>toll-free verification</strong> instead; short codes offer the highest throughput but cost more and take longer to approve.</p>
<p class="small muted">This guide is general information, not legal advice. Consent rules (e.g., TCPA in the US, CASL in Canada) apply to marketing texts.</p>
"""),
("hipaa-compliant-voip-checklist", "HIPAA-Compliant VoIP: A 12-Point Checklist for Healthcare Practices",
 "What clinics, dental offices and telehealth providers should verify before choosing a phone system.", "Industry", 7, """
<p>Phone systems in healthcare handle protected health information (PHI) in voicemails, recordings, texts and call logs. A provider marketing itself as "HIPAA-ready" is not enough — you must verify.</p>
<h2>The checklist</h2>
<ol><li>Provider will sign a <strong>Business Associate Agreement (BAA)</strong>.</li><li>Encryption in transit (TLS/SRTP) for calls and messages.</li><li>Encryption at rest for voicemail, recordings and transcripts.</li><li>Role-based admin access and multi-factor authentication.</li><li>Audit logs for access to recordings and voicemail.</li><li>Configurable retention and deletion policies.</li><li>Secure texting or the ability to disable SMS for PHI.</li><li>Fax-to-email with encryption if you still fax.</li><li>Data-center security attestations (e.g., SOC 2 reports).</li><li>Documented breach notification process.</li><li>After-hours routing to on-call staff with privacy controls.</li><li>Staff training on what not to leave in voicemail or SMS.</li></ol>
<div class="callout">Practices typically also want appointment-reminder texts, EHR integration and after-hours answering. <a href="../quotes.html?need=phone">Request healthcare-ready quotes →</a></div>
<p class="small muted">General information only; consult your compliance officer or counsel for your specific obligations.</p>
"""),
("contact-center-kpis", "15 Contact Center KPIs That Actually Matter (with Benchmarks to Aim For)",
 "Service level, ASA, AHT, FCR, occupancy and more — definitions, formulas and what 'good' looks like.", "Contact Center", 8, """
<p>Contact centers can measure hundreds of things. These 15 metrics explain almost all customer experience and cost outcomes.</p>
<table><thead><tr><th>KPI</th><th>Formula</th><th>Common target</th></tr></thead><tbody>
<tr><td>Service level</td><td>% answered within X sec</td><td>80% in 20 sec (voice)</td></tr>
<tr><td>Average speed of answer</td><td>Total wait ÷ answered calls</td><td>Under 30 sec</td></tr>
<tr><td>Abandonment rate</td><td>Abandoned ÷ offered</td><td>Under 5–8%</td></tr>
<tr><td>Average handle time</td><td>(Talk + hold + wrap) ÷ calls</td><td>Varies by industry</td></tr>
<tr><td>First contact resolution</td><td>Resolved first time ÷ total</td><td>70%+</td></tr>
<tr><td>Occupancy</td><td>Handle time ÷ available time</td><td>75–85%</td></tr>
<tr><td>Shrinkage</td><td>Unavailable paid time ÷ paid time</td><td>Often 25–35%</td></tr>
<tr><td>CSAT</td><td>Satisfied responses ÷ total</td><td>80%+</td></tr>
<tr><td>NPS</td><td>% promoters − % detractors</td><td>Positive and rising</td></tr>
<tr><td>Customer effort score</td><td>Avg ease rating</td><td>Low effort</td></tr>
<tr><td>Schedule adherence</td><td>Time in adherence ÷ scheduled</td><td>90%+</td></tr>
<tr><td>Transfer rate</td><td>Transferred ÷ handled</td><td>Low and falling</td></tr>
<tr><td>Cost per contact</td><td>Total cost ÷ contacts</td><td>Trend down</td></tr>
<tr><td>Agent attrition</td><td>Leavers ÷ avg headcount</td><td>Below industry avg</td></tr>
<tr><td>Self-service containment</td><td>Resolved in IVR/bot ÷ total</td><td>Rising without hurting CSAT</td></tr></tbody></table>
<p>Benchmarks vary widely by industry and channel; use targets as starting points. To translate service-level targets into headcount, use the <a href="../tools/call-center-staffing-calculator.html">Erlang C calculator</a>.</p>
"""),
("remote-team-communication-stack", "The Remote Team Communication Stack: Tools, Rules and Rituals",
 "How distributed teams combine phone, chat, video and async tools without drowning in notifications.", "Strategy", 7, """
<p>Remote teams don't fail because of missing tools — they fail because of too many overlapping ones with no rules. A good stack has one tool per job and clear norms.</p>
<h2>One tool per job</h2>
<table><thead><tr><th>Job</th><th>Tool type</th><th>Norm</th></tr></thead><tbody>
<tr><td>Customers calling/texting</td><td>Cloud phone (UCaaS)</td><td>Shared numbers, ring groups, SLAs</td></tr>
<tr><td>Quick internal questions</td><td>Team chat</td><td>Channels over DMs; reply within hours</td></tr>
<tr><td>Decisions & discussion</td><td>Video meeting</td><td>Agenda required; record & summarize</td></tr>
<tr><td>Long-form updates</td><td>Docs / async video</td><td>Weekly written updates</td></tr>
<tr><td>Urgent incidents</td><td>Phone / paging</td><td>Only for true emergencies</td></tr></tbody></table>
<h2>Five rules that cut noise</h2>
<ol><li>Default to async; meet only when a decision needs real-time debate.</li><li>Publish response-time expectations per channel.</li><li>Use AI meeting summaries so non-attendees stay informed.</li><li>Set "focus hours" with notifications paused.</li><li>Review the stack every six months and cut overlapping subscriptions.</li></ol>
<p>Consolidating onto a single UCaaS platform that covers phone, chat and video often lowers cost and context-switching. <a href="../compare.html">Compare all-in-one platforms →</a></p>
"""),
]
