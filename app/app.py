import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
import io

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

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


# ==========================================
# PDF Report Generator
# ==========================================

def create_pdf_report(
    customer_data,
    prediction,
    probability,
    risk_level,
    recommendations
):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]

    story = []

    # ------------------------------------------
    # Title
    # ------------------------------------------

    story.append(
        Paragraph(
            "Customer Churn Prediction Report",
            title_style
        )
    )

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "Machine Learning Customer Retention Analysis",
            normal_style
        )
    )

    story.append(Spacer(1, 20))

    # ------------------------------------------
    # Prediction Result
    # ------------------------------------------

    story.append(
        Paragraph(
            "Prediction Result",
            heading_style
        )
    )

    prediction_text = (
        "Customer is likely to churn"
        if prediction == 1
        else "Customer is likely to remain"
    )

    prediction_data = [
        ["Prediction", prediction_text],
        ["Churn Probability", f"{probability * 100:.2f}%"],
        ["Risk Level", risk_level]
    ]

    prediction_table = Table(
        prediction_data,
        colWidths=[170, 300]
    )

    prediction_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("PADDING", (0, 0), (-1, -1), 7),
        ])
    )

    story.append(prediction_table)

    story.append(Spacer(1, 20))

    # ------------------------------------------
    # Customer Information
    # ------------------------------------------

    story.append(
        Paragraph(
            "Customer Information",
            heading_style
        )
    )

    customer_rows = [
        ["Field", "Value"]
    ]

    for column, value in customer_data.items():
        customer_rows.append([
            str(column),
            str(value)
        ])

    customer_table = Table(
        customer_rows,
        colWidths=[220, 250]
    )

    customer_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("PADDING", (0, 0), (-1, -1), 6),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ])
    )

    story.append(customer_table)

    story.append(Spacer(1, 20))

    # ------------------------------------------
    # Recommendations
    # ------------------------------------------

    story.append(
        Paragraph(
            "Recommended Action",
            heading_style
        )
    )

    for recommendation in recommendations:
        story.append(
            Paragraph(
                f"• {recommendation}",
                normal_style
            )
        )

        story.append(Spacer(1, 5))

    story.append(Spacer(1, 15))

    # ------------------------------------------
    # Model Information
    # ------------------------------------------

    story.append(
        Paragraph(
            "Model Information",
            heading_style
        )
    )

    model_data = [
        ["Algorithm", "Logistic Regression"],
        ["Dataset", "IBM Telco Customer Churn"],
        ["Accuracy", "80.62%"],
        ["ROC-AUC", "0.842"],
        ["Training Samples", "5,634"],
        ["Testing Samples", "1,409"],
    ]

    model_table = Table(
        model_data,
        colWidths=[170, 300]
    )

    model_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
            ("PADDING", (0, 0), (-1, -1), 6),
        ])
    )

    story.append(model_table)

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Developed by HyBeek | Customer Churn Prediction System",
            normal_style
        )
    )

    story.append(
        Paragraph(
            "© 2026 HyBeek",
            normal_style
        )
    )

    doc.build(story)

    buffer.seek(0)

    return buffer



# ===========================================
# Phone Service
# ===========================================

phone_service = st.sidebar.selectbox(
    "Phone Service",
    ["No", "Yes"],
    key="phone_service"
)


# ===========================================
# Multiple Lines
# ===========================================

if phone_service == "No":

    multiple_lines = "No phone service"

    st.sidebar.selectbox(
        "Multiple Lines",
        ["No phone service"],
        index=0,
        disabled=True,
        key="multiple_lines"
    )

else:

    multiple_lines = st.sidebar.selectbox(
        "Multiple Lines",
        ["No", "Yes"],
        key="multiple_lines"
    )


# ===========================================
# Internet Service
# ===========================================

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"],
    key="internet_service"
)


# ===========================================
# Online Security
# ===========================================

if internet_service == "No":

    online_security = "No internet service"

    st.sidebar.selectbox(
        "Online Security",
        ["No internet service"],
        index=0,
        disabled=True,
        key="online_security"
    )

else:

    online_security = st.sidebar.selectbox(
        "Online Security",
        ["No", "Yes"],
        key="online_security"
    )


# ===========================================
# Online Backup
# ===========================================

if internet_service == "No":

    online_backup = "No internet service"

    st.sidebar.selectbox(
        "Online Backup",
        ["No internet service"],
        index=0,
        disabled=True,
        key="online_backup"
    )

else:

    online_backup = st.sidebar.selectbox(
        "Online Backup",
        ["No", "Yes"],
        key="online_backup"
    )


# ===========================================
# Device Protection
# ===========================================

if internet_service == "No":

    device_protection = "No internet service"

    st.sidebar.selectbox(
        "Device Protection",
        ["No internet service"],
        index=0,
        disabled=True,
        key="device_protection"
    )

else:

    device_protection = st.sidebar.selectbox(
        "Device Protection",
        ["No", "Yes"],
        key="device_protection"
    )


# ===========================================
# Tech Support
# ===========================================

