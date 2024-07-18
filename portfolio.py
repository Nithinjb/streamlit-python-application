import streamlit as st
from PIL import Image

# Load images
profile_pic = Image.open('profile_picture.jpg')

# Sidebar
st.sidebar.image(profile_pic, use_column_width=True)
st.sidebar.title("Nithin S S")
st.sidebar.subheader("Data Scientist")

# Home Section
def home():
    st.title("Welcome to My Portfolio")
    st.write("""
    Hi, I'm **Nithin S S**. I am a data scientist skilled in data analytics, data engineering, and machine learning. 
    I specialize in using Power BI, Tableau, and Matplotlib for data visualization, 
    data preprocessing for data engineering, and regression, classification, and predictions for machine learning.
    """)

# Skills Section
def skills():
    st.title("Skills")
    st.write("""
    ### Data Analytics
    - Power BI
    - Tableau
    - Matplotlib
    
    ### Data Engineering
    - Data Preprocessing
    
    ### Machine Learning
    - Regression
    - Classification
    - Predictions
    """)

# Projects Section
def projects():
    st.title("Projects")
    st.write("""
    #### Project 1: Data Analysis using Power BI
    Description: Conducted comprehensive data analysis using Power BI to derive business insights.

    #### Project 2: Data Pipeline with Python
    Description: Built an automated data pipeline for preprocessing large datasets.

    #### Project 3: Predictive Modeling with Machine Learning
    Description: Developed predictive models for customer churn using regression and classification techniques.
    """)

# Contact Section
def contact():
    st.title("Contact Me")
    st.write("""
    - Email: your.email@example.com
    - LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/yourprofile)
    - GitHub: [Your GitHub Profile](https://github.com/yourprofile)
    """)

# Navigation
pages = {
    "Home": home,
    "Skills": skills,
    "Projects": projects,
    "Contact": contact
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
