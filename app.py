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
st.title("Make a Better Coffee ☕")
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

# Initialize brew time in session_state if not already set
if "brew_time" not in st.session_state:
    st.session_state.brew_time = "2:00"

# Function to convert brew time to seconds
def seconder(brew_time):
    mins, secs = map(int, brew_time.split(':'))
    td = timedelta(minutes=mins, seconds=secs)
    brew_time_seconds = td.total_seconds()
    return brew_time_seconds

# Add time adjustment buttons
def update_brew_time(brew_time):
    mins, secs = map(int, brew_time.split(':'))
    total_seconds = mins * 60 + secs

    # Increment by 10 seconds but not exceed 3:00
    if total_seconds < 180:
        total_seconds += 10
        if total_seconds > 180:  # Ensure it doesn't go beyond 3:00
            total_seconds = 180
        new_minutes = total_seconds // 60
        new_seconds = total_seconds % 60
        return f"{new_minutes:02}:{new_seconds:02}"
    return brew_time

# Display + button for increasing brew time
if st.sidebar.button("Add 10 seconds"):
    st.session_state.brew_time = update_brew_time(st.session_state.brew_time)

# Display the current brew time
st.sidebar.write(f"Current Brew Time: {st.session_state.brew_time}")

# Calculate coffee strength
coffee_strength = determine_coffee_strength(coffee_dose, water_temp, water_vol, num_pours, seconder(st.session_state.brew_time))

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