if internet_service == "No":

    tech_support = "No internet service"

    st.sidebar.selectbox(
        "Tech Support",
        ["No internet service"],
        index=0,
        disabled=True,
        key="tech_support"
    )

else:

    tech_support = st.sidebar.selectbox(
        "Tech Support",
        ["No", "Yes"],
        key="tech_support"
    )


# ===========================================
# Streaming TV
# ===========================================

if internet_service == "No":

    streaming_tv = "No internet service"

    st.sidebar.selectbox(
        "Streaming TV",
        ["No internet service"],
        index=0,
        disabled=True,
        key="streaming_tv"
    )

else:

    streaming_tv = st.sidebar.selectbox(
        "Streaming TV",
        ["No", "Yes"],
        key="streaming_tv"
    )


# ===========================================
# Streaming Movies
# ===========================================

if internet_service == "No":

    streaming_movies = "No internet service"

    st.sidebar.selectbox(
        "Streaming Movies",
        ["No internet service"],
        index=0,
        disabled=True,
        key="streaming_movies"
    )

else:

    streaming_movies = st.sidebar.selectbox(
        "Streaming Movies",
        ["No", "Yes"],
        key="streaming_movies"
    )


# ===========================================
# Contract
# ===========================================

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"],
    key="contract"
)


# ===========================================
# Paperless Billing
# ===========================================

paperless = st.sidebar.selectbox(
    "Paperless Billing",
    ["No", "Yes"],
    key="paperless"
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
    ],
    key="payment_method"
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


# ==========================================
# Customer Churn Prediction
# ==========================================

predict_button = st.button(
    "Predict Customer Churn"
)

if predict_button:

    # --------------------------------------
    # Make Prediction
    # --------------------------------------

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    # --------------------------------------
    # Model Prediction
    # --------------------------------------

    if prediction == 1:

        st.error(
            "⚠️ Customer is likely to churn."
        )

    else:

        st.success(
            "✅ Customer is likely to remain."
        )

    # --------------------------------------
    # Churn Probability
    # --------------------------------------

    st.metric(
        "Churn Probability",
        f"{probability:.2%}"
    )

    st.progress(float(probability))

    # --------------------------------------
    # Risk Classification
    # --------------------------------------

    if probability < 0.30:

        risk_level = "Low Churn Risk"

        recommendations = [
            "Continue current engagement.",
            "Maintain service quality.",
            "Promote premium service packages."
        ]

        st.success(
            "🟢 Low Churn Risk"
        )

    elif probability < 0.60:

        risk_level = "Medium Churn Risk"

        recommendations = [
            "Offer loyalty rewards.",
            "Schedule customer follow-up.",
            "Recommend annual contract."
        ]

        st.warning(
            "🟡 Medium Churn Risk"
        )

    else:

        risk_level = "High Churn Risk"

        recommendations = [
            "Launch an immediate retention campaign.",
            "Offer a targeted discount.",
            "Assign dedicated customer support.",
            "Contact customer within 48 hours."
        ]

        st.error(
            "🔴 High Churn Risk"
        )

    # --------------------------------------
    # Recommendations
    # --------------------------------------

    st.info("### Recommendation")

    for recommendation in recommendations:

        st.write(
            f"• {recommendation}"
        )

    # ======================================
    # PDF CUSTOMER REPORT
    # ======================================

    customer_data = {
        "Gender": gender,
        "Senior Citizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure (Months)": tenure,
        "Monthly Charges": monthly,
        "Total Charges": total,
        "Phone Service": phone_service,
        "Multiple Lines": multiple_lines,
        "Internet Service": internet_service,
        "Online Security": online_security,
        "Online Backup": online_backup,
        "Device Protection": device_protection,
        "Tech Support": tech_support,
        "Streaming TV": streaming_tv,
        "Streaming Movies": streaming_movies,
        "Contract": contract,
        "Paperless Billing": paperless,
        "Payment Method": payment_method
    }

    pdf_file = create_pdf_report(
        customer_data=customer_data,
        prediction=prediction,
        probability=probability,
        risk_level=risk_level,
        recommendations=recommendations
    )

    st.download_button(
        label="📄 Download Customer Report",
        data=pdf_file,
        file_name="customer_churn_report.pdf",
        mime="application/pdf"
    )


# ==========================================
# Model Information
# ==========================================

st.divider()

st.subheader(
    "ℹ️ Model Information"
)

col1, col2 = st.columns(2)

with col1:

    st.write(
        "**Algorithm:** Logistic Regression"
    )

    st.write(
        "**Accuracy:** 80.62%"
    )

    st.write(
        "**ROC-AUC:** 0.842"
    )


with col2:

    st.write(
        "**Dataset:** IBM Telco Customer Churn"
    )

    st.write(
        "**Training Samples:** 5,634"
    )

    st.write(
        "**Testing Samples:** 1,409"
    )


# ==========================================
# Developer Information
# ==========================================

st.divider()

st.markdown(
    """
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
"""
)