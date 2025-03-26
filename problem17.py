# PROBLEM 17-----
# A matrix with 10 rows, each row k+1 values:
# An individual vector of size k with integer elements  {1, 2, 3, 4, 5, 6}.
#The last element of the vector must be even.
#The quality of the individual is the product of its elements.
#Display individuals in ascending order of their qualities.
import numpy as np

def f17():
    k = int(input("Enter the size of the individual vector (k): "))
    matrix = []
    for i in range(10):
        while True:
            individual = np.random.choice([1, 2, 3, 4, 5, 6], k)
            if individual[-1] % 2 == 0:
                break
        quality = np.prod(individual)
        row = np.append(individual, quality)
        matrix.append(row)
    matrix.sort(key=lambda x: x[-1])
    print("Individuals and their qualities (ascending order):")
    for row in matrix:
        print(row)
f17()