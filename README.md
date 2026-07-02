# BridgeAIPH MSME Social Media Planner

Website implementation of the BridgeAIPH Social Media Concierge Agent for Philippine local Micro, Small and Medium Enterprises (outputs in Taglish) An automated AI-powered social media assistant designed explicitly for Micro, Small, and Medium Enterprises (MSMEs) in the Philippines. This agent functions as an on-demand, zero-cost digital marketing concierge that translates basic business descriptions into structured, culturally resonant weekly social media plans.

---

## 1. The Problem
Micro, Small, and Medium Enterprises (MSMEs) form the backbone of the Philippine economy, yet they face severe barriers to digital transformation. Local businesses—such as neighborhood *bakery* shops in Marikina, *sari-sari* stores, homegrown *carinderias*, or independent online clothing boutiques—frequently struggle with the overhead costs of traditional digital marketing.

Key bottlenecks include:
* **Resource Constraints:** Small business owners wear multiple hats (production, operations, finance) and lack the dedicated time required to manage consistent social media platforms.
* **Financial Barriers:** High agency fees or specialized copywriting software subscriptions are cost-prohibitive for micro-scale operational budgets.
* **Content Fatigue:** Consistently maintaining high engagement levels, coming up with interactive hooks, and keeping track of dynamic local holiday marketing opportunities requires continuous creative energy that owners cannot spare.

---

## 2. The Solution
The **BridgeAIPH Social Media Concierge** completely removes these friction points by serving as an automated, localized digital marketing assistant. Built on top of the `google.adk` framework and powered by `gemini-2.5-flash`, the agent converts simple business details into a full weekly strategic layout within seconds.

### Key Capabilities:
* **Dynamic Information Gathering:** The agent systematically prompts the business owner for their business name, precise Philippine location, and target promotional items to guarantee output relevance.
* **Localized Context Engineering:** Leverages native cultural awareness, tracking dynamic Filipino markers such as seasonal elements (*tag-ulan* vs. *tag-init*), corporate milestones (payday periods on the 15th/30th), regional town fiestas, and early *Ber-months* Christmas preparations.
* **Dual-Language Fluency:** Generates copy utilizing professional but highly approachable English mixed with conversational, natural **Taglish** formatting—matching the authentic communication style of modern Filipino consumers.
* **Structured Deliverables:** Outputs a rigid, comprehensive 3-post weekly template featuring a value-driven **Educational** piece, an interactive **Engaging Hook**, and a conversion-focused **Promotional** call-to-action complete with visual content ideas.

---

## 3. Technical Project Architecture
The architecture is designed to map directly to the standardized evaluation requirements of the Capstone project:

```
msme_planner/
├── google/
│   └── adk/                      # Localized core Agent Development Kit (omitted from repo / local runtime only)
├── skills/
│   └── context.md                # System instructions, personas, and guardrails
├── agent.py                      # Main Python initialization and execution loop
├── agents-cli-manifest.yaml      # Environment declarations and configuration map
└── README.md                     # Project overview and grading rubric documentation
```

---

## 4. The Trace Video Link
Below is the deployment verification trace documenting successful, error-free local validation testing and interaction execution in the playground environment:

* **[Watch the 5-Minute Capstone Demonstration Video](https://youtu.be/jhtXxnFR0dg)**
