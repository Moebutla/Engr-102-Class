# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Name:                 Mose Butler
# UIN:                  128004413
# Class and Section:    535
# Assignment:           Lab 11B
# Date:                 11/15/2018

from turtle import *

tally = int(input("Enter number to tally (Note: any tally over 100 may go off the page): "))


# Sets start towards top left of screen
def start_position():
    up()
    left(180)
    forward(300)
    right(90)
    forward(200)
    left(270)
    down()


# if only drawing one line at a time
def draw_one():
    left(91)
    forward(50)
    right(92)
    up()
    forward(5)
    right(90)
    forward(50)
    left(87)
    down()


# draws a full set of 5 tallies
def draw_five():
    left(93)
    forward(50)
    right(88)
    up()
    forward(5)
    down()
    right(90)
    forward(50)
    left(91)
    up()
    forward(5)
    down()
    left(89)
    forward(50)
    right(91)
    up()
    forward(5)
    down()
    right(91)
    forward(50)
    left(179)
    up()
    forward(50)
    right(91)
    forward(5)
    down()
    right(119)
    forward(56)
    left(119)
    up()
    forward(50)
    down()


# sets turtle to position for a new row
def new_row_v1():
    right(155)
    up()
    forward(230)
    right(198.5)
    down()


# making a second one for variation
def new_row_v2():
    right(155)
    up()
    forward(290)
    right(210)
    down()

# draw a row
def draw_row():
    draw_five()
    draw_five()
    draw_five()
    draw_five()
    draw_five()

# computes counting values
fullCounts = tally // 5  # finds number of full tallies (take whole value of tally / 5)
remainingTally = tally%5  # take that previous remainder and compute single tallies
numRows = tally / 5  # find number of rows
rowsRemaining = fullCounts // 5  # how many full rows
extraRows = fullCounts % 5  # finds number of full tallies if not a full row

# sets starting position of turtle
start_position()

# decides if full row is needed or just a partial
print(range(rowsRemaining))
for i in range(rowsRemaining):
    if rowsRemaining >= 1:  # if there are whole rows(25 tallies)
        if i < 2:  # does two iterations then moves on
            draw_row()
            new_row_v1()
        else:  # after 2 iterations changes new row.
            draw_row()
            new_row_v2()
    else:  # if no full row
        draw_five()

# draws full tallies if not a full row after full rows have been tallied
for i in range(extraRows):
    draw_five()

# draws individual tallies as needed
for i in range(remainingTally):
    draw_one()

input()
done()  # closes out turtle