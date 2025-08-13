# Causal-Analysis-Visualization-AP

## NORC County Analysis and Pattern-Based Clustering

A data analysis project that combines NORC (National Opinion Research Center) county-level data with patterns generated from the AK Analyst Platform to create meaningful county personas through hierarchical clustering.

This project analyzes county-level socioeconomic and health indicators to identify patterns and create meaningful personas. It consists of two main components:

## Part 1: Data Processing and Pattern Integration
- Processes NORC county-level dataset (2017-2020)
- Integrates patterns from AK Analyst Platform
- Creates feature dictionaries and pattern constraints
- Normalizes data and applies pattern-based transformations
- Generates intermediate processed datasets

## Part 2: Hierarchical Clustering Analysis
- Performs hierarchical clustering on processed county data
- Creates dendrograms showing county relationships
- Generates detailed cluster visualizations
- Produces cluster analysis reports and statistics

## Project Structure
```
advanced-project/
├── data/
│   ├── raw/                                      # Original datasets
│   │   ├── NORC_data_2017-2020.csv
│   │   └── patterns_for_death-rate-2018-2021.csv
│   ├── processed/                                # Intermediate files
│   │   ├── feature_dict.csv
│   │   ├── pattern_constraints.csv
│   │   ├── norc_with_pattern.csv
│   │   ├── normalized_norc_with_pattern.csv
│   │   └── final.csv
│   └── output/                                   # Analysis results
│       ├── cluster_data.json
│       ├── cluster_structure.json
│       └── cluster_histograms.pdf
├── src/
│   ├── data_processing/                          # Data processing modules
│   │   ├── data_processor.py
│   │   ├── feature_engineering.py
│   │   └── utils.py
│   └── clustering/                               # Clustering analysis
│       ├── hierarchical_clustering.py
│       └── visualization.py
├── notebooks/                                    # Jupyter notebooks
│   ├── advacned_project_data_processing.ipynb    # Data processing notebook
│   └── advacned_project_clustering.ipynb         # Clustering analysis notebook
└── requirements.txt
```

## Features

- **Data Integration**: Combines NORC county data with AK Analyst patterns
- **Feature Engineering**: Normalizes and transforms features based on patterns
- **Hierarchical Clustering**: Groups counties with similar characteristics
- **Visualization**: Generates dendrograms and feature distribution plots
- **Pattern Analysis**: Identifies significant county patterns and relationships

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/advanced-project.git
cd advanced-project
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place raw data files in `data/raw/`:
   - `NORC_data_2017-2020.csv`: NORC county dataset
   - `patterns_for_death-rate-2018-2021.csv`: Pattern file from AK Analyst

2. Run the processing pipeline:
```bash
python main.py
```

3. Check the output files in `data/output/`

## Jupyter Notebooks

The project includes two Jupyter notebooks demonstrating the workflow:

1. `AP_Semester3.ipynb`: Data processing and pattern integration
2. `building_clusters.ipynb`: Clustering analysis and visualization

To use the notebooks:
```bash
pip install jupyter
jupyter notebook
```

## Dependencies
- pandas>=1.3.0
- numpy>=1.21.0
- scipy>=1.7.0
- scikit-learn>=0.24.0
- matplotlib>=3.4.0
- seaborn>=0.11.0

## Output Files

The pipeline generates several files:
- `feature_dict.csv`: Maps features to unique IDs
- `pattern_constraints.csv`: Defines pattern constraints
- `normalized_norc_with_pattern.csv`: Processed county data
- `cluster_data.json`: Detailed cluster analysis
- `cluster_histograms.pdf`: Cluster visualizations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Acknowledgments

- NORC at the University of Chicago for the county-level dataset
- AK Analyst Platform for pattern generation tools
- Contributors and maintainers of the scientific Python ecosystem