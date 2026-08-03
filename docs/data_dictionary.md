# Data Dictionary

---

## Dataset Overview

The IBM Telco Customer Churn dataset contains customer-level information collected from a telecommunications service provider.

Each row represents one customer.

The target variable is **Churn**, indicating whether the customer left the telecom service.

---

| Feature | Description | Data Type |
|----------|-------------|----------|
| customerID | Unique identifier assigned to each customer | Identifier |
| gender | Customer gender (Male/Female) | Categorical |
| SeniorCitizen | Indicates whether the customer is a senior citizen (1 = Yes, 0 = No) | Binary |
| Partner | Whether the customer has a partner | Binary |
| Dependents | Whether the customer has dependents | Binary |
| tenure | Number of months the customer has remained with the company | Numerical |
| PhoneService | Whether the customer subscribes to phone service | Binary |
| MultipleLines | Whether multiple phone lines are subscribed | Categorical |
| InternetService | Type of internet service (DSL, Fiber optic, None) | Categorical |
| OnlineSecurity | Whether online security service is subscribed | Binary |
| OnlineBackup | Whether online backup service is subscribed | Binary |
| DeviceProtection | Whether device protection service is subscribed | Binary |
| TechSupport | Whether technical support service is subscribed | Binary |
| StreamingTV | Whether streaming TV service is subscribed | Binary |
| StreamingMovies | Whether streaming movie service is subscribed | Binary |
| Contract | Customer contract type | Categorical |
| PaperlessBilling | Whether paperless billing is enabled | Binary |
| PaymentMethod | Customer payment method | Categorical |
| MonthlyCharges | Monthly subscription charges | Numerical |
| TotalCharges | Total amount paid by the customer | Numerical |
| Churn | Target variable indicating customer churn (Yes/No) | Target |