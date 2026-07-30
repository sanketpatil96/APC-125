#Write a PYTHON program to print even numbers up to n
n=int(input("Enter the number:"))
for i in range(n+1):
    if i%2==0:
        print(i)
