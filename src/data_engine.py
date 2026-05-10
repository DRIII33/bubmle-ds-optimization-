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
MEMBER_LIMIT = 50000
INTERACTION_LIMIT = 50000
TXN_LIMIT = 10000

def generate_bumble_ecosystem():
    """Vectorized generation of the Kindness Graph dataset."""
    print("🚀 Generating 110,000+ data points...")

    # 1. dim_members
    member_ids = [str(uuid.uuid4()) for _ in range(MEMBER_LIMIT)]
    df_members = pd.DataFrame({
        'member_id': member_ids,
        'signup_date': pd.to_datetime(np.random.choice(pd.date_range('2024-01-01', '2025-01-01'), MEMBER_LIMIT)),
        'persona_segment': np.random.choice(['The Connector', 'The Selective', 'The Newbie', 'The Ghost'], MEMBER_LIMIT),
        'acquisition_channel': np.random.choice(['Paid Social', 'Organic', 'Referral'], MEMBER_LIMIT),
        'is_premium': np.random.choice([0, 1], MEMBER_LIMIT, p=[0.85, 0.15])
    })

    # 2. fact_interactions
    df_interactions = pd.DataFrame({
        'interaction_id': np.arange(INTERACTION_LIMIT),
        'actor_id': np.random.choice(member_ids, INTERACTION_LIMIT),
        'target_id': np.random.choice(member_ids, INTERACTION_LIMIT),
        'interaction_type': np.random.choice(['Swipe_Right', 'Swipe_Left', 'Message'], INTERACTION_LIMIT, p=[0.4, 0.5, 0.1]),
        'sentiment_score': np.random.uniform(-1.0, 1.0, INTERACTION_LIMIT)
    })

    # 3. fact_transactions
    df_transactions = pd.DataFrame({
        'transaction_id': np.arange(TXN_LIMIT),
        'member_id': np.random.choice(member_ids, TXN_LIMIT),
        'product_type': np.random.choice(['Subscription', 'Spotlight', 'SuperSwipe'], TXN_LIMIT),
        'amount_usd': np.random.choice([9.99, 19.99, 39.99], TXN_LIMIT),
        'is_refunded': np.random.choice([False, True], TXN_LIMIT, p=[0.98, 0.02])
    })

    return df_members, df_interactions, df_transactions

def run_clustering_pipeline(df_members, df_interactions):
    """Executes behavioral segmentation using K-Means."""
    print("🧠 Training Behavioral Clusters...")

    # Feature Engineering
    features = df_interactions.groupby('actor_id').agg(
        activity_count=('interaction_id', 'count'),
        avg_sentiment=('sentiment_score', 'mean'),
        right_swipe_rate=('interaction_type', lambda x: (x == 'Swipe_Right').mean())
    ).reset_index()

    # Merge and Scale
    model_df = df_members.merge(features, left_on='member_id', right_on='actor_id', how='inner')
    X = model_df[['activity_count', 'avg_sentiment', 'right_swipe_rate']]

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=4, random_state=42, n_init=10))
    ])

    model_df['behavioral_cluster'] = pipeline.fit_predict(X)
    print("✅ Logic Check: Top 5 rows of clustered data:")
    print(model_df[['member_id', 'behavioral_cluster', 'right_swipe_rate']].head())
    return model_df

if __name__ == "__main__":
    m, i, t = generate_bumble_ecosystem()
    final_dataset = run_clustering_pipeline(m, i)

    # Save the final dataset to a specified directory
    output_dir = 'src_data_engine_output'
    os.makedirs(output_dir, exist_ok=True)
    final_dataset.to_csv(os.path.join(output_dir, 'clustered_data.csv'), index=False)
    print(f"Dataset saved to {os.path.join(output_dir, 'clustered_data.csv')}")
