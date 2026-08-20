#21. Create a dictionary containing numbers from 1 to 10 as keys and their squares as values.
squares = {}

for i in range(1, 11):
    squares[i] = i * i

print(squares)


#22. Create a dictionary containing numbers from 1 to 20 as keys and their squares as values, but include only even numbers.
squares = {}

for i in range(2, 21, 2):
    squares[i] = i * i

print(squares)


#23. Given a list of numbers, create a dictionary containing each unique number and its frequency.
numbers = [10, 20, 10, 30, 20, 10, 40, 30, 50]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)


#24. Create a dictionary containing integers from 1 to 10 and their cubes.
cubes = {}

for i in range(1, 11):
    cubes[i] = i * i * i

print(cubes)


#25. Create a dictionary containing student names and marks. Develop a program to add a student, update marks, delete a student, search for a student, display all students, find the highest marks and calculate the average.
students = {
    "Amit": 80,
    "Rahul": 90,
    "Sneha": 85
}

name = input("Enter student name to add: ")
marks = int(input("Enter marks: "))
students[name] = marks

name = input("Enter student name to update: ")
if name in students:
    marks = int(input("Enter new marks: "))
    students[name] = marks

name = input("Enter student name to delete: ")
if name in students:
    del students[name]

name = input("Enter student name to search: ")
if name in students:
    print("Marks:", students[name])
else:
    print("Student not found")

print("All students:")
for name, marks in students.items():
    print(name, ":", marks)

highest = max(students.values())
print("Highest marks:", highest)

average = sum(students.values()) / len(students)
print("Average marks:", average)


#26. Create a dictionary containing employee names and salaries. Find highest salary, lowest salary, average salary and employees earning more than ₹50,000.
employees = {
    "Amit": 45000,
    "Rahul": 65000,
    "Sneha": 55000,
    "Priya": 48000,
    "Neha": 70000
}

highest = max(employees.values())
lowest = min(employees.values())
average = sum(employees.values()) / len(employees)

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)

print("Employees earning more than ₹50,000:")
for name, salary in employees.items():
    if salary > 50000:
        print(name, ":", salary)


#27. Create a dictionary containing product names and quantities. Perform add a product, update quantity, delete a product, search for a product and display products with quantity below 10.
products = {
    "Laptop": 5,
    "Mouse": 15,
    "Keyboard": 8,
    "Monitor": 12
}

name = input("Enter product to add: ")
quantity = int(input("Enter quantity: "))
products[name] = quantity

name = input("Enter product to update: ")
if name in products:
    quantity = int(input("Enter new quantity: "))
    products[name] = quantity

name = input("Enter product to delete: ")
if name in products:
    del products[name]

name = input("Enter product to search: ")
if name in products:
    print("Quantity:", products[name])
else:
    print("Product not found")

print("Products with quantity below 10:")
for name, quantity in products.items():
    if quantity < 10:
        print(name, ":", quantity)


#28. Create a dictionary containing names and phone numbers. Implement add contact, search contact, update contact, delete contact and display all contacts.
contacts = {
    "Amit": "9876543210",
    "Rahul": "9876501234",
    "Sneha": "9876512345"
}

name = input("Enter contact name to add: ")
phone = input("Enter phone number: ")
contacts[name] = phone

name = input("Enter contact name to search: ")
if name in contacts:
    print("Phone number:", contacts[name])
else:
    print("Contact not found")

name = input("Enter contact name to update: ")
if name in contacts:
    phone = input("Enter new phone number: ")
    contacts[name] = phone

name = input("Enter contact name to delete: ")
if name in contacts:
    del contacts[name]

print("All contacts:")
for name, phone in contacts.items():
    print(name, ":", phone)


#29. Create a dictionary containing book IDs and book names. Implement add a book, search a book, remove a book, display all books and count total books.
books = {
    101: "Python Programming",
    102: "Java Programming",
    103: "Data Structures"
}

book_id = int(input("Enter book ID to add: "))
book_name = input("Enter book name: ")
books[book_id] = book_name

book_id = int(input("Enter book ID to search: "))
if book_id in books:
    print("Book:", books[book_id])
else:
    print("Book not found")

book_id = int(input("Enter book ID to remove: "))
if book_id in books:
    del books[book_id]

print("All books:")
for book_id, book_name in books.items():
    print(book_id, ":", book_name)

print("Total books:", len(books))


#30. Take a dictionary containing student names and their departments; create a new dictionary that groups students according to their department.
students = {
    "Amit": "Computer",
    "Rahul": "IT",
    "Sneha": "Computer",
    "Priya": "ENTC",
    "Neha": "IT",
    "Karan": "Computer"
}

departments = {}

for name, department in students.items():
    if department not in departments:
        departments[department] = []
    departments[department].append(name)

print(departments)
