# By submitting this assignment, all team members agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Names:        Mose Butler      128004413
# Section:        535
# Assignment:     Lab 10B - Program 2
# Date:           10/25/2018

import numpy as np
import matplotlib.pyplot as plt

# Opens file and reads in lines
dataFile = open("WeatherDataWindows.csv")
data = dataFile.readlines()

# creates lists of data while getting rid of excess characters and splitting on ","
for lineNum in range(len(data)):
    data[lineNum] = data[lineNum].rstrip().split(',')

# Deletes titles from columns
variables = data.pop(0)
del variables[0]

# Gets rid of dates column
dates = []

# deletes dates from lists
for row in range(len(data)):
    dates.append(data[row].pop(0))

# Converts values as strings into float values
for lineNum in range(len(data)):
    for value in range(len(data[0])):
        data[lineNum][value] = float(data[lineNum][value])

# creates an array of the number of days
daysNumbered = np.arange(len(dates))

# Empty list for the rows
dataList = []

# Creates a list of each row
for index in range(len(variables)):
    tempList = []
    for line in data:
        tempList.append(line[index])
    dataList.append(tempList)


# Indexing Guide:
# 0: Temp High
# 1: Temp Avg
# 2: Temp Low
# 3: Dew Point High
# 4: Dew Point Avg
# 5: Dew Point Low
# 6: Humidity High
# 7: Humidity Avg
# 8: Humidity Low
# 9: Pressure High
# 10: Pressure Avg
# 11: Pressure Low
# 12: Precipitation


# Graph one - Line graph showing avg temp & avg pressure. Uses same x but different y scales.
# Set Graph Layout
fig, tempLineGraph = plt.subplots()
tempLineGraph.set_title("Average Temp and Pressure from 1/1/15 - 12/31/17")
tempLineGraph.set_xlabel("Days since January 1, 2015")
tempLineGraph.set_ylabel("Average Temp (\N{DEGREE SIGN}F)", color='b')

tempLineGraph.plot(daysNumbered, dataList[1], 'r-')

# Sets up pressure part of graph
pressureGraph = tempLineGraph.twinx()
pressureGraph.plot(daysNumbered, dataList[11])
pressureGraph.set_ylabel("Average Pressure (Pa)", color='r')


plt.show()

# Graph two - Graphs Precipitation over 3 years
fig, precipitationGraph = plt.subplots()
precipitationGraph.set_title("Precipitation from 1/1/15 - 12/31/17")
precipitationGraph.set_xlabel("Precipitation (in.)")
precipitationGraph.set_ylabel("Number of days")
plt.yscale('log')
precipitationGraph.hist(dataList[12], rwidth=0.5 , range = [0, 4])

plt.show()

# Graph three - Compares Avg Temp and Dew point over 3 years
fig, tempScatter = plt.subplots()
tempScatter.set_title("Comparison between Avg. Temperature and Dew Point")
tempScatter.set_xlabel("Temperature (\N{DEGREE SIGN}F)")
tempScatter.set_ylabel("Dew Point")

tempScatter.scatter(dataList[1], dataList[4], color = 'maroon')

plt.show()



# defines several variables to use when calculating the data needed for the final graph

# base day for the range in which data is collected per month
index = 0
# stores the average of average temperatures
monthlyTempAvg = []
# holds the highest and lowest temperatures for each month
monthlyMax = []
monthlyMin = []

# list of the numbers of days in each month
monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# creates a list from 0-35 for each month,
months = np.arange(36)
# number of years
years = 3

# iterates through each year
for i in range(years):
    # iterates through each day in t
    for days in monthDays:

        # sets the minimum and maximum temp for each month to the lowest and highest temp
        # in each month (index:index+days+1) splices the list to include all days in the current
        # month

        #calculates the average of the average temperatures in the month
        average = sum(dataList[1][index:index + days])/days

        # calculates how high the highest temperature in the month is above the average
        maxi = max(dataList[0][index:index + days])-average

        # calculates how low the lowest temperature in the month is below the average
        mini = average-min(dataList[2][index:index + days])

        # appends calculations to their list
        monthlyTempAvg.append(average)
        monthlyMax.append(maxi)
        monthlyMin.append(mini)
        tempError = [monthlyMin, monthlyMax]
        # increases the base index to be the start of the next month
        index += days

# Graph four - Tracks Avg Temp, Highest Temp, Lowest Temp by month
fig, tempBarGraph = plt.subplots()
tempBarGraph.set_title("Monthly Temperature Tracking (Avgs)")
tempBarGraph.set_xlabel("Months since 1/1/15")
tempBarGraph.set_ylabel("Temperature (\N{DEGREE SIGN}F)")
tempBarGraph.bar(months, monthlyTempAvg, width = 0.5, yerr=tempError)

plt.show()