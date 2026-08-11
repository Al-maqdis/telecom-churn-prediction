# 📊 Customer Churn Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 🚀 Project Overview

Customer churn is one of the biggest challenges facing telecommunication companies. Retaining an existing customer is significantly less expensive than acquiring a new one.

This project develops an end-to-end Machine Learning solution capable of predicting whether a customer is likely to discontinue a telecommunications service based on demographic information, account details, subscribed services, and billing history.

The project covers the complete Machine Learning lifecycle—from business understanding and data preprocessing to model deployment through a Streamlit web application.

---

## 🎯 Objectives

- Understand the customer churn problem.
- Explore and clean the dataset.
- Engineer useful features.
- Train multiple Machine Learning models.
- Compare model performance.
- Deploy the best-performing model.
- Provide an interactive prediction dashboard.

---

## 📂 Dataset

**Source**

IBM Telco Customer Churn Dataset

**Records**

7,043 Customers

**Target Variable**

- Churn

**Features**

- Customer demographics
- Service subscriptions
- Internet services
- Contract information
- Billing information
- Payment methods

---

## 🏗 Machine Learning Workflow

```
Business Understanding
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Feature Scaling
        │
        ▼
Train/Test Split
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Model Comparison
        │
        ▼
Model Deployment
```

---

## 🤖 Models Evaluated

| Model | Accuracy | ROC-AUC |
|-------|---------:|---------:|
| Logistic Regression | **80.62%** | 0.842 |
| Decision Tree | 79.42% | 0.827 |
| Random Forest | 80.48% | **0.844** |
| XGBoost | 79.63% | 0.842 |

---

## 🏆 Selected Model

The deployed model is **Logistic Regression** because it provides:

- Excellent predictive performance
- High interpretability
- Fast prediction speed
- Simple deployment
- Easy business explanation

Although Random Forest achieved a slightly higher ROC-AUC score, Logistic Regression offered the best balance between performance and interpretability.

---

## 📊 Key Results

- Accuracy: **80.62%**
- ROC-AUC Score: **0.842**
- Training Samples: **5,634**
- Testing Samples: **1,409**

---

## 💻 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- XGBoost
- Joblib
- Streamlit

---

## 📁 Project Structure

```text
telecom-churn-prediction/

├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
├── docs/
│
├── models/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_exploratory_data_analysis.ipynb
│   └── 03_data_preprocessing.ipynb
│
├── reports/
│
├── src/
│
├── tests/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/HYBEEK/telecom-churn-prediction.git
```

Move into the project

```bash
cd telecom-churn-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app/app.py
```

---

## 📸 Application Preview

### Home Page

![Home](reports/figures/screenshots/home_page.png)

---

### Low Churn Prediction

![Low Risk](reports/figures/screenshots/prediction_low_risk.jpg)

---

### Medium Churn Prediction

![Medium Risk](reports/figures/screenshots/prediction_medium_risk.jpg)

---

### High Churn Prediction

![High Risk](reports/figures/screenshots/prediction_high_risk.jpg)

---

### Processed Customer Record

![Processed](reports/figures/screenshots/processed_features.jpg)

---

## 🔮 Future Improvements

- Hyperparameter tuning
- SHAP Explainability
- Docker Containerization
- FastAPI Backend
- CI/CD Pipeline
- Cloud Deployment
- Database Integration

---

## 👨‍💻 Author

**HyBeek**

Machine Learning | Data Science | Python Developer

---

## 📜 License

This project is licensed under the MIT License.
