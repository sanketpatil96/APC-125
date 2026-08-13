#6.	Write a program to find the largest and smallest number in a list without using max() or min().
numbers = [15, 42, 7, 23, 89, 3, 56]

largest = numbers[0]
smallest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest number:", largest)
print("Smallest number:", smallest)