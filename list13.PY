"""13.	Accept 10 numbers and sort them in:
•	Ascending order 
•	Descending order
"""
numbers = [12,45,1,67,43,89,23,56,78,34]
print("Original list:", numbers)
# Ascending order
numbers.sort()
print("Sorted list in ascending order:", numbers)
# Descending order
numbers.sort(reverse=True)
print("Sorted list in descending order:", numbers)