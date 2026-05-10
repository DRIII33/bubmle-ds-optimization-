def extract_behavioral_features(df_interactions):
    """Calculates swipe ratios and sentiment metrics per user."""
    behavior_metrics = df_interactions.groupby('actor_id').agg(
        total_interactions=('interaction_id', 'count'),
        avg_sentiment=('sentiment_score', 'mean'),
        right_swipe_rate=('interaction_type', lambda x: (x == 'Swipe_Right').mean())
    ).reset_index()
    return behavior_metrics
