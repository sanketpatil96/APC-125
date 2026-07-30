'''Write a PYTHON program to print the natural numbers up to n
'''
n=int(input("Enter the value for natural numbers:"))
i=0
while(i<=n):
    print(i)

    i+=1
'''Write a PYTHON program to print even numbers up to n

'''
n=int(input("Enter the value for even numbers:"))
i=0
while(i<=n):
    print(i)

    i+=2
'''Write a PYTHON program to print odd numbers up to n
'''
n=int(input("Enter the value for odd numbers:"))
i=1
while(i<=n):
    print(i)

    i+=2
'''Write a PYTHON program to print sum of natural numbers up to n
'''
n=int(input("Enter the limit for sum of natural numbers:"))
s=0
i=0
while(i<=n):
    s+=i
    i+=1
print("Sum of the natural numbers upto",n,"is:",s)
