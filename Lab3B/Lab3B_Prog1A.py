# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# UIN:
# Section:		535
# Assignment:	Lab 3b-1a
# Date:		    09/18/18

## This program will take user given mass and velocity as user input then calculate and
## output a value of kinetic energy.

# Declare Variables
givenMass = float(input("Input given mass (Kg): "))
givenVelocity = float(input("Input given velocity (m/s): "))
KINETIC_CONSTANT = 1/2

# Using variables given by the user input, calculates the kinetic energy ((1/2)Kg*(m/s)^2)
kineticCalculation = KINETIC_CONSTANT * givenMass * givenVelocity**2

print("Your kinetic energy is %s in Kg per (m/s)^2." % kineticCalculation)
