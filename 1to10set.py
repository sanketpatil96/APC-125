#1. Write a Python program to create a set containing five integers and display all its elements.
numbers = {10, 20, 30, 40, 50}

print(numbers)


#2. Create a list containing duplicate values. Convert the list into a set and display the resulting set.
numbers = [10, 20, 10, 30, 20, 40, 30]

numbers = set(numbers)

print(numbers)


#3. Create a set of five fruits. Add two new fruits using appropriate set methods and display the updated set.
fruits = {"Apple", "Banana", "Mango", "Orange", "Grapes"}

fruits.add("Pineapple")
fruits.add("Watermelon")

print(fruits)


#4. Create a set of numbers and remove a specified number from the set.
numbers = {10, 20, 30, 40, 50}

num = int(input("Enter number to remove: "))

numbers.remove(num)

print(numbers)


#5. Create a set of student names. Ask the user to enter a name and check whether the student exists in the set.
students = {"Amit", "Rahul", "Sneha", "Priya", "Neha"}

name = input("Enter student name: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")


#6. Create a set of cities and determine the total number of cities using an appropriate function.
cities = {"Pune", "Mumbai", "Delhi", "Nashik", "Nagpur"}

print("Total number of cities:", len(cities))


#7. Create a set of programming languages and display each language using a for loop.
languages = {"Python", "Java", "C++", "JavaScript", "C"}

for language in languages:
    print(language)


#8. Create a list containing duplicate numbers, use a set to remove the duplicates.
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

numbers = set(numbers)

print(numbers)


#9. Create two sets of integers and find their union.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Union:", set1.union(set2))


#10. Create two sets and find the elements common to both sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Common elements:", set1.intersection(set2))
