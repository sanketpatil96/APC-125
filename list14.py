#14.Create a list containing duplicate values and display only unique elements.
l1 = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7]
print("Original list with duplicates:", l1)
unique_elements = list(set(l1))
print("Unique elements in the list:", unique_elements)