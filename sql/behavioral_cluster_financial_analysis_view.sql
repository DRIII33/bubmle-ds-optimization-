CREATE OR REPLACE VIEW `driiiportfolio.bumble_data.behavioral_cluster_financial_analysis_view` AS
-- Script 3: Behavioral Cluster Financial Analysis
WITH cluster_revenue AS (
    SELECT 
        member_id,
        SUM(amount_usd) AS total_rev
    FROM `driiiportfolio.bumble_data.fact_transactions`
    GROUP BY 1
)
SELECT 
    s.behavioral_cluster,
    COUNT(s.member_id) AS user_count,
    ROUND(AVG(s.total_interactions), 2) AS avg_interactions,
    ROUND(AVG(s.right_swipe_rate), 4) AS avg_swipe_rate,
    ROUND(SUM(r.total_rev), 2) AS total_cluster_revenue,
    ROUND(SAFE_DIVIDE(SUM(r.total_rev), COUNT(s.member_id)), 2) AS cluster_ARPU
FROM `driiiportfolio.bumble_data.segmented_data` s
LEFT JOIN cluster_revenue r ON s.member_id = r.member_id
GROUP BY 1
ORDER BY behavioral_cluster ASC;
