#.  Write a short PYTHON program to check weather the 
#     square root of number is prime or  not.


n = int(input("Enter a number: "))

root = int(n ** 0.5)

if root * root != n:
    print("Square root is not an integer")
else:
    prime = True

    if root < 2:
        prime = False
    else:
        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

    if prime:
        print("Square root =", root)
        print("Prime")
    else:
        print("Square root =", root)
        print("Not Prime")
