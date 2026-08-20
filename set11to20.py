#11. Create two sets and find the elements present in the first set but not the second and the elements present in the second set but not the first.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("First set but not second:", set1.difference(set2))
print("Second set but not first:", set2.difference(set1))


#12. Create two sets of numbers and find the elements that are present in either set but not in both.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("Elements in either set but not both:", set1.symmetric_difference(set2))


#13. Create two sets and determine whether the first set is a subset of the second set.
set1 = {10, 20, 30}
set2 = {10, 20, 30, 40, 50}

print("First set is subset of second:", set1.issubset(set2))


#14. Create two sets and determine whether the first set is a superset of the second set.
set1 = {10, 20, 30, 40, 50}
set2 = {10, 20, 30}

print("First set is superset of second:", set1.issuperset(set2))


#15. Write a program to determine whether two sets have no elements in common.
set1 = {10, 20, 30}
set2 = {40, 50, 60}

print("Sets have no elements in common:", set1.isdisjoint(set2))


#16. Create two sets and check whether they are equal.
set1 = {10, 20, 30, 40}
set2 = {40, 30, 20, 10}

if set1 == set2:
    print("Sets are equal")
else:
    print("Sets are not equal")


#17. Two students have selected different subjects. Store their subjects in two sets and determine the subjects studied by both students.
student1 = {"Python", "Java", "DBMS", "CN"}
student2 = {"Python", "C++", "DBMS", "OS"}

print("Subjects studied by both students:", student1.intersection(student2))


#18. Accept a sentence from the user and use a set to display all unique words.
sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words:", words)


#19. Create two sets representing students present in the morning session and afternoon session. Find students present in both sessions, only in the morning, only in the afternoon and at least one session.
morning = {"Amit", "Rahul", "Sneha", "Priya"}
afternoon = {"Sneha", "Priya", "Neha", "Karan"}

print("Students present in both sessions:", morning.intersection(afternoon))
print("Students present only in morning:", morning.difference(afternoon))
print("Students present only in afternoon:", afternoon.difference(morning))
print("Students present in at least one session:", morning.union(afternoon))


#20. Create sets representing students enrolled in Python and Java.
python_students = {"Amit", "Rahul", "Sneha", "Priya"}
java_students = {"Rahul", "Priya", "Neha", "Karan"}

print("Students enrolled in Python:", python_students)
print("Students enrolled in Java:", java_students)
