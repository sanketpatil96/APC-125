import pandas as pd

# Create dictionary
data = {
    "Student ID": [101, 102, 103, 104, 105],
    "Student Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohan"],
    "Python Marks": [80, 65, 90, 70, 85],
    "DBMS Marks": [75, 70, 95, 68, 80],
    "Mathematics Marks": [85, 60, 88, 72, 90]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

# 1. Display DataFrame
print("Student Data:")
print(df)

# 2. Calculate Total Marks
df["Total Marks"] = (
    df["Python Marks"] +
    df["DBMS Marks"] +
    df["Mathematics Marks"]
)

# 3. Calculate Average Marks
df["Average Marks"] = df["Total Marks"] / 3

print("\nDataFrame with Total and Average:")
print(df)

# 4. Display students with more than 75% average
print("\nStudents with Average Marks more than 75:")
print(df[df["Average Marks"] > 75])

#2 progranmm
# Program 2
# Create a dictionary containing Employee ID, Employee Name,
# Department, Salary and Experience.
# Convert it into a Pandas DataFrame and:
# 1. Displays employees with salary greater than ₹50,000.
# 2. Find the average salary.
# 3. Find the highest salary.
# 4. Find the employee with the highest experience.

import pandas as pd

data = {
    "Employee ID": [101, 102, 103, 104, 105],
    "Employee Name": ["Sanket", "Piyusha", "Parth", "Raj", "Sarth"],
    "Department": ["Media", "Sales", "Data", "Intelligence", "ML"],
    "Salary": [45000, 56000, 34000, 45300, 50000],
    "Experience": [2, 4, 5, 6, 9]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Employee Data:")
print(df)

# 1. Employees with salary greater than 50000
print("\nEmployees with Salary greater than 50000:")
print(df[df["Salary"] > 50000])

# 2. Average salary
print("\nAverage Salary:")
print(df["Salary"].mean())

# 3. Highest salary
print("\nHighest Salary:")
print(df["Salary"].max())

# employe with highest experince
print("highest experience:")
print(df.loc[df(Experience).idMax()])





# 1. Product Dictionary -> DataFrame -> Highest Total Sales
print("\n--- 1. Product Sales ---")
data = {
    "Product_ID": [101, 102, 103, 104],
    "Product_Name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics"],
    "Price": [50000, 800, 1500, 12000],
    "Quantity": [2, 10, 5, 3]
}
df = pd.DataFrame(data)
df["Total_Amount"] = df["Price"] * df["Quantity"]
print(df)
print("Product with highest total sales:")
print(df.loc[df["Total_Amount"].idxmax()])


# 2. Patient Dictionary -> DataFrame
print("\n--- 2. Patient Analysis ---")
data = {
    "Patient_ID": [1, 2, 3, 4, 5],
    "Patient_Name": ["Amit", "Rahul", "Priya", "Sneha", "Rohan"],
    "Age": [65, 45, 72, 30, 68],
    "Disease": ["Diabetes", "Fever", "Heart", "Cold", "BP"],
    "Medical_Charges": [60000, 25000, 80000, 15000, 55000]
}
df = pd.DataFrame(data)
print("Patients above 60:")
print(df[df["Age"] > 60])
print("Average medical charge:", df["Medical_Charges"].mean())
print("Maximum medical charge:", df["Medical_Charges"].max())
print("Patients with charges greater than 50000:")
print(df[df["Medical_Charges"] > 50000])


# 3. Orders -> Final Amount
print("\n--- 3. Order Analysis ---")
data = {
    "Order_ID": [101, 102, 103, 104],
    "Customer": ["Amit", "Rahul", "Priya", "Sneha"],
    "Product": ["Laptop", "Mobile", "TV", "Tablet"],
    "Quantity": [1, 2, 1, 3],
    "Price": [60000, 25000, 45000, 15000],
    "Discount": [5000, 2000, 3000, 1000]
}
df = pd.DataFrame(data)
df["Final_Amount"] = df["Quantity"] * df["Price"] - df["Discount"]
print("All orders:")
print(df)
print("Orders above 5000:")
print(df[df["Final_Amount"] > 5000])
print("Highest-value order:")
print(df.loc[df["Final_Amount"].idxmax()])
print("Average order value:", df["Final_Amount"].mean())


