#25.	Remove all duplicate elements while preserving the original order.
list1 = [10, 20, 10, 30, 20, 40, 50, 30]
new_list = []

for i in list1:
    if i not in new_list:
        new_list.append(i)

print("Original List :", list1)
print("New List      :", new_list)