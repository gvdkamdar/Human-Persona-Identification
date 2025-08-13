import pandas as pd
import numpy as np
from src.config import *

class FeatureEngineer:
    def __init__(self):
        self.norc_with_pattern = None
        self.pattern_constraints = None
        self.feature_dict = None
        self.data = None
        
    def load_data(self):
        # Load required data files
        self.norc_with_pattern = pd.read_csv(PROCESSED_DIR / NORC_WITH_PATTERN_FILE)
        self.pattern_constraints = pd.read_csv(PROCESSED_DIR / PATTERN_CONSTRAINTS_FILE)
        self.feature_dict = pd.read_csv(PROCESSED_DIR / FEATURE_DICT_FILE)
        self.data = self.norc_with_pattern.copy()  # Create a copy for normalization
        return self
        
    def normalize_data(self):
        # Normalize numeric columns and convert Urbanicity to binary
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        # First convert Urbanicity to binary (0/1)
        if 'Urbanicity' in self.data.columns:
            self.data['Urbanicity'] = self.data['Urbanicity'].map({'Urban': 1, 'Rural': 0})
        
        # Select numeric columns for normalization
        numeric_columns = [col for col in self.data.columns 
                         if pd.api.types.is_numeric_dtype(self.data[col]) 
                         and col not in ['Pattern_id', 'fips']]
        
        # Normalize numeric columns
        self.data[numeric_columns] = self.data[numeric_columns].apply(
            lambda x: (x - x.min()) / (x.max() - x.min()) if (x.max() - x.min()) != 0 else x
        )
        return self

    def generate_final_output(self):
        # Generate final output file with modified features
        if any(x is None for x in [self.data, self.pattern_constraints, self.feature_dict]):
            raise ValueError("Required data not loaded. Call load_data() first.")
            
        # Create Feature_ID to Feature_Name mapping
        feature_map = dict(zip(self.feature_dict['Feature_ID'], self.feature_dict['Feature_Name']))
        
        # Create Pattern_id to feature names mapping
        pattern_feature_map = {}
        for _, row in self.pattern_constraints.iterrows():
            pattern_id = row['Pattern_id']
            feature_name = feature_map.get(row['Feature_ID'])
            if feature_name:
                if pattern_id not in pattern_feature_map:
                    pattern_feature_map[pattern_id] = []
                pattern_feature_map[pattern_id].append(feature_name)
        
        # Process each row
        output_rows = []
        for _, row in self.data.iterrows():
            pattern_id = row['Pattern_id']
            valid_features = pattern_feature_map.get(pattern_id, [])
            
            new_row = row.copy()
            for col in self.data.columns:
                if col not in ['Pattern_id', 'fips'] and col not in valid_features:
                    new_row[col] = -1
            output_rows.append(new_row)
        
        # Create and save output DataFrame
        output_df = pd.DataFrame(output_rows)
        output_df.to_csv(PROCESSED_DIR / FINAL_OUTPUT_FILE, index=False)
        return self

    def process_data(self):
        # Complete data processing pipeline
        return (self.load_data()
                .normalize_data()
                .generate_final_output())
