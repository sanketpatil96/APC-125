#1. Write a lambda function to calculate the square of a given number.

square = lambda n: n * n

print("Square:", square(5))


# 2. Create a lambda function that returns the cube of a number.

cube = lambda n: n * n * n

print("Cube:", cube(4))



# 3. Write a lambda function that returns True if a number is
# even and False otherwise.

is_even = lambda n: n % 2 == 0

print("Is Even:", is_even(10))
print("Is Even:", is_even(7))



# 4. Use a lambda function to find the maximum of two numbers.

maximum = lambda a, b: a if a > b else b

print("Maximum:", maximum(25, 40))



# 5. Create a lambda function to calculate simple interest
# using principal, rate, and time.
# Formula: SI = (P * R * T) / 100


simple_interest = lambda p, r, t: (p * r * t) / 100

print("Simple Interest:", simple_interest(10000, 5, 2))


# 6. Take a list of numbers, use map() and a lambda function
# to generate a list containing their squares.


numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n * n, numbers))

print("Original List:", numbers)
print("Squares:", squares)


# 7. Use map() with lambda to calculate the cube of every
# element in a list.


numbers = [1, 2, 3, 4, 5]

cubes = list(map(lambda n: n * n * n, numbers))

print("Original List:", numbers)
print("Cubes:", cubes)


# 8. Take two lists of numbers, use map() and lambda to create
# a third list containing the sum of corresponding elements.


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

sum_list = list(map(lambda a, b: a + b, list1, list2))

print("First List:", list1)
print("Second List:", list2)
print("Sum List:", sum_list)


# 9. Take a list of integers, use filter() and lambda to
# extract all even numbers.


numbers = [10, 15, 22, 33, 40, 51, 64, 77]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("1. Even Numbers:", even_numbers)



# 10. Take a list of integers, use filter() with an appropriate
# lambda expression to identify prime numbers.

numbers = [2, 3, 4, 5, 6, 7, 8, 11, 13, 15, 17, 20]


def is_prime(n):
    if n < 2:
        return False

    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


prime_numbers = list(filter(lambda x: is_prime(x), numbers))

print("2. Prime Numbers:", prime_numbers)



# 11. Use filter() and lambda to extract positive numbers
# from a list.


numbers = [-10, 5, -3, 8, 0, 12, -7, 15]

positive_numbers = list(filter(lambda x: x > 0, numbers))

print("3. Positive Numbers:", positive_numbers)



# 12. Take a list of numbers, use filter() and lambda to find
# numbers greater than 50.


numbers = [25, 55, 40, 75, 90, 12, 60, 45]

greater_than_50 = list(filter(lambda x: x > 50, numbers))

print("4. Numbers Greater Than 50:", greater_than_50)



# 13. Take a list of words, use filter() and lambda to find
# words having more than five characters.


words = ["Python", "Java", "Computer", "Data", "Programming", "AI"]

long_words = list(filter(lambda word: len(word) > 5, words))

print("5. Words Having More Than 5 Characters:", long_words)



# 14. Take a list of words; sort them according to their length
# using lambda.


words = ["Python", "Java", "C", "Programming", "AI", "Database"]

sorted_words = sorted(words, key=lambda word: len(word))

print("6. Words Sorted According to Length:", sorted_words)



# 15. Take a list of tuples containing student names and marks,
# sort the students according to their marks using lambda.

students = [
    ("Shravani", 85),
    ("Piyusha", 92),
    ("Neha", 75),
    ("Sneha", 88)
]

sorted_students = sorted(students, key=lambda student: student[1])

print("7. Students Sorted According to Marks:")

for student in sorted_students:
    print(student)



# 8. Take employee records containing name and salary, sort
# them according to salary using lambda.


employees = [
   ("Shravani", 85000),
       ("Piyusha", 50000),
       ("Neha", 750000),
       ("Sneha", 88000)
]

sorted_employees = sorted(employees, key=lambda employee: employee[1])

print("8. Employees Sorted According to Salary:")

for employee in sorted_employees:
    print(employee)


