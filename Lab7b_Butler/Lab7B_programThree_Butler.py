# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler UIN 128004413
# Section:		535
# Assignment:	Lab 7b - Program 1
# Date:		    10/11/18

inputQTY = int(input("input number user name and passwords"))

userLogIn = {}

for i in range(inputQTY):
    userName = input('Input username %i: ' % (i + 1))
    passWord = input('Input Password %i: ' % (i + 1))
    userLogIn[userName] = passWord
    print("Log in saved!")
print("All username(s) and password(s) have been saved.")

while True:
    accessUsername = input("Enter Username: ")
    accessPassword = input("Enter Password: ")
    try:
        if userLogIn[accessUsername] == accessPassword:
            print("Access Granted.")
            break
        else:
            print("Username or password incorrect.")
            break
    except KeyError:
        print("Username or password incorrect.")


