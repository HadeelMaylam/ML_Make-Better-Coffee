import streamlit as st
from datetime import timedelta

# Function to determine the strength of the coffee
def determine_coffee_strength(coffee_dose, water_temp, water_vol, num_pours, brew_time_sec):
    # Simplified model to evaluate coffee strength (this can be adjusted as needed)
    strength_score = (coffee_dose * 0.5) + (water_temp * 0.2) - (water_vol * 0.1) + (num_pours * 0.3) + (brew_time_sec * 0.05)

    if strength_score > 30:
        return "Strong"
    elif 20 <= strength_score <= 30:
        return "Balanced"
    else:
        return "Weak"

# Streamlit page design
st.set_page_config(page_title="Coffee Strength Calculator", page_icon="☕", layout="wide")

# Title and description
st.title("Coffee Strength Calculator ☕")
st.write(
    "Welcome to the Coffee Strength Calculator! Enter the details of your coffee brewing process to determine if your coffee is strong, balanced, or weak. Let's make that perfect cup!"
)

# Input Fields
st.sidebar.header("Enter your coffee brewing details")

# User inputs for the coffee brewing process
coffee_dose = st.sidebar.number_input("Coffee Dose (grams)", min_value=1, value=10, step=1)
water_temp = st.sidebar.slider("Water Temperature (°C)", min_value=60, max_value=100, value=90)
water_vol = st.sidebar.number_input("Water Volume (ml)", min_value=50, value=200, step=10)
num_pours = st.sidebar.number_input("Number of Pours", min_value=1, value=3, step=1)
brew_time = st.sidebar.text_input("Brew Time (mm:ss)", value="0:00")

def seconder(brew_time):
    mins, secs = map(float, brew_time.split(':'))
    td = timedelta(minutes=mins, seconds=secs)
    brew_time_seconds = td.total_seconds()
    return brew_time_seconds

# Calculate coffee strength
coffee_strength = determine_coffee_strength(coffee_dose, water_temp, water_vol, num_pours, brew_time_seconds)

# Display the result
st.subheader("Coffee Strength")
st.write(f"Based on your inputs, your coffee is **{coffee_strength}**.")

# Display explanation
if coffee_strength == "Strong":
    st.write("Your coffee is strong! You used a good amount of coffee with high temperature and a decent brew time. Enjoy your bold cup!")
elif coffee_strength == "Balanced":
    st.write("Your coffee is balanced! You've found a nice middle ground with your inputs.")
else:
    st.write("Your coffee is weak. Maybe try using more coffee, a higher temperature, or a longer brew time next time.")

# Add some visual appeal with coffee-related images
st.image("https://www.pexels.com/photo/person-holding-a-mug-of-coffee-1366911/", caption="Enjoy your coffee!", use_column_width=True)

# Optionally, add more styling or widgets to enhance the user experience
