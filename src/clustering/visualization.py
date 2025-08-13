from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from src.config import *

class ClusterVisualizer:
    def __init__(self, clusterer):
        self.clusterer = clusterer
        
    def create_visualizations(self):
        # Create all visualizations and save to a single PDF
        with PdfPages(OUTPUT_DIR / 'clustering_results.pdf') as pdf:
            # Create dendrogram
            plt.figure(figsize=(20, 12))
            dendrogram(
                self.clusterer.linkage_matrix,
                truncate_mode='lastp',
                p=N_CLUSTERS,
                show_leaf_counts=True,
                leaf_rotation=90.,
                leaf_font_size=12.
            )
            plt.title('Hierarchical Clustering Dendrogram')
            plt.xlabel('Cluster Index')
            plt.ylabel('Distance')
            pdf.savefig()
            plt.close()
            
            # Create histograms for each cluster
            feature_columns = [col for col in self.clusterer.data.columns 
                             if col not in ['Pattern_id', 'fips', 'cluster_label']]
            
            for cluster_num in sorted(self.clusterer.data['cluster_label'].unique()):
                cluster_df = self.clusterer.data[
                    self.clusterer.data['cluster_label'] == cluster_num
                ]
                
                # Create feature distribution plots
                plt.figure(figsize=(20, 10))
                plt.suptitle(f'Cluster {cluster_num} Feature Distributions', fontsize=16)
                
                for i, feature in enumerate(feature_columns):
                    plt.subplot(5, 6, i + 1)
                    sns.histplot(
                        cluster_df[feature],
                        bins=30,
                        color='skyblue',
                        edgecolor='black'
                    )
                    plt.title(feature, fontsize=8)
                    plt.xticks(fontsize=6)
                    plt.yticks(fontsize=6)
                
                plt.tight_layout(rect=[0, 0.03, 1, 0.95])
                pdf.savefig()
                plt.close()
