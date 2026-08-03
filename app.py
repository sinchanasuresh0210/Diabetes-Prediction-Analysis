import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ---------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="AI Health Analytics | Diabetes Risk",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# 2. MODEL LOADING (WITH CACHING & ERROR HANDLING)
# ---------------------------------------------------
@st.cache_resource
def load_assets():
    try:
        model = joblib.load("diabetes_model.pkl")
        scaler = joblib.load("scaler.pkl")
        return model, scaler
    except Exception as e:
        return None, None

model, scaler = load_assets()

# ---------------------------------------------------
# 3. CUSTOM CSS FOR MODERN UI
# ---------------------------------------------------
st.markdown("""
<style>
    /* Gradient Background & Fonts */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
    }
    
    /* Hero Banner */
    .hero-container {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 50%, #06b6d4 100%);
        padding: 2.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
        margin-bottom: 2rem;
    }
    .hero-container h1 {
        font-size: 2.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    /* Cards */
    .feature-card {
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1.2rem;
        border-radius: 15px;
        text-align: center;
        backdrop-filter: blur(10px);
    }
    
    /* Input Container Styling */
    .input-box {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1.5rem;
        border-radius: 16px;
        margin-bottom: 1rem;
    }

    /* Custom Submit Button */
    div.stButton > button {
        background: linear-gradient(90deg, #06b6d4 0%, #3b82f6 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        border: none;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5);
    }

    /* Sidebar Customization */
    [data-testid="stSidebar"] {
        background-color: rgba(15, 23, 42, 0.95);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# 4. SIDEBAR NAVIGATION & INFO
# ---------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/387/387561.png", width=110)
    st.title("Clinical AI Assistant")
    st.caption("Powered by Machine Learning")
    
    st.markdown("---")
    st.markdown("### 📊 Model Architecture")
    st.info("""
    * **Algorithm:** Random Forest
    * **Input Features:** 8 Health Metrics
    * **Preprocessing:** StandardScaler
    """)
    
    st.markdown("---")
    st.warning("⚠️ **Disclaimer:** This tool is designed for educational/screening purposes and should not replace clinical diagnosis.")

# ---------------------------------------------------
# 5. HERO HEADER
# ---------------------------------------------------
st.markdown("""
<div class="hero-container">
    <h1>🩺 Diabetes Prediction Analysis</h1>
    <p>Provide the clinical data below to get an instant AI evaluation and tailored health analysis.</p>
</div>
""", unsafe_allow_html=True)

# Feature Highlights
col_a, col_b, col_c, col_d = st.columns(4)
col_a.markdown('<div class="feature-card">⚡ <b>Instant Analysis</b></div>', unsafe_allow_html=True)
col_b.markdown('<div class="feature-card">🎯 <b>High Precision</b></div>', unsafe_allow_html=True)
col_c.markdown('<div class="feature-card">🔒 <b>Private & Secure</b></div>', unsafe_allow_html=True)
col_d.markdown('<div class="feature-card">📈 <b>Risk Scoring</b></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# Check if models exist
if model is None or scaler is None:
    st.error("🚨 Model or Scaler files (`diabetes_model.pkl`, `scaler.pkl`) not found in the current directory. Please make sure both files are saved next to `app.py`.")
    st.stop()

# ---------------------------------------------------
# 6. PATIENT INPUT FORM
# ---------------------------------------------------
st.markdown("### 📝 Patient Health Metrics")

with st.form("prediction_form"):
    col1, col2 = st.columns(2, gap="medium")
    
    with col1:
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=1, step=1)
        glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=300, value=120)
        blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=0, max_value=180, value=70)
        skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="input-box">', unsafe_allow_html=True)
        insulin = st.number_input("Insulin Level (mu U/ml)", min_value=0, max_value=900, value=80)
        bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.47, step=0.01)
        age = st.number_input("Age (Years)", min_value=1, max_value=120, value=33, step=1)
        st.markdown('</div>', unsafe_allow_html=True)

    submit_btn = st.form_submit_button("🔍 Evaluate Diabetes Risk")

# ---------------------------------------------------
# 7. PREDICTION & RESULTS DISPLAY
# ---------------------------------------------------
if submit_btn:
    # Prepare input data array
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    
    # Scale input data
    scaled_data = scaler.transform(input_data)
    
    # Make prediction & probability estimate
    prediction = model.predict(scaled_data)[0]
    
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(scaled_data)[0]
        risk_percentage = probabilities[1] * 100
    else:
        risk_percentage = 100.0 if prediction == 1 else 0.0

    st.markdown("---")
    st.markdown("### 📊 Assessment Summary")

    res_col1, res_col2 = st.columns([1, 1], gap="medium")

    with res_col1:
        if prediction == 1:
            st.error("🚨 **High Risk of Diabetes Detected**")
            st.write(f"The evaluation indicates a strong likelihood of diabetes based on the parameters provided.")
        else:
            st.success("✅ **Low Risk of Diabetes Detected**")
            st.write(f"The health parameters fall within normal ranges for diabetes risk.")

    with res_col2:
        st.metric(label="Calculated Risk Probability", value=f"{risk_percentage:.1f}%")
        st.progress(int(risk_percentage))

    # Recommendations Section
    with st.expander("💡 Recommended Next Steps", expanded=True):
        if prediction == 1:
            st.write("- **Consult a Physician:** Schedule an HbA1c lab test for clinical confirmation.")
            st.write("- **Dietary Adjustments:** Consider lowering refined carbohydrate and simple sugar intake.")
            st.write("- **Regular Monitoring:** Track blood glucose levels consistently.")
        else:
            st.write("- **Maintain Active Lifestyle:** Aim for 150 minutes of moderate exercise per week.")
            st.write("- **Balanced Diet:** Continue prioritizing fiber-rich whole foods.")
            st.write("- **Routine Checkups:** Perform annual health screenings.")