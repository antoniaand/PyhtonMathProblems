# PROBLEM 11 ----
# maximization function f: (x,y,z,t) | x,y,z,t in [-2,2], t = x+y-z} -> R
# f(x,y,z) = t * x^2 - 2yz
# Generate n elements (n input) and display max quality
import numpy as np
def f11():
    n = int(input(f"Enter the size of the matrix: "))
    matrix = []
    max_quality = 0
    while len(matrix) < n:
        x = np.random.uniform(-2, 3)
        y = np.random.uniform(-2, 3)
        z = np.random.uniform(-2, 3)
        t = x + y - z
        f_x_y_z = t*x**2 - 2*y*z
        if f_x_y_z > max_quality:
            max_quality = f_x_y_z
        row=[x, y, z, t, f_x_y_z]
        matrix.append(row)
    print("The matrix is:")
    for i in matrix:
        print(row)
        print("\n f(x,y,z) = ", row[-1])
    print("The maximum quality is: ", max_quality)

f11()