# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		Mose Butler
# Section:		535
# Assignment:	Lab 1b-1
# Date:		08/30/18

from math import *

# This section will print the answer for the "a" bullet point:
#   My name. My UIN number. The section number for my class.
print("My name is Mose Butler." + " My UNI is 128004413." + " The section number for my class is 535."
      )

# This section will print an interesting fact about me.
print("An interesting fact about me, is that I attended a NASA scholars program this summer!"
      )

# Volume of sphere.

radius = 3
Vol_Sphere = pi*radius**3*(4/3)

print("The volume of the sphere is" + " " + str(Vol_Sphere) + "."
      )


# Volume of a pyramid.
Pyramid_Side = 2.5
Pyramid_Height = 4
Vol_Pyramid = ((Pyramid_Side**2*Pyramid_Height)/3)

print("The volume of the pyramid is" + " " + str(Vol_Pyramid)
      )

# Kinetic energy of some object
Mass = 100
Velocity = 21
Kinetic_Energy = 1/2*Mass*Velocity**2
print("The kinetic energy of the object is" + " " + str(Kinetic_Energy) + "."
      )

# Impedance of a circuit
Resistance = 0.3
Inductive_reactance = 0.2
Impedance = sqrt(Resistance**2 + Inductive_reactance**2)
print("The impedance of this circuit is" + " " + str(Impedance) + "."
      )

# Reynold's number
Fluid_Velocity = 100
Kinematic_Viscosity = 1.2
Linear_Dimension = 2.5
Reynolds_Number = (Fluid_Velocity*Linear_Dimension)/Kinematic_Viscosity
print("Reynold's number is" + " " + str(Reynolds_Number) + "."
      )

# Average length of a M/M/1 Queue
Arrival_Rate = 20
Service_Rate = 35
MM1_Queue = Arrival_Rate/(Service_Rate*(Service_Rate - Arrival_Rate))
print("The average length of the M/M/1 queue is " + str(MM1_Queue) + "."
      )

# Chemical reaction rate

Pre_Exponent_Factor = (5*10**10)
Activation_Energy = (2*10**5)
Temperature = 525
Gas_Constant = 8.31446
Chem_Reaction = Pre_Exponent_Factor*e**(Activation_Energy/(Temperature*Gas_Constant))

print("The rate constant of a chemical reaction is " + str(Chem_Reaction) + "."
      )

# Shear stress

Normal_Stress = 20
Cohesion = 2
Angle_Friction = 35

print("The shear stress of this object is " + str(Cohesion + Normal_Stress*tan(Angle_Friction)) + "."
      )

