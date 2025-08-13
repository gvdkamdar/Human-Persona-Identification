# UNCOMMENT - To increase the recursion limit
# import sys
# sys.setrecursionlimit(10000)

from src.data_processing.data_processor import DataProcessor
from src.data_processing.feature_engineering import FeatureEngineer
from src.clustering.hierarchical_clustering import HierarchicalClusterer
from src.clustering.visualization import ClusterVisualizer

def process_data():
    # Initialize processors
    processor = DataProcessor()
    engineer = FeatureEngineer()
    clusterer = HierarchicalClusterer()
    
    try:
        # Process data
        processor.load_data()
        processor.generate_norc_with_pattern()      

        engineer.process_data()  
        
        # Perform clustering
        clusterer.load_data()
        clusterer.fit()
        clusterer.save_cluster_data()
        
        # Create visualizations
        visualizer = ClusterVisualizer(clusterer)
        visualizer.create_visualizations()
        
    except Exception as e:
        print(f"Error processing data: {e}")
        raise

if __name__ == "__main__":
    process_data()
