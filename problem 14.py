# PROBLEM 14 ---
# Matrix with 10 rows, each row has a permutation of size k (input)
# p[1] = 1, p[k] = k + quality
# quality = no. of elements i with p[i] < i
import  numpy as np
def f14():
   population = []
   k = int(input("Enter permutation size: "))
   for i in range(10):
     ind = np.random.permutation(k)
     ind[0] = 1
     ind[-1] = k
     quality = 0
     for j in range(k):
        if ind[j] < j + 1:
            quality += 1
     ind = np.append(ind, quality)
     population.append(ind)
   max_quality = 0
   for ind in population:
        if ind[-1] > max_quality:
            max_quality = ind[-1]
   print("Population: ")
   for ind in population:
        print(ind)
   print("\nCandidates with max quality: ")
   for ind in population:
     if ind[-1] == max_quality:
        print(ind)


f14()