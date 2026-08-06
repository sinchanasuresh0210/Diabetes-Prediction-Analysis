import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="AI Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("diabetes_model.pkl")
    scaler = joblib.load("scaler.pkl")
    return model, scaler

try:
    model, scaler = load_model()
except:
    st.error("Model files not found.")
    st.stop()

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#0f172a,#1e293b);
color:white;
}

.big-title{
font-size:48px;
font-weight:bold;
text-align:center;
color:white;
}

.subtitle{
text-align:center;
font-size:20px;
color:#cbd5e1;
}

.box{
background:#1e293b;
padding:20px;
border-radius:15px;
box-shadow:0px 0px 15px rgba(0,0,0,.3);
}

div.stButton > button{
background:#2563eb;
color:white;
font-size:20px;
font-weight:bold;
width:100%;
height:60px;
border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/387/387561.png",
        width=120
    )

    st.title("Clinical AI")

    st.markdown("---")

    st.success("Random Forest Classifier")

    st.info("""
Features Used

✔ Pregnancies

✔ Glucose

✔ Blood Pressure

✔ Skin Thickness

✔ Insulin

✔ BMI

✔ DPF

✔ Age
""")

    st.markdown("---")

    st.warning(
        "This application is only for educational purposes."
    )

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
"""
<h1 class='big-title'>
🩺 Diabetes Prediction System
</h1>

<p class='subtitle'>
Machine Learning Based Clinical Decision Support System
</p>
""",
unsafe_allow_html=True
)

# --------------------------------------------------
# FEATURE CARDS
# --------------------------------------------------

c1,c2,c3,c4=st.columns(4)

c1.metric("Model","Random Forest")
c2.metric("Features","8")
c3.metric("Accuracy","High")
c4.metric("Prediction","Instant")

st.write("")

# --------------------------------------------------
# INPUT FORM
# --------------------------------------------------

st.header("Patient Information")

with st.form("form"):

    left,right=st.columns(2)

    with left:

        pregnancies=st.number_input(
            "Pregnancies",
            0,
            20,
            1
        )

        glucose=st.number_input(
            "Glucose",
            0,
            300,
            120
        )

        blood_pressure=st.number_input(
            "Blood Pressure",
            0,
            180,
            70
        )

        skin=st.number_input(
            "Skin Thickness",
            0,
            100,
            20
        )

    with right:

        insulin=st.number_input(
            "Insulin",
            0,
            900,
            80
        )

        bmi=st.number_input(
            "BMI",
            0.0,
            70.0,
            25.0
        )

        dpf=st.number_input(
            "Diabetes Pedigree Function",
            0.0,
            3.0,
            0.47
        )

        age=st.number_input(
            "Age",
            1,
            120,
            33
        )

    predict=st.form_submit_button(
        "Predict Diabetes"
    )
    # --------------------------------------------------
# PREDICTION
# --------------------------------------------------

if predict:

    input_data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin,
        insulin,
        bmi,
        dpf,
        age
    ]])

    scaled = scaler.transform(input_data)

    prediction = model.predict(scaled)[0]

    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(scaled)[0][1] * 100
    else:
        probability = 100 if prediction == 1 else 0

    st.markdown("---")
    st.header("📊 AI Prediction Result")

    col1, col2 = st.columns(2)

    # -----------------------------------------
    # Prediction Card
    # -----------------------------------------

    with col1:

        if prediction == 1:
            st.error("🚨 Diabetes Detected")
        else:
            st.success("✅ No Diabetes Detected")

        st.metric(
            "Risk Probability",
            f"{probability:.2f}%"
        )

        st.progress(int(probability))

    # -----------------------------------------
    # Gauge Meter
    # -----------------------------------------

    with col2:

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability,

            title={
                "text":"Diabetes Risk (%)"
            },

            gauge={
                "axis":{
                    "range":[0,100]
                },

                "bar":{
                    "color":"red"
                },

                "steps":[
                    {
                        "range":[0,30],
                        "color":"green"
                    },
                    {
                        "range":[30,70],
                        "color":"yellow"
                    },
                    {
                        "range":[70,100],
                        "color":"red"
                    }
                ]
            }
        ))

        fig.update_layout(height=350)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# --------------------------------------------------
