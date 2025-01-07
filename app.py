import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the model and feature names
saved_data = joblib.load("models/optimized_fetal_health_model.pkl")
model = saved_data["model"]
feature_names = saved_data["feature_names"]

# App title
st.title("Fetal Health Classification")

# Description
st.write("""
This app classifies fetal health based on input features. 
Provide the necessary details below to get a prediction.
""")

# Sidebar input form
st.sidebar.header("Input Features")
def user_input_features():
    baseline_value = st.sidebar.number_input("Baseline Value (FHR)", 100, 180, 130)
    accelerations = st.sidebar.number_input("Accelerations per second", 0.0, 0.02, 0.005)
    fetal_movement = st.sidebar.number_input("Fetal Movement per second", 0.0, 0.5, 0.01)
    uterine_contractions = st.sidebar.number_input("Uterine Contractions per second", 0.0, 0.02, 0.005)
    histogram_mean = st.sidebar.number_input("Histogram Mean", 50.0, 200.0, 135.0)
    histogram_variance = st.sidebar.number_input("Histogram Variance", 0.0, 300.0, 20.0)
    
    data = {
        "baseline value": baseline_value,
        "accelerations": accelerations,
        "fetal_movement": fetal_movement,
        "uterine_contractions": uterine_contractions,
        "histogram_mean": histogram_mean,
        "histogram_variance": histogram_variance,
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Reorder the input DataFrame to match the model's feature order
input_df = input_df.reindex(columns=feature_names, fill_value=0)

# Show input features
st.write("### Input Features", input_df)

# Prediction
if st.button("Classify"):
    prediction = model.predict(input_df)
    prediction_map = {1: "Normal", 2: "Suspect", 3: "Pathological"}
    st.write(f"### Predicted Fetal Health: **{prediction_map[prediction[0]]}**")
