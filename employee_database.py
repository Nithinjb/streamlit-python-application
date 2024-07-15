import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('employees.db')
c = conn.cursor()

# Create the employees table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (employee_id TEXT PRIMARY KEY, name TEXT, position TEXT)''')
conn.commit()

# Function to add employee
def add_employee(employee_id, name, position):
    try:
        c.execute("INSERT INTO employees (employee_id, name, position) VALUES (?, ?, ?)", 
                  (employee_id, name, position))
        conn.commit()
        st.success("Employee added successfully!")
    except sqlite3.IntegrityError:
        st.error("Employee ID already exists.")

# Function to view all employees
def view_employees():
    st.write("### List of Employees")
    c.execute("SELECT * FROM employees")
    data = c.fetchall()
    if not data:
        st.write("No employees added yet.")
    else:
        df = pd.DataFrame(data, columns=["Employee ID", "Name", "Position"])
        st.table(df)

# Function to search employee by ID or name
def search_employee(query):
    st.write("### Search Results")
    query = f"%{query}%"
    c.execute("SELECT * FROM employees WHERE employee_id LIKE ? OR name LIKE ?", (query, query))
    results = c.fetchall()
    if not results:
        st.write("No matching employee found.")
    else:
        df = pd.DataFrame(results, columns=["Employee ID", "Name", "Position"])
        st.table(df)

# Function to delete employee by ID
def delete_employee(employee_id):
    c.execute("DELETE FROM employees WHERE employee_id = ?", (employee_id,))
    conn.commit()
    if c.rowcount > 0:
        st.success("Employee deleted successfully!")
    else:
        st.error("Employee ID not found.")

# Main function to define Streamlit app
def main():
    st.title("Employee Database")
    st.write("Welcome to the Employee Database!")

    menu = st.sidebar.selectbox("Menu", ["Add Employee", "View Employees", "Search Employee", "Delete Employee"])

    if menu == "Add Employee":
        st.header("Add Employee")
        employee_id = st.text_input("Employee ID")
        name = st.text_input("Name")
        position = st.text_input("Position")
        if st.button("Add"):
            add_employee(employee_id, name, position)

    elif menu == "View Employees":
        st.header("View Employees")
        view_employees()

    elif menu == "Search Employee":
        st.header("Search Employee")
        query = st.text_input("Enter Employee ID or Name")
        if st.button("Search"):
            search_employee(query)

    elif menu == "Delete Employee":
        st.header("Delete Employee")
        employee_id = st.text_input("Enter Employee ID to Delete")
        if st.button("Delete"):
            delete_employee(employee_id)

# Run the app
if __name__ == "__main__":
    main()
