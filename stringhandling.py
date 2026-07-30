# 1. String Length: Input a string and display its length without using the len() function.
text = input("Enter a string: ")
length = 0
for char in text:
    length += 1
print("Length of string:", length)


# 2. Character Count: Count the number of vowels, consonants, digits, spaces, and special characters in a given string.
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_count = c_count = d_count = s_count = sp_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1
    elif char.isdigit():
        d_count += 1
    elif char.isspace():
        s_count += 1
    else:
        sp_count += 1

print(f"Vowels: {v_count}, Consonants: {c_count}, Digits: {d_count}, Spaces: {s_count}, Special: {sp_count}")


# 3. Reverse a String: Reverse the given string without using built-in reverse functions.
text = input("Enter a string: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed String:", reversed_text)


# 4. Palindrome Check: Check whether the entered string is a palindrome.
text = input("Enter a string: ")
rev_text = ""
for char in text:
    rev_text = char + rev_text

if text.lower() == rev_text.lower():
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")


# 5. Uppercase and Lowercase Count: Count the number of uppercase and lowercase letters in a string.
text = input("Enter a string: ")
upper_cnt = 0
lower_cnt = 0

for char in text:
    if char.isupper():
        upper_cnt += 1
    elif char.islower():
        lower_cnt += 1

print(f"Uppercase: {upper_cnt}, Lowercase: {lower_cnt}")


# 6. Replace Characters: Replace all occurrences of a given character with another character.
text = input("Enter main string: ")
target = input("Enter character to replace: ")
new_char = input("Enter new character: ")

result = ""
for char in text:
    if char == target:
        result += new_char
    else:
        result += char

print("Updated String:", result)


# 7. Remove Spaces: Remove all spaces from the input string.
text = input("Enter a sentence: ")
no_spaces = ""

for char in text:
    if char != " ":
        no_spaces += char

print("String without spaces:", no_spaces)


# 8. Frequency of a Character: Find the number of times a specified character appears in a string.
text = input("Enter string: ")
target = input("Enter character to search: ")
count = 0

for char in text:
    if char == target:
        count += 1

print(f"Character '{target}' appears {count} times.")


# 9. First and Last Character: Print the first and last character of a string.
text = input("Enter a string: ")

if len(text) > 0:
    print("First Character:", text[0])
    print("Last Character:", text[-1])
else:
    print("String is empty.")


# 10. ASCII Values: Display each character of a string along with its ASCII value.
text = input("Enter a string: ")

for char in text:
    print(f"'{char}' -> ASCII: {ord(char)}")


# 11. Word Count: Count the total number of words in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total number of words:", len(words))


# 12 and 13. Longest and Shortest Word: Find the longest and shortest word in a sentence.
sentence = input("Enter a sentence: ")
words = sentence.split()

if words:
    longest = words[0]
    shortest = words[0]
    
    for word in words:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word

    print("Longest Word:", longest)
    print("Shortest Word:", shortest)


# 14. Title Case: Convert the first letter of every word to uppercase.
sentence = input("Enter a sentence: ")
words = sentence.split()
title_words = []

for word in words:
    capitalized = word[0].upper() + word[1:].lower()
    title_words.append(capitalized)

print("Title Case Result:", " ".join(title_words))


# 15. Duplicate Characters: Print all duplicate characters in a string.
text = input("Enter a string: ")
duplicates = []

for char in text:
    if text.count(char) > 1 and char not in duplicates:
        duplicates.append(char)

print("Duplicate characters:", duplicates)


# 16. Character Frequency: Display the frequency of every character in a string.
text = input("Enter a string: ")
freq_dict = {}

for char in text:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1

for char, freq in freq_dict.items():
    print(f"'{char}': {freq}")


# 17. Anagram Check: Check whether two strings are anagrams.
s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("The strings are Anagrams.")
else:
    print("The strings are NOT Anagrams.")


# 18. Remove Duplicate Characters: Remove duplicate characters while maintaining the original order.
text = input("Enter a string: ")
unique_str = ""

for char in text:
    if char not in unique_str:
        unique_str += char

print("String without duplicates:", unique_str)


# 19. Substring Search: Check whether a given substring exists in the main string.
main_str = input("Enter main string: ")
sub_str = input("Enter substring to search: ")

if sub_str in main_str:
    print(f"'{sub_str}' exists in the main string.")
else:
    print(f"'{sub_str}' does NOT exist in the main string.")


# 20. Count Occurrences of a Word: Count how many times a specific word appears in a sentence.
sentence = input("Enter sentence: ")
target_word = input("Enter word to count: ")

words = sentence.split()
count = 0
for word in words:
    if word.lower() == target_word.lower():
        count += 1

print(f"The word '{target_word}' appears {count} times.")


# 21. Password Validator: Validate a password (min 8 chars, upper, lower, digit, special char).
pwd = input("Enter password to validate: ")

has_upper = has_lower = has_digit = has_special = False
special_chars = "!@#$%^&*()-_+=[]{}|;:,.<>?"

if len(pwd) >= 8:
    for char in pwd:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

if len(pwd) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Valid Password!")
else:
    print("Invalid Password.")


# 22 and 23. Run-Length Encoding and String Compression: Compress repeated characters.
text = input("Enter string to compress: ")

if len(text) == 0:
    compressed = ""
else:
    compressed = ""
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            compressed += text[i-1] + str(count)
            count = 1
    compressed += text[-1] + str(count)

if len(compressed) < len(text):
    print("Compressed String:", compressed)
else:
    print("Original String:", text)


# 24 and 25. Most and Second Most Frequent Character: Find character with highest and second highest frequency.
text = input("Enter string: ").replace(" ", "")

freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_freq) >= 1:
    print("Most Frequent Character:", sorted_freq[0][0])
if len(sorted_freq) >= 2:
    print("Second Most Frequent Character:", sorted_freq[1][0])


# 26. Caesar Cipher: Encrypt and decrypt a message using Caesar Cipher algorithm.
msg = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = ""
for char in msg:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        encrypted += chr((ord(char) - start + shift) % 26 + start)
    else:
        encrypted += char

print("Encrypted Message:", encrypted)


# 27. Email Validator: Validate whether a given email address follows a valid format.
email = input("Enter email address: ")

if "@" in email and "." in email:
    at_index = email.find("@")
    dot_index = email.rfind(".")
    if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email) - 1:
        print("Valid Email Address Format.")
    else:
        print("Invalid Email Address Format.")
else:
    print("Invalid Email Address Format.")


# 28. Word Frequency Dictionary: Count the frequency of every word in a paragraph.
para = input("Enter a paragraph: ")
words = para.lower().split()

word_freq = {}
for word in words:
    clean_word = word.strip(".,!?\"'")
    word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

print("Word Frequencies:")
for w, f in word_freq.items():
    print(f"'{w}': {f}")


# 29. Sentence Reversal: Reverse the order of words in a sentence without changing the words themselves.
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = " ".join(words[::-1])

print("Output:", reversed_sentence)


# 30. String Rotation: Check whether one string is a rotation of another.
s1 = input("Enter original string: ")
s2 = input("Enter rotated string: ")

if len(s1) == len(s2) and len(s1) > 0:
    temp = s1 + s1
    if s2 in temp:
        print("Output: Yes")
    else:
        print("Output: No")
else:
    print("Output: No")
