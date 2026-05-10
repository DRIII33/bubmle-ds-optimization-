# SOP Blueprints: Core Data Science Workflows

**Data Scientist:** Daniel Rodriguez III

## SOP-01: Lifecycle Segmentation
**Objective:** Define distinct user cohorts based on interaction depth and platform utility.

*   **Methodology:** Utilizing **K-Means** or **Gaussian Mixture Models (GMM)**.
*   **Input Features:** Swipe frequency, message-to-match ratio, session duration, and response latency.
*   **Output Segments:**
    *   **Power Users:** High reciprocity and high session frequency.
    *   **Casual Browsers:** High swipe volume but low messaging/conversion.
    *   **At-Risk Subs:** Premium users with declining interaction scores.
    *   **The Ghost:** Inactive accounts nearing churn thresholds.

## SOP-02: Propensity Scoring (P2P)
**Objective:** Predict the "Propensity to Pay" (P2P) within the first 72 hours of user registration.

*   **Model Architecture:** Deployment of **XGBoost** or **LightGBM** pipelines.
*   **Target Variable:** Boolean (`is_premium`) conversion within 3 days.
*   **Key Predictors:** Acquisition channel, initial sentiment scores of first 10 messages, and profile completion percentage.
*   **Application:** Real-time triggering of localized promotional offers for high-propensity users who have not yet converted.

## SOP-03: Incrementality & Causal Testing
**Objective:** Measure the true revenue lift of product deployments or pricing adjustments.

*   **Framework:** Designing **Quasi-experiments** and Synthetic Control Methods.
*   **Primary Focus:** "Focus Friday" product deployments and tiered pricing adjustments.
*   **Metrics:** Delta in ARPU (Average Revenue Per User) and Marketplace Liquidity Ratio (Successful Matches / Total Swipes).
*   **Goal:** Isolate the incremental lift of a feature from baseline organic growth.
