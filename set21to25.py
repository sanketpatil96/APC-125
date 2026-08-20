#21. Find students enrolled in both courses and students enrolled in only one course.
python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Rahul", "Priya", "Neha", "Karan"}

print("Students enrolled in both courses:", python_students.intersection(java_students))
print("Students enrolled in only one course:", python_students.symmetric_difference(java_students))


#22. Create two sets representing technical skills of two employees. Find common skills, skills unique to Employee 1, skills unique to Employee 2 and all available skills.
employee1 = {"Python", "SQL", "Git", "Java"}
employee2 = {"Python", "JavaScript", "Git", "Linux"}

print("Common skills:", employee1.intersection(employee2))
print("Skills unique to Employee 1:", employee1.difference(employee2))
print("Skills unique to Employee 2:", employee2.difference(employee1))
print("All available skills:", employee1.union(employee2))


#23. Create a set containing available books and another set containing requested books. Determine which requested books are available.
available_books = {"Python Basics", "Java Programming", "Data Structures", "Operating Systems"}
requested_books = {"Python Basics", "Data Structures", "Computer Networks", "Java Programming"}

print("Requested books that are available:", requested_books.intersection(available_books))


#24. Store visitor IDs from two different days in separate sets. Determine unique visitors across both days, returning visitors, visitors who came only on the first day and visitors who came only on the second day. Create sets representing products belonging to different categories and find products that belong to both categories.
day1 = {101, 102, 103, 104, 105}
day2 = {103, 104, 105, 106, 107}

print("Unique visitors across both days:", day1.union(day2))
print("Returning visitors:", day1.intersection(day2))
print("Visitors only on the first day:", day1.difference(day2))
print("Visitors only on the second day:", day2.difference(day1))

category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Keyboard", "Monitor", "Printer", "Scanner"}

print("Products belonging to both categories:", category1.intersection(category2))


#25. Represent the friends of two users using sets. Find mutual friends, friends unique to User 1, friends unique to User 2 and total unique friends.
user1 = {"Amit", "Rahul", "Sneha", "Priya", "Karan"}
user2 = {"Rahul", "Priya", "Neha", "Karan", "Riya"}

print("Mutual friends:", user1.intersection(user2))
print("Friends unique to User 1:", user1.difference(user2))
print("Friends unique to User 2:", user2.difference(user1))
print("Total unique friends:", len(user1.union(user2)))
