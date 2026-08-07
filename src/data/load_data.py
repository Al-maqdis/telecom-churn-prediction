"""
Load customer churn dataset.
"""

import pandas as pd


def load_dataset(filepath):
    """
    Load Telco Customer Churn dataset.

    Parameters
    ----------
    filepath : str
        Path to CSV file.

    Returns
    -------
    pandas.DataFrame
    """

    return pd.read_csv(filepath)