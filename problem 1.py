#PROBLEM 1
#Write a Python function to implement the maximization function f:
#f: { (x,y,z)/x,y,z belongs to the vector space [-2,7]; x+y+z<10 }  with values in--> R domain
#f(x,y,z)=x^2-2yz
#Generate 20 elements from the solution space(solution candidates), evaluate them, and display the obtained values.
import numpy as np
def f1():
    matrix = []
    for _ in range(20):
        while True:
            x = np.random.uniform(-2, 7)
            y = np.random.uniform(-2, 7)
            z = np.random.uniform(-2, 7)
            if x + y + z < 10:
                break
        f_x_y_z = x**2 - 2 * y * z
        row = [x, y, z, f_x_y_z]
        matrix.append(row)
    print("Generated elements and their values:")
    for row in matrix:
        print(row)

f1()



































