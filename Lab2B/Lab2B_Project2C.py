# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# Section:		535
# Assignment:	Lab 1b-1
# Date:		09/06/18

# Program is made to print values (x,y,z) at input times T in a linear interpolation of each value.


## Setting values of T
Time_Start = 20
Time_End = 50
Time_Segment = (Time_End - Time_Start) / 4


## Value at T = 20 (First Measurement)
T = Time_Start

# Printed for spacing different sets of points
print("---------------------")

# Setting values and variable to output position of X(T).
BforX = -215 / 71  # Y intercept
X_Thirteen = 1
X_Eightyfour = 23
T_Thirteen = 13
T_Eightyfour = 84
Delta_X = X_Eightyfour - X_Thirteen
Delta_T = T_Eightyfour - T_Thirteen
Slope = Delta_X / Delta_T
Final_X = Slope * T + BforX  # Putting all variables in to find final value of X

print(str(Final_X))

# Setting values and variable to output position of Y(T).
BforY = 317 / 71  # Y intercept
Y_Thirteen = 3
Y_Eighty_four = -5
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Y = Y_Eighty_four - Y_Thirteen
Slope = Delta_Y / Delta_T
Final_Y = Slope * T + BforY  # Putting all variables in to find final value of Y

print(str(Final_Y))

# Setting values and variable to output position of Z(T).
BforZ = 458 / 71  # Y intercept
Z_Thirteen = 7
Z_Eighty_four = 10
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Z = Z_Eighty_four - Z_Thirteen
Slope = Delta_Z / Delta_T
Final_Z = Slope * T + BforZ  # Putting all variables in to find final value of Z

print(str(Final_Z))

## Value at T = 51 (Second Measurement)
T = Time_Start + Time_Segment

# Printed for spacing different sets of points
print("---------------------")

# Setting values and variable to output position of X(T).
BforX = -215 / 71  # Y intercept
X_Thirteen = 1
X_Eightyfour = 23
T_Thirteen = 13
T_Eightyfour = 84
Delta_X = X_Eightyfour - X_Thirteen
Delta_T = T_Eightyfour - T_Thirteen
Slope = Delta_X / Delta_T
Final_X = Slope * T + BforX  # Putting all variables in to find final value of X

print(str(Final_X))

# Setting values and variable to output position of Y(T).
BforY = 317 / 71  # Y intercept
Y_Thirteen = 3
Y_Eighty_four = -5
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Y = Y_Eighty_four - Y_Thirteen
Slope = Delta_Y / Delta_T
Final_Y = Slope * T + BforY  # Putting all variables in to find final value of Y

print(str(Final_Y))

# Setting values and variable to output position of Z(T).
BforZ = 458 / 71  # Y intercept
Z_Thirteen = 7
Z_Eighty_four = 10
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Z = Z_Eighty_four - Z_Thirteen
Slope = Delta_Z / Delta_T
Final_Z = Slope * T + BforZ  # Putting all variables in to find final value of Z

print(str(Final_Z))

## Value at T = 52 (Third Measurement)
T = Time_Start + (Time_Segment * 2)

# Printed for spacing different sets of points
print("---------------------")

# Setting values and variable to output position of X(T).
BforX = -215 / 71  # Y intercept
X_Thirteen = 1
X_Eightyfour = 23
T_Thirteen = 13
T_Eightyfour = 84
Delta_X = X_Eightyfour - X_Thirteen
Delta_T = T_Eightyfour - T_Thirteen
Slope = Delta_X / Delta_T
Final_X = Slope * T + BforX  # Putting all variables in to find final value of X

print(str(Final_X))

# Setting values and variable to output position of Y(T).
BforY = 317 / 71  # Y intercept
Y_Thirteen = 3
Y_Eighty_four = -5
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Y = Y_Eighty_four - Y_Thirteen
Slope = Delta_Y / Delta_T
Final_Y = Slope * T + BforY  # Putting all variables in to find final value of Y

print(str(Final_Y))

# Setting values and variable to output position of Z(T).
BforZ = 458 / 71  # Y intercept
Z_Thirteen = 7
Z_Eighty_four = 10
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Z = Z_Eighty_four - Z_Thirteen
Slope = Delta_Z / Delta_T
Final_Z = Slope * T + BforZ  # Putting all variables in to find final value of Z

print(str(Final_Z))

## Value at T = (Fourth Measurement)
T = Time_Start + (Time_Segment * 3)

# Printed for spacing different sets of points
print("---------------------")

# Setting values and variable to output position of X(T).
BforX = -215 / 71  # Y intercept
X_Thirteen = 1
X_Eightyfour = 23
T_Thirteen = 13
T_Eightyfour = 84
Delta_X = X_Eightyfour - X_Thirteen
Delta_T = T_Eightyfour - T_Thirteen
Slope = Delta_X / Delta_T
Final_X = Slope * T + BforX  # Putting all variables in to find final value of X

print(str(Final_X))

# Setting values and variable to output position of Y(T).
BforY = 317 / 71  # Y intercept
Y_Thirteen = 3
Y_Eighty_four = -5
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Y = Y_Eighty_four - Y_Thirteen
Slope = Delta_Y / Delta_T
Final_Y = Slope * T + BforY  # Putting all variables in to find final value of Y

print(str(Final_Y))

# Setting values and variable to output position of Z(T).
BforZ = 458 / 71  # Y intercept
Z_Thirteen = 7
Z_Eighty_four = 10
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Z = Z_Eighty_four - Z_Thirteen
Slope = Delta_Z / Delta_T
Final_Z = Slope * T + BforZ  # Putting all variables in to find final value of Z

print(str(Final_Z))


## Value at T = 50 (Final Measurement)
T = Time_End

# Printed for spacing different sets of points
print("---------------------")

# Setting values and variable to output position of X(T).
BforX = -215 / 71  # Y intercept
X_Thirteen = 1
X_Eightyfour = 23
T_Thirteen = 13
T_Eightyfour = 84
Delta_X = X_Eightyfour - X_Thirteen
Delta_T = T_Eightyfour - T_Thirteen
Slope = Delta_X / Delta_T
Final_X = Slope * T + BforX  # Putting all variables in to find final value of X

print(str(Final_X))

# Setting values and variable to output position of Y(T).
BforY = 317 / 71   # Y intercept
Y_Thirteen = 3
Y_Eighty_four = -5
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Y = Y_Eighty_four - Y_Thirteen
Slope = Delta_Y / Delta_T
Final_Y = Slope * T + BforY  # Putting all variables in to find final value of Y

print(str(Final_Y))

# Setting values and variable to output position of Z(T).
BforZ = 458 / 71   # Y intercept
Z_Thirteen = 7
Z_Eighty_four = 10
T_Thirteen = 13
T_Eighty_four = 84
Delta_T = T_Eighty_four - T_Thirteen
Delta_Z = Z_Eighty_four - Z_Thirteen
Slope = Delta_Z / Delta_T
Final_Z = Slope * T + BforZ  # Putting all variables in to find final value of Z

print(str(Final_Z))

# Printed for spacing different sets of points
print("---------------------")
