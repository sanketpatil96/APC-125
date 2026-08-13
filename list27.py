"""27.	Store salaries of employees and determine:
•	Highest salary 
•	Lowest salary 
•	Average salary 
•	Employees earning above ₹50,000 
•	Employees earning below ₹30,000 
"""
salary = []

n = int(input("Enter number of employees: "))

for i in range(n):
    s = int(input("Enter salary: "))
    salary.append(s)

highest = max(salary)
lowest = min(salary)
average = sum(salary) / len(salary)

above = 0
below = 0

for i in salary:
    if i > 50000:
        above += 1
    if i < 30000:
        below += 1

print("Highest Salary:", highest)
print("Lowest Salary:", lowest)
print("Average Salary:", average)
print("Employees earning above ₹50000:", above)
print("Employees earning below ₹30000:", below)