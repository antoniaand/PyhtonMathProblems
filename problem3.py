# PROBLEM 3
# Write a python fct to implement the maximization function f: { x = (x1...x10) | xi in [-1, 1], x1 + ... + x9 = 1 - x10 } -> R
# f(x) = a1*x1 + a2*x2 + ... + a10 * x10  where a=(a1..a10) is a vector given as INPUT
#Generate 10 elements from the solution space, evaluate them and display the average obtained value )

import numpy as np
def f3():
    a=[]
    vectors_x=[]
    f_x_values=[]
    print("Enter the 10 elements of vector 'a':")
    for i in range(10):
        while True:
            try:
                value = float(input(f"Enter element {i + 1}: "))
                a.append(value)
                break
            except ValueError:
                print("Invalid input")

    for i in range(10):
        while True:
          x= np.random.uniform(-1,1, 9)
          x10 = 1- np.sum(x)
          if -1 <= x10 <= 1:
              break

        x=np.append(x,x10)
        vectors_x.append(x)

        f_x= np.dot(a,x)
        f_x_values.append(f_x)

    average_value=np.mean(f_x_values)

    print("\nGenerated vectors: ")
    for i, x in enumerate(vectors_x):
        print(f"Vector {i+1}: {x}")
    print("\nFunction Values:")
    for i, f_x in enumerate(f_x_values):
        print(f"f(x{i + 1}) = {f_x}")
    print(f"\nAverage Function Value: {average_value}")

f3()





