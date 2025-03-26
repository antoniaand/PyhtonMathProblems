# PROBLEM 7 ------
# Generates a matrix with n rows (n input)
# row: vector of size 8 with elements from {1, 2, 3, 4}
# value at 5th position is odd
# quality = product of the elements (9th pos)
import numpy as np
def f7():
    size=int(input(f"Enter the size of the matrix: "))
    matrix=[]
    for i in range(size):
        row = np.random.randint(1, 5, 8).tolist()
        quality=1
        if row[4]%2==0:
                row[4]-=1
        for j in range(8):
         quality=quality*row[j]
        row.append(quality)
        matrix.append(row)
    print("\nThe matrix is: ")
    for row in matrix:
        print(row)

    min_quality = min(row[-1] for row in matrix)

    print("\nThe minimum quality is: ", min_quality)

f7()
