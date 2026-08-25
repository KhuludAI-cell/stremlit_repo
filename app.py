import streamlit as st

st.set_page_config(
    page_title="My Streamlit App", 
    page_icon=":smiley:", 
    layout="wide"
    )

st.title("Students Grade Calculator.")

st.divider()

name = st.text_input("Enter your name:")    
python_score = st.slider("Python :", 0, 100, 50)
cloud_score = st.slider("Cloud :", 0, 100, 50)
database_score = st.slider("Database :", 0, 100, 50)

score= {
    "Python": python_score,
    "Cloud": cloud_score,
    "Database": database_score
}

def calculate_average(scores):
    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    return average_score

def get_grade(average_score):
    if average_score >= 9:
        return "A"
    elif average_score >= 8:
        return "B"
    elif average_score >= 7:
        return "C"
    elif average_score >= 6:
        return "D"
    else:
        return "F"


if st.button("Clculate Average", use_container_width=True):
    if not name:
        st.warning("Please enter your name.")
    else:
        average_score = calculate_average(score)
        grade = get_grade(average_score)

        st.success(f"Hello {name}, your average score is {average_score:.2f} and your grade is {grade}.")

