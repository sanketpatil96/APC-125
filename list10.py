#10.	Write a program to reverse a list without using the reverse() method.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_numbers = []
for i in range(len(numbers)-1, -1, -1):
    reversed_numbers.append(numbers[i])
print("Original list:", numbers)
print("Reversed list:", reversed_numbers)