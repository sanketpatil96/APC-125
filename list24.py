"""24.	Rotate a list:
•	Left by one position 
•	Right by one position
"""
# Rotate a list left and right by one position

list1 = [10, 20, 30, 40, 50]

# Left Rotation
left = list1[1:] + [list1[0]]
print("Left Rotation :", left)

# Right Rotation
right = [list1[-1]] + list1[:-1]
print("Right Rotation:", right)