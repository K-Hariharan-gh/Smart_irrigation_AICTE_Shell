import streamlit as st
import numpy as np
import joblib  

# Load the trained model
model = joblib.load("Farm_Irrigation_System.pkl")  
st.title("Smart Sprinkler System")
st.subheader("Enter scaled sensor values (0 to 1) to predict sprinkler status")
st.text("Sensors are used here to measure the various changes in the soil, these are the changes which will determine the sprinkler status")
# Collect sensor inputs (scaled values)
sensor_values = []
for i in range(20):
    val = st.slider(f"Sensor {i}", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    sensor_values.append(val)

st.text("With the data that Sensors had gathered, let us predict the sprinklers status.")
# Predict button
if st.button("Predict Sprinklers"):
    input_array = np.array(sensor_values).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    st.markdown("### Prediction:")
    for i, status in enumerate(prediction):
        st.write(f"Sprinkler {i} (parcel_{i}): {'ON' if status == 1 else 'OFF'}")
    result_data = [
        {"Sprinkler": f"Sprinkler {i}", "Parcel": f"parcel_{i}", "Status": "ON" if status == 1 else "OFF"}
        for i, status in enumerate(prediction)
    ]

    st.markdown("### Prediction Table:")
    st.table(result_data)  
    st.success("Sprinkler prediction was successful!")