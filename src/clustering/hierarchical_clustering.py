import numpy as np
import pandas as pd
import os
import json
from pathlib import Path
from scipy.cluster.hierarchy import linkage, fcluster, dendrogram
from sklearn.preprocessing import StandardScaler
from src.config import *

class HierarchicalClusterer:
    def __init__(self):
        self.data = None
        self.linkage_matrix = None
        self.cluster_labels = None
    
    def load_data(self):
        # Load data and check if file exists
        file_path = os.path.join(PROCESSED_DIR, FINAL_OUTPUT_FILE)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found at {file_path}")
        self.data = pd.read_csv(file_path)
        return self
    
    def fit(self):
        # Perform hierarchical clustering and add cluster labels
        features = self.data.drop(columns=['Pattern_id', 'fips'])
        X_scaled = StandardScaler().fit_transform(features)
        
        # Perform clustering
        self.linkage_matrix = linkage(X_scaled, method='ward')
        self.cluster_labels = fcluster(self.linkage_matrix, N_CLUSTERS, criterion='maxclust')
        
        # Add cluster labels to the DataFrame
        self.data['cluster_label'] = self.cluster_labels
        return self
    
    def save_cluster_data(self):
        # Save cluster data to JSON
        if 'cluster_label' not in self.data.columns:
            raise ValueError("Cluster labels not found. Run fit() first.")
            
        cluster_data = {}
        feature_columns = [col for col in self.data.columns 
                         if col not in ['Pattern_id', 'fips', 'cluster_label']]
        
        for cluster_num in np.unique(self.cluster_labels):
            cluster_df = self.data[self.data['cluster_label'] == cluster_num][feature_columns]
            
            cluster_data[str(cluster_num)] = {
                'size': len(cluster_df),
                'mean': cluster_df.mean().to_dict(),
                'std': cluster_df.std().to_dict()
            }
        
        with open(OUTPUT_DIR / CLUSTER_DATA_FILE, 'w') as f:
            json.dump(cluster_data, f, indent=4)
        return self

