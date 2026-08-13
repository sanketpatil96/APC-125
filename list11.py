"""11.	Create a list of 10 numbers and display:
•	First 5 elements 
•	Last 5 elements 
•	Middle 4 elements 
•	Alternate elements 
•	Reverse list using slicing
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# First 5 elements
first_five = numbers[:5]
# Last 5 elements
last_five = numbers[-5:]
# Middle 4 elements
middle_four = numbers[3:7]
# Alternate elements
alternate_elements = numbers[::2]
# Reverse list using slicing
reversed_list = numbers[::-1]
print("First 5 elements:", first_five)
print("Last 5 elements:", last_five)
print("Middle 4 elements:", middle_four)
print("Alternate elements:", alternate_elements)
print("Reversed list:", reversed_list)