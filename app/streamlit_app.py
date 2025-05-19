import streamlit as st
from src.calculator import calculate_bmi, calculate_bmr
from src.recommender import suggest_workouts

st.set_page_config(page_title="AI Fitness Coach", page_icon="💪")
st.title("💪 AI Fitness Coach")

age = st.slider("Your Age", 18, 65)
gender = st.radio("Gender", ["male", "female"])
weight = st.number_input("Weight (kg)", 40, 150)
height = st.number_input("Height (cm)", 120, 220)
goal = st.selectbox("Your Fitness Goal", ["Lose Weight", "Gain Muscle", "Stay Fit"])
experience = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Plan"):
    bmi = calculate_bmi(weight, height)
    bmr = calculate_bmr(weight, height, age, gender)
    workouts = suggest_workouts(goal, experience)

    st.success(f"Your BMI: {bmi} | BMR: {int(bmr)} kcal/day")
    st.subheader("🏃 Recommended Workouts:")
    for w in workouts:
        st.write(f"✔️ {w}")
