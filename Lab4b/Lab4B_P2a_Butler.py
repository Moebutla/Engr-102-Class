# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# UIN:          128004413
# Section:		535
# Assignment:	Lab4B_3A
# Date:		09/26/18

# Declare Variable based on user input
heightInches = float(input("Input height in inches: "))
weightPounds = float(input("Input weight in pounds: "))


indexBMI = float(weightPounds/(heightInches**2) * 703)


if indexBMI < 18.5:
    print("You're BMI Index is %i, you are considered underweight." % int(indexBMI))
elif indexBMI <= 24.9:
    print("You're BMI Index is %i, you are considered normal weight." % int(indexBMI))
elif indexBMI <= 29.9:
    print("You're BMI Index is %i, you are considered overweight." % int(indexBMI))
else:
    print("You're BMI Index is %i, you are considered obese." % int(indexBMI))
