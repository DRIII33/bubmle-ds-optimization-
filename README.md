# Bumble Strategic Intelligence: The Kindness Graph

## Project Overview
This portfolio project simulates the role of a **Data Scientist** (*Daniel Rodriguez III*) at **Bumble Inc.** within the Core Data Science team. The mission is to uncover the drivers of member behavior and performance across Bumble products, providing insights that directly inform product strategies and answer key business questions regarding revenue growth.

## Business Problem & Context
Bumble Inc. operates in a multi-sided marketplace where "Kind Connections" are the primary value proposition. The business faced challenges with:
1.  **Subscription Fatigue:** Identifying when and how to prompt users for premium features without degrading the user experience.
2.  **Marketplace Liquidity:** Understanding the balance of supply and demand (interactions vs. matches).
3.  **Revenue Attribution:** Determining which acquisition channels drive the highest-value members (ARPU).

## Technical Stack
-   **Python:** Synthetic data generation (NumPy/Pandas) and Machine Learning (Scikit-Learn).
-   **SQL (Google BigQuery):** Advanced data engineering, relational schema architecture, and view creation.
-   **Looker Studio:** Strategic Business Intelligence and visual storytelling.

## Methodology & Pipeline

### Phase 1: Synthetic Data Engineering
To demonstrate proficiency in handling large-scale datasets, I engineered a synthetic ecosystem of **50,000 members** and **50,000+ interactions**. This involved creating:
-   `dim_members`: Demographic and acquisition data.
-   `fact_interactions`: Behavioral logs with sentiment scoring.
-   `fact_transactions`: Financial records including Subscriptions, Spotlights, and SuperSwipes.

### Phase 2: Machine Learning & Segmentation
Utilizing **K-Means Clustering**, I developed a behavioral segmentation framework to categorize users by intent rather than just demographics. 
-   **Clusters Identified:** 4 distinct groups, ranging from "Power Users" to "Passive Observers."
-   **Metric Discovery:** Isolated "Interaction Depth" as the leading indicator for Propensity to Pay (P2P).

### Phase 3: BigQuery Analytics
I architected three SQL Views to serve as the foundation for the BI layer:
1.  `marketplace_metrics_view`: Calculating the "Kindness Index" and Liquidity Ratios.
2.  `behavioral_cluster_financial_analysis_view`: Mapping ML clusters to financial outcomes.
3.  `attribution_logic_view`: Isolating ARPU by acquisition channel.

### Phase 4: Visualization & Strategy
The final output is a 3-page **Looker Studio Dashboard** that translates complex ML outputs into actionable insights:
-   **Marketplace Health:** Monitoring the reciprocal success of segments.
-   **Intent-Based Visuals:** Mapping swipe rates against interaction volume.
-   **Monetization Yield:** Prescribing budget reallocation based on channel performance.

## Repository Structure
```text
├── data/                   # Synthetic CSV datasets
├── docs/                   # Executive Summary and BI strategy docs
├── notebooks/              # Python ML pipelines and data generation
├── sql/                    # BigQuery SQL scripts and View definitions
├── Project_Disclaimer.md   # Legal and data usage disclosure
├── README.md               # Project documentation (You are here)
└── requirements.txt        # Python dependencies
