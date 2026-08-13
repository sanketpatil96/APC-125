#16. Store ten numbers in a tuple and calculate their sum.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

total = sum(numbers)

print("Sum:", total)


#17. Find the largest and smallest number in a tuple without using max() and min().
numbers = (45, 12, 78, 23, 89, 34, 9, 56)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)


#18. Calculate the average of elements stored in a tuple.
numbers = (10, 20, 30, 40, 50)

average = sum(numbers) / len(numbers)

print("Average:", average)


#19. Store 15 integers in a tuple and count even numbers and odd numbers.
numbers = (10, 21, 32, 43, 54, 65, 76, 87, 98, 19, 20, 31, 42, 53, 64)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)


#20. Accept a number from the user and determine whether it exists in the tuple.
numbers = (10, 20, 30, 40, 50)

num = int(input("Enter a number: "))

if num in numbers:
    print("Number exists in the tuple")
else:
    print("Number does not exist in the tuple")


#21. Store student details in a tuple: Roll Number, Name, Department, Marks. Display all the details.
student = (101, "Sanket", "Computer Engineering", 85)

print("Roll Number:", student[0])
print("Name:", student[1])
print("Department:", student[2])
print("Marks:", student[3])


#22. Create tuples containing Employee ID, Name, Salary. Display all employee information.
employees = (
    (101, "Amit", 30000),
    (102, "Rahul", 35000),
    (103, "Sneha", 40000)
)

for employee in employees:
    print("Employee ID:", employee[0])
    print("Name:", employee[1])
    print("Salary:", employee[2])
    print()


#23. Store item prices in a tuple and calculate total bill, average price, highest-priced item and lowest-priced item.
prices = (100, 250, 150, 500, 300)

total = sum(prices)
average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price
    if price < lowest:
        lowest = price

print("Total bill:", total)
print("Average price:", average)
print("Highest price:", highest)
print("Lowest price:", lowest)


#24. Store temperatures of seven days in a tuple and determine maximum temperature, minimum temperature and average temperature.
temperatures = (32, 34, 31, 35, 33, 30, 36)

maximum = temperatures[0]
minimum = temperatures[0]

for temperature in temperatures:
    if temperature > maximum:
        maximum = temperature
    if temperature < minimum:
        minimum = temperature

average = sum(temperatures) / len(temperatures)

print("Maximum temperature:", maximum)
print("Minimum temperature:", minimum)
print("Average temperature:", average)


#25. Store runs scored in 10 matches and calculate total runs, highest score, lowest score and average score.
runs = (45, 78, 23, 91, 56, 34, 88, 67, 42, 75)

total = sum(runs)
average = total / len(runs)

highest = runs[0]
lowest = runs[0]

for run in runs:
    if run > highest:
        highest = run
    if run < lowest:
        lowest = run

print("Total runs:", total)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Average score:", average)


#26. Create two tuples and find the common elements between them.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = ()

for num in tuple1:
    if num in tuple2:
        common += (num,)

print("Common elements:", common)


#27. Merge two tuples and remove duplicate elements.
tuple1 = (10, 20, 30, 40)
tuple2 = (30, 40, 50, 60)

merged = tuple(set(tuple1 + tuple2))

print("Merged tuple without duplicates:", merged)


#28. Count the frequency of each element in a tuple.
numbers = (10, 20, 10, 30, 20, 10, 40, 30)

for num in set(numbers):
    print(num, ":", numbers.count(num))


#29. Convert a tuple into a sorted tuple in ascending and descending order.
numbers = (50, 20, 80, 10, 40, 30)

ascending = tuple(sorted(numbers))
descending = tuple(sorted(numbers, reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)


#30. Create a tuple containing patient records and display all records, search for a patient by ID, count total patients and display patients with a specific blood group.
patients = (
    (101, "Amit", 25, "A+"),
    (102, "Rahul", 30, "B+"),
    (103, "Sneha", 28, "O+"),
    (104, "Priya", 35, "A+"),
    (105, "Neha", 22, "O-")
)

print("Patient Records:")
for patient in patients:
    print(patient)

patient_id = int(input("Enter patient ID to search: "))

found = False

for patient in patients:
    if patient[0] == patient_id:
        print("Patient found:", patient)
        found = True
        break

if not found:
    print("Patient not found")

print("Total number of patients:", len(patients))

blood_group = input("Enter blood group: ")

print("Patients with blood group", blood_group, ":")

for patient in patients:
    if patient[3] == blood_group:
        print(patient)
