
import streamlit as st


def calculate_gpa(grades):
    total_credits = 0
    total_grade_points = 0
    for course, grade, credits in grades:
        total_credits += credits
        total_grade_points += grade * credits
    if total_credits == 0:
        return 0
    return total_grade_points / total_credits

def main():
    st.title("GPA Calculator")
    # Sidebar for input fields
    st.sidebar.header("Enter Course Information")
    num_courses = st.sidebar.number_input("Number of Courses", min_value=1, step=1)
    grades = []
    # Input fields for each course
    for i in range(num_courses):
        course = st.sidebar.text_input(f"Course {i+1} Name")
        grade = st.sidebar.number_input(f"Course {i+1} Grade", min_value=0, max_value=100, step=1)
        credits = st.sidebar.number_input(f"Course {i+1} Credits", min_value=1, step=1)
        grades.append((course, grade, credits))
    # Calculate GPA
    gpa = calculate_gpa(grades)
    # Display GPA
    st.write("Your GPA:", round(gpa, 2))

# Run the app
if __name__ == "__main__":
    main()
