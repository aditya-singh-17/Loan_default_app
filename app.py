import streamlit as st
import joblib
import tensorflow as tf
import numpy as np

# Load models
xgb = joblib.load("xgb_model.pkl")
#ann = tf.keras.models.load_model("ann_model.h5")

st.title("Loan Default Prediction App")
st.write("Enter loan application details to check risk of default.")

# User inputs
interest_rate_spread = st.number_input("Interest Rate Spread", min_value=0.0, step=0.1)
ltv = st.number_input("Loan to Value Ratio (LTV)", min_value=0.0, step=0.1)
rate_of_interest = st.number_input("Rate of Interest", min_value=0.0, step=0.1)
upfront_charges = st.number_input("Upfront Charges", min_value=0.0, step=0.1)

model_choice = st.radio("Select Model", ["XGBoost"])

input_data = np.array([[interest_rate_spread, ltv, rate_of_interest, upfront_charges]])

if st.button("Predict"):
    pred = xgb.predict(input_data)
    result = "Default" if pred[0] == 1 else "No Default"
    st.success(f"Prediction: {result}")

    if prediction[0] == 1:
        st.error("⚠ Loan is likely to *DEFAULT*.")
    else:
        st.success("✅ Loan is likely to be *SAFE*.")
