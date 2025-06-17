import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind
from typing import Tuple, Dict

# --- Metrics Calculation ---
def calculate_claim_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate claim frequency, claim severity, and margin.

    Args:
        df (pd.DataFrame): The input data containing TotalPremium, TotalClaims, and policy details.

    Returns:
        pd.DataFrame: DataFrame with added claim frequency, severity, and margin columns.
    """
    try:
        df['ClaimFrequency'] = df['NumberOfClaims'] / df['TotalPolicies']
        df['ClaimSeverity'] = df['TotalClaims'] / np.maximum(df['NumberOfClaims'], 1)
        df['Margin'] = df['TotalPremium'] - df['TotalClaims']
        return df
    except KeyError as e:
        raise KeyError(f"Missing column in input data: {e}")

# --- Data Segmentation ---
def segment_data(df: pd.DataFrame, feature: str, group_a: str, group_b: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Segment the data into two groups based on the specified feature.

    Args:
        df (pd.DataFrame): The input data.
        feature (str): Column name for segmentation.
        group_a (str): Control group value.
        group_b (str): Test group value.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: DataFrames for Group A and Group B.
    """
    try:
        group_a_data = df[df[feature] == group_a]
        group_b_data = df[df[feature] == group_b]
        return group_a_data, group_b_data
    except KeyError as e:
        raise KeyError(f"Feature column not found: {e}")

# --- Statistical Testing ---
def perform_t_test(group_a: pd.Series, group_b: pd.Series) -> Dict[str, float]:
    """
    Perform a T-Test between two groups.

    Args:
        group_a (pd.Series): Numerical data for Group A.
        group_b (pd.Series): Numerical data for Group B.

    Returns:
        Dict[str, float]: Test statistic and p-value.
    """
    stat, p_value = ttest_ind(group_a, group_b, equal_var=False)
    return {"t_statistic": stat, "p_value": p_value}

def perform_chi_squared_test(df: pd.DataFrame, feature: str, target: str) -> Dict[str, float]:
    """
    Perform a Chi-Squared test for categorical data.

    Args:
        df (pd.DataFrame): Input data.
        feature (str): Categorical feature column.
        target (str): Target variable column (e.g., ClaimFrequency).

    Returns:
        Dict[str, float]: Chi-Squared statistic and p-value.
    """
    try:
        contingency_table = pd.crosstab(df[feature], df[target])
        chi2, p, dof, _ = chi2_contingency(contingency_table)
        return {"chi2_statistic": chi2, "p_value": p, "degrees_of_freedom": dof}
    except KeyError as e:
        raise KeyError(f"Column not found for Chi-Squared test: {e}")

# --- Reporting Results ---
def interpret_results(feature: str, test_result: Dict[str, float], alpha: float = 0.05) -> str:
    """
    Interpret the statistical test results.

    Args:
        feature (str): The feature being tested.
        test_result (Dict[str, float]): Results of the statistical test.
        alpha (float): Significance level.

    Returns:
        str: Interpretation of results.
    """
    if test_result['p_value'] < alpha:
        return f"The null hypothesis for {feature} is rejected (p = {test_result['p_value']:.3f}). Significant effect detected."
    else:
        return f"The null hypothesis for {feature} is not rejected (p = {test_result['p_value']:.3f}). No significant effect detected."
