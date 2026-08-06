# 🏥 Diabetes Prediction System using Machine Learning

## 📌 Project Overview

The **Diabetes Prediction System** is a Machine Learning web application developed using **Python**, **Scikit-learn**, and **Streamlit**. The application predicts whether a patient is likely to have diabetes based on various medical parameters.

This project uses the **PIMA Indians Diabetes Dataset** and applies Machine Learning algorithms to analyze patient data and provide instant predictions through an interactive web interface.

---

# 🎯 Objectives

- Predict whether a patient has diabetes.
- Compare multiple Machine Learning algorithms.
- Select the best-performing model.
- Deploy the model using Streamlit.
- Provide a user-friendly interface for predictions.

---

# 📂 Dataset

**Dataset Name:** PIMA Indians Diabetes Dataset

### Features

| Feature | Description |
|----------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure (mm Hg) |
| SkinThickness | Triceps skin fold thickness (mm) |
| Insulin | 2-Hour serum insulin (mu U/ml) |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Genetic influence of diabetes |
| Age | Age of the patient |
| Outcome | Target Variable (0 = No Diabetes, 1 = Diabetes) |

---

# 🛠 Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

# 📊 Machine Learning Models Used

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Gaussian Naive Bayes

The model with the highest accuracy was selected for deployment.

---

# 🔄 Project Workflow

1. Data Collection
2. Data Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Data Splitting
6. Feature Scaling
7. Model Training
8. Model Evaluation
9. Model Saving
10. Streamlit Deployment

---

# 📊 Exploratory Data Analysis

EDA includes:

- Dataset Information
- Missing Value Analysis
- Correlation Heatmap
- Distribution Plots
- Count Plots
- Box Plots
- Pair Plots
- Feature Relationships

---

# ⚙ Data Preprocessing

- Removed duplicate records
- Checked missing values
- Separated features and target
- Split dataset into training and testing sets
- Applied StandardScaler

---

# 🤖 Model Training

The dataset was trained using multiple classification algorithms.

The best model was selected based on:

- Accuracy
- Precision
- Recall
- F1 Score

The trained model was saved as:

```
diabetes_model.pkl
```

The scaler was saved as:

```
scaler.pkl
```

---

# 🌐 Streamlit Application

The web application allows users to:

- Enter patient details
- Predict diabetes
- View prediction probability
- Receive health recommendations

---

# 📁 Project Structure

```
Diabetes_Prediction/
│
├── app.py
├── diabetes.csv
├── diabetes_model.pkl
├── scaler.pkl
├── requirements.txt
├── README.md
└── Diabetes_Prediction.ipynb
```

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Diabetes_Prediction.git
```

Move to the project folder

```bash
cd Diabetes_Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

The application opens at:

```
http://localhost:8501
```

---

# 📈 Model Evaluation

Evaluation metrics used:

- Accuracy Score
- Precision Score
- Recall Score
- F1 Score
- Confusion Matrix
- Classification Report
- ROC-AUC Score

---

# 📊 Sample Input

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

# 📌 Sample Output

```
Prediction:
Patient is NOT likely to have Diabetes.

Probability:
82.45%
```

or

```
Prediction:
Patient is likely to have Diabetes.

Probability:
91.76%
```

---

# 🚀 Future Enhancements

- User Login System
- Prediction History
- PDF Report Generation
- Email Report Feature
- Cloud Deployment
- Mobile Responsive Design
- Interactive Charts
- Doctor Recommendation System

---

# 🎓 Learning Outcomes

This project helped in understanding:

- Machine Learning Classification
- Data Preprocessing
- Feature Scaling
- Model Evaluation
- Model Deployment
- Streamlit Development
- Real-Time Prediction Systems

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

# 👩‍💻 Developed By

**Name:** Sinchana Suresh

Department of Artificial Intelligence and Machine Learning

Academic Project

---

# ⭐ Conclusion

The Diabetes Prediction System demonstrates how Machine Learning can assist in the early detection of diabetes by analyzing patient health parameters. It provides a fast, simple, and user-friendly interface for prediction while showcasing practical skills in data preprocessing, model training, evaluation, and deployment using Streamlit.
