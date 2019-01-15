# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Mose Butler, 128004413
# Section:        535
# Assignment:     (lab 11b-d)
# Date:           (November 10, 2018)

# make a function that replaces commas with tabs
def csv_converter(file_name):
    # make the new file name
    file_new = file_name[:-4] + '.tsv'
    # show the user their new file name
    print(f"Your new tsv file is saved as: {file_new}")
    # open the original csv file
    file = open(file_name, 'r')
    # open the new tsv file
    with open(file_new, 'w') as data:
        # use a loop to replace all the commas with tabs in every line of the old csv file
        for lines in file:
            new_lines = lines.replace(',', '\t')
            data.write(new_lines)
    # close the original csv file
    file.close()
    return


# input the name of a .csv file from the user
user_file_name = input('Enter the name of the csv file that you want to change to a tsv file '
                       '(do not include the .csv extension): ') + ".csv"

# call the function that replaces comas with tabs
csv_converter(user_file_name)
print('Done.')
