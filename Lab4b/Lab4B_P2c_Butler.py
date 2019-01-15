# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# UIN:          128004413
# Section:		535
# Assignment:	Lab4B_3C
# Date:		09/26/18

# Declaring variables
feature = input("Please select a feature: ")
trimLevel = input("Please select a trim package: ")

# Constant variables are used as output print statements
STANDARD_CONSTANT = "% s comes standard with % s package." % (feature.capitalize(), trimLevel)
AVAILABLE_CONSTANT = "% s is available for an extra charge with % s package." % (feature.capitalize(), trimLevel)
UNAVAILABLE_CONSTANT = "% s is not available with % s package." % (feature.capitalize(), trimLevel)

# Base package
if trimLevel.lower() == 'base':
    if feature.lower() == 'power windows':
        print(STANDARD_CONSTANT)
    elif feature.lower() == 'v-6 engine':
        print(UNAVAILABLE_CONSTANT)
    elif feature.lower() == 'traction control':
        print(AVAILABLE_CONSTANT)
    elif feature.lower() == 'sport package':
        print(UNAVAILABLE_CONSTANT)
    elif feature.lower() == 'multi-tone paint':
        print(UNAVAILABLE_CONSTANT)
    elif feature.lower() == 'parking assist':
        print(UNAVAILABLE_CONSTANT)
    else:
        print("% s is not a valid feature." % feature.capitalize())

# Premium package
elif trimLevel.lower() == 'premium':
    if feature.lower() == 'power windows':
        print(STANDARD_CONSTANT)
    elif feature.lower() == 'v-6 engine':
        print(AVAILABLE_CONSTANT)
    elif feature.lower() == 'traction control':
        print(STANDARD_CONSTANT)
    elif feature.lower() == 'sport package':
        print(UNAVAILABLE_CONSTANT)
    elif feature.lower() == 'multi-tone paint':
        print(AVAILABLE_CONSTANT)
    elif feature.lower() == 'parking assist':
        print(AVAILABLE_CONSTANT)
    else:
        print("% s is not a valid feature." % feature.capitalize())

# Luxury Package
elif trimLevel.lower() == 'luxury':
    if feature.lower() == 'power windows':
        print(STANDARD_CONSTANT)
    elif feature.lower() == 'v-6 engine':
        print(STANDARD_CONSTANT)
    elif feature.lower() == 'traction control':
        print(STANDARD_CONSTANT)
    elif feature.lower() == 'sport package':
        print(AVAILABLE_CONSTANT)
    elif feature.lower() == 'multi-tone paint':
        print(AVAILABLE_CONSTANT)
    elif feature.lower() == 'parking assist':
        print(STANDARD_CONSTANT)
    else:
        print("% s is not a valid feature." % feature.capitalize())

# else net
else:
    print("% s is not a valid package." % trimLevel.capitalize())
