# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# UIN:          128004413
# Section:		535
# Assignment:	Lab4B_3B
# Date:		09/26/18

# Reynolds number

# Declare variable by user input
fluidVelocity = int(input("Input the fluid viscosity(units): "))
kinematicViscosity = int(input("Input the kinematic viscosity: "))
linearDimension = int(input("Input the characteristic linear dimension: "))

# Formula for Reynolds number based on https://tinyurl.com/ybcmcy6b
reynoldsNumber = fluidVelocity * linearDimension / kinematicViscosity

print("Reynolds number is %s." % reynoldsNumber)
print("Formula used: https://tinyurl.com/ybcmcy6b "
      "\nBreakpoints used: https://en.wikipedia.org/wiki/Reynolds_number#Laminar%E2%80%93turbulent_transition ")
if reynoldsNumber > 2900:
    print("The flow is turbulent based on the Reynolds number: % s." % reynoldsNumber)
elif reynoldsNumber < 2300:
    print("The flow is laminar based on the Reynolds number: % s." % reynoldsNumber)
else:
    print("The flow is transient based on the Reynolds number: % s." % reynoldsNumber)
