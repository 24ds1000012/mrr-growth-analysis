# SaaS Technology Performance Analysis — MRR Growth (2024)

**Author / Contact:** 24ds1000012@ds.study.iitm.ac.in

This pull request contains code, visualization, and a data story to brief the executive team on the company’s slowing revenue growth and the gap to the industry benchmark.

## Dataset
**Monthly Recurring Revenue (MRR) Growth — 2024 Quarterly Data**
- Q1: 4.5
- Q2: 7.46
- Q3: 7.12
- Q4: 11.61

**Average (2024): 7.67**  
**Industry Target:** 15

> Data file: [`mrr_growth_2024.csv`](mrr_growth_2024.csv)

## Key Findings
1. **Growth improved sequentially but remains below target.** Q4 rose to **11.61%**, yet the **full-year average is 7.67**, which is **7.33pp below** the **15%** benchmark.
2. **Volatility and underperformance in H1** (Q1: 4.5%) created a full-year drag. Even a strong H2 was insufficient to close the gap.
3. **Execution tailwinds exist** (operational recovery in H2), suggesting that targeted initiatives can compound into 2025.

## Business Implications
- **Budgeting & GTM focus:** With an average of **7.67%**, we are **not compounding fast enough** to hit FY25 targets without strategic changes.
- **Risk to valuation & unit economics:** Sustained underperformance vs. 15% may compress valuation multiples and force heavier CAC to defend growth.
- **Resource allocation:** Investments should prioritize **market expansion initiatives** that demonstrably lift growth in the next two quarters.

## Recommendations (to reach 15)
**Primary solution: _expand into new market segments_.** This should be the flagship initiative, supported by:
- **Segment scouting & sizing:** Identify 2–3 adjacent ICPs with high ARPU and short sales cycles (e.g., SMB prosumer, mid-market verticals).
- **Localized GTM plays:** Regional bundles, language support, and in-segment partnerships to accelerate trust and distribution.
- **Focused product-led growth (PLG):** Self-serve trials with in-product prompts tailored to each new segment’s core jobs-to-be-done.
- **Pricing & packaging tests:** Create segment-specific entry SKUs and expansion packs; run A/B tests on paywalls and upgrade prompts.
- **Marketing mix shift:** Increase partner/channel allocation; use content and field events targeted at the new segments.

### Evidence via Simple Projection
In `analysis.py`, we simulate entering **two new segments** contributing **+2.0pp** and **+2.5pp** to the next two quarters. Even with conservative base trends, the **projected growth lifts toward the 15% target**. (Illustrative only; replace with your internal pipeline and conversion models.)

## Files in this PR
- `analysis.py` — loads data, prints stats, saves `mrr_growth_vs_target.png`, and writes a simple projection `projection_2025.csv`.
- `mrr_growth_2024.csv` — quarterly data.
- `mrr_growth_vs_target.png` — chart comparing quarterly growth vs. target and annual average.
- `requirements.txt` — Python deps for quick repro.

## How to Reproduce
```bash
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python analysis.py
