from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def train_clustering_model(analysis_df, n_clusters=4):
    """Trains a K-Means pipeline on user behavioral features."""
    features = ['total_interactions', 'avg_sentiment', 'right_swipe_rate']
    
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('kmeans', KMeans(n_clusters=n_clusters, random_state=42, n_init=10))
    ])
    
    analysis_df['behavioral_cluster'] = pipeline.fit_predict(analysis_df[features])
    return analysis_df, pipeline
