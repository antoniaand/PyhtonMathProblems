# PROBLEM 4 -------
# Write a Python function that generates a matrix with 15 rows, each containing
# a permutation of size k (input parameter) and a value representing the quality of
# the permutation. The quality of an individual permutation is given by the number of
# pairs (i,j), i<j, for which P(i) - P(j) is an even number
# Evaluate the n generated individuals and display the max quality value
import numpy as np
def f4():
    size = int(input(f"\nInput the size of each permutation : ") )
    matrix=[]
    maxi_value=0
    for i in range(15):
        row=np.random.permutation(size).tolist()
        quality=0
        for i in range(size):
            for j in range(i+1, size):
              if (row[i]-row[i+1])%2==0:
                 quality+=1
        row.append(quality)
        matrix.append(row)
        if quality>maxi_value:
         maxi_value=quality
    print("\nThe permutations are: ")
    for row in matrix:
        print(row)
    print("\nThe maximum value of the quality of the above permutations is: ", maxi_value)
    for row in matrix:
        if row[-1]==maxi_value:
            print("\nThe permutation", row[:-1], "The quality: ", row[-1])

f4()




