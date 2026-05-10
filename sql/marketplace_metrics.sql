-- Marketplace Liquidity & Ecosystem Health Analysis
WITH user_activity AS (
    SELECT 
        m.member_id,
        m.persona_segment,
        COUNT(i.interaction_id) AS total_swipes,
        COUNTIF(i.interaction_type = 'Swipe_Right') AS right_swipes,
        AVG(i.sentiment_score) AS avg_kindness_score
    FROM `bumble_data.dim_members` m
    LEFT JOIN `bumble_data.fact_interactions` i ON m.member_id = i.actor_id
    GROUP BY 1, 2
)
SELECT 
    persona_segment,
    COUNT(member_id) AS total_users,
    ROUND(AVG(total_swipes), 2) AS avg_engagement,
    ROUND(SAFE_DIVIDE(SUM(right_swipes), SUM(total_swipes)), 4) AS liquidity_ratio,
    ROUND(AVG(avg_kindness_score), 3) AS kindness_index
FROM user_activity
GROUP BY 1
ORDER BY liquidity_ratio DESC;
