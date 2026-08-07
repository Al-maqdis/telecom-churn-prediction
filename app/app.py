import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

# ==========================================
# Load Model
# ==========================================

model = joblib.load(MODEL_DIR / "logistic_regression_model.pkl")

feature_names = joblib.load(MODEL_DIR / "model_features.pkl")

scaler = joblib.load(
    MODEL_DIR / "scaler.pkl"
)

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction System")

st.write(
    """
Predict whether a telecommunications customer is likely
to churn using a trained Machine Learning model.
"""
) 

st.sidebar.header("Customer Information") 

gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)

senior = st.sidebar.selectbox(
    "Senior Citizen",
    [0,1]
)

partner = st.sidebar.selectbox(
    "Partner",
    ["No","Yes"]
)

dependents = st.sidebar.selectbox(
    "Dependents",
    ["No","Yes"]
)


tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

monthly = st.sidebar.number_input(
    "Monthly Charges",
    18.25,
    120.0,
    70.0
)

total = st.sidebar.number_input(
    "Total Charges",
    0.0,
    9000.0,
    1000.0
)
# ===========================================
# Phone Service
# ===========================================

phone_service = st.sidebar.selectbox(
    "Phone Service",
    ["No", "Yes"]
)

# ===========================================
# Multiple Lines
# ===========================================

multiple_lines = st.sidebar.selectbox(
    "Multiple Lines",
    ["No phone service", "No", "Yes"]
)

# ===========================================
# Internet Service
# ===========================================

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

# ===========================================
# Online Security
# ===========================================

online_security = st.sidebar.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

# ===========================================
# Online Backup
# ===========================================

online_backup = st.sidebar.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

# ===========================================
# Device Protection
# ===========================================

device_protection = st.sidebar.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

# ===========================================
# Tech Support
# ===========================================

tech_support = st.sidebar.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

# ===========================================
# Streaming TV
# ===========================================

streaming_tv = st.sidebar.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

# ===========================================
# Streaming Movies
# ===========================================

streaming_movies = st.sidebar.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

# ===========================================
# Contract
# ===========================================

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

# ===========================================
# Paperless Billing
# ===========================================

paperless = st.sidebar.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

# ===========================================
# Payment Method
# ===========================================

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)


# ===========================================
# Create Customer Record
# ===========================================

input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless],
    "PaymentMethod": [payment_method],
    "MonthlyCharges": [monthly],
    "TotalCharges": [total]
})

input_data = pd.get_dummies(
    input_data,
    drop_first=True,
    dtype=int
)

input_data = input_data.reindex(
    columns=feature_names,
    fill_value=0
)

# ==========================================
# Scale Numerical Features
# ==========================================

numerical_columns = [
    "tenure",
    "MonthlyCharges",
    "TotalCharges"
]

input_data[numerical_columns] = scaler.transform(
    input_data[numerical_columns]
)


predict_button = st.button("Predict Customer Churn")

if predict_button:

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    # Show prediction
    if prediction == 1:
        st.error("⚠ Customer is likely to churn.")
    else:
        st.success("✅ Customer is likely to remain.")

    # Probability
    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    # Progress bar
    st.progress(float(probability))

    # Risk level
    if probability < 0.30:

        st.success("🟢 Low Churn Risk")

        st.info("""
### Recommendation

• Continue current engagement.

• Maintain service quality.

• Promote premium service packages.
""")

    elif probability < 0.60:

        st.warning("🟡 Medium Churn Risk")

        st.info("""
### Recommendation

• Offer loyalty rewards.

• Schedule customer follow-up.

• Recommend annual contract.
""")

    else:

        st.error("🔴 High Churn Risk")

        st.info("""
### Recommendation

• Immediate retention campaign.

• Offer discount.

• Assign customer support.

• Contact customer within 48 hours.
""")

        st.divider()

st.subheader("ℹ️ Model Information")

col1, col2 = st.columns(2)

with col1:
    st.write("**Algorithm:** Logistic Regression")
    st.write("**Accuracy:** 80.62%")
    st.write("**ROC-AUC:** 0.842")

with col2:
    st.write("**Dataset:** IBM Telco Customer Churn")
    st.write("**Training Samples:** 5,634")
    st.write("**Testing Samples:** 1,409")

    st.divider()

st.markdown("""
### 👨‍💻 Developed By

**HyBeek**

Customer Churn Prediction System

Built with:

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Matplotlib

© 2026
""")