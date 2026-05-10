# Analytical Logic & Engineering Specifications

**Data Scientist:** Daniel Rodriguez III

## 1. Vectorized Data Generation
To simulate the Bumble ecosystem within performance constraints, the engine utilizes `numpy` and `pandas` vectorized operations. By avoiding iterative loops, 50,000 rows of relational data are generated in **<2 seconds**.

## 2. Core Metrics Formulas
The following mathematical definitions are used for behavioral clustering and marketplace health:

*   **Swipe Right Ratio ($SRR$):**
$$SRR = \frac{\sum \text{Swipe\_Right}}{\sum (\text{Swipe\_Right} + \text{Swipe\_Left})}$$

*   **Marketplace Liquidity ($L$):**
$$L = \frac{\text{Successful Reciprocal Matches}}{\text{Total Active Members}}$$

*   **Ecosystem Health Score ($EHS$):**
$$EHS = \mu(\text{sentiment\_score})$$

## 3. Feature Engineering for Clustering
The machine learning pipeline will aggregate `fact_interactions` into a feature matrix at the `member_id` level:
1.  **Activity Intensity:** Frequency of interactions per 24-hour window.
2.  **Selectivity Index:** Inverse of the Swipe Right Ratio.
3.  **Responsiveness:** Average latency (time delta) between receiving a message and responding.
