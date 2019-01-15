# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Mose Butler, 128004413
# Section:        535
# Assignment:     (lab 11b-e)
# Date:           (November 10, 2018)

# Define a function that will take the  minimum, mean, and  maximum
def list_analytics(array):
    print('The smallest number in your list is : %0.1f' % min(array))
    array_average = (sum(array)/len(array))
    print("The average of the numbers in your list are : %0.1f" % array_average)
    print('The largest number in your list is : %0.1f' % max(array))
    return


# use a while loop to let the user input the list
isMore = True
userList = []
counter = 1
while isMore:
    user_input = float(input("Enter component %s (If you are done entering numbers enter 'done'): " % counter))
    if user_input != 'done':
        userList.append(user_input)
    else:
        isMore = False
    counter +=1

# Verifies that numbers were input into list
if len(userList)>0:
    list_analytics(userList)
else:
    print("You did not enter any numbers into the list.")