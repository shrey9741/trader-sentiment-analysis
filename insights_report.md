# Trader Behavior Insights Report
## Bitcoin Market Sentiment × Hyperliquid Trading Performance
**Dataset:** 211,224 trades | May 2023 – May 2025  
**Analyst:** Junior Data Scientist Assignment — PrimeTrade.ai

---

## Executive Summary

Analysis of 211,224 Hyperliquid trades merged with the Bitcoin Fear & Greed Index reveals a **strong, counterintuitive pattern**: traders perform *best* during periods of Extreme Greed and *surprisingly well* during Extreme Fear — while the middle-ground sentiment (Neutral) delivers the weakest results. Win rates exceed 75% across all sentiment categories, and total cumulative PnL trends upward — pointing to a skilled trader cohort with clear sentiment-driven behavioral patterns.

---

## Dataset Overview

| Metric | Value |
|---|---|
| Total trades | 211,224 |
| Date range | May 2023 – May 2025 |
| Unique accounts | Multiple |
| Closed trades (PnL ≠ 0) | ~104,000+ |
| Fear/Greed index coverage | 2018–2025 (2,644 days) |
| Overlap period | May 2023 – May 2025 |

---

## Key Findings

### 1. Extreme Greed = Best Trading Conditions

| Sentiment | Avg PnL (USD) | Win Rate | Trades |
|---|---|---|---|
| Extreme Fear | $71.03 | 76.2% | 10,406 |
| Fear | $112.63 | 87.0% | 29,808 |
| Neutral | $71.20 | 82.0% | 18,159 |
| Greed | $85.40 | 77.0% | 25,176 |
| **Extreme Greed** | **$130.21** | **89.2%** | **20,853** |

**Insight:** Extreme Greed produced the highest average PnL ($130.21) AND the highest win rate (89.2%). This suggests traders on Hyperliquid are trend-followers who ride momentum effectively during bull sentiment.

---

### 2. Fear Periods Are Surprisingly Profitable

Fear sentiment (not Extreme Fear) delivered the **second-best average PnL ($112.63)** and an **87% win rate** — higher than both Neutral and Greed periods. This suggests:

- Skilled traders actively exploit fear-driven capitulation by taking the other side
- Dip-buying during Fear periods is a viable and profitable strategy
- The Hyperliquid user base skews toward experienced traders who use volatility advantageously

---

### 3. Neutral Sentiment = Weakest Performance

Despite feeling "safe," Neutral periods produced the **lowest average PnL ($71.20)** and a middling win rate of 82%. This is likely because:

- Low volatility = smaller price moves = smaller profits per trade
- Directional conviction is low, leading to hesitant position sizing
- The market offers fewer clear entry/exit opportunities

**Strategy implication:** Reduce position frequency or size during Neutral periods.

---

### 4. Traders Go More Long During Greed (Expected)

Long bias shifts predictably with sentiment:
- Traders are **more long-biased** during Greed/Extreme Greed periods
- They reduce long exposure during Fear — suggesting some degree of sentiment-awareness
- However, no sentiment period shows a **short majority** — Hyperliquid traders are structurally bullish

---

### 5. Top 5 Coins by Total PnL

| Coin | Total PnL |
|---|---|
| @107 | $2,783,912 |
| HYPE | $1,948,484 |
| SOL | $1,639,555 |
| ETH | $1,319,978 |
| BTC | $868,044 |

**Insight:** The top-performing coin (@107) is an altcoin/perp unique to Hyperliquid, suggesting platform-native assets offer the best alpha. HYPE (Hyperliquid's own token) is second — confirming platform insiders trade it profitably.

---

### 6. Maximum Drawdown

- **Max drawdown:** -$419,020 (aggregate across all traders)
- **Occurred:** April 23, 2025
- This coincides with a period of market stress, highlighting concentration risk when many traders hold correlated positions

---

## Hidden Patterns

### Pattern A: The "Greed Momentum" Effect
Traders perform best when everyone is greedy — not because they are reckless, but because momentum strategies thrive in high-confidence markets. The Hyperliquid cohort appears to systematically **ride the trend** during Extreme Greed rather than fade it.

### Pattern B: Fear as Opportunity
The Fear bucket (76.2%–87% win rates, above-average PnL) reveals a subset of traders who treat Fear as a buying signal. This contrarian behavior during Fear (not Extreme Fear) is a **profitable edge** — worth building a dedicated strategy around.

### Pattern C: Trade Frequency Peaks During Fear
29,808 closed trades occurred during Fear periods — the highest of any sentiment bucket. This suggests traders *increase activity* when others are scared, possibly executing mean-reversion and accumulation strategies.

### Pattern D: Extreme Fear = Lower Activity but Positive PnL
Only 10,406 trades during Extreme Fear — the fewest of all buckets — yet average PnL is positive ($71). Traders who *do* trade in Extreme Fear conditions are likely highly selective, which explains the decent win rate despite choppy conditions.

---

## Strategy Recommendations

### Recommendation 1: Lean Into Greed Momentum
- **Signal:** When Fear & Greed Index > 75 (Extreme Greed), increase long position sizing by 20–30%
- **Rationale:** 89.2% win rate and $130 avg PnL at this level — the data strongly supports momentum continuation
- **Risk control:** Use trailing stops; Extreme Greed can flip fast

### Recommendation 2: Deploy Contrarian Capital During Fear
- **Signal:** When index reads 25–45 (Fear), selectively buy dips on top-performing coins (SOL, ETH, HYPE)
- **Rationale:** 87% win rate and $112 avg PnL during Fear — second-best performance period
- **Sizing:** Medium — not max, as volatility is high

### Recommendation 3: Reduce Sizing During Neutral
- **Signal:** When index reads 45–55 (Neutral), reduce trade frequency by ~30%
- **Rationale:** Weakest avg PnL ($71) and no clear directional edge
- **Alternative:** Focus on range-bound strategies or smaller scalp targets

### Recommendation 4: Prioritize Platform-Native Assets
- **Signal:** Allocate meaningful capital to @107 and HYPE perpetuals
- **Rationale:** Top 2 performers by total PnL — informational edge exists for those trading Hyperliquid-native tokens

### Recommendation 5: Monitor Aggregate Drawdown as a Risk Signal
- The $419K max drawdown occurred in April 2025 — track when aggregate PnL begins to diverge from its rolling max
- Use this as a portfolio-level stop signal for reducing exposure across the book

---

## Conclusion

Hyperliquid traders in this dataset are skilled, with win rates consistently above 75% across all sentiment regimes. The data challenges the assumption that trading during Fear is dangerous — in fact, Fear periods show some of the best risk-adjusted outcomes. The clearest edge lies in **momentum trading during Extreme Greed** and **selective dip-buying during Fear**, while Neutral periods should be traded conservatively.

These insights can be operationalized into a simple **sentiment-gated position sizing model** — a straightforward but data-backed enhancement to any systematic trading strategy.

---

*Analysis conducted using Python (pandas, matplotlib, seaborn). Full code available in `trader_sentiment_analysis.py`.*
