#17.	Create two 3 × 3 matrices using nested lists and perform matrix addition.
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

print("Matrix A:")
for row in A:
    print(row)
print("\nMatrix B:")
for row in B:
    print(row)

# Matrix addition
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
print("\nResultant Matrix after addition:")
for row in result:
    print(row)