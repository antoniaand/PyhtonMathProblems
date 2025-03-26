#PROBLEM 19--------
# Generate a matrix with n rows.
# A permutation of size 6 where the value 1 does not appear in the first half.
# The quality of a permutation P is the sum of the positions (starting from 0) where even values appear.
# Evaluate the n generated individuals and display the maximum quality.
import numpy as np
def f19():
    n = int(input("Enter the number of rows (n): "))
    matrix = []
    max_quality = 0
    for i in range(n):
        while True:
            permutation = np.random.permutation(6)
            if 1 not in permutation[:3]:
                break
        quality = sum(i for i, val in enumerate(permutation) if val % 2 == 0)
        row = np.append(permutation, quality)
        matrix.append(row)
        if quality > max_quality:
            max_quality = quality
    print("Generated permutations and their qualities:")
    for row in matrix:
        print(row)
    print("Maximum quality:", max_quality)
f19()