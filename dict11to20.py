#11. Create a dictionary containing student names and marks. Find the student who has scored the highest marks.
students = {
    "Amit": 78,
    "Rahul": 92,
    "Sneha": 85,
    "Priya": 88,
    "Neha": 76
}

highest = 0
student = ""

for name, marks in students.items():
    if marks > highest:
        highest = marks
        student = name

print("Highest marks:", highest)
print("Student:", student)


#12. Create a dictionary containing student names and marks. Find the student with the lowest marks.
students = {
    "Amit": 78,
    "Rahul": 92,
    "Sneha": 85,
    "Priya": 88,
    "Neha": 76
}

lowest = list(students.values())[0]
student = ""

for name, marks in students.items():
    if marks < lowest:
        lowest = marks
        student = name

print("Lowest marks:", lowest)
print("Student:", student)


#13. Create a dictionary containing student names and marks. Calculate the average marks of all students.
students = {
    "Amit": 78,
    "Rahul": 92,
    "Sneha": 85,
    "Priya": 88,
    "Neha": 76
}

total = sum(students.values())
average = total / len(students)

print("Average marks:", average)


#14. Accept a string from the user and create a dictionary containing each character and its frequency.
text = input("Enter a string: ")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)


#15. Accept a sentence and create a dictionary containing each word and the number of times it occurs.
sentence = input("Enter a sentence: ")

words = sentence.split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)


#16. Create two dictionaries and merge them into a single dictionary.
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "D": 40,
    "E": 50,
    "F": 60
}

merged = dict1.copy()
merged.update(dict2)

print("Merged dictionary:", merged)


#17. Given two dictionaries, find the keys that are common to both dictionaries.
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

dict2 = {
    "C": 50,
    "D": 60,
    "E": 70,
    "F": 80
}

common_keys = dict1.keys() & dict2.keys()

print("Common keys:", common_keys)


#18. Given two dictionaries, identify the values that are common to both dictionaries.
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30,
    "D": 40
}

dict2 = {
    "E": 30,
    "F": 40,
    "G": 50,
    "H": 60
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common values:", common_values)


#19. Create a dictionary containing duplicate values and remove duplicate values while retaining the corresponding keys where appropriate.
students = {
    "Amit": 80,
    "Rahul": 90,
    "Sneha": 80,
    "Priya": 95,
    "Neha": 90
}

unique_students = {}
values = set()

for name, marks in students.items():
    if marks not in values:
        unique_students[name] = marks
        values.add(marks)

print("Dictionary after removing duplicate values:", unique_students)


#20. Create a dictionary and display its elements in ascending order of keys.
students = {
    "Rahul": 85,
    "Amit": 90,
    "Sneha": 78,
    "Priya": 92,
    "Neha": 88
}

sorted_students = dict(sorted(students.items()))

for key, value in sorted_students.items():
    print(key, ":", value)
