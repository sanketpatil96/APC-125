#15.	Find the second largest element in a list.
numbers = [12, 45, 67, 23, 89, 34, 56, 78, 90, 21]
# Remove duplicates and sort the list in descending order
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[1]
    print("The second largest element in the list is:", second_largest)
else:
    print("The list does not have a second largest element.")