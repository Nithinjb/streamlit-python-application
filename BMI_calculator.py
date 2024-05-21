import streamlit as st
import numpy as np

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: black;
        color: white;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: blue;
        border-radius: 8px;
        font-size: 16px;
        padding: 10px 24px;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stSlider > div > div > div > div > div {
        background: linear-gradient(90deg, #4CAF50 0%, #8BC34A 100%);
    }
    .stMetric {
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height / 100) ** 2
    return bmi

# Main function to define Streamlit app
def main():
    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI)")

    # Sidebar for input fields
    st.sidebar.header("Enter Your Details")
    weight = st.sidebar.slider("Weight (kg)", 20, 200, 70)
    height = st.sidebar.slider("Height (cm)", 100, 250, 170)

    if st.sidebar.button("Calculate"):
        bmi = calculate_bmi(weight, height)
        st.metric(label="Your BMI", value=f"{bmi:.2f}")

        if bmi < 18.5:
            st.write("You are **underweight**. It's important to eat a healthy, balanced diet.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a **normal weight**. Keep up the good work!")
        elif 25 <= bmi < 29.9:
            st.write("You are **overweight**. Consider a balanced diet and regular exercise.")
        else:
            st.write("You are **obese**. It's important to consult with a healthcare provider.")

    # Footer
    st.markdown(
        """
        <footer style='text-align: center; padding: 10px 0;'>
        <hr>
        <p style='font-size: 14px;'>Developed by <a href='https://www.linkedin.com/in/your-profile/' target='_blank'>Your Name</a></p>
        </footer>
        """,
        unsafe_allow_html=True
    )

# Run the app
if __name__ == "__main__":
    main()
