# PROBLEM 12 ------
# Matrix with 10 rows, each row a binary vector with 8 elements
# 7 bits + quality (quality = nr. of 1 bits in odd positions)
# Calculate and display avg. quality
import numpy as np
def f12():
    matrix = []
    for i in range(10):
        row = []
        for j in range(7):
            row.append(np.random.randint(0,2))

        quality = 0
        for j in range(1,len(row),2):
            if row[j] == 1:
                quality += 1
        row.append(quality)
        matrix.append(row)
        print(row)
    avg_quality = 0
    for row in matrix:
        avg_quality += row[-1]
    avg_quality /= len(matrix)

    print("\nAverage quality for the matrix: ", avg_quality)

f12()