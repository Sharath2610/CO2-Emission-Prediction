# 🚗 CO₂ Emission Prediction Using Machine Learning

### 📌 Overview

This project predicts the CO₂ emissions (g/km) of vehicles using machine learning based on engine specifications and fuel consumption data. It helps environmental teams, automobile manufacturers, and researchers estimate emission levels and support sustainability-focused decisions.

---

## 🧠 Problem Statement

With rising climate concerns and government regulations, predicting vehicle CO₂ emissions accurately is essential.  
This project builds an ML model capable of forecasting emission output based on vehicle specifications.

---

## 📂 Dataset Information

| Detail          | Value           |
| --------------- | --------------- |
| Total Rows      | **7385**        |
| Total Columns   | **12**          |
| Target Variable | `co2_emissions` |

### Example Features

- Engine Size
- Cylinders
- Transmission Type
- Fuel Type
- City/Highway Fuel Consumption
- Vehicle Class

_A detailed Exploratory Data Analysis (EDA) is included in the notebook._

---

## 🔍 Project Workflow

1. **Data Loading & Cleaning**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Encoding and Processing**
4. **Model Selection & Training**
5. **Model Evaluation**
6. **Saving Model using Joblib**
7. **Deployment using Streamlit**

---

## 🛠️ Technologies Used

| Category            | Tools               |
| ------------------- | ------------------- |
| Language            | Python              |
| ML Framework        | Scikit-learn        |
| Data Handling       | Pandas, NumPy       |
| Visualization       | Matplotlib, Seaborn |
| Deployment          | Streamlit           |
| Model Serialization | Joblib              |
| Version Control     | Git & GitHub        |

---

## 🤖 Model Used

| Model                   | Description                                |
| ----------------------- | ------------------------------------------ |
| Random Forest Regressor | Final trained ML model used for prediction |

---

## 📈 Model Performance

> Values will be updated once metrics are finalized.

| Metric   | Score         |
| -------- | ------------- |
| R² Score | _To be added_ |
| RMSE     | _To be added_ |
| MAE      | _To be added_ |

---

## 🧪 Example Prediction

| Input                                     | Output          |
| ----------------------------------------- | --------------- |
| (Engine Size, Fuel Type, Cylinders, etc.) | **167.10 g/km** |

---

## 🚀 Deployment Status

| Component            | Status                 |
| -------------------- | ---------------------- |
| Local Model Training | ✔ Completed            |
| Streamlit App        | ✔ Running Successfully |
| Hosted Deployment    | ⏳ Coming Soon         |

---

## 📁 Project Structure

```
CO2-Emission-Prediction
│── app.py
│── requirements.txt
│── README.md
│── co2_emissions.csv
│
└── notebooks
     │── model_training.ipynb
     │── co2_model.pkl
```

---

## 📌 How to Run This Project Locally

```bash
# Clone the repository
git clone <repository-link>

# Go to project folder
cd CO2-Emission-Prediction

# Install required libraries
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---

## 👨‍💻 Author

**Sharath R**  
📍 India  
_Data Science Project_

---
