"""4.	Create a list of numbers. Add:
•	One element at the end 
•	One element at the beginning 
•	One element at a specified position 
Display the remaining list.
"""
numbers = [10, 20, 30, 40, 50]
print("Initial list of numbers:", numbers)
# Adding an element at the end
numbers.append(60)
# Adding an element at the beginning
numbers.insert(0, 5)
# Adding an element at a specified position (e.g., index 3)
numbers.insert(3, 25)
print("Updated list of numbers:", numbers)