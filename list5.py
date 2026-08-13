"""5.	Create a list of student names. Remove:
•	First student 
•	Last student 
•	A specific student by name 
Display the remaining list.
"""
students = ["Yash", "Amit", "Priya", "Rohit", "Sneha"]
print("Initial list of students:", students)
# Removing the first student
students.pop(0)
# Removing the last student
students.pop()
# Removing a specific student by name (e.g., "Priya")
students.remove("Priya")
print("Updated list of students:", students)