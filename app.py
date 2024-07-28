import streamlit as st

# Title of the Health Tracker App
st.title("Health Tracker App")

# Sidebar for user inputs
st.sidebar.header("User Input")

def user_input_features():
    weight = st.sidebar.number_input('Weight (kg)', min_value=30, max_value=300, value=70)
    height = st.sidebar.number_input('Height (cm)', min_value=100, max_value=250, value=170)
    age = st.sidebar.number_input('Age (years)', min_value=1, max_value=120, value=30)
    return weight, height, age

weight, height, age = user_input_features()

# BMI Calculation
if height > 0:
    height_m = height / 100  # convert cm to meters
    bmi = weight / (height_m ** 2)
    st.write(f"Your BMI is: {bmi:.2f}")

    # BMI Category
    if bmi < 18.5:
        st.write("You are Underweight")
    elif 18.5 <= bmi < 24.9:
        st.write("You have a Normal weight")
    elif 25 <= bmi < 29.9:
        st.write("You are Overweight")
    else:
        st.write("You are Obese")

# Display the user's inputs
st.write("## Your Information")
st.write(f"**Weight:** {weight} kg")
st.write(f"**Height:** {height} cm")
st.write(f"**Age:** {age} years")

# Add a simple exercise recommendation section
st.write("## Exercise Recommendations")
st.write("Regular exercise is essential for maintaining your health. Consider the following activities:")
st.write("- Walking: Aim for at least 30 minutes daily.")
st.write("- Jogging: A great way to maintain cardiovascular health.")
st.write("- Cycling: A low-impact exercise suitable for all ages.")
st.write("- Swimming: Excellent for full-body strength and cardio.")

# Nutrition tips based on BMI
st.write("### Nutrition Tips")
if bmi < 18.5:
    st.write("Focus on nutrient-rich foods that are high in calories: avocados, nuts, cheese, and dried fruits.")
elif 18.5 <= bmi < 24.9:
    st.write("Maintain a balanced diet including fruits, vegetables, proteins, and whole grains.")
elif 25 <= bmi < 29.9:
    st.write("Incorporate more fruits, vegetables, and whole grains into your diet. Limit processed foods.")
else:
    st.write("Consider speaking with a healthcare professional for advice on weight management.")

# Footer
st.write("### Stay healthy and active!")
