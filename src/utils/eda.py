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

def summarize_data(data):
    """
    Generate summary statistics for the dataset.
    Args:
        data (pd.DataFrame): Dataset to summarize.
    Returns:
        None
    """
    print("\n--- Dataset Summary ---")
    print(data.describe(include='all'))
    print("\n--- Missing Values ---")
    print(data.isnull().sum())
    print("\n--- Data Types ---")
    print(data.dtypes)

def plot_distributions(data, numerical_columns):
    """
    Plot histograms for numerical columns.
    Args:
        data (pd.DataFrame): Dataset containing numerical columns.
        numerical_columns (list): List of numerical column names.
    Returns:
        None
    """
    for col in numerical_columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(data[col], kde=True, bins=30)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.show()

def plot_categorical_counts(data, categorical_columns):
    """
    Plot bar charts for categorical columns.
    Args:
        data (pd.DataFrame): Dataset containing categorical columns.
        categorical_columns (list): List of categorical column names.
    Returns:
        None
    """
    for col in categorical_columns:
        plt.figure(figsize=(8, 5))
        sns.countplot(data=data, x=col, order=data[col].value_counts().index)
        plt.title(f"Count of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()

def detect_outliers(data, numerical_columns):
    """
    Detect outliers using box plots.
    Args:
        data (pd.DataFrame): Dataset containing numerical columns.
        numerical_columns (list): List of numerical column names.
    Returns:
        None
    """
    for col in numerical_columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=data[col])
        plt.title(f"Outliers in {col}")
        plt.xlabel(col)
        plt.show()

def analyze_correlations(data, numerical_columns):
    """
    Generate a correlation heatmap for numerical columns.
    Args:
        data (pd.DataFrame): Dataset containing numerical columns.
        numerical_columns (list): List of numerical column names.
    Returns:
        None
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = data[numerical_columns].corr()
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
