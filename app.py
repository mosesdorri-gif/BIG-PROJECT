import streamlit as st
import joblib

# Load trained model
model = joblib.load("gradient_boosting_model.pkl")

# Page title
st.title("Churn prediction model")

st.write("Gradient Boosting model loaded successfully!")

# Add inputs later based on your dataset features
st.header("Make a Prediction")

st.write("Your model is ready. Add your input features below.")

# Example placeholder
if st.button("Test Model"):
    st.success("The model is working!")
