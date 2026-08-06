import os
import joblib
import numpy as np

print("Current Folder:", os.getcwd())
print("Files:", os.listdir())

model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("scaler (1).pkl")   # Change to scaler.pkl if you rename the file

new_patient = np.array([[2, 120, 70, 20, 80, 28.5, 0.45, 35]])

new_patient_scaled = scaler.transform(new_patient)

prediction = model.predict(new_patient_scaled)

print("Prediction:", prediction)

if prediction[0] == 1:
    print("The patient is predicted to have Diabetes.")
else:
    print("The patient is predicted NOT to have Diabetes.")