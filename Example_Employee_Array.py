"""
Employee Data Management using NumPy Structured Arrays

✅ This script demonstrates how to store and manage employee records using NumPy's structured arrays.
✅ Structured arrays allow different data types (int, float, string) in a single array.

🔹 Fields:
    - ID (Integer)
    - Name (String, max 10 characters)
    - Salary (Float)

🔹 Features:
    - Store multiple employees
    - Access employee records by index
    - Access specific columns (e.g., all employee names)
    - Filter employees based on salary
    - Iterate through records

🔹 Author: Deepak Pushpad
"""

import numpy as np  # Import NumPy for structured array operations

# ✅ Step 1: Define structured array with tuples (each employee is a tuple)
employee_data = np.array([
    (1, "Deepak", 50000),  
    (2, "Alice", 25000),     
    (3, "Bob", 9565),
    (4, "Charlie", 18000),
    (5, "David", 32000)
], dtype=[("ID", "i4"), ("Name", "U10"), ("Salary", "f8")])  # Define field names and data types

# ✅ Step 2: Access individual employee records by index
print("\n🔹 Accessing individual employee records:")
print(employee_data[1])  # Output: (2, 'Alice', 25000.)
print(employee_data[3])  # Output: (4, 'Charlie', 18000.)

# ✅ Step 3: Accessing specific fields (columns)
print("\n🔹 Accessing specific columns:")
print("Employee Names:", employee_data["Name"])  # Output: ['Deepak' 'Alice' 'Bob' 'Charlie' 'David']
print("Salaries:", employee_data["Salary"])      # Output: [50000. 25000. 9565. 18000. 32000.]

# ✅ Step 4: Filtering Employees with Salary > 20,000
print("\n🔹 Employees with salary > 20000:")
high_salary_employees = employee_data[employee_data["Salary"] > 20000]
print(high_salary_employees)

# ✅ Step 5: Iterating through the structured array
print("\n🔹 Iterating through employee records:")
for emp in employee_data:
    print(f"ID: {emp['ID']}, Name: {emp['Name']}, Salary: {emp['Salary']}")

# ✅ Step 6: Updating a record (Modifying employee salary)
print("\n🔹 Updating salary of employee ID 3 (Bob):")
employee_data[2]["Salary"] = 15000  # Change Bob's salary from 9565 to 15000
print(employee_data[2])  # Output: (3, 'Bob', 15000.)

# ✅ Step 7: Sorting employees by Salary
print("\n🔹 Sorting employees by salary:")
sorted_employees = np.sort(employee_data, order="Salary")
print(sorted_employees)

# ✅ Step 8: Finding the employee with the highest salary
highest_paid_employee = employee_data[np.argmax(employee_data["Salary"])]
print("\n🔹 Employee with highest salary:", highest_paid_employee)

"""
✅ Pros and Cons of Using NumPy Structured Arrays:

✔ Pros:
   1️⃣ Efficient memory usage ✅
   2️⃣ Faster operations compared to Python lists ✅
   3️⃣ Allows column-based access ✅
   4️⃣ Supports multiple data types ✅

❌ Cons:
   1️⃣ Less flexible (difficult to modify structure) ❌
   2️⃣ Not as widely used as Pandas DataFrames ❌
   3️⃣ Slightly slower than regular NumPy arrays ❌


   🔹 Recommended Use:
   - Use NumPy structured arrays for **small structured datasets**.
   - For large datasets, **Pandas DataFrames** are more suitable.
"""

