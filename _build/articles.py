# Single source of truth for BuildTek article metadata.
# Used by rebuild_blog_heads.py, make_og.py and build_blog_index.py.

SITE = "https://buildtek.in"
ORG = "BuildTek Events"
PUBLISHED = "2026-08-17"          # real authoring date of the pharma set
AISEC_PUBLISHED = "2026-08-30"    # AI-Sec set, written today

ARTICLES = [
 dict(slug="navigating-the-2026-patent-cliff-what-pharmaceutical-leaders-must-do-now",
   title="Navigating the 2026 Patent Cliff: What Pharma Leaders Must Do Now",
   h1="Navigating the 2026 Patent Cliff: What Pharmaceutical Leaders Must Do Now",
   desc="Over $300bn in annual drug revenue loses patent protection by 2030. How pharmaceutical executives are restructuring portfolios, M&A and lifecycle strategy now.",
   cat="Strategy", mins=6, topic="patent cliff",
   kw=["pharma patent cliff 2026","drug patent expiry","pharmaceutical portfolio strategy","loss of exclusivity"],
   img="https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1200&q=80&fit=crop"),

 dict(slug="ai-in-drug-discovery-from-algorithms-to-clinical-reality-in-2026",
   title="AI in Drug Discovery: From Algorithms to Clinical Reality in 2026",
   h1="AI in Drug Discovery: From Algorithms to Clinical Reality in 2026",
   desc="AI-discovered molecules have reached Phase 2. Where machine learning genuinely accelerates pharmaceutical R&D in 2026 — and where caution is still warranted.",
   cat="R&D", mins=7, topic="AI drug discovery",
   kw=["AI drug discovery 2026","machine learning pharma R&D","AI clinical trials","computational drug design"],
   img="https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=1200&q=80&fit=crop"),

 dict(slug="pharma-supply-chain-resilience-in-2026-the-strategic-imperative-no-executive-can-ignore",
   title="Pharma Supply Chain Resilience in 2026: The Strategic Imperative",
   h1="Pharma Supply Chain Resilience in 2026: The Strategic Imperative No Executive Can Ignore",
   desc="The FDA logged ~270 active drug shortages in 2025. The three pillars of pharmaceutical supply chain resilience — API diversification, visibility and CDMO strategy.",
   cat="Operations", mins=7, topic="supply chain",
   kw=["pharma supply chain resilience","drug shortages 2026","API sourcing diversification","CDMO strategy"],
   img="https://images.unsplash.com/photo-1578575437130-527eed3abbec?w=1200&q=80&fit=crop"),

 dict(slug="pharma-4-0-what-it-actually-means-for-pharmaceutical-manufacturing-leaders-in-2026",
   title="Pharma 4.0: What It Actually Means for Manufacturing Leaders",
   h1="Pharma 4.0: What It Actually Means for Pharmaceutical Manufacturing Leaders in 2026",
   desc="Beyond the buzzword. The core Pharma 4.0 technologies, the implementation barriers executives actually hit, and what regulators now expect from digital manufacturing.",
   cat="Manufacturing", mins=8, topic="Pharma 4.0",
   kw=["Pharma 4.0","pharmaceutical smart manufacturing","digital twin pharma","continuous manufacturing GMP"],
   img="https://images.unsplash.com/photo-1581093588401-fbb62a02f120?w=1200&q=80&fit=crop"),

 dict(slug="why-pharma-executives-attend-virtual-leadership-summits-in-2026-and-what-they-get-from-it",
   title="Why Pharma Executives Attend Virtual Leadership Summits in 2026",
   h1="Why Pharma Executives Attend Virtual Leadership Summits in 2026 — And What They Get From It",
   desc="The pharma conference calendar is crowded. Why senior leaders increasingly choose focused virtual formats over large trade shows, and what they expect in return.",
   cat="Leadership", mins=6, topic="virtual summits",
   kw=["virtual pharma summit 2026","pharma leadership conference","pharmaceutical executive events","B2B virtual conference"],
   img="https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?w=1200&q=80&fit=crop"),

 dict(slug="commercializing-biosimilars-strategies-for-the-2026-market-landscape",
   title="Commercializing Biosimilars: Strategies for the 2026 Market",
   h1="Commercializing Biosimilars: Strategies for the 2026 Market Landscape",
   desc="Biosimilars have moved from novelty to fierce competition. Pricing, market penetration and physician engagement strategies for the 2026 biosimilar landscape.",
   cat="Commercial", mins=6, topic="biosimilars",
   kw=["biosimilar commercialization","biosimilar pricing strategy","biologics patent expiry","biosimilar market access"],
   img="https://images.unsplash.com/photo-1579154204601-01588f351e67?w=1200&q=80&fit=crop"),

 dict(slug="navigating-global-quality-standards-the-new-era-of-data-integrity",
   title="Global Quality Standards: The New Era of Data Integrity",
   h1="Navigating Global Quality Standards: The New Era of Data Integrity",
   desc="ALCOA+ is now a board-level concern. How FDA and EMA data integrity expectations are reshaping GMP compliance, and what moving beyond paper actually requires.",
   cat="Quality", mins=6, topic="data integrity",
   kw=["pharma data integrity","ALCOA+ principles","GMP compliance 2026","FDA EMA data integrity"],
   img="https://images.unsplash.com/photo-1516549655169-df83a0774514?w=1200&q=80&fit=crop"),

 dict(slug="candida-auris-why-the-world-s-most-dangerous-superbug-is-a-pharma-industry-wake-up-call",
   title="Candida Auris: Pharma's Antifungal Resistance Wake-Up Call",
   h1="Candida Auris: Why the World's Most Dangerous Superbug Is a Pharma Industry Wake-Up Call",
   desc="A multidrug-resistant fungal pathogen is spreading through hospitals worldwide. What Candida auris reveals about the broken economics of antimicrobial development.",
   cat="Public Health", mins=6, topic="AMR",
   kw=["Candida auris","antimicrobial resistance pharma","antifungal drug pipeline","AMR drug development"],
   img="https://images.unsplash.com/photo-1583912267550-d6c2ac3196c0?w=1200&q=80&fit=crop"),

 dict(slug="the-2026-covid-summer-surge-and-what-it-reveals-about-the-antiviral-drug-pipeline",
   title="The 2026 COVID Summer Surge and the Antiviral Drug Pipeline",
   h1="The 2026 COVID Summer Surge and What It Reveals About the Antiviral Drug Pipeline",
   desc="COVID has slipped down the pharma agenda, but the 2026 summer surge exposes uncomfortable truths about antiviral pipeline investment and pandemic preparedness.",
   cat="Public Health", mins=6, topic="antivirals",
   kw=["COVID 2026 surge","antiviral drug pipeline","pandemic preparedness pharma","respiratory antivirals"],
   img="https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?w=1200&q=80&fit=crop"),

 dict(slug="eli-lilly-s-retatrutide-lawsuits-what-the-glp-1-black-market-tells-us-about-pharma-s-ip-crisis",
   title="Retatrutide Lawsuits: The GLP-1 Black Market and Pharma's IP Crisis",
   h1="Eli Lilly's Retatrutide Lawsuits: What the GLP-1 Black Market Tells Us About Pharma's IP Crisis",
   desc="An unapproved Phase 3 drug is already sold online. Eli Lilly's retatrutide lawsuits expose how compounding, peptide sellers and demand are outrunning pharma IP enforcement.",
   cat="Legal & IP", mins=7, topic="GLP-1 IP",
   kw=["retatrutide lawsuit","GLP-1 black market","pharma IP enforcement","compounded semaglutide legal"],
   img="https://images.unsplash.com/photo-1471864190281-a93a3070b6de?w=1200&q=80&fit=crop"),
]

