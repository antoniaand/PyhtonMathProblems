# PROBLEM 15 ----
# Matrix with n rows (n input), each row with 10 elements
# binary vector of 9  + quality = sum of positions that contain 1 (starting pos is 0)
import numpy as np

def f15():
    matrix= []
    n = int(input("Enter number of elements in population: "))
    while len(matrix) < n:
        binary_v = []
        for i in range(9):
            binary_v.append(np.random.randint(0,1))
        quality = 0
        for j in range(9):
            if binary_v[j] == 1:
                quality += j
        binary_v.append(quality)
        matrix.append(binary_v)

    for binary_v in matrix:
        print(binary_v)

f15()