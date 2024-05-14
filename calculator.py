import streamlit as st

# Define the pre-determined grading scale
grading_scale = {
    (90, 100): 'A',
    (80, 89): 'B',
    (70, 79): 'C',
    (60, 69): 'D',
    (0, 59): 'F'
}

# Function to calculate the overall grade based on test scores
def calculate_grade(*scores):
    average_score = sum(scores) / len(scores)
    for grade_range, letter_grade in grading_scale.items():
        if grade_range[0] <= average_score <= grade_range[1]:
            return letter_grade

# Main function to define Streamlit app
def main():
    st.title("Grade Calculator")
    # Sidebar for input fields
    st.sidebar.header("Enter Test Scores")
    # Input fields for test scores
    test1_score = st.sidebar.number_input("Test 1 Score", min_value=0, max_value=100, step=1)
    test2_score = st.sidebar.number_input("Test 2 Score", min_value=0, max_value=100, step=1)
    test3_score = st.sidebar.number_input("Test 3 Score", min_value=0, max_value=100, step=1)
    test4_score = st.sidebar.number_input("Test 4 Score", min_value=0, max_value=100, step=1)
    test5_score = st.sidebar.number_input("Test 5 Score", min_value=0, max_value=100, step=1)
    # Calculate overall grade
    overall_grade = calculate_grade(test1_score, test2_score, test3_score, test4_score, test5_score)
    # Display final grade
    st.write("Final Grade:", overall_grade)

# Run the app
if __name__ == "__main__":
    main()


