# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
# 
# Name: 		Mose Butler UIN 128004413
# Section:		535
# Assignment:	Lab 7b - Program 1
# Date:		    10/11/18

# Declare Variable
pigLatinString = input("Enter a word to be translated to pig latin: ")

# Create a list of vowels [a,e,i,o,u,y] for comparison
vowelCheck = ['a', 'e', 'i', 'o', 'u', 'y']

# Loop runs until variable is 'stop'
while pigLatinString.lower() != 'stop':
    # If comparison checks variable for starting vowel.
    if pigLatinString[0].lower() in vowelCheck:
        # If word has vowel as first letter, just adds yay to end of word.
        print("%s is %syay in Pig Latin." % (pigLatinString, pigLatinString))
        print("Type 'Stop' to stop the program.")
        pigLatinString = input("Enter a word to be translated to pig latin: ")

    # If first letter of string is not a vowel it is at consonant.
    else:
        pigLatinConsonent = list(pigLatinString)  # Turns string into list
        pigLatinConsonent.append(pigLatinConsonent[0])  # Moves first letter to the end of list.
        pigLatinConsonent.remove(pigLatinConsonent[0])  # Removes first letter.
        print("%s is " % pigLatinString + ''.join(pigLatinConsonent) + 'ay' + " in pig latin.")
        print("Type 'Stop' to stop the program.")
        pigLatinString = input("Enter a word to be translated to pig latin: ")

# Print stop statement
print("This program has toppedsay!")
