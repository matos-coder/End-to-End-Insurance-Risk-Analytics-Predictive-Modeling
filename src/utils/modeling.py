# modeling.py

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from xgboost import XGBRegressor, XGBClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, precision_score, recall_score, f1_score
import shap

# **Data Preparation Functions**
def handle_missing_data(df, method="drop"):
    """
    Handle missing values in the dataset.
    Args:
        df (pd.DataFrame): The dataset.
        method (str): The method to handle missing values ('drop' or 'impute').
    Returns:
        pd.DataFrame: Dataset with missing values handled.
    """
    if method == "drop":
        return df.dropna()
    elif method == "impute":
        for col in df.select_dtypes(include=[np.number]):
            df[col].fillna(df[col].mean(), inplace=True)
        for col in df.select_dtypes(include=["object"]):
            df[col].fillna(df[col].mode()[0], inplace=True)
    return df


def encode_categorical_variables(df):
    """
    Encode categorical variables using one-hot encoding.
    Args:
        df (pd.DataFrame): The dataset.
    Returns:
        pd.DataFrame: Encoded dataset.
    """
    return pd.get_dummies(df, drop_first=True)


def split_data(df, target_col, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    Args:
        df (pd.DataFrame): The dataset.
        target_col (str): The target column.
        test_size (float): Proportion of the dataset to include in the test split.
        random_state (int): Random seed for reproducibility.
    Returns:
        tuple: Training and testing datasets (X_train, X_test, y_train, y_test).
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

# **Modeling Functions**
def train_regression_models(X_train, y_train):
    """
    Train regression models: Linear Regression, Random Forest, and XGBoost.
    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target values.
    Returns:
        dict: Trained models.
    """
    models = {
        "LinearRegression": LinearRegression(),
        "RandomForest": RandomForestRegressor(random_state=42),
        "XGBoost": XGBRegressor(random_state=42, verbosity=0)
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
    return models


def evaluate_regression_models(models, X_test, y_test):
    """
    Evaluate regression models using RMSE and R-squared.
    Args:
        models (dict): Trained models.
        X_test (pd.DataFrame): Testing features.
        y_test (pd.Series): Testing target values.
    Returns:
        dict: Model evaluation results.
    """
    results = {}
    for name, model in models.items():
        predictions = model.predict(X_test)
        results[name] = {
            "RMSE": np.sqrt(mean_squared_error(y_test, predictions)),
            "R2": r2_score(y_test, predictions)
        }
    return results


def train_classification_models(X_train, y_train):
    """
    Train classification models: Random Forest and XGBoost.
    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target values.
    Returns:
        dict: Trained models.
    """
    models = {
        "RandomForest": RandomForestClassifier(random_state=42),
        "XGBoost": XGBClassifier(random_state=42, verbosity=0)
    }
    for name, model in models.items():
        model.fit(X_train, y_train)
    return models


def evaluate_classification_models(models, X_test, y_test):
    """
    Evaluate classification models using accuracy, precision, recall, and F1-score.
    Args:
        models (dict): Trained models.
        X_test (pd.DataFrame): Testing features.
        y_test (pd.Series): Testing target values.
    Returns:
        dict: Model evaluation results.
    """
    results = {}
    for name, model in models.items():
        predictions = model.predict(X_test)
        results[name] = {
            "Accuracy": accuracy_score(y_test, predictions),
            "Precision": precision_score(y_test, predictions),
            "Recall": recall_score(y_test, predictions),
            "F1": f1_score(y_test, predictions)
        }
    return results


def analyze_feature_importance(model, X_train):
    """
    Analyze feature importance using SHAP.
    Args:
        model: Trained model.
        X_train (pd.DataFrame): Training features.
    Returns:
        None
    """
    explainer = shap.Explainer(model)
    shap_values = explainer(X_train)
    shap.summary_plot(shap_values, X_train)

