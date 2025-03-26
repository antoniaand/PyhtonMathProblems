# EX 6 ------
# Matrix with n rows (input), each row containing a permutation of size 8
# and a value representing the quality
# quality = no. pairs (i,j) i<j, for which P[i] = j and P[j] = i
# Evaluate the n generated individuals and display the maximum quality value
import numpy as np
def f6():
    size=int(input("\nThe size of the matrix: "))
    matrix=[]
    maxi_quality=0
    for i in range(size):
        quality=0
        row=np.random.permutation(8).tolist()
        for k in range(8):
            for j in range(k+1,8):
                if row[k]==j and row[j]==k:
                    quality+=1
        if quality>maxi_quality:
            maxi_quality=quality
        row.append(quality)
        matrix.append(row)
    print("\nThe matrix is: ")
    for row in matrix:
        print(row)
    print("\nThe maximum quality value is: ",maxi_quality)
f6()