# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name: 		 Mose Butler
# UIN:          128004413
# Section:      535
# Assignment:   Lab 3b-1d
# Date:		    09/19/18

# Calculate average length of a M/M/1 Queue

# User Declared variables
Arrival_Rate = float(input("Input the arrival rate: "))
Service_Rate = float(input("Input the service rate: "))

# Calculates MM1 Queue Arrival rate divided by the service rate time the difference of arrival rate from service rate.
MM1_Queue = Arrival_Rate/(Service_Rate*(Service_Rate - Arrival_Rate))
print("The average length of the M/M/1 queue is %0.6f." % MM1_Queue)