AISEC_ARTICLES = [
 dict(slug="blog-01-mcp-attack-surface",
   title="The MCP Attack Surface: Securing Model Context Protocol",
   h1="The MCP Attack Surface: What Security Leaders Need to Know About Model Context Protocol",
   desc="Model Context Protocol connects LLMs to live tools and data. The trust boundaries it creates, the attack classes it enables, and how to govern MCP servers in production.",
   cat="AI Security", mins=9, topic="MCP security",
   kw=["MCP security","Model Context Protocol attack surface","LLM tool security","AI agent security"],
   img="https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&q=80&fit=crop"),

 dict(slug="blog-02-indirect-prompt-injection-rag",
   title="Indirect Prompt Injection in RAG Pipelines",
   h1="Indirect Prompt Injection in RAG Pipelines: The Threat Hiding in Your Own Documents",
   desc="Retrieval-augmented generation turns your document store into an untrusted input channel. How indirect prompt injection works against RAG, and the controls that hold up.",
   cat="AI Security", mins=9, topic="prompt injection",
   kw=["indirect prompt injection","RAG security","LLM injection defence","retrieval augmented generation risk"],
   img="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1200&q=80&fit=crop"),

 dict(slug="blog-03-eu-ai-act-enforcement",
   title="EU AI Act Enforcement: What Changes for Security Teams",
   h1="EU AI Act Enforcement in 2026: What Actually Changes for Security and Compliance Teams",
   desc="The EU AI Act's obligations are landing. Risk classification, GPAI duties, documentation expectations and the security controls that regulators will look for.",
   cat="Regulation", mins=8, topic="EU AI Act",
   kw=["EU AI Act enforcement","AI Act compliance 2026","GPAI obligations","AI regulation security"],
   img="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1200&q=80&fit=crop"),

 dict(slug="blog-04-agent-tool-calling-hijacks",
   title="Agent Tool-Calling Hijacks: When Your AI Acts Against You",
   h1="Agent Tool-Calling Hijacks: When Your AI Assistant Acts Against You",
   desc="Autonomous agents that call tools can be steered into destructive actions. The hijack patterns seen in the wild and the authorisation design that contains them.",
   cat="AI Security", mins=8, topic="agent hijacking",
   kw=["AI agent hijacking","tool calling security","autonomous agent risk","LLM agent authorisation"],
   img="https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=1200&q=80&fit=crop"),

 dict(slug="blog-05-shadow-ai-unsanctioned-models",
   title="Shadow AI: Governing Unsanctioned Models in the Enterprise",
   h1="Shadow AI: Finding and Governing Unsanctioned Models in Your Enterprise",
   desc="Employees adopted AI tools faster than security teams could approve them. How to discover shadow AI, assess the real data exposure, and build a governance path that sticks.",
   cat="Governance", mins=8, topic="shadow AI",
   kw=["shadow AI","unsanctioned AI tools","enterprise AI governance","AI data leakage"],
   img="https://images.unsplash.com/photo-1633265486064-086b219458ec?w=1200&q=80&fit=crop"),
]

ALL = ARTICLES + AISEC_ARTICLES
