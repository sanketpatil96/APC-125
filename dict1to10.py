#1. Create a dictionary containing student details such as roll number, name, department, and marks. Display all key-value pairs.
student = {
    "Roll Number": 101,
    "Name": "Sanket",
    "Department": "Computer Engineering",
    "Marks": 85
}

for key, value in student.items():
    print(key, ":", value)


#2. Create a dictionary containing employee information and display the value associated with a specified key.
employee = {
    "ID": 101,
    "Name": "Amit",
    "Department": "IT",
    "Salary": 35000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")


#3. Create a dictionary of five products and their prices. Add a new product and price to the dictionary.
products = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Monitor": 12000,
    "Printer": 8000
}

products["Headphones"] = 2000

print(products)


#4. Create a dictionary containing student marks. Update the marks of a specified student.
marks = {
    "Amit": 75,
    "Rahul": 82,
    "Sneha": 90,
    "Priya": 85
}

name = input("Enter student name: ")
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks
    print(marks)
else:
    print("Student not found")


#5. Create a dictionary of cities and their populations. Remove a specified city from the dictionary.
cities = {
    "Pune": 7000000,
    "Mumbai": 20000000,
    "Delhi": 33000000,
    "Nashik": 1800000,
    "Nagpur": 3000000
}

city = input("Enter city to remove: ")

if city in cities:
    cities.pop(city)
    print(cities)
else:
    print("City not found")


#6. Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.
employees = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya",
    105: "Neha"
}

employee_id = int(input("Enter employee ID: "))

if employee_id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")


#7. Create a dictionary containing student records and find the total number of key-value pairs.
students = {
    101: "Amit",
    102: "Rahul",
    103: "Sneha",
    104: "Priya",
    105: "Neha"
}

print("Total number of key-value pairs:", len(students))


#8. Create a dictionary and display all keys, all values and all key-value pairs.
student = {
    "Roll Number": 101,
    "Name": "Sanket",
    "Department": "Computer Engineering",
    "Marks": 85
}

print("Keys:", student.keys())
print("Values:", student.values())
print("Key-value pairs:", student.items())


#9. Create a dictionary of programming languages and their creators. Display each key and value using a loop.
languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

for key, value in languages.items():
    print(key, ":", value)


#10. Accept five student names and their marks from the user and store them in a dictionary.
students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Student dictionary:", students)
