# PROBLEM 9 -------
# Matrix with 10 rows with k+1 elements (k input)
# 0,1 possibilities-- if 0,0 or 1,1 consecutive order, and equal +=quality
# display generated individuals in ascending quality order


import numpy as np
def f9():
    k=int(input(f"Enter the number of elements on each row: ") )
    matrix=[]
    for i in range(10):
        row=np.random.randint(0,2,k).tolist()
        quality=0
        for j in range(k):
            for c in range(j+1,k):
                if row[j]==row[c]:
                    quality+=1
        row.append(quality)
        matrix.append(row)
    print("\nThe initial matrix is: ")
    for row in matrix:
        print(row)
    matrix=sorted(matrix, key=lambda row: row[-1])
    print("\nThe ascending sorted matrix based on the quality is:")
    for row in matrix:
        print(row)
f9()

