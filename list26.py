"""26.	Store marks of 20 students in a list and determine:
•	Highest marks 
•	Lowest marks 
•	Average marks 
•	Number of students scoring above average 
•	Number of students scoring below average
"""

marks = []

for i in range(20):
    m = int(input("Enter marks: "))
    marks.append(m)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

above = 0
below = 0

for i in marks:
    if i > average:
        above += 1
    elif i < average:
        below += 1

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Students Above Average:", above)
print("Students Below Average:", below)