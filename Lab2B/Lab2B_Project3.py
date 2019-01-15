# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# Section:		535
# Assignment:	Lab 1b-1
# Date:		    09/07/18

# Expected output = 1
x = 1
z = 0

z += x
print(z)


# Expected output = 3
x = 1
z = 0
x += 1
x += 1

z += x
print(z)

# Expected output = 11
x = 1
y = 10
z = 0
y += x

z += y
print(z)

# Expected output = 28
x = 1
y = 10
z = 0
x += 1
x += 1
x += 1
y += x
x = 1
x += 1
y *= x

z += y
print(z)

# Expected output = 123
x = 1
y = 10
z = 0
x = y
y *= x
z += y
x = 1
y = 10
x += 1
y *= x
z += y
x = 1
x += 1
x += 1

z += x


# Expected output = 100000000000000000000000000000000

print(z)
x = 1
y = 10
z = 0
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x
x = y
y *= x

z += y
print(z)

# Expected output = 4321
x = 1
y = 10
z = 0
x = y
y *= x
y *= x
x = 1
x += 1
x += 1
x += 1
y *= x
z += y
x = 1
y = 10
x = y
y *= x
x = 1
x += 1
x += 1
y *= x
z += y
x = 1
y = 10
x += 1
y *= x
z += y
x = 1

z += x
print(z)
