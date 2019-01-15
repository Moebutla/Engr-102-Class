# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler UIN 128004413
# Section:		535
# Assignment:	Lab 7b - Program 1
# Date:		    10/11/18

from math import *

# Asks user for number of dimensions vectors are in.
numberDimensions = int(input("Enter how many dimensions your vector has: "))

# loop asks for vector components for how many dimensions they input.
componentsA = []
componentsB = []
for i in range(numberDimensions):
    componentsA.append(float(input("Enter the components of vector A one at a time: ")))
for j in range(numberDimensions):
    componentsB.append(float(input("Enter the components of vector B one at a time: ")))

# Algorithm to find magnitude of vectors
squaredComponentsA = []
squaredComponentsB = []

for i in range(numberDimensions):
    squaredComponentsA.append(componentsA[i] ** 2)

magnitudeA = sqrt(sum(squaredComponentsA))
print("Magnitude A = ", magnitudeA)

for j in range(numberDimensions):
    squaredComponentsB.append(componentsB[j] ** 2)

magnitudeB = sqrt(sum(squaredComponentsB))
print("Magnitude B = ", magnitudeB)

# loop finds vector a + vector b
vectorAddition = []

for i in range(numberDimensions):
    vectorAddition.append(componentsA[i] + componentsB[i])
print("Vector A + Vector B =", vectorAddition)

# loop finds vector a - vector b
vectorSubtraction = []

for i in range(numberDimensions):
    vectorSubtraction.append(componentsA[i] - componentsB[i])
print("Vector A - Vector B =", vectorSubtraction)

# loops finds dot product of vectors
vectorDotProduct = []

for i in range(numberDimensions):
    vectorDotProduct.append(componentsA[i] * componentsB[i])
print("The Dot Product is:", sum(vectorDotProduct))
