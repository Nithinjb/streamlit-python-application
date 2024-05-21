import streamlit as st

# Function to calculate CGPA
def calculate_cgpa(semesters):
    total_credits = 0
    total_grade_points = 0
    for _, gpa, credits in semesters:
        total_credits += credits
        total_grade_points += gpa * credits
    if total_credits == 0:
        return 0
    return total_grade_points / total_credits

# Main function to define Streamlit app
def main():
    st.title("CGPA Calculator (Indian System)")
    st.write("Welcome to the CGPA Calculator!")
    st.write("Enter your semester GPA and credits below.")

    semesters = []
    # Input fields for each semester
    add_semester = st.button("Add Semester")
    if add_semester:
        st.sidebar.write("Enter Semester Details")
        semester_num = st.sidebar.number_input("Semester Number", min_value=1, step=1)
        gpa = st.sidebar.number_input("Semester GPA", min_value=0.0, max_value=10.0, step=0.01)
        credits = st.sidebar.number_input("Credits", min_value=1, step=1)
        semesters.append((semester_num, gpa, credits))
        st.success("Semester added successfully!")

    # Calculate CGPA
    if semesters:
        try:
            cgpa = calculate_cgpa(semesters)
            st.write("Your CGPA:", round(cgpa, 2))
        except Exception as e:
            st.error("An error occurred while calculating CGPA. Please check your inputs and try again.")
    else:
        st.warning("Please add at least one semester to calculate your CGPA.")

# Run the app
if __name__ == "__main__":
    main()
