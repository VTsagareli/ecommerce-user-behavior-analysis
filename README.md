# 📦 Ecommerce User Behavior Analysis – October 2019

**An end-to-end data analytics project exploring user behavior in an e-commerce setting to uncover key trends, performance insights, and conversion metrics. Built using SQL, Python, and Tableau.**

[🔗 View Interactive Dashboard](https://public.tableau.com/views/EcommerceUserBehaviorOctober2019AnalysisDashboard/EcommerceUserBehaviorOctober2019Analysis)

[📁 View This Repository on GitHub](https://github.com/VTsagareli/ecommerce-user-behavior-analysis)

[Data source: Oct 2019 eCommerce Behavior Dataset](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

---

## 🧠 Project Background

This project simulates a real-world business scenario where an e-commerce company wants to better understand how users interact with their platform — from viewing products, adding items to cart, and completing purchases.

The goal was to build a **clean, insightful dashboard** that enables business stakeholders to answer:

- Where and when are users most active?
- What portion of sessions result in purchases?
- Which brands are generating the most revenue?
- When are users most likely to engage in high-intent actions (carting or purchasing)?

All of this was done by taking a **raw 42M+ row dataset**, processing and analyzing it using SQL and Python, and designing an interactive dashboard using **Tableau Public**.

---

## 🧱 Data Structure Overview

| Column            | Description                                     |
|-------------------|-------------------------------------------------|
| `event_time`      | Timestamp of the user event                     |
| `event_type`      | One of: `view`, `cart`, `purchase`              |
| `product_id`      | Unique product identifier                       |
| `category_id`     | Numeric category ID                             |
| `category_code`   | Categorical label for the product category      |
| `brand`           | Product brand                                   |
| `price`           | Price of the product at time of event           |
| `user_id`         | Anonymized user ID                              |
| `user_session`    | Session ID for grouping actions                 |
| `main_category`   | General category of the product                 |
| `event_date`      | Parsed calendar date                            |
| `event_hour`      | Extracted hour from `event_time` (0–23)         |
| `day_of_week`     | Day of week (`Monday`, etc.)                    |
| `event_dayofweek` | Numerical day of week                           |
| `event_month`     | Month of event                                  |
| `event_day`       | Day of month                                    |

---

## 🚀 Executive Summary

Using SQL and Tableau, this project delivers:

- **Business-ready KPIs** — Conversion rate, total revenue, average spend per purchase, total purchases, and peak engagement time.
- **User journey insights** — How users transition through the funnel (view → cart → purchase).
- **Behavioral trends** — When users are most active and most likely to purchase.
- **Brand revenue analysis** — Highlighting which brands contribute most to revenue.

> The dashboard is fully interactive, filterable by event type, and designed to enable real-world decision-making.

---

## 🔍 Key Insights

| Insight | Description |
|--------|-------------|
| 🔄 **Conversion Rate** | Only **1.82%** of views lead to purchases — a potential point of optimization. |
| ⏰ **Peak Activity Hour** | Most user actions occur at **16:00**, primarily views. *(Filter out views to analyze purchase intent.)* |
| 💰 **Top Brands** | The top brand generated over **$1.15M** in revenue during October. |
| 📈 **Daily Purchase Trend** | Mid-month (Oct 15–17) showed the highest purchasing activity. |
| 🕑 **Hourly Activity Pattern** | Usage builds throughout the day and peaks in the late afternoon. *(Filtering view reveals different peak patterns.)* |

---

## 🛠️ Tech Stack

| Tool       | Why It Was Used | What It Was Used For |
|------------|------------------|-----------------------|
| **PostgreSQL** | Scalable relational database to handle 42M+ rows efficiently | Loaded data, wrote analytical queries, calculated KPIs |
| **pgAdmin 4**  | GUI for managing PostgreSQL | Created tables, verified data, and tested queries |
| **Python**     | Automated data handling and script execution | Scripted data chunking and export of query results to CSV using `psycopg2` and `pandas` |
| **Tableau Public** | Leading tool for business dashboards | Created a clean, filterable, professional dashboard |
| **VSCode**     | Code editor with Git integration | SQL and Python development, project management |
| **Git + GitHub** | Version control and portfolio visibility | Tracked code and published project for employers/stakeholders |

---

## 🗂️ Project Structure

ecommerce-user-behavior-project/
├── data/                   # Raw, cleaned, and chunked datasets
├── docs/                  # ERDs, documentation, visuals (optional)
├── exports/
│   └── tableau/
│       ├── analysis/      # CSVs for analysis charts
│       └── kpis/          # CSVs for KPI visualizations
├── python/
│   ├── cleaning-and-eda/
│   └── scripts/           # Data chunking + export to CSV
├── sql/
│   ├── analysis/          # SQL queries for each analysis
│   └── kpis/              # SQL for calculated KPIs
├── tableau/
│   └── dashboards/        # .twb/.twbx files (excluded from GitHub)
└── README.md

---

## 📈 Dashboard Preview

📊 [Live Dashboard on Tableau Public](https://public.tableau.com/views/EcommerceUserBehaviorOctober2019AnalysisDashboard/EcommerceUserBehaviorOctober2019Analysis)

**Features:**
- 🎯 Five dynamic KPIs
- 📅 Daily purchase trend
- 🕒 Hourly activity distribution
- 💸 Top 10 revenue-generating brands
- 📊 Event type funnel (view → cart → purchase)
- 🔎 Interactive filtering and hover tooltips

---

## 📝 Recommendations

1. **Reduce Drop-Off** — With a low conversion rate, optimize the path from view → cart → purchase.
2. **Capitalize on Peak Times** — Engage users during 16:00–18:00 with targeted offers.
3. **Reassess Low Revenue Brands** — Consider bundling or retargeting strategies.
4. **Segment by Behavior** — Introduce user-level cohorting in future analysis.
5. **Add Multimonth Trends** — To uncover seasonality or campaign effectiveness.

---

## ⚠️ Caveats & Assumptions

- **One-month snapshot** — Analysis limited to October 2019 only.
- **Anonymized user data** — No demographics or repeat behavior tracking.
- **No campaign data** — Could not correlate purchases with marketing.
- **Assumes complete event capture** — Data completeness not guaranteed.

---

## ✅ Next Steps

- Extend the project to include **Nov–Dec** data for holiday trends.
- Implement **session-level analysis** to detect funnel drop-offs.
- Apply **RFM segmentation** or **LTV modeling** to understand customer value.
- Join with **product metadata** for deeper category or price band insights.

---

## 🤝 Contact

Created by [@VTsagareli](https://github.com/VTsagareli)  
Feel free to connect or reach out with questions, suggestions, or collaboration ideas.