# 4. Student Attendance
print("\n--- 4. Student Attendance ---")
data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Rohan"],
    "Department": ["CSE", "IT", "CSE", "ENTC", "CSE"],
    "Total_Classes": [100, 100, 120, 100, 80],
    "Classes_Attended": [90, 70, 85, 95, 50]
}
df = pd.DataFrame(data)
df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100
print(df)
print("Students with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])


# 5. Retail Shop Sales
print("\n--- 5. Retail Shop Sales ---")
data = {
    "Product_ID": [101, 102, 103, 104],
    "Product_Name": ["Laptop", "Mobile", "Keyboard", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics"],
    "Price": [50000, 30000, 1500, 12000],
    "Quantity": [2, 3, 5, 4]
}
df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]
print(df)
print("Products with sales greater than 10000:")
print(df[df["Total_Sales"] > 10000])
print("Product with maximum sales:")
print(df.loc[df["Total_Sales"].idxmax()])
print("Average sales:", df["Total_Sales"].mean())


# 6. Student Marks Series
print("\n--- 6. Student Marks Series ---")
marks = {
    "Amit": 85,
    "Rahul": 72,
    "Priya": 92,
    "Sneha": 68,
    "Rohan": 78
}
s = pd.Series(marks)
print("Series:")
print(s)
print("Marks of Priya:", s["Priya"])
print("Maximum marks:", s.max())
print("Minimum marks:", s.min())
print("Average marks:", s.mean())
print("Students scoring more than 75:")
print(s[s > 75])


# 7. Employee Salary Series
print("\n--- 7. Employee Salary Series ---")
salary = {
    "Amit": 45000,
    "Rahul": 60000,
    "Priya": 75000,
    "Sneha": 48000,
    "Rohan": 55000
}
s = pd.Series(salary)
print("Series:")
print(s)
print("Highest salary:", s.max())
print("Lowest salary:", s.min())
print("Average salary:", s.mean())
print("Employees earning more than 50000:")
print(s[s > 50000])


# 8. Product Price Series
print("\n--- 8. Product Price Series ---")
prices = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}
s = pd.Series(prices)
print("Products and prices:")
print(s)
s = s * 1.10
print("Prices after 10% increase:")
print(s)
print("Most expensive product:")
print(s.idxmax())
print("Products costing more than 1000:")
print(s[s > 1000])


# 9. Patient Age Series
print("\n--- 9. Patient Age Series ---")
ages = {
    101: 65,
    102: 45,
    103: 72,
    104: 30,
    105: 68
}
s = pd.Series(ages)
print("Average age:", s.mean())
print("Oldest patient:", s.max())
print("Youngest patient:", s.min())
print("Patients above 60:")
print(s[s > 60])


# 10. Student Attendance Series
print("\n--- 10. Student Attendance Series ---")
attendance = {
    "Amit": 85,
    "Rahul": 72,
    "Priya": 95,
    "Sneha": 68,
    "Rohan": 91
}
s = pd.Series(attendance)
print("Average attendance:", s.mean())
print("Attendance below 75%:")
print(s[s < 75])
print("Attendance above 90%:")
print(s[s > 90])
print("Highest attendance:", s.max())


# 11. students.csv
print("\n--- 11. students.csv ---")
df = pd.read_csv("students.csv")
print("First 5 records:")
print(df.head())
print("Last 5 records:")
print(df.tail())
df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3
print("Total and average marks:")
print(df)
print("Students with average marks greater than 75:")
print(df[df["Average"] > 75])
print("Student with highest average:")
print(df.loc[df["Average"].idxmax()])
print("Average marks for each subject:")
print(df[["Python", "DBMS", "Maths"]].mean())


# 12. employees.csv
print("\n--- 12. employees.csv ---")
df = pd.read_csv("employees.csv")
print("Employees from CSE:")
print(df[df["Department"] == "CSE"])
print("Average salary:", df["Salary"].mean())
print("Highest salary:", df["Salary"].max())
print("Lowest salary:", df["Salary"].min())
print("Employees earning more than 50000:")
print(df[df["Salary"] > 50000])
print("Department-wise average salary:")
print(df.groupby("Department")["Salary"].mean())


# 13. patients.csv
print("\n--- 13. patients.csv ---")
df = pd.read_csv("patients.csv")
print("Patients above 60:")
print(df[df["Age"] > 60])
print("Average medical expense:", df["Medical_Expense"].mean())
print("Patient with highest medical expense:")
print(df.loc[df["Medical_Expense"].idxmax()])
print("Number of patients for each disease:")
print(df["Disease"].value_counts())
print("Patients with expense greater than 50000:")
print(df[df["Medical_Expense"] > 50000])


# 14. weather.csv
print("\n--- 14. weather.csv ---")
df = pd.read_csv("weather.csv")
print("Maximum temperature:", df["Temperature"].max())
print("Minimum temperature:", df["Temperature"].min())
print("Average temperature:", df["Temperature"].mean())
print("Records with temperature above 35:")
print(df[df["Temperature"] > 35])
print("City-wise average temperature:")
print(df.groupby("City")["Temperature"].mean())


# 15. Quick Pandas Commands
print("\n--- 15. Important Pandas Commands ---")
print("pd.DataFrame(data)  -> Create DataFrame")
print("pd.Series(data)     -> Create Series")
print("pd.read_csv()       -> Read CSV")
print("df.head()           -> First 5 rows")
print("df.tail()           -> Last 5 rows")
print("df.max()            -> Maximum")
print("df.min()            -> Minimum")
print("df.mean()           -> Average")
print("df.sum()            -> Total")
print("df.idxmax()         -> Index of maximum")
print("df.groupby()        -> Group data")
print("value_counts()      -> Count occurrences")

path = "/mnt/data/Pandas_Practical_Programs.py"
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print(path)
