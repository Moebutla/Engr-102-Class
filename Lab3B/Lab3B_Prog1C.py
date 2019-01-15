# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		 Mose Butler
# UIN:          128004413
# Section:      535
# Assignment:   Lab 3b-1c
# Date:		    09/18/18

## This program will calculate impedance of a circuit based on user input of resistance and  inductive resistance

from math import *
# Declare Variables
resistance = float(input("Input resistance: "))
inductiveResistance = float(input("Input inductive resistance: "))

# Calculate impedance based on known formula
circuitImpedance = sqrt(resistance ** 2 + inductiveResistance ** 2)

print("The impedance of the circuit is %0.4f." % circuitImpedance)