# RISK CATEGORY
# --------------------------------------------------

    st.markdown("---")

    st.header("Risk Assessment")

    if probability < 30:

        st.success("🟢 LOW RISK")

        st.write("""
Your health parameters indicate a **low probability** of diabetes.

Continue maintaining a healthy lifestyle.
""")

    elif probability < 70:

        st.warning("🟡 MODERATE RISK")

        st.write("""
Your health parameters indicate a **moderate probability** of diabetes.

Lifestyle improvements and regular checkups are recommended.
""")

    else:

        st.error("🔴 HIGH RISK")

        st.write("""
Your health parameters indicate a **high probability** of diabetes.

Please consult a healthcare professional as soon as possible.
""")

# --------------------------------------------------
# AI SUMMARY
# --------------------------------------------------

    st.markdown("---")

    st.subheader("🤖 AI Clinical Summary")

    summary = f"""

Prediction : {"Positive" if prediction==1 else "Negative"}

Risk Percentage : {probability:.2f}%

Glucose : {glucose}

Blood Pressure : {blood_pressure}

BMI : {bmi}

Age : {age}

Insulin : {insulin}

Diabetes Pedigree Function : {dpf}

"""

    st.code(summary)

# --------------------------------------------------
# RISK SCORE CARD
# --------------------------------------------------

    st.subheader("Overall Risk Score")

    score = round(probability)

    if score < 30:

        color = "green"

    elif score < 70:

        color = "orange"

    else:

        color = "red"

    st.markdown(
        f"""
        <h2 style='text-align:center;color:{color};'>
        {score}/100
        </h2>
        """,
        unsafe_allow_html=True
    )
    # --------------------------------------------------
# HEALTH PARAMETER ANALYSIS
# --------------------------------------------------

    st.markdown("---")
    st.header("🩺 Health Parameter Analysis")

    # ---------------- Glucose ----------------
    if glucose < 100:
        st.success("✅ Glucose Level: Normal")
    elif glucose <= 125:
        st.warning("⚠️ Glucose Level: Prediabetes Range")
    else:
        st.error("🚨 Glucose Level: Diabetes Range")

    # ---------------- Blood Pressure ----------------
    if blood_pressure < 80:
        st.success("✅ Blood Pressure: Normal")
    elif blood_pressure <= 89:
        st.warning("⚠️ Blood Pressure: Slightly High")
    else:
        st.error("🚨 Blood Pressure: High")

    # ---------------- BMI ----------------
    if bmi < 18.5:
        st.info("📉 BMI: Underweight")
    elif bmi < 25:
        st.success("✅ BMI: Normal Weight")
    elif bmi < 30:
        st.warning("⚠️ BMI: Overweight")
    else:
        st.error("🚨 BMI: Obese")

    # ---------------- Age ----------------
    if age < 40:
        st.success("✅ Age Risk: Low")
    elif age < 60:
        st.warning("⚠️ Age Risk: Moderate")
    else:
        st.error("🚨 Age Risk: High")

    # ---------------- Insulin ----------------
    if insulin < 25:
        st.warning("⚠️ Insulin: Lower than Normal")
    elif insulin <= 166:
        st.success("✅ Insulin: Normal")
    else:
        st.error("🚨 Insulin: High")

    # ---------------- Diabetes Pedigree Function ----------------
    if dpf < 0.5:
        st.success("✅ Family History Risk: Low")
    elif dpf < 1:
        st.warning("⚠️ Family History Risk: Moderate")
    else:
        st.error("🚨 Family History Risk: High")

