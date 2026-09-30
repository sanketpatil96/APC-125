# Create an array and display its elements.

from array import array

arr = array('i', [10, 20, 30, 40, 50])

print("Array:", arr)

# Find the sum of elements in an array.

from array import array

arr = array('i', [10, 20, 30, 40, 50])

total = 0

for n in arr:
    total += n

print("Sum:", total)

#  Copy the elements of one array into another array.

from array import array

arr1 = array('i', [10, 20, 30, 40, 50])
arr2 = array('i', [])

for n in arr1:
    arr2.append(n)

print("First array:", arr1)
print("Copied array:", arr2) 

# Find the position of a given element in an array.

from array import array

arr = array('i', [10, 20, 30, 40, 50])

target = int(input("Enter element: "))

if target in arr:
    print("Position:", arr.index(target))
else:
    print("Element not found")

# Search for an element in an array.

from array import array

arr = array('i', [10, 20, 30, 40, 50])

target = int(input("Enter element to search: "))

if target in arr:
    print("Element found")
else:
    print("Element not found")

# Find the common elements between two arrays.

from array import array

arr1 = array('i', [10, 20, 30, 40, 50])
arr2 = array('i', [30, 40, 50, 60, 70])

common = array('i', [])

for n in arr1:
    if n in arr2:
        common.append(n)

print("Common elements:", common)

# Calculate the average of elements in an array.

from array import array

arr = array('i', [10, 20, 30, 40, 50])

total = 0

for n in arr:
    total += n

average = total / len(arr)

print("Average:", average)

#Copy the elements of one array into another array.

from array import array

arr1 = array('i', [10, 20, 30, 40, 50])
arr2 = array('i', [])

for n in arr1:
    arr2.append(n)

print("First array:", arr1)
print("Copied array:", arr2)

#Find the second largest element in an array.

from array import array

arr = array('i', [10, 50, 30, 40, 20])

arr = array('i', sorted(arr))

print("Second largest:", arr[-2])

# Array built-in functions and methods

from array import array

arr = array('i', [10, 20, 30, 20, 40])

print("Length:", len(arr))

arr.append(50)
print("After append:", arr)

arr.insert(2, 25)
print("After insert:", arr)

arr.remove(20)
print("After remove:", arr)

arr.pop()
print("After pop:", arr)

print("Index of 30:", arr.index(30))

print("Count of 20:", arr.count(20))

arr.reverse()
print("After reverse:", arr)

arr.extend([60, 70])
print("After extend:", arr)

lst = arr.tolist()
print("List:", lst)
