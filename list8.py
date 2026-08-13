"""8.	Store 15 integers in a list. Count how many numbers are:
•	Even 
•	Odd"""
integers = [12,13,64,78,9,23,45,67,89,90,34,56,78,21,43,65,87]
even = 0
odd = 0
for num in integers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Count of even numbers:", even)
print("Count of odd numbers:", odd)