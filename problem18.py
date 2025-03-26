#PROBLEM 18------
#f(x) = x1 + x2 + x3 + x4 - (x5 + x6 + x7 + x8), where xi ∈ [-1, 1] and x1 + x2 + x3 + x4 >= x5 + x6 + x7 + x8.
# Generate n elements from the solution space.
# Evaluate them and display the maximum quality.
import numpy as np

def f18():
    n = int(input("Enter the number of elements (n): "))
    matrix = []
    max_quality = -float('inf')

    for i in range(n):
        while True:
            x = np.random.uniform(-1, 1, 8)
            if sum(x[:4]) >= sum(x[4:]):
                break
        quality = sum(x[:4]) - sum(x[4:])
        row = np.append(x, quality)
        matrix.append(row)
        if quality > max_quality:
            max_quality = quality
    print("Generated individuals and their qualities:")
    for row in matrix:
        print(row)
    print("Maximum quality:", max_quality)
f18()