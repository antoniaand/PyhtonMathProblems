# PROBLEM 8 ------
# Matrix with 10 rows - each row contains k+1 values
# a) k values from interval [-4, 4] (integers) and sum of elements is positive
# b)  quality = sum of absolute values in row, if k=3 and x=[2,4,-3] feasible, quality=9 ( *(-1) odd numbers )
#calculate and display the weakest individuals: min quality
import numpy as np
def f8():
    size = int(input(f"\nInput the size of the matrix : "))
    matrix=[]
    sum_vector=[]
    abs_sum_vector=[]
    for i in range(10):
        while True:
            row = np.random.randint(-4, 5, size).tolist()
            if sum(row) > 0:
                break
        sum_vector.append(sum(row))
        quality=0
        for c in range(size):
            if row[c]>=0:
                quality+=row[c]
            else:
                quality+=row[c]*(-1)
        abs_sum_vector.append(quality)
        row.append(quality)
        matrix.append(row)
    print("\nThe matrix is: ")
    for row in matrix:
        print(row)
    print(f"\nThe sum of elements vector: ", sum_vector)
    print(f"\nThe quality( absolut sum of elements ) vector: ", abs_sum_vector)
    min_quality = min(row[-1] for row in matrix)
    print("\nThe minimum quality is: ", min_quality)

f8()

