# PROBLEM 10 -----
# maximization function f: {x=(x1,x2...x10) | xi in {-1, 1}, x1 + x2 +... + x10 >= 0} -> R
# f(x) = a1x1 + a2x2 + a3x3 + ... + a10x10 (a given parameter)
# Generate a population with n elements (n input), evaluate them and display max quality
import numpy as np

def f10():
    size=int(input(f"Enter the size of the matrix: "))
    matrix=[]
    a = []
    x=[]
    max_quality=-float('inf')
    print("Enter the 10 elements of vector a: ")
    for i in range(10):
      value = float(input(f"Enter element {i + 1}: "))
      a.append(value)
    for i in range(size):  # x=row
        while True:
            x = np.random.uniform(-1, 2, 10).tolist()
            if sum(x)>=0:
                break
        f_x = np.dot(a, x)
        if f_x>max_quality:
            max_quality=f_x
        x.append(f_x)
        matrix.append(x)
    print("The  matrix is: " )
    for row in matrix:
        print(row)
    print("Maximum quality value is: ", max_quality)
    print("The vectors responsible are: ")
    for row in matrix:
        if row[-1]==max_quality:
           print(row)

f10()