# 9. Take a list containing student names and marks, use
# functions and lambda expressions to:
#
# a) Calculate average marks.
# b) Filter students scoring above 75.
# c) Sort students according to marks.


students = [
    ("Aarav", 80),
    ("Neha", 78),
    ("Shaurya", 70)
]


# a) Calculate average marks
def calculate_average(students):
    marks = list(map(lambda student: student[1], students))
    return sum(marks) / len(marks)


average_marks = calculate_average(students)

print("9(a). Average Marks:", average_marks)


# b) Filter students scoring above 75
above_75 = list(filter(lambda student: student[1] > 75, students))

print("9(b). Students Scoring Above 75:")

for student in above_75:
    print(student)


# c) Sort students according to marks
sorted_students = sorted(students, key=lambda student: student[1])

print("9(c). Students Sorted According to Marks:")

for student in sorted_students:
    print(student)



# 10. Take employee records containing name, department,
# and salary, use filter(), map(), and sorted() with lambda
# functions to:
#
# a) Find employees earning more than ₹50,000.
# b) Increase salaries by 10%.
# c) Sort employees according to salary.


employees = [
    ("Shaurya", "IT", 60000),
    ("Riya", "HR", 45000),
    ("Abhishek", "Finance", 70000),
    ("Gaurav", "IT", 55000),
    ("Shruti", "Sales", 40000)
]


# a) Find employees earning more than ₹50,000
high_salary = list(filter(lambda emp: emp[2] > 50000, employees))

print("10(a). Employees Earning More Than ₹50,000:")

for employee in high_salary:
    print(employee)


# b) Increase salaries by 10%
increased_salary = list(
    map(lambda emp: (emp[0], emp[1], emp[2] * 1.10), employees)
)

print("10(b). Salaries After 10% Increase:")

for employee in increased_salary:
    print(employee)


# c) Sort employees according to salary
sorted_employees = sorted(employees, key=lambda emp: emp[2])

print("10(c). Employees Sorted According to Salary:")

for employee in sorted_employees:
    print(employee)



# 11. Take a list of products with names, prices, and quantities,
# use functions and lambda expressions to:
#
# a) Calculate total value of each product.
# b) Filter products costing more than ₹1,000.
# c) Sort products according to total value.


products = [
    ("Laptop", 50000, 2),
    ("Mouse", 800, 3),
    ("Keyboard", 1500, 2),
    ("Monitor", 12000, 1),
    ("USB Cable", 500, 5)
]


# a) Calculate total value of each product
def calculate_product_value(product):
    name, price, quantity = product
    return (name, price, quantity, price * quantity)


product_values = list(map(calculate_product_value, products))

print("11(a). Total Value of Each Product:")

for product in product_values:
    print(product)


# b) Filter products costing more than ₹1,000
# Here, total product value is considered.
expensive_products = list(
    filter(lambda product: product[3] > 1000, product_values)
)

print("11(b). Products Costing More Than ₹1,000:")

for product in expensive_products:
    print(product)


# c) Sort products according to total value
sorted_products = sorted(product_values, key=lambda product: product[3])

print("11(c). Products Sorted According to Total Value:")

for product in sorted_products:
    print(product)



# 12. Write a program using functions, map(), filter(), and
# lambda expressions to process a list of words and:
#
# a) Find the length of every word.
# b) Extract words having more than five characters.
# c) Sort words according to their length.


words = [
    "Python",
    "Java",
    "Programming",
    "Data",
    "Computer",
    "AI",
    "Database"
]


# a) Find the length of every word
def word_lengths(words):
    return list(map(lambda word: len(word), words))


lengths = word_lengths(words)

print("12(a). Length of Every Word:", lengths)


# b) Extract words having more than five characters
long_words = list(
    filter(lambda word: len(word) > 5, words)
)

print("12(b). Words Having More Than 5 Characters:", long_words)


# c) Sort words according to their length
sorted_words = sorted(words, key=lambda word: len(word))

print("12(c). Words Sorted According to Length:", sorted_words)
