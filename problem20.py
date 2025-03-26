#PROBLEM 20-------
# Generate a matrix with 10 rows.
#Each row contains an individual vector of size 6 with integer elements from the set {-2, -1, 0, 1, 2, 3, 4}.
# sum of the elements must be less than 10.
#The quality of the individual is the product of the absolute values of its elements.
#Display in reverse order of their qualities.
import numpy as np
def f20():
    matrix = []
    for i in range(10):
        while True:
            individual = np.random.choice([-2, -1, 0, 1, 2, 3, 4], 6)
            if sum(individual) < 10:
                break
        quality = np.prod(np.abs(individual))
        row = np.append(individual, quality)
        matrix.append(row)
    matrix.sort(key=lambda x: x[-1], reverse=True)
    print("Generated individuals and their qualities (in reverse order):")
    for row in matrix:
        print(row)
f20()