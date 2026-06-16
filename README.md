# How a Country Broke Itself — and What It's Doing to Recover

### Sri Lanka's Economic Crisis: Data \& Visualisations



> \*Sri Lanka's 2022 collapse wasn't a natural disaster. It was a slow-motion political-economy failure in which institutional decay systematically silenced every feedback loop that should have corrected bad policy before it hit the cliff edge.\*

\---

## Overview

This repository contains the data and Python visualisation code for my Substack article on Sri Lanka's 2022 economic crisis and IMF-backed recovery. The article examines the structural causes of the collapse — fiscal missteps, governance failure, and debt composition — and situates Sri Lanka's experience within a broader emerging economy risk framework.

**Read the full article →** [vatsaladagar.substack.com](https://vatsaladagar.substack.com)

\---

## Charts

### 1\. Real GDP Growth Rate (2010–2024)

Bar chart showing Sri Lanka's post-civil war growth, the steady slowdown after 2012, the COVID-19 collapse in 2020, and the IMF-supported recovery through 2024.

!\[GDP Growth](chart1_gdp_growth.png)

**Source:** World Bank World Development Indicators; IMF World Economic Outlook (April 2026)

\---

### 2\. Gross Foreign Exchange Reserves (2020–2026)

Line chart tracing the depletion of reserves from $7.6bn (January 2020) to near zero at the crisis trough, and the subsequent rebuild to $7bn (March 2026) under the IMF Extended Fund Facility.

!\[FX Reserves](chart2_fx_reserves.png)

**Source:** Central Bank of Sri Lanka Monthly Bulletins; IMF EFF Programme Reviews (2023–2026)

\---

### 3\. Tax Revenue \& Public Debt as % of GDP (2015–2024)

Dual-axis chart showing how the 2019 tax cuts collapsed the tax-to-GDP ratio from 12% to 7.7% while public debt simultaneously rose above 100% of GDP — the fiscal double-bind at the heart of the crisis.

!\[Tax and Debt](chart3_tax_debt.png)

**Source:** IMF Article IV Consultations; World Bank Fiscal Monitor; Central Bank of Sri Lanka Annual Reports

\---

## Data Sources

|Chart|Dataset|Source|URL|
|-|-|-|-|
|GDP Growth|World Development Indicators|World Bank|[link](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=LK)|
|GDP Growth (2022–24)|World Economic Outlook|IMF|[link](https://www.imf.org/en/countries/LKA)|
|FX Reserves|Monthly Statistical Bulletins|Central Bank of Sri Lanka|[link](https://www.cbsl.gov.lk/en/statistics/statistical-tables/external-sector)|
|FX Reserves (2023–26)|EFF Programme Reviews|IMF|[link](https://www.imf.org/en/countries/LKA)|
|Tax Revenue \& Debt|Article IV / EFF Reviews|IMF|[link](https://www.imf.org/en/countries/LKA)|
|Tax Revenue \& Debt|Fiscal Monitor|World Bank|[link](https://www.worldbank.org/en/country/srilanka)|

\---

## Repository Structure

```
├── sri_lanka_charts.py       # All chart generation code
├── chart1_gdp_growth.png     # Output: GDP growth bar chart
├── chart2_fx_reserves.png    # Output: Foreign reserves line chart
├── chart3_tax_debt.png       # Output: Tax revenue \& debt dual-axis chart
└── README_sri_lanka.md       # This file
```

\---

## Requirements

```bash
pip install matplotlib numpy
```

## Usage

```bash
python sri\_lanka\_charts.py
```

Charts are saved as `.png` files at 180 dpi, suitable for Substack embedding.

\---

## Key Findings

* Sri Lanka's tax-to-GDP ratio fell to **7.7% in 2021** following the 2019 cuts — one of the lowest in Asia and a structural inability to absorb external shocks
* Foreign reserves fell from **$4.06bn (June 2021) to $1.92bn (April 2022)**, triggering the default on $51bn of external debt
* Under the IMF's $3bn Extended Fund Facility (March 2023), reserves recovered to **$7bn by March 2026** and GDP growth returned to **4.5% in 2024**
* The Hambantota Port "debt trap" narrative is contested: Chatham House and Johns Hopkins research found Chinese loans constituted just **9% of Sri Lankan government debt** by 2016; the port was a Sri Lankan initiative, not a Chinese one

\---

*Author: Vatsala Dagar |* [*Substack*](https://vatsaladagar.substack.com) *|* [*GitHub*](https://github.com/vatsaladagar)

