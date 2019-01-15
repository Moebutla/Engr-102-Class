# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# UIN:          128004413
# Section:		535
# Assignment:	Lab4B_1
# Date:		09/26/18

firstNumber = int(input("Insert first number: "))
secondNumber = int(input("Insert second number: "))
thirdNumber = int(input("Insert third number: "))

# compares first number to second and third numbers
if firstNumber >= secondNumber and firstNumber >= thirdNumber:
    if firstNumber == secondNumber:
        print("There is no individual maximum number.")
    if firstNumber == thirdNumber:
        print("There is no individual maximum number.")
    else:
        print("The maximum number is %i." % firstNumber)

# compares second number to first and third numbers
elif secondNumber >= firstNumber and secondNumber >= thirdNumber:
    if secondNumber == firstNumber:
        print("There is no individual maximum number.")
    if secondNumber == thirdNumber:
        print("There is no individual maximum number.")
    else:
        print("The maximum number is %i." % secondNumber)

# compares third number to first and second numbers
elif thirdNumber > firstNumber and thirdNumber > secondNumber:
    print("The maximum number is %i." % thirdNumber)

# only shows if there are two or more answers as the highest number.
else:
    print("There is no individual maximum number.")
