# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		 Mose Butler
# UIN:          128004413
# Section:      535
# Assignment:   Lab 3b-2
# Date:		    09/19/18

from math import *

# User declared variables declaring observer positions, point A position, point B position. All in (x,y,z)
observerX_position = float(input("Input Observers \"X\" position: "))
observerY_position = float(input("Input Observers \"Y\" position: "))
observerZ_position = float(input("Input Observers \"Z\" position: "))



pntA_Xposition = float(input("Input Point A \"X\" position: "))
pntA_Yposition = float(input("Input Point A \"Y\" position: "))
pntA_Zposition = float(input("Input Point A \"Z\" position: "))



pntB_Xposition = float(input("Input Point B \"X\" position: "))
pntB_Yposition = float(input("Input Point B \"Y\" position: "))
pntB_Zposition = float(input("Input Point B \"Z\" position: "))



## Moves angle AOB to origin - note: from here on observer is calculated as if sitting at (0,0,0) no matter
##  the original input
# Point A
originAx = pntA_Xposition - observerX_position
originAy = pntA_Yposition - observerY_position
originAz = pntA_Zposition - observerZ_position
# Point B
originBx = pntB_Xposition - observerX_position
originBy = pntB_Yposition - observerY_position
originBz = pntB_Zposition - observerZ_position


# Finds magnitude of vector A
magnitudeA = sqrt(originAx**2 + originAy**2 + originAz**2)

# Finds magnitude of vector B
magnitudeB = sqrt(originBx**2 + originBy**2 + originBz**2)

# Normalizes Vector A (x,y,z)
normalizedAx = originAx / magnitudeA
normalizedAy = originAy / magnitudeA
normalizedAz = originAz / magnitudeA

# Normalizes Vector B (x,y,z)
normalizedBx = originBx / magnitudeB
normalizedBy = originBy / magnitudeB
normalizedBz = originBz / magnitudeB

## Using vector points and magnitudes of vectors we will now find the angle based on following formula:
## cos(theta) = (a * b)/(magnitude(a) * magnitude(b)) while solving for theta in degrees

# Find dot product of vectors a and b

dotProductAB = (originAx * originBx) + (originAy * originBy) + (originAz * originBz)


# Multiplying magnitudes
combinedMagnitudeAB = magnitudeA * magnitudeB


# Dividing combinedMagnitude from dotProductAB
angleThetaRadians = acos(dotProductAB / combinedMagnitudeAB)

# Converts angle in radians to angle in degrees
angleThetaDegrees = angleThetaRadians * (180 / pi)

print("The angle of the observer from point A to point B is %.5f degrees." % angleThetaDegrees)



