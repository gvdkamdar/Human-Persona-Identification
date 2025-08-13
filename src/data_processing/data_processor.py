import pandas as pd
from src.config import *

class DataProcessor:
    def __init__(self):
        self.norc_data = None
        self.pattern_constraints = None
        self.feature_dict = None
        
    def load_data(self):
        # Load all required data files
        self.norc_data = pd.read_csv(RAW_DATA_DIR / NORC_DATA_FILE)
        self.pattern_constraints = pd.read_csv(PROCESSED_DIR / PATTERN_CONSTRAINTS_FILE)
        self.feature_dict = pd.read_csv(PROCESSED_DIR / FEATURE_DICT_FILE)
        
    def generate_norc_with_pattern(self):
        # Create Feature_ID to Feature_Name mapping
        feature_map = dict(zip(self.feature_dict['Feature_ID'], self.feature_dict['Feature_Name']))
        output_rows = []

        # Process each pattern
        for pattern_id in self.pattern_constraints['Pattern_id'].unique():
            pattern_features = self.pattern_constraints[
                self.pattern_constraints['Pattern_id'] == pattern_id
            ]
            valid_counties = self.norc_data.copy()

            # Apply constraints for each feature
            for _, row in pattern_features.iterrows():
                feature_name = feature_map[row['Feature_ID']]
                lb, ub = row['LB'], row['UB']

                if pd.notna(lb):
                    valid_counties = valid_counties[valid_counties[feature_name] >= lb]
                if pd.notna(ub):
                    valid_counties = valid_counties[valid_counties[feature_name] <= ub]

            # Add valid counties to output
            for _, county_row in valid_counties.iterrows():
                output_row = [pattern_id] + county_row.tolist()
                output_rows.append(output_row)

        # Create and save output DataFrame
        output_columns = ['Pattern_id'] + self.norc_data.columns.tolist()
        output_df = pd.DataFrame(output_rows, columns=output_columns)
        output_df.to_csv(PROCESSED_DIR / NORC_WITH_PATTERN_FILE, index=False)
