# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Mose Butler, 128004413
# Section:        535
# Assignment:     (lab 11b-b)
# Date:           (November 10, 2018)

# Function to find least profitable facility.
def lowest_profit(names, cost, value):
    profit = []
    for company in range(len(names)):
        profit.append(value[company] - cost[company])

    leastProfitable = [names[profit.index(min(profit))] , profit[profit.index(min(profit))]]

    return leastProfitable

# Create empty lists for inputs
production_facility = []
grossProfit = []
runCost = []

# use a while loop to take user inputs
moreToEnter = True
while moreToEnter:
    facility_name = input('Enter the name of the production facility (if done entering, enter \'done\'): ')
    if facility_name != 'done':
        production_facility.append(facility_name)
        grossProfitInput = input('Enter the gross profit of that facility: $ ')
        grossProfit.append(float(grossProfitInput))
        cost_to_run_input = input('Enter the cost to run that facility: $ ')
        runCost.append(float(cost_to_run_input))

    else:
        moreToEnter = False

if len(production_facility) == 0:
    print('\nNot able to calculate because there was nothing input')

else:
    # Use function to find lowest profit
    lowest_netProfit = lowest_profit(production_facility, runCost, grossProfit)

    print("\nThe production facility with the lowest profitability is: %s. Their profitability is: $ %s"
          % (lowest_netProfit[0], lowest_netProfit[1]))