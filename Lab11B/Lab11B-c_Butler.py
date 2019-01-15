# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Mose Butler, 128004413
# Section:        535
# Assignment:     (lab 11b-c)
# Date:           (November 10, 2018)

# Function to create a mailing label.
def mailing_label(name, address, address2, city, state, zip_code):
    print("\n")
    print(name)
    print(address)
    if address2 != "":
        print(address2)
    print(city, ",", state, zip_code)
    return


# Explain program and get inputs
print("Fill in fields as needed to create a mailing label.")
print("\tIf second line of street address is unneeded, leave blank.")
nameAddressee = input("Enter Name: ")
line1Addressee = input("Enter street address: ")
line2Addressee = input("Enter street address (line 2): ")
cityAddressee = input("Enter city: ")
stateAddressee = input("Enter state: ")
zipAddressee = input("Enter zip code: ")

# Run function
mailing_label(nameAddressee, line1Addressee, line2Addressee, cityAddressee, stateAddressee, zipAddressee)