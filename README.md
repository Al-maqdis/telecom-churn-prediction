# 📊 Customer Churn Prediction System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20Application-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 🚀 Project Overview

Customer churn is a major challenge for telecommunications companies. Losing customers affects recurring revenue and increases the cost of acquiring new customers.

The **Customer Churn Prediction System** is an end-to-end Machine Learning application designed to predict whether a telecommunications customer is likely to churn.

The system uses customer demographic information, account details, subscribed services, contract information, and billing history to estimate the probability of customer churn.

Beyond prediction, the system converts the Machine Learning output into:

- Churn probability
- Customer risk level
- Recommended retention actions
- Downloadable customer churn report

The project covers the complete Machine Learning lifecycle, from business understanding and data preprocessing to model evaluation and deployment.

---

## 🚀 Live Demo

**Try the deployed application:**

👉 https://hybeek-telecom-churn.streamlit.app/

The deployed application allows users to:

- Enter customer information
- Generate a churn prediction
- View churn probability
- Identify customer risk level
- Receive recommended retention actions
- Generate a downloadable PDF report

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Understand the telecommunications customer churn problem.
- Explore and clean customer data.
- Perform exploratory data analysis.
- Engineer and transform relevant features.
- Train multiple Machine Learning classification models.
- Compare model performance using appropriate evaluation metrics.
- Analyse classification thresholds.
- Select an interpretable model for deployment.
- Develop an interactive prediction application.
- Provide actionable customer retention recommendations.

---

## 📂 Dataset

### Source

**IBM Telco Customer Churn Dataset**

### Dataset Size

**7,043 customers**

### Target Variable

**Churn**

The target variable indicates whether a customer discontinued the telecommunications service.

### Main Feature Categories

- Customer demographics
- Customer account information
- Phone services
- Internet services
- Security and support services
- Streaming services
- Contract information
- Billing information
- Payment methods

---

## 🏗️ Machine Learning Workflow

The project follows a structured end-to-end Machine Learning workflow:

