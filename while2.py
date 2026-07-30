
# AVERAGE PROGRAMS USING WHILE LOOP



# Write a PYTHON program to check the entered number is prime or not

print("--- 1. Check Prime Number ---")
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    i = 2
    is_prime = True
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

print("\n" + "="*40 + "\n")



# Write a PYTHON program to find the sum of digits of given number

print("--- 2. Sum of Digits ---")
num = int(input("Enter a number: "))
temp = num
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp //= 10

print("Sum of digits of", num, "is:", digit_sum)

print("\n" + "="*40 + "\n")



# Write a PYTHON program to check the entered number is palindrome or not

print("--- 3. Check Palindrome Number ---")
num = int(input("Enter a number: "))
temp = num
rev_num = 0

while temp > 0:
    digit = temp % 10
    rev_num = (rev_num * 10) + digit
    temp //= 10

if num == rev_num:
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")

print("\n" + "="*40 + "\n")



# Write a PYTHON program to reverse the given number

print("--- 4. Reverse Given Number ---")
num = int(input("Enter a number: "))
temp = num
rev_num = 0

while temp > 0:
    digit = temp % 10
    rev_num = (rev_num * 10) + digit
    temp //= 10

print("Reversed number is:", rev_num)





# Write a PYTHON program to print the multiplication table

print("--- 1. Multiplication Table ---")
num = int(input("Enter the number for multiplication table: "))
limit = int(input("Enter the limit: "))
i = 1

while i <= limit:
    print(f"{num} x {i} = {num * i}")
    i += 1

print("\n" + "="*40 + "\n")



# Write a PYTHON program to print the largest of n numbers

print("--- 2. Find Largest of N Numbers ---")
n = int(input("How many numbers do you want to enter? "))

if n <= 0:
    print("Please enter a valid count greater than 0.")
else:
    i = 1
    num = float(input(f"Enter number {i}: "))
    largest = num

    while i < n:
        i += 1
        num = float(input(f"Enter number {i}: "))
        if num > largest:
            largest = num

    print("The largest number is:", largest)

print("\n" + "="*40 + "\n")



# Write a PYTHON program to print smallest of n numbers

print("--- 3. Find Smallest of N Numbers ---")
n = int(input("How many numbers do you want to enter? "))

if n <= 0:
    print("Please enter a valid count greater than 0.")
else:
    i = 1
    num = float(input(f"Enter number {i}: "))
    smallest = num

    while i < n:
        i += 1
        num = float(input(f"Enter number {i}: "))
        if num < smallest:
            smallest = num

    print("The smallest number is:", smallest)
