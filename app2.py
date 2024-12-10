import streamlit as st
from datetime import timedelta
import pandas as pd
import pickle
import sklearn
# Load the trained model
def new_func():
    with open(r'C:\Users\80104061\Documents\GitHub\machine-learning-project-team-4\Model\lineareg_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = new_func()

# Streamlit page design
st.set_page_config(page_title="Make better coffee", page_icon="☕", layout="wide")

# Title and description
st.title("Coffee ☕")
st.write(
    "Welcome to the Coffee Strength Calculator! Enter the details of your coffee brewing process. Let's make that perfect cup!"
)

# Input Fields
st.sidebar.header("Enter your coffee brewing details")

def seconder(brew_time):
    mins, secs = map(float, brew_time.split(':'))
    td = timedelta(minutes=mins, seconds=secs)
    return td.total_seconds()

# User inputs for the coffee brewing process
coffee_dose = st.sidebar.number_input("Coffee Dose (grams)", min_value=1, value=10, step=1)
water_temp = st.sidebar.slider("Water Temperature (°C)", min_value=60, max_value=100, value=90)
water_vol = st.sidebar.number_input("Water Volume (ml)", min_value=50, value=200, step=10)
num_pours = st.sidebar.number_input("Number of Pours", min_value=1, value=3, step=1)
brew_time = st.sidebar.text_input("Brew Time (min:sec)", value="0:00")

# Button to trigger prediction
if st.button("Calculate Coffee Strength"):
    try:
        brew_time_seconds = seconder(brew_time)

        # Prepare input data
        data = {
            "dose (g)": [coffee_dose],
            "water temp ( C )": [water_temp],
            "water vol (ml)": [water_vol],
            "number of pours": [num_pours],
            "seconds": [brew_time_seconds],
        }
        input_df = pd.DataFrame(data)

        #Ensure all features are present
        for feature in model.feature_names_in_:
            if feature not in input_df.columns:
                input_df[feature] = 0  # Add missing features with default value

        # Reorder columns to match the model's training order
        input_df = input_df[model.feature_names_in_]

        # Predict coffee strength
        input_predict = model.predict(input_df)

        #print(input_predict[0])
        st.write((float(input_predict[0])))
        


    except Exception as e:
        st.error(f"An error occurred: {str(e)}")