# --------------------------------------------------
# PERSONALIZED RECOMMENDATIONS
# --------------------------------------------------

    st.markdown("---")
    st.header("💡 Personalized Recommendations")

    if probability < 30:

        st.success("""
### 🟢 Low Risk

✔ Continue regular exercise

✔ Maintain healthy body weight

✔ Drink enough water

✔ Eat fruits and vegetables

✔ Avoid excessive sugar intake

✔ Annual health checkup recommended
""")

    elif probability < 70:

        st.warning("""
### 🟡 Moderate Risk

✔ Reduce sugar and processed foods

✔ Walk at least 30 minutes daily

✔ Increase fiber intake

✔ Maintain healthy BMI

✔ Monitor blood glucose regularly

✔ Consult a physician if symptoms appear
""")

    else:

        st.error("""
### 🔴 High Risk

✔ Consult a diabetologist immediately

✔ Get HbA1c Test

✔ Get Fasting Blood Sugar Test

✔ Follow prescribed medications

✔ Reduce carbohydrate intake

✔ Daily exercise under medical supervision

✔ Monitor blood glucose frequently
""")

# --------------------------------------------------
# LIFESTYLE SUGGESTIONS
# --------------------------------------------------

    st.markdown("---")
    st.header("🏃 Healthy Lifestyle Suggestions")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🥗 Diet")

        st.write("""
• Whole grains

• Green vegetables

• Fruits

• Lean protein

• Nuts

• Plenty of water
""")

    with col2:

        st.subheader("🚫 Avoid")

        st.write("""
• Sugary drinks

• White bread

• Cakes

• Junk food

• Smoking

• Alcohol
""")

# --------------------------------------------------
# FINAL HEALTH SUMMARY
# --------------------------------------------------

    st.markdown("---")
    st.header("📋 Final Health Summary")

    if probability < 30:

        st.success("""
## Excellent

Your health parameters suggest a **Low Diabetes Risk**.

Maintain your healthy lifestyle and continue annual health checkups.
""")

    elif probability < 70:

        st.warning("""
## Moderate Risk

Some health parameters require attention.

Lifestyle modifications and periodic monitoring are recommended.
""")

    else:

        st.error("""
## High Risk

The AI model predicts a high probability of diabetes.

Please consult a healthcare professional as soon as possible for further evaluation.
""")
        # --------------------------------------------------
# HEALTH METRICS VISUALIZATION
# --------------------------------------------------

    st.markdown("---")
    st.header("📊 Health Metrics Overview")

    chart_data = pd.DataFrame({
        "Parameter": [
            "Glucose",
            "Blood Pressure",
            "Skin Thickness",
            "Insulin",
            "BMI",
            "Age"
        ],
        "Value": [
            glucose,
            blood_pressure,
            skin,
            insulin,
            bmi,
            age
        ]
    })

    st.bar_chart(
        chart_data.set_index("Parameter")
    )

# --------------------------------------------------
# PREDICTION HISTORY
# --------------------------------------------------

    if "history" not in st.session_state:
        st.session_state.history = []

    history_record = {
        "Date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Prediction": "Positive" if prediction == 1 else "Negative",
        "Risk (%)": round(probability, 2),
        "Glucose": glucose,
        "BMI": bmi,
        "Age": age
    }

    st.session_state.history.append(history_record)

    st.markdown("---")
    st.header("📋 Prediction History")

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True
    )

# --------------------------------------------------
# DOWNLOAD REPORT
# --------------------------------------------------

    csv = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction Report (CSV)",
        data=csv,
        file_name="diabetes_prediction_report.csv",
        mime="text/csv"
    )

# --------------------------------------------------
# RESET BUTTON
# --------------------------------------------------

    st.markdown("---")

    if st.button("🔄 Clear Prediction History"):
        st.session_state.history = []
        st.success("Prediction history cleared successfully!")

# --------------------------------------------------
# DISCLAIMER
# --------------------------------------------------

st.markdown("---")

st.info("""
### ⚠ Medical Disclaimer

This application is intended **only for educational and demonstration purposes**.

The prediction is generated using a Machine Learning model trained on the PIMA Indians Diabetes Dataset and **must not be considered a medical diagnosis**.

Always consult a qualified healthcare professional for proper diagnosis and treatment.
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown(
"""
<div style='text-align:center'>

<h4>🩺 AI Diabetes Prediction System</h4>

Developed using

✅ Python

✅ Streamlit

✅ Scikit-Learn

✅ Random Forest Classifier

✅ Plotly

<hr>

<b>Developed by:</b> Sinchana Suresh

</div>
""",
unsafe_allow_html=True
)
