#22.	Find common elements between two lists.
l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common_elements = list(set(l1) & set(l2))
print("List 1:", l1)
print("List 2:", l2)
print("Common elements between the two lists:", common_elements)