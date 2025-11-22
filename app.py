import streamlit as st
import pandas as pd
import joblib

# ---- Load Model ----
model = joblib.load("notebooks/co2_model.pkl")  # adjust path if needed

st.set_page_config(page_title="CO2 Emission Prediction", layout="centered")

st.title("🚗 CO2 Emission Prediction App")
st.write("Enter vehicle details below to predict CO2 emissions.")

# ---- Input Fields ----

make = st.text_input("Car Make (Example: Toyota, Ford)")
model_name = st.text_input("Car Model (Example: Civic, Corolla)")

vehicle_class = st.selectbox("Vehicle Class", 
                             ["COMPACT", "SUV", "MID-SIZE", "TWO-SEATER", "FULL-SIZE", "PICKUP TRUCK", "MINICOMPACT", "STATION WAGON", "SUBCOMPACT"]
                            )

transmission = st.selectbox("Transmission", 
                            ["A6", "A8", "M5", "AV", "AS6", "AS8", "AM7", "A7", "AS7", "AM6", "A5"]
                           )

fuel_type = st.selectbox("Fuel Type", ["X", "Z", "D", "E"])

engine_size = st.number_input("Engine Size (L)", step=0.1, min_value=0.5, value=1.0)
cylinders = st.number_input("Number of Cylinders", step=1, min_value=2, value=4)

fuel_city = st.number_input("Fuel Consumption (City L/100 km)", step=0.1, min_value=1.0, value=7.5)
fuel_hwy = st.number_input("Fuel Consumption (Highway L/100 km)", step=0.1, min_value=1.0, value=5.5)
fuel_comb_l = st.number_input("Fuel Consumption Combined (L/100 km)", step=0.1, min_value=1.0, value=6.5)
fuel_comb_mpg = st.number_input("Fuel Consumption Combined (MPG)", step=1, min_value=5, value=30)

# ---- Prediction ----

if st.button("Predict"):

    input_data = pd.DataFrame([{
        "make": make,
        "model": model_name,
        "vehicle_class": vehicle_class,
        "engine_size": engine_size,
        "cylinders": cylinders,
        "transmission": transmission,
        "fuel_type": fuel_type,
        "fuel_consumption_city": fuel_city,
        "fuel_consumption_hwy": fuel_hwy,
        "fuel_consumption_comb(l/100km)": fuel_comb_l,
        "fuel_consumption_comb(mpg)": fuel_comb_mpg
    }])

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated CO2 Emission: **{prediction:.2f} g/km**")
    except Exception as e:
        st.error(f"Error in prediction: {e}")
        st.write("⚠️ Make sure the input formatting matches the dataset format.")


st.write("---")
st.caption("Made with ❤️ using Machine Learning & Streamlit")
