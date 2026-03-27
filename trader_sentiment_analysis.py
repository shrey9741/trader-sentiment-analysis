"""
=============================================================================
  Bitcoin Market Sentiment vs. Trader Performance Analysis
  Dataset: Hyperliquid Historical Trades + Fear & Greed Index
  Author: Junior Data Scientist Assignment
=============================================================================
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 1. LOAD & CLEAN DATA
# =============================================================================

trades = pd.read_csv('historical_data.csv')
fg     = pd.read_csv('fear_greed_index.csv')

# Parse dates
trades['date'] = pd.to_datetime(trades['Timestamp IST'], dayfirst=True).dt.date
fg['date']     = pd.to_datetime(fg['date']).dt.date

print(f"Trades loaded  : {trades.shape[0]:,} rows | {trades.shape[1]} columns")
print(f"Fear/Greed rows: {fg.shape[0]:,} rows")
print(f"Trade date range: {trades['date'].min()} → {trades['date'].max()}")

# =============================================================================
# 2. MERGE DATASETS ON DATE
# =============================================================================

merged = trades.merge(fg[['date', 'value', 'classification']], on='date', how='inner')
print(f"\nMerged dataset : {merged.shape[0]:,} rows")

# Keep only closed trades (PnL != 0)
closed = merged[merged['Closed PnL'] != 0].copy()
closed['is_profitable'] = closed['Closed PnL'] > 0
print(f"Closed trades  : {closed.shape[0]:,} rows")

# =============================================================================
# 3. SENTIMENT ORDER & PALETTE
# =============================================================================

ORDER = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
PALETTE = {
    'Extreme Fear' : '#d32f2f',
    'Fear'         : '#f57c00',
    'Neutral'      : '#fbc02d',
    'Greed'        : '#388e3c',
    'Extreme Greed': '#1b5e20',
}

# =============================================================================
# 4. SENTIMENT-WISE PERFORMANCE AGGREGATION
# =============================================================================

sent_stats = (
    closed.groupby('classification')
    .agg(
        avg_pnl     = ('Closed PnL', 'mean'),
        median_pnl  = ('Closed PnL', 'median'),
        total_pnl   = ('Closed PnL', 'sum'),
        win_rate    = ('is_profitable', 'mean'),
        trade_count = ('Closed PnL', 'count'),
    )
    .reindex(ORDER)
)

print("\n=== Sentiment Performance Summary ===")
print(sent_stats.round(2).to_string())

# =============================================================================
# 5. LONG / SHORT BIAS PER SENTIMENT
# =============================================================================

side_ratio = (
    closed.groupby(['classification', 'Side'])
    .size().unstack(fill_value=0)
    .reindex(ORDER)
)
side_ratio['long_pct'] = (
    side_ratio['BUY'] / (side_ratio['BUY'] + side_ratio['SELL']) * 100
)

print("\n=== Long Bias (%) per Sentiment ===")
print(side_ratio[['BUY', 'SELL', 'long_pct']].round(1).to_string())

# =============================================================================
# 6. DAILY AGGREGATION FOR TIME-SERIES
# =============================================================================

daily = (
    closed.groupby('date')
    .agg(daily_pnl=('Closed PnL', 'sum'), trade_count=('Closed PnL', 'count'))
    .reset_index()
)
daily['date'] = pd.to_datetime(daily['date'])
daily = daily.merge(
    fg[['date', 'value', 'classification']].assign(
        date=lambda d: pd.to_datetime(d['date'])
    ),
    on='date', how='left'
)
daily['cum_pnl'] = daily['daily_pnl'].cumsum()

# Max drawdown
daily = daily.sort_values('date').reset_index(drop=True)
daily['roll_max'] = daily['cum_pnl'].cummax()
daily['drawdown'] = daily['cum_pnl'] - daily['roll_max']
max_dd_date = daily.loc[daily['drawdown'].idxmin(), 'date'].date()
max_dd_val  = daily['drawdown'].min()
print(f"\nMax Drawdown: ${max_dd_val:,.2f} on {max_dd_date}")

# =============================================================================
# 7. TOP TRADERS
# =============================================================================

top_traders = (
    closed.groupby('Account')
    .agg(
        total_pnl = ('Closed PnL', 'sum'),
        win_rate  = ('is_profitable', 'mean'),
        trades    = ('Closed PnL', 'count'),
    )
    .query('trades >= 20')
    .nlargest(10, 'total_pnl')
    .reset_index()
)
top_traders['short_acct'] = top_traders['Account'].str[:6] + '...'

print("\n=== Top 10 Traders by Total PnL ===")
print(top_traders[['short_acct', 'total_pnl', 'win_rate', 'trades']].round(2).to_string())

# =============================================================================
# 8. TOP COINS BY PNL
# =============================================================================

top_coins = closed.groupby('Coin')['Closed PnL'].sum().nlargest(10).round(2)
print("\n=== Top 10 Coins by Total PnL ===")
print(top_coins.to_string())

# =============================================================================
# 9. CONTRARIAN SIGNAL ANALYSIS
# =============================================================================

print("\n=== Contrarian Signal Check ===")
for s in ORDER:
    sub = closed[closed['classification'] == s]['Closed PnL']
    print(f"{s:15s} | Avg PnL: ${sub.mean():8.2f} | Win Rate: {(sub>0).mean()*100:.1f}% | n={len(sub):,}")

# =============================================================================
# 10. VISUALISATIONS  (saved to PNG)
# =============================================================================

fig = plt.figure(figsize=(22, 28), facecolor='#0d1117')
gs  = gridspec.GridSpec(4, 2, figure=fig, hspace=0.52, wspace=0.35,
                        left=0.07, right=0.96, top=0.93, bottom=0.05)

def ax_style(ax, title):
    ax.set_facecolor('#161b22')
    for sp in ax.spines.values(): sp.set_color('#30363d')
    ax.tick_params(colors='#8b949e', labelsize=10)
    ax.xaxis.label.set_color('#8b949e')
    ax.yaxis.label.set_color('#8b949e')
    ax.set_title(title, color='#e6edf3', fontsize=13, fontweight='bold', pad=10)
    ax.grid(axis='y', color='#21262d', linewidth=0.7, linestyle='--')

colors_list = [PALETTE[o] for o in ORDER]

# Chart 1 – Avg PnL
ax1 = fig.add_subplot(gs[0, 0])
ax_style(ax1, '① Avg Closed PnL by Market Sentiment')
bars = ax1.bar(ORDER, sent_stats['avg_pnl'], color=colors_list, edgecolor='#0d1117', zorder=3)
for b, v in zip(bars, sent_stats['avg_pnl']):
    ax1.text(b.get_x()+b.get_width()/2, b.get_height()+0.5,
             f'${v:.1f}', ha='center', va='bottom', color='#e6edf3', fontsize=9, fontweight='bold')
ax1.axhline(0, color='#58a6ff', linewidth=1, linestyle='--')
ax1.set_ylabel('Avg PnL (USD)')
ax1.set_xticklabels(ORDER, rotation=15, ha='right')

# Chart 2 – Win Rate
ax2 = fig.add_subplot(gs[0, 1])
ax_style(ax2, '② Win Rate (%) by Market Sentiment')
wr_vals = sent_stats['win_rate'] * 100
bars2   = ax2.bar(ORDER, wr_vals, color=colors_list, edgecolor='#0d1117', zorder=3)
ax2.axhline(50, color='#58a6ff', linewidth=1.2, linestyle='--', label='50% baseline')
for b, v in zip(bars2, wr_vals):
    ax2.text(b.get_x()+b.get_width()/2, v+0.3, f'{v:.1f}%',
             ha='center', va='bottom', color='#e6edf3', fontsize=9, fontweight='bold')
ax2.set_ylabel('Win Rate (%)')
ax2.set_ylim(0, 80)
ax2.set_xticklabels(ORDER, rotation=15, ha='right')
ax2.legend(fontsize=9, facecolor='#161b22', labelcolor='#8b949e', edgecolor='#30363d')

# Chart 3 – Trade Count
ax3 = fig.add_subplot(gs[1, 0])
ax_style(ax3, '③ Number of Trades by Sentiment')
bars3 = ax3.bar(ORDER, sent_stats['trade_count'], color=colors_list, edgecolor='#0d1117', zorder=3)
for b, v in zip(bars3, sent_stats['trade_count']):
    ax3.text(b.get_x()+b.get_width()/2, v+50, f'{int(v):,}',
             ha='center', va='bottom', color='#e6edf3', fontsize=9, fontweight='bold')
ax3.set_ylabel('Trade Count')
ax3.set_xticklabels(ORDER, rotation=15, ha='right')

# Chart 4 – Long Bias
ax4 = fig.add_subplot(gs[1, 1])
ax_style(ax4, '④ Long Bias (%) by Sentiment')
lp         = side_ratio['long_pct']
bar_colors = ['#d32f2f' if v < 50 else '#388e3c' for v in lp]
bars4      = ax4.bar(ORDER, lp, color=bar_colors, edgecolor='#0d1117', zorder=3)
ax4.axhline(50, color='#58a6ff', linewidth=1.2, linestyle='--', label='50% neutral')
for b, v in zip(bars4, lp):
    ax4.text(b.get_x()+b.get_width()/2, v+0.5, f'{v:.1f}%',
             ha='center', va='bottom', color='#e6edf3', fontsize=9, fontweight='bold')
ax4.set_ylabel('% Long Trades')
ax4.set_ylim(0, 80)
ax4.set_xticklabels(ORDER, rotation=15, ha='right')
ax4.legend(fontsize=9, facecolor='#161b22', labelcolor='#8b949e', edgecolor='#30363d')

# Chart 5 – Cumulative PnL
ax5 = fig.add_subplot(gs[2, :])
ax_style(ax5, '⑤ Cumulative PnL Over Time — Colored by Market Sentiment')
seg_colors = PALETTE.copy()
for i in range(len(daily) - 1):
    c = seg_colors.get(daily['classification'].iloc[i], '#8b949e')
    ax5.fill_between([daily['date'].iloc[i], daily['date'].iloc[i+1]],
                     [daily['cum_pnl'].iloc[i], daily['cum_pnl'].iloc[i+1]],
                     alpha=0.15, color=c)
    ax5.plot([daily['date'].iloc[i], daily['date'].iloc[i+1]],
             [daily['cum_pnl'].iloc[i], daily['cum_pnl'].iloc[i+1]], color=c, linewidth=1.5)
legend_patches = [mpatches.Patch(color=v, label=k) for k, v in seg_colors.items()]
ax5.legend(handles=legend_patches, loc='upper left', fontsize=9,
           facecolor='#161b22', labelcolor='#e6edf3', edgecolor='#30363d', ncol=5)
ax5.set_ylabel('Cumulative PnL (USD)')
ax5.set_xlabel('Date')
ax5.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))

# Chart 6 – Top 10 Traders
ax6 = fig.add_subplot(gs[3, 0])
ax_style(ax6, '⑥ Top 10 Traders by Total PnL')
bh = ax6.barh(top_traders['short_acct'][::-1], top_traders['total_pnl'][::-1],
              color='#58a6ff', edgecolor='#0d1117', zorder=3)
for b, v in zip(bh, top_traders['total_pnl'][::-1]):
    ax6.text(v + 200, b.get_y()+b.get_height()/2, f'${v:,.0f}',
             va='center', color='#e6edf3', fontsize=8)
ax6.set_xlabel('Total PnL (USD)')

# Chart 7 – PnL Distribution Boxplot
ax7 = fig.add_subplot(gs[3, 1])
ax_style(ax7, '⑦ PnL Distribution by Sentiment')
plot_data = [closed[closed['classification'] == s]['Closed PnL'].clip(-500, 2000) for s in ORDER]
bp = ax7.boxplot(plot_data, patch_artist=True, notch=False,
                 medianprops=dict(color='white', linewidth=2),
                 whiskerprops=dict(color='#8b949e'),
                 capprops=dict(color='#8b949e'),
                 flierprops=dict(marker='.', color='#8b949e', markersize=2, alpha=0.3))
for patch, color in zip(bp['boxes'], colors_list):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)
ax7.set_xticklabels(ORDER, rotation=15, ha='right', fontsize=9)
ax7.set_ylabel('Closed PnL (USD, clipped ±500–2000)')
ax7.axhline(0, color='#58a6ff', linewidth=1, linestyle='--')

fig.suptitle(
    'Bitcoin Market Sentiment vs. Trader Performance Analysis\n'
    'Hyperliquid Historical Data  |  Fear & Greed Index',
    color='#e6edf3', fontsize=17, fontweight='bold', y=0.97
)

plt.savefig('sentiment_analysis.png', dpi=150, bbox_inches='tight', facecolor='#0d1117')
print("\nChart saved → sentiment_analysis.png")
print("\nAnalysis complete.")
