# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Mose Butler, 128004413
# Section:        535
# Assignment:     (lab 11b-f)
# Date:           (November 10, 2018)


# make a function that finds velocity
def velocity(x1,x2,y1,y2):
    return (y2-y1)/(x2-x1)


# use a while loop to take in user input for time and position
isMore = True
timeList = []
positionList = []
velocityList = []
counter = 1

# Loop to gather inputs
while isMore:
    timeInput = input('Enter the time %s (Enter "stop" when you are done inputting values): ' % counter)
    if timeInput != 'stop':
        positionInput = float(input("Enter the position at time %s: " % timeInput))
        timeList.append(float(timeInput))
        positionList.append(positionInput)
    else:
        isMore = False
    counter += 1

# call function that finds velocity
for i in range(len(timeList)-1):
    velocityList.append(velocity(timeList[i], timeList[i+1], positionList[i], positionList[i+1]))

print(f"The velocities between points are: {velocityList}")
