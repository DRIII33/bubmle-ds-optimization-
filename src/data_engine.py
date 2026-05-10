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
import uuid

def generate_bumble_ecosystem(row_limit=50000, txn_limit=10000):
    """Generates the three-tier relational schema for Bumble Core DS simulation."""
    np.random.seed(42)
    
    # 1. Generate dim_members
    member_ids = [str(uuid.uuid4()) for _ in range(row_limit)]
    df_members = pd.DataFrame({
        'member_id': member_ids,
        'signup_date': pd.to_datetime(np.random.choice(pd.date_range('2025-01-01', '2025-12-31'), row_limit)),
        'persona_segment': np.random.choice(['The Connector', 'The Selective', 'The Newbie', 'The Ghost'], row_limit, p=[0.2, 0.3, 0.3, 0.2]),
        'acquisition_channel': np.random.choice(['Paid Social', 'Organic', 'Referral'], row_limit),
        'is_premium': np.random.choice([0, 1], row_limit, p=[0.85, 0.15])
    })

    # 2. Generate fact_interactions
    df_interactions = pd.DataFrame({
        'interaction_id': np.arange(row_limit),
        'actor_id': np.random.choice(member_ids, row_limit),
        'target_id': np.random.choice(member_ids, row_limit),
        'interaction_type': np.random.choice(['Swipe_Right', 'Swipe_Left', 'Message'], row_limit, p=[0.4, 0.5, 0.1]),
        'sentiment_score': np.random.uniform(-1.0, 1.0, row_limit)
    })

    # 3. Generate fact_transactions
    df_transactions = pd.DataFrame({
        'transaction_id': np.arange(txn_limit),
        'member_id': np.random.choice(member_ids, txn_limit),
        'product_type': np.random.choice(['Subscription', 'Spotlight', 'SuperSwipe'], txn_limit),
        'amount_usd': np.random.choice([9.99, 19.99, 39.99], txn_limit),
        'transaction_date': pd.to_datetime(np.random.choice(pd.date_range('2025-06-01', '2025-12-31'), txn_limit))
    })

    return df_members, df_interactions, df_transactions
