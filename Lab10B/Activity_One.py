# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Mose Butler      128004413
# Section:        535
# Assignment:     Lab 10B - Program 1
# Date:           10/25/2018

import numpy as np
import matplotlib.pyplot as plt

# Function to multiply two matrices together
def matrixMultiplier (x, y):
    pointPrime = y @ x
    return pointPrime


# Sets up graph before plotting
plt.title("Multiplying Matrices")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Sets up arrays to hold points to be graphed
xPoints = np.array([1])
yPoints = np.array([0])

# Original matrices based on lab assignment
vectorMatrix = np.array([1, 0]).reshape(2, 1)
matrixM = np.array([(1.00583, -0.087156), (0.087156, 1.00583)])

# Random iterable between 150-250
iterable = np.random.randint(150, 250)
print(iterable)

# Find points for graph
# finds original product matrix, makes using loops for rest of the work easier.
primeMatrix = matrixMultiplier(vectorMatrix, matrixM)
# Finds points from position 2 to iterable and appends to lists.
for i in range(iterable):
    primeMatrix = matrixMultiplier(primeMatrix, matrixM)
    xPoints = np.hstack((xPoints, primeMatrix[0]))
    yPoints = np.hstack((yPoints, primeMatrix[1]))

# Plots points based on lists and shows graph.
plt.plot(xPoints, yPoints, linewidth = 2.0)
plt.show()