```text
Business Understanding
        │
        ▼
Data Understanding
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
Encoding & Scaling
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
Threshold Analysis
        │
        ▼
Model Selection
        │
        ▼
Application Development
        │
        ▼
Cloud Deployment
        │
        ▼
Customer Churn Prediction
````

---

## 🤖 Models Evaluated

Several classification algorithms were evaluated during the project.

| Model                   |   Accuracy |   ROC-AUC |
| ----------------------- | ---------: | --------: |
| **Logistic Regression** | **80.62%** |     0.842 |
| Decision Tree           |     79.42% |     0.827 |
| Random Forest           |     80.48% | **0.844** |
| XGBoost                 |     79.63% |     0.842 |

---

## 🏆 Selected Model: Logistic Regression

The deployed model is **Logistic Regression**.

Random Forest achieved a marginally higher ROC-AUC score, but Logistic Regression was selected because it provides a strong balance between predictive performance, interpretability, computational efficiency, and ease of deployment.

### Reasons for selecting Logistic Regression

* Strong predictive performance
* High interpretability
* Fast prediction
* Efficient computational requirements
* Easy deployment
* Coefficients can be interpreted as churn risk factors
* Suitable for explaining predictions to business stakeholders

The model therefore provides not only predictions, but also a more understandable basis for customer retention decisions.

---

## 📊 Model Performance

The final model achieved the following results on the test dataset:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **80.62%** |
| Precision | **65.93%** |
| Recall    | **55.88%** |
| F1-Score  | **60.49%** |
| ROC-AUC   |  **0.842** |

### Dataset Split

| Dataset  | Samples |
| -------- | ------: |
| Training |   5,634 |
| Testing  |   1,409 |

---

## 🎚️ Classification Threshold Analysis

The project also investigated different classification thresholds rather than relying only on the default 50% probability threshold.

The analysis showed a trade-off between precision and recall.

| Threshold |  Precision |     Recall |   F1-Score | Customers Flagged |
| --------: | ---------: | ---------: | ---------: | ----------------: |
|       25% |     49.84% | **81.02%** | **61.71%** |               608 |
|       40% |     56.95% |     66.84% |     61.50% |               439 |
|       50% | **65.93%** |     55.88% |     60.49% |               317 |

This analysis demonstrates that the choice of classification threshold should depend on the business objective.

For example:

* A lower threshold can identify more potentially at-risk customers.
* A higher threshold can reduce the number of customers targeted by retention campaigns.
* The appropriate threshold depends on the relative cost of false positives and false negatives.

---

## 🔍 Model Interpretation

Because Logistic Regression is an interpretable model, its coefficients were analysed to understand factors associated with customer churn.

### Important Churn Risk Factors

The analysis identified factors such as:

* Higher total charges
* Fiber optic internet service
* Streaming TV subscription
* Streaming Movies subscription
* Paperless billing
* Electronic check payment

### Important Protective Factors

Factors associated with lower predicted churn included:

* Longer customer tenure
* Two-year contracts
* One-year contracts
* Lower monthly charges
* Phone service
* Online security
* Technical support

These insights help transform the Machine Learning model from a simple prediction tool into a potential customer retention decision-support system.

---

## 🖥️ Application Features

The Streamlit application provides an interactive interface for customer churn analysis.

### Customer Input

Users can provide:

* Gender
* Senior citizen status
* Partner status
* Dependents
* Tenure
* Monthly charges
* Total charges
* Phone service
* Multiple lines
* Internet service
* Online security
* Online backup
* Device protection
* Technical support
* Streaming TV
* Streaming movies
* Contract
* Paperless billing
* Payment method

The interface also includes conditional controls.

For example:

* If **Phone Service = No**, Multiple Lines is automatically set to **No phone service**.
* If **Internet Service = No**, internet-dependent services are automatically set to **No internet service**.

This helps maintain valid input combinations consistent with the dataset.

---

## 🎯 Prediction Output

After submitting a customer record, the system provides:

### 1. Churn Prediction

The system predicts whether the customer is likely to:

* Remain
* Churn

### 2. Churn Probability

The model provides a probability estimate such as:

```text
Churn Probability: 61.52%
```

### 3. Risk Classification

Customers are classified into:

```text
Low Churn Risk
Medium Churn Risk
High Churn Risk
```

### 4. Recommended Action

The system provides business-oriented recommendations based on the predicted risk.

For example, high-risk customers may receive recommendations such as:

* Launch an immediate retention campaign
* Offer a targeted discount
* Assign dedicated customer support
* Contact the customer within 48 hours

---

## 📄 Customer Churn PDF Report

The application can generate a downloadable PDF report containing:

* Prediction result
* Churn probability
* Risk level
* Customer information
* Recommended action
* Model information
* Model performance metrics

This makes the system more practical for communicating predictions to business users.

---

## 💻 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit
* ReportLab
* Jupyter Notebook

---

## 📁 Project Structure

```text
telecom-churn-prediction/

├── .github/
│   └── workflows/
│
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
│   └── figures/
│       └── screenshots/
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

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Al-maqdis/telecom-churn-prediction.git
```

### 2. Move into the project directory

```bash
cd telecom-churn-prediction
```

### 3. Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app/app.py
```

---

## 📸 Application Preview

### Home Page

![Home](reports/figures/screenshots/home_page.png)

---

### Low Churn Risk

![Low Risk](reports/figures/screenshots/prediction_low_risk.jpg)

---

### Medium Churn Risk

![Medium Risk](reports/figures/screenshots/prediction_medium_risk.jpg)

---

### High Churn Risk

![High Risk](reports/figures/screenshots/prediction_high_risk.jpg)

---

### Processed Customer Record

![Processed](reports/figures/screenshots/processed_features.jpg)

---

## 📈 Project Deliverables

This project delivers:

* End-to-end Machine Learning pipeline
* Exploratory Data Analysis
* Data preprocessing
* Feature engineering
* Multiple model comparison
* Model evaluation
* Confusion matrix analysis
* ROC-AUC analysis
* Classification threshold analysis
* Model feature interpretation
* Interactive Streamlit application
* Customer risk classification
* Retention recommendations
* Downloadable PDF customer report
* Public cloud deployment
* Complete project documentation

---

## 🔮 Future Improvements

Potential future improvements include:

* Hyperparameter optimization
* SHAP-based explainable AI
* Docker containerization
* FastAPI backend
* Automated CI/CD pipeline
* Database integration
* Customer-level monitoring
* Model retraining pipeline
* Advanced customer segmentation
* Cost-sensitive threshold optimization

---

## 👨‍💻 Author

### HyBeek

**Machine Learning | Data Science | Python Developer**

Customer Churn Prediction System

---

## 📜 License

This project is licensed under the MIT License.

````



