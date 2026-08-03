<div align="center">

# 🏥 Diabetes Prediction Analysis



<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn">
  <img src="https://img.shields.io/badge/Streamlit-Web%20Application-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy">
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">
</p>

---

### 🏥 Diabetes Prediction Dashboard

> A Machine Learning web application that predicts the likelihood of diabetes based on patient health information using the **PIMA Indians Diabetes Dataset**.

</div>

---

# 📑 Table of Contents

- 📌 Project Overview
- 🎯 Objectives
- 📂 Dataset
- 🛠 Technologies Used
- 🔄 Project Workflow
- 📊 Exploratory Data Analysis
- 🤖 Machine Learning Models
- 📈 Model Evaluation
- 🌐 Streamlit Web Application
- 📸 Project Screenshots
- 📁 Folder Structure
- 🚀 Installation Guide
- ▶️ How to Run
- 📊 Sample Prediction
- 🚀 Future Enhancements
- 👨‍💻 Author
- 📚 References

---

# 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early diagnosis can help reduce serious complications.

This project uses **Machine Learning** to predict whether a patient is likely to have diabetes based on medical attributes such as:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

The trained model is deployed using **Streamlit**, providing an interactive web interface for predictions.

---

# 🎯 Objectives

- Predict diabetes using Machine Learning
- Analyze the PIMA Diabetes Dataset
- Compare multiple ML algorithms
- Select the best-performing model
- Deploy the model with Streamlit
- Build an interactive web application

---

# 📂 Dataset

**Dataset:** PIMA Indians Diabetes Dataset

| Feature | Description |
|----------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Skin fold thickness |
| Insulin | Serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes family history |
| Age | Patient age |
| Outcome | 0 = No Diabetes, 1 = Diabetes |

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Google Colab | Model Development |
| Pandas | Data Processing |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Graphs |
| Scikit-learn | Machine Learning |
| Joblib | Model Saving |
| Streamlit | Web Application |
| Git | Version Control |
| GitHub | Project Hosting |

---

# 🔄 Project Workflow

```text
          PIMA Diabetes Dataset
                    │
                    ▼
         Data Preprocessing
                    │
                    ▼
     Exploratory Data Analysis
                    │
                    ▼
       Feature Selection
                    │
                    ▼
      Train-Test Split (80:20)
                    │
                    ▼
      Standard Feature Scaling
                    │
                    ▼
    Machine Learning Algorithms
                    │
                    ▼
       Model Evaluation
                    │
                    ▼
      Best Model Selection
                    │
                    ▼
 Save Model (.pkl) using Joblib
                    │
                    ▼
     Streamlit Web Application
                    │
                    ▼
      Diabetes Prediction
```

---

# 📊 Exploratory Data Analysis

Performed the following analyses:

- Dataset Information
- Missing Value Analysis
- Duplicate Record Check
- Correlation Heatmap
- Histograms
- Box Plots
- Count Plots
- Pair Plots
- Feature Distribution

---

# 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gaussian Naive Bayes

The **Random Forest Classifier** achieved the best performance and was selected for deployment.

---

# 📈 Model Evaluation

Evaluation Metrics:

- Accuracy Score
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report
- ROC-AUC Score

---

# 🌐 Streamlit Web Application

### Features

✅ Interactive User Interface

✅ Real-Time Prediction

✅ Diabetes Probability

✅ User-Friendly Dashboard

✅ Fast Prediction

---

# 📁 Folder Structure

```text
Diabetes_Prediction/
│
├── app.py
├── Diabetes_Prediction.ipynb
├── diabetes.csv
├── diabetes_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md

---

# 🚀 Installation Guide

## Clone Repository

```bash
git clone https://github.com/sinchanasuresh0210/Diabetes-Prediction-Analysis.git
```

---

## Open Project

```bash
cd Diabetes-Prediction-Analysis
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

---

Application URL

```text
http://localhost:8501
```

---

# 📊 Sample Prediction

### Sample Input

| Feature | Value |
|----------|------:|
| Pregnancies | 2 |
| Glucose | 120 |
| Blood Pressure | 70 |
| Skin Thickness | 20 |
| Insulin | 80 |
| BMI | 28.5 |
| Diabetes Pedigree Function | 0.45 |
| Age | 35 |

---

### Sample Output

```text
Prediction

✅ Patient is NOT likely to have Diabetes

Probability

82.45%
```

or

```text
Prediction

⚠ Patient is likely to have Diabetes

Probability

91.76%
```

---

# 🚀 Future Enhancements

- User Authentication
- Cloud Deployment
- PDF Report Generation
- Email Prediction Report
- Patient Database
- Doctor Recommendation
- Mobile Application
- Explainable AI (SHAP/LIME)

---

# 🎓 Learning Outcomes

This project demonstrates:

- Machine Learning Classification
- Data Preprocessing
- Feature Scaling
- Exploratory Data Analysis
- Model Training
- Model Evaluation
- Model Deployment
- Streamlit Development
- Git & GitHub Version Control

---

# 👨‍💻 Author

**Name:** Sinchana G.S

🎓 Department of Artificial Intelligence


📧 GitHub: https://github.com/sinchanasuresh0210

---

# 📚 References

- PIMA Indians Diabetes Dataset
- Scikit-learn Documentation
- Streamlit Documentation
- Pandas Documentation
- NumPy Documentation
- Matplotlib Documentation
- Seaborn Documentation

---

# ✅ Conclusion


The Diabetes Prediction System is an end-to-end Machine Learning application that predicts the risk of diabetes using patient medical data. By combining data analysis, machine learning, and a Streamlit web interface, the project provides accurate, fast, and user-friendly predictions. It demonstrates how AI can support early disease detection and showcases practical skills in data science, model deployment, and web application development.




