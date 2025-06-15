# eda.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath):
    """
    Load the dataset into a pandas DataFrame.
    Args:
        filepath (str): Path to the dataset file.
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None