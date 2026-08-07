"""
Preprocessing utilities.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(df):
    """
    Clean and preprocess customer churn dataset.
    """

    df = df.copy()

    # Convert TotalCharges
    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"].astype(str).str.strip(),
        errors="coerce"
    )

    # Fill missing values
    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    # Remove customerID
    df = df.drop(columns=["customerID"])

    return df


def encode_features(df):

    return pd.get_dummies(
        df,
        drop_first=True,
        dtype=int
    )


def scale_features(df, numerical_columns):

    scaler = StandardScaler()

    df[numerical_columns] = scaler.fit_transform(
        df[numerical_columns]
    )

    return df, scaler