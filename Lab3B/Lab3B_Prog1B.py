# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		 Mose Butler
# UIN:          128004413
# Section:      535
# Assignment:   Lab 3b-1b
# Date:		    09/18/18

## This will calculate shear stress based on user inputting the normal stress applied,
## the cohesion, and the angle of internal friction,

from math import *

# Declaring Variables
Normal_Stress = float(input("Input normal stress applied to the material: "))
Cohesion = float(input("Input given cohesion: "))
Angle_Friction = float(input("Input the the angle of internal friction in degrees: "))

# Converts angle given by input into radians for python to compute accurate value
radianFriction = float(Angle_Friction * (pi / 180))

#Calculates shear stress based on known function
shearStress = float(Cohesion + Normal_Stress * tan(radianFriction))

print("The shear stress of this object is %s." % shearStress)

