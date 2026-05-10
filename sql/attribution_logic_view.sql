CREATE OR REPLACE VIEW `driiiportfolio.bumble_data.attribution_logic_view` AS
-- Revenue Attribution & Channel Performance
WITH revenue_summary AS (
    SELECT 
        member_id,
        SUM(amount_usd) AS total_revenue
    FROM `driiiportfolio.bumble_data.fact_transactions`
    GROUP BY 1
)
SELECT 
    m.acquisition_channel,
    COUNT(DISTINCT m.member_id) AS user_count,
    ROUND(SUM(r.total_revenue), 2) AS gross_revenue,
    ROUND(SAFE_DIVIDE(SUM(r.total_revenue), COUNT(DISTINCT m.member_id)), 2) AS ARPU
FROM `driiiportfolio.bumble_data.dim_members` m
LEFT JOIN revenue_summary r ON m.member_id = r.member_id
GROUP BY 1
ORDER BY ARPU DESC;
