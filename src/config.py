from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).parent.parent

# Data directories
RAW_DATA_DIR = ROOT_DIR / "data" / "raw"
PROCESSED_DIR = ROOT_DIR / "data" / "processed"
OUTPUT_DIR = ROOT_DIR / "data" / "output"

# Input files
NORC_DATA_FILE = "NORC_data_2017-2020.csv"
PATTERN_DATA_FILE = "patterns_for_death-rate-2018-2021.csv"

# Output files
FEATURE_DICT_FILE = "feature_dict.csv"
PATTERN_CONSTRAINTS_FILE = "pattern_constraints.csv"
NORC_WITH_PATTERN_FILE = "norc_with_pattern.csv"
NORMALIZED_NORC_FILE = "normalized_norc_with_pattern.csv"
FINAL_OUTPUT_FILE = "final.csv"
CLUSTER_DATA_FILE = "cluster_data.json"
CLUSTER_STRUCTURE_FILE = "cluster_structure.json"
CLUSTER_HISTOGRAMS_FILE = "cluster_histograms.pdf"

# Clustering parameters
N_CLUSTERS = 14
