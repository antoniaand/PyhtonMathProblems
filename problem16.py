# PROBLEM 16 ---
# Generate a matrix with n rows.
# Each row contains a permutation of size 7 and its quality.
# The quality of a permutation P is the number of pairs (i, i+1) where P[i] = i+1 and P[i+1] = i.
# valuate the n generated individuals and display the maximum quality.
import numpy as np

def f16():
    n = int(input("Enter the number of rows (n): "))
    matrix = []
    max_quality = 0
    for j in range(n):
        permutation = np.random.permutation(7) + 1
        quality = 0
        for i in range(6):
            if permutation[i] == i + 2 and permutation[i + 1] == i + 1:
                quality += 1
        row = np.append(permutation, quality)
        matrix.append(row)
        if quality > max_quality:
            max_quality = quality
    print("Generated permutations and their qualities:")
    for row in matrix:
        print(row)
    print("Maximum quality:", max_quality)
f16()