'''. Write a PYTHON program to produce following  
      design
      1
      1 2
      1 2 3
      1 2 3 4
      1 2 3 4 5
      If user enters n value as 5
'''
n=int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
