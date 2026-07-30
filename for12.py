'''12. Write a PYTHON program to produce following design
      1
      2 2
      3 3 3
      4 4 4 4 
      5 5 5 5 5
      If user enters n value as 5
'''
n=int(input("Enter the Number:"))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()
