"""19.	Store names of students present in class.
Display:
•	Total students 
•	Search a student's attendance 
•	Add a new student 
•	Remove an absent student 
"""
students = []

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Display Total Students")
    print("4. Remove Student")
    print("5. Display Student List")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        students.append(name)
        print(name, "added successfully.")

    elif choice == 2:
        name = input("Enter student name to search: ")
        if name in students:
            print(name, "is present in the class.")
        else:
            print(name, "is absent.")

    elif choice == 3:
        print("Total Students:", len(students))

    elif choice == 4:
        name = input("Enter absent student's name: ")
        if name in students:
            students.remove(name)
            print(name, "removed successfully.")
        else:
            print("Student not found.")

    elif choice == 5:
        print("Students Present:", students)

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")