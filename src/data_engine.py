!# Install specific versions of data science and geospatial libraries
!pip install \
    geopandas==1.1.3 \
    numpy==2.0.2 \
    pandas==2.2.2 \
    pandas-datareader==0.10.0 \
    pandas-gbq==0.30.0 \
    pandas-stubs==2.2.2.240909 \
    scikit-learn==1.6.1 \
    scipy==1.16.3 \
    sklearn-pandas

---

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import uuid
import os

# Configuration & Seed
np.random.seed(42)
ROW_LIMIT = 50000
TXN_LIMIT = 10000

def generate_bumble_ecosystem():
    print("🚀 Initializing Kind-Connection Data Generation...")

    # 1. Generate dim_members (50,000 rows)
    member_ids = [str(uuid.uuid4()) for _ in range(ROW_LIMIT)]
    segments = ['The Connector', 'The Selective', 'The Newbie', 'The Ghost']
    channels = ['Paid Social', 'Organic', 'Referral']

    df_members = pd.DataFrame({
        'member_id': member_ids,
        'signup_date': pd.to_datetime(np.random.choice(pd.date_range('2025-01-01', '2025-12-31'), ROW_LIMIT)),
        'persona_segment': np.random.choice(segments, ROW_LIMIT, p=[0.2, 0.3, 0.3, 0.2]),
        'acquisition_channel': np.random.choice(channels, ROW_LIMIT),
        'is_premium': np.random.choice([0, 1], ROW_LIMIT, p=[0.85, 0.15])
    })

    # 2. Generate fact_interactions (50,000 rows)
    # Using vectorized random choice for actor/target matching
    df_interactions = pd.DataFrame({
        'interaction_id': np.arange(ROW_LIMIT),
        'actor_id': np.random.choice(member_ids, ROW_LIMIT),
        'target_id': np.random.choice(member_ids, ROW_LIMIT),
        'interaction_type': np.random.choice(['Swipe_Right', 'Swipe_Left', 'Message'], ROW_LIMIT, p=[0.4, 0.5, 0.1]),
        'sentiment_score': np.random.uniform(-1.0, 1.0, ROW_LIMIT)
    })

    # 3. Generate fact_transactions (10,000 rows)
    df_transactions = pd.DataFrame({
        'transaction_id': np.arange(TXN_LIMIT),
        'member_id': np.random.choice(member_ids, TXN_LIMIT),
        'product_type': np.random.choice(['Subscription', 'Spotlight', 'SuperSwipe'], TXN_LIMIT),
        'amount_usd': np.random.choice([9.99, 19.99, 39.99], TXN_LIMIT),
        'transaction_date': pd.to_datetime(np.random.choice(pd.date_range('2025-06-01', '2025-12-31'), TXN_LIMIT))
    })

    return df_members, df_interactions, df_transactions

def execute_behavioral_segmentation(df_members, df_interactions):
    print("🧠 Executing Behavioral Segmentation Pipeline...")

    # Feature Engineering: Swiping behavior
    behavior_metrics = df_interactions.groupby('actor_id').agg(
        total_interactions=('interaction_id', 'count'),
        avg_sentiment=('sentiment_score', 'mean'),
        right_swipe_rate=('interaction_type', lambda x: (x == 'Swipe_Right').mean())
    ).reset_index()

    # Join with members
    analysis_df = df_members.merge(behavior_metrics, left_on='member_id', right_on='actor_id', how='inner')

    # ML Pipeline
    features = ['total_interactions', 'avg_sentiment', 'right_swipe_rate']
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=4, random_state=42, n_init=10))
    ])

    analysis_df['behavioral_cluster'] = pipeline.fit_predict(analysis_df[features])
    print("✅ Segmentation Complete. Sample output:")
    print(analysis_df[['member_id', 'persona_segment', 'behavioral_cluster']].head())
    return analysis_df

# Run Execution
members, interactions, txns = generate_bumble_ecosystem()
segmented_data = execute_behavioral_segmentation(members, interactions)

# Save outputs to the specified directory
output_dir = 'src_data_engine_output'
os.makedirs(output_dir, exist_ok=True)

members.to_csv(os.path.join(output_dir, 'dim_members.csv'), index=False)
interactions.to_csv(os.path.join(output_dir, 'fact_interactions.csv'), index=False)
txns.to_csv(os.path.join(output_dir, 'fact_transactions.csv'), index=False)
segmented_data.to_csv(os.path.join(output_dir, 'segmented_data.csv'), index=False)

print(f"All dataframes saved to '{output_dir}' directory.")
