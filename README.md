📊 Trader Behavior Insights — Bitcoin Sentiment × Hyperliquid

    Assignment Submission — Junior Data Scientist | PrimeTrade.ai
    Analyzing the relationship between Bitcoin market sentiment and trader performance on Hyperliquid.

🗂️ Repository Structure

├── trader_sentiment_analysis.py   # Full analysis script (data cleaning, merging, charts)
├── sentiment_analysis.png         # 7-panel visualization dashboard
├── insights_report.md             # Written insights & strategy recommendations
└── README.md                      # This file

📁 Datasets Used
Dataset 	Source 	Rows
Hyperliquid Historical Trades 	Provided by PrimeTrade.ai 	211,224
Bitcoin Fear & Greed Index 	Provided by PrimeTrade.ai 	2,644 days

Date range covered: May 2023 – May 2025
🔍 Objective

Explore the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance on Hyperliquid — uncovering hidden behavioral patterns and delivering actionable trading strategy recommendations.
📈 Key Findings
Sentiment vs. Performance Summary
Sentiment 	Avg PnL (USD) 	Win Rate 	Trades
Extreme Fear 	$71.03 	76.2% 	10,406
Fear 	$112.63 	87.0% 	29,808
Neutral 	$71.20 	82.0% 	18,159
Greed 	$85.40 	77.0% 	25,176
Extreme Greed 	$130.21 	89.2% 	20,853
🏆 Top 3 Insights

    Extreme Greed = Best Performance — Highest avg PnL ($130) and win rate (89.2%). Momentum strategies dominate in bull sentiment.
    Fear is an Opportunity — 87% win rate during Fear periods, second-highest avg PnL ($112). Skilled traders exploit capitulation.
    Neutral = Weakest Conditions — Lowest avg PnL ($71). Low volatility reduces edge; reduce position sizing here.

📊 Visualization Dashboard

Sentiment Analysis Dashboard

7 charts covering:

    Average PnL by sentiment
    Win rate by sentiment
    Trade volume per sentiment regime
    Long/Short bias across sentiments
    Cumulative PnL timeline (colored by sentiment)
    Top 10 traders by total PnL
    PnL distribution boxplot per sentiment

💡 Strategy Recommendations
Signal 	Sentiment 	Action
Index > 75 (Extreme Greed) 	Bullish momentum 	Increase long sizing +20–30%
Index 25–45 (Fear) 	Dip opportunity 	Selective buys on SOL, ETH, HYPE
Index 45–55 (Neutral) 	Low edge 	Reduce trade frequency ~30%
Extreme Fear 	Cautious 	Trade selectively, smaller size
🛠️ Tech Stack

    Python 3 — pandas, numpy, matplotlib, seaborn
    Data: CSV files (211K+ rows)
    Visualization: Custom dark-theme 7-panel dashboard

▶️ How to Run

# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/trader-sentiment-analysis.git
cd trader-sentiment-analysis

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn

# 3. Add datasets to the same folder
#    - historical_data.csv
#    - fear_greed_index.csv

# 4. Run the analysis
python trader_sentiment_analysis.py

📬 Submission

Submitted for: Junior Data Scientist – Trader Behavior Insights
Company: PrimeTrade.ai
Contact: saami@primetrade.ai | nagasai@primetrade.ai | chetan@primetrade.ai
CC: sonika@primetrade.ai
