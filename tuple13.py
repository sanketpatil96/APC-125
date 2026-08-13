#13.	Modify a tuple by converting it into a list and then back into a tuple.
numbers = (10, 20, 30, 40, 50)

numbers = list(numbers)
numbers[2] = 35
numbers = tuple(numbers)

print(numbers)
