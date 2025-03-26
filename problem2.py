# PROBLEM 2
# Write a python function that generates a matrix (population) with 18 rows, each containing vectors with 6 elements:
# 5 bits representing an individual and an integer
# representing its quality. Calculate and display individuals with the highest quality value
import numpy as np
def f2():
    matrix = []
    max_quality = -float('inf')
    best_individuals = []
    for i in range(18):
        individual = np.random.randint(0, 2, 5)
        quality = np.sum(individual)
        row = np.append(individual, quality)
        matrix.append(row)
        if quality > max_quality:
            max_quality = quality
            best_individuals = [row]
        elif quality == max_quality:
            best_individuals.append(row)
    print("Generated population:")
    for row in matrix:
        print(row)
    print("\nIndividuals with the highest quality value:")
    for individual in best_individuals:
        print(individual)

f2()










