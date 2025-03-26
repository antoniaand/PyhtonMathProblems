# PROBLEM 13 -------
# maximization function f{x=(x1,x2...x7) | xi in [-10, 10], x1+x2+..+x7 <= 10} -> R
# f(x) = a1x1 + a2x2 +... + a7x7 (a input)
# Generate 10 elements, display max quality and an individual with that quality
import numpy as np

def f13():
    matrix=[]
    a = []
    x=[]
    max_quality=-float('inf')
    print("Enter the 7 elements of vector a: ")
    for i in range(7):
      value = float(input(f"Enter element {i + 1}: "))
      a.append(value)
    for i in range(10):  # x=row
        while True:
            x = np.random.uniform(-10, 11, 7).tolist()
            if sum(x)<=10:
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

f13()