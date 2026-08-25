import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="Health",
    layout="centered"
)

st.title("📊 BMI Calculator")
st.caption("Python Fundamentals + Streamlit Demo")

st.divider()

name = st.text_input("Name")

st.number_input("Enter your weight (kg)",  placeholder="e.g., 70", key="weight")
st.number_input("Enter your height (cm)", min_value=50.00, max_value=250.00, placeholder="e.g., 175", key="height")

if st.button("Calculate BMI",type="primary", use_container_width=True):

    if not name:
        st.warning("Please enter your name.")

    else:
        weight = st.session_state.weight
        height_cm = st.session_state.height
        height_m = height_cm / 100

        bmi = weight / (height_m ** 2)

        st.subheader(f"Results for {name}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("BMI", f"{bmi:.1f}")

        with col2:
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"

            st.metric("Category", category)

st.divider()

st.warning("If you have any health concerns, please consult a healthcare professional.", icon="⚠️")
