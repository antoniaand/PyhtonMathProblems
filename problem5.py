# PROBLEM 5 ------
# Matrix with n rows (input n), each row containing a binary vector of size 8
# (odd nr. of 1) and the quality of each sequence
# quality = decimal value of binary representation , display the highest quality
import numpy as np
def f5():
  size=int(input(f"\nThe size of the matrix: "))
  matrix=[]
  highest_quality=0
  for i in range(size):
   row=np.random.randint(0,2,8).tolist()

   if row.count(1) % 2 == 0:
     row[row.index(1)]=0

   decimal=int(''.join(map(str, row)),2) #tensform into binary, and then the binary into decimal with the base 2
   row.append(decimal)
   matrix.append(row)

   if decimal>highest_quality:
     highest_quality=decimal
  print("\nThe matrix: ")
  for row in matrix:
      print(row)
  print("\nThe highest quality is: ",highest_quality)

f5()