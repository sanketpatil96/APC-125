"""7.	Accept 10 numbers from the user and store them in a list. Calculate:
•	Sum 
•	Average """
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
total_sum = sum(numbers)
average = total_sum / len(numbers)
print("Sum of the numbers:", total_sum)
print("Average of the numbers:", average)