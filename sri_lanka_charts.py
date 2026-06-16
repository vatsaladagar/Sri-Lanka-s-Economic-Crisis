"""
sri_lanka_charts.py
────────────────────────────────────────────────────────────────────────────
"How a Country Broke Itself — and What It's Doing to Recover"
Published at: vatsaladagar.substack.com

Charts
──────
1. Real GDP Growth Rate (2010–2024)
   Source: World Bank World Development Indicators; IMF World Economic
   Outlook (April 2026) for 2022–2024 estimates.
   URL: https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=LK

2. Gross Foreign Exchange Reserves (2020–2026)
   Source: Central Bank of Sri Lanka (CBSL) Monthly Bulletins;
   IMF Sri Lanka EFF Programme Reviews (2023–2026).
   URL: https://www.cbsl.gov.lk/en/statistics/statistical-tables/external-sector
        https://www.imf.org/en/countries/LKA

3. Tax Revenue & Public Debt as % of GDP (2015–2024)
   Source: IMF Article IV Consultations and EFF Reviews;
   World Bank Fiscal Monitor; Central Bank of Sri Lanka Annual Reports.
   URL: https://www.imf.org/en/countries/LKA
        https://www.worldbank.org/en/country/srilanka

Author: Vatsala Dagar
GitHub: github.com/vatsaladagar
────────────────────────────────────────────────────────────────────────────
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── Shared style ────────────────────────────────────────────────────────────
NAVY   = "#1B3A6B"
TEAL   = "#1D7A6B"
AMBER  = "#C8860A"
GRAY   = "#888888"
BG     = "#FFFFFF"

plt.rcParams.update({
    "figure.facecolor":  BG,
    "axes.facecolor":    BG,
    "axes.edgecolor":    "#CCCCCC",
    "axes.linewidth":    0.8,
    "axes.grid":         True,
    "grid.color":        "#E5E5E5",
    "grid.linewidth":    0.6,
    "grid.linestyle":    "-",
    "xtick.color":       "#444444",
    "ytick.color":       "#444444",
    "xtick.labelsize":   9,
    "ytick.labelsize":   9,
    "font.family":       "DejaVu Sans",
    "legend.frameon":    False,
    "legend.fontsize":   9,
})

def style_ax(ax, title):
    ax.set_title(title, fontsize=13, fontweight="bold", color="#111111", pad=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#CCCCCC")
    ax.spines["bottom"].set_color("#CCCCCC")
    ax.tick_params(length=0)

# ── Chart 1: GDP Growth Rate 2010–2024 ──────────────────────────────────────
years_gdp = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]
gdp       = [8.01, 8.4, 9.14, 3.39, 4.96, 5.0, 4.48, 3.57, 3.27, 2.25,-3.56, 3.4,-2.3, 3.0, 4.5]

fig, ax = plt.subplots(figsize=(8, 4.5))
style_ax(ax, "Sri Lanka: Real GDP Growth Rate (2010–2024)")

colors_bar = [NAVY if v >= 0 else "#C0392B" for v in gdp]
bars = ax.bar(years_gdp, gdp, color=colors_bar, width=0.6, zorder=3)

ax.axhline(0, color="#AAAAAA", linewidth=0.8)
ax.set_xticks(years_gdp)
ax.set_xticklabels([str(y) for y in years_gdp], rotation=45, ha="right")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f%%"))
ax.set_ylabel("GDP Growth (%)", fontsize=9, color="#444444")

# Annotate the crisis trough and 2024 recovery
ax.annotate("COVID\ncollapse", xy=(2020, -3.56), xytext=(2017.5, -4.8),
            fontsize=8, color="#C0392B",
            arrowprops=dict(arrowstyle="->", color="#C0392B", lw=0.8))
ax.annotate("Recovery\n+4.5%", xy=(2024, 4.5), xytext=(2022.2, 6.5),
            fontsize=8, color=TEAL,
            arrowprops=dict(arrowstyle="->", color=TEAL, lw=0.8))

ax.text(0.01, -0.18, "Source: World Bank, IMF (2024)",
        transform=ax.transAxes, fontsize=7.5, color=GRAY)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/chart1_gdp_growth.png", dpi=180, bbox_inches="tight")
plt.close()
print("Chart 1 saved.")

# ── Chart 2: Foreign Exchange Reserves ──────────────────────────────────────
months_fx = [
    "Jan 2020","Jun 2020","Dec 2020",
    "Jun 2021","Dec 2021",
    "Apr 2022","Jun 2022",
    "Dec 2022","Jun 2023","Dec 2023",
    "Jun 2024","Dec 2024",
    "Jun 2025","Mar 2026"
]
reserves = [7.6, 6.6, 5.7, 4.06, 3.1, 1.92, 1.7, 1.9, 3.5, 4.4, 5.5, 6.0, 6.1, 7.0]
x = np.arange(len(months_fx))

fig, ax = plt.subplots(figsize=(9, 4.5))
style_ax(ax, "Sri Lanka: Gross Foreign Exchange Reserves (USD Billion)")

ax.plot(x, reserves, color=NAVY, linewidth=2.2, marker="o",
        markersize=5, markerfacecolor=NAVY, zorder=4)
ax.fill_between(x, reserves, alpha=0.08, color=NAVY, zorder=2)

# Danger zone shading
crisis_start = months_fx.index("Jun 2021")
crisis_end   = months_fx.index("Jun 2022")
ax.axvspan(crisis_start, crisis_end, color="#C0392B", alpha=0.07, zorder=1)
ax.text((crisis_start + crisis_end)/2, 0.3, "Crisis period",
        ha="center", fontsize=8, color="#C0392B")

# IMF programme line
imf_x = months_fx.index("Jun 2023")
ax.axvline(imf_x, color=TEAL, linewidth=1.2, linestyle="--")
ax.text(imf_x + 0.15, 5.8, "IMF EFF\nbegins", fontsize=7.5, color=TEAL)

ax.set_xticks(x)
ax.set_xticklabels(months_fx, rotation=45, ha="right", fontsize=8)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("$%.1fbn"))
ax.set_ylabel("Reserves (USD Billion)", fontsize=9, color="#444444")
ax.set_ylim(0, 9)

ax.text(0.01, -0.22, "Source: Central Bank of Sri Lanka, IMF (2026)",
        transform=ax.transAxes, fontsize=7.5, color=GRAY)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/chart2_fx_reserves.png", dpi=180, bbox_inches="tight")
plt.close()
print("Chart 2 saved.")

# ── Chart 3: Tax Revenue & Debt-to-GDP ──────────────────────────────────────
years_tax  = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
tax_gdp    = [13.1, 13.4, 12.8, 12.6, 11.6,  9.2,  7.7,  8.3,  9.9, 11.2]
debt_gdp   = [77.6, 79.3, 77.0, 82.9, 86.9,100.6,105.6,128.0,115.0,105.0]

fig, ax1 = plt.subplots(figsize=(8, 4.5))
style_ax(ax1, "Sri Lanka: Tax Revenue & Public Debt as % of GDP")

x = np.arange(len(years_tax))

# Tax revenue — bars
bars = ax1.bar(x - 0.2, tax_gdp, width=0.35, color=TEAL,
               alpha=0.85, label="Tax Revenue (% GDP)", zorder=3)
ax1.set_ylabel("Tax Revenue (% of GDP)", fontsize=9, color=TEAL)
ax1.yaxis.label.set_color(TEAL)
ax1.tick_params(axis="y", colors=TEAL)
ax1.set_ylim(0, 18)

# Debt — line on secondary axis
ax2 = ax1.twinx()
ax2.plot(x + 0.15, debt_gdp, color=NAVY, linewidth=2.2,
         marker="s", markersize=5, markerfacecolor=NAVY,
         label="Public Debt (% GDP)", zorder=4)
ax2.set_ylabel("Public Debt (% of GDP)", fontsize=9, color=NAVY)
ax2.yaxis.label.set_color(NAVY)
ax2.tick_params(axis="y", colors=NAVY)
ax2.set_ylim(50, 145)
ax2.spines["right"].set_color("#CCCCCC")

# Annotate the 2019 tax cut
ax1.annotate("2019 tax cuts", xy=(4, 11.6), xytext=(2.2, 14.5),
             fontsize=8, color="#C0392B",
             arrowprops=dict(arrowstyle="->", color="#C0392B", lw=0.8))

ax1.set_xticks(x)
ax1.set_xticklabels([str(y) for y in years_tax])

# Combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2,
           loc="upper center", bbox_to_anchor=(0.5, -0.12),
           ncol=2, fontsize=9)

ax1.text(0.01, -0.26, "Source: IMF, Central Bank of Sri Lanka, World Bank",
         transform=ax1.transAxes, fontsize=7.5, color=GRAY)

plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/chart3_tax_debt.png", dpi=180, bbox_inches="tight")
plt.close()
print("Chart 3 saved.")

print("\nAll three charts saved to /mnt/user-data/outputs/")
