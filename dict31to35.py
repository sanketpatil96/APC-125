#31. Take a list of words, create a dictionary where the key is the word length and the value is a list of words having that length.
words = ["apple", "cat", "banana", "dog", "grape", "sun"]

result = {}

for word in words:
    length = len(word)
    if length not in result:
        result[length] = []
    result[length].append(word)

print(result)


#32. Take a list of integers and a target value, find two numbers whose sum is equal to the target using a dictionary.
numbers = [2, 7, 11, 15, 5, 3]

target = int(input("Enter target: "))

data = {}
found = False

for num in numbers:
    diff = target - num
    if diff in data:
        print("Numbers are:", diff, num)
        found = True
        break
    data[num] = True

if not found:
    print("No pair found")


#33. Take a string, use a dictionary to find the first character that occurs only once.
text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in text:
    if freq[ch] == 1:
        print("First non-repeating character:", ch)
        break


#34. Take a string, use a dictionary to find the first character that occurs more than once.
text = input("Enter a string: ")

freq = {}

for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in text:
    if freq[ch] > 1:
        print("First repeating character:", ch)
        break


#35. Accept a paragraph and create a dictionary where key = word length and value = number of words having that length.
paragraph = input("Enter a paragraph: ")

words = paragraph.split()
result = {}

for word in words:
    length = len(word)
    if length in result:
        result[length] += 1
    else:
        result[length] = 1

print(result)
