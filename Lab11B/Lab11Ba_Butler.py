# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Mose Butler, 128004413
# Section:        535
# Assignment:     (lab 11b-a)
# Date:           (November 10, 2018)

from math import*


def volume_of_parts_left(length, width, height, radius, diameter, hypotonuse):
    # function for a hole with a diameter <= the length or width of the block
    if user_diameter <= user_length and user_diameter <= user_width:
        volumeSquare = length * width * height
        volumeCylinder = pi * radius ** 2 * height
        volume_left = volumeSquare - volumeCylinder
        return volume_left

    # function for a hole that has a diameter >= than the diagonal of the block
    elif diameter >= hypotonuse:
        volume_left = 0
        return volume_left

    # function for a hole that has a diameter that is larger than the length and has a square top
    elif diameter > length and width == length:
        theta = acos((0.5 * length) / radius)
        area_left = ((radius ** 2) / 2) * (theta - sin(theta))
        volume_left = area_left * height
        return volume_left

    # function for a hole that has a diameter that is larger than the width but smaller than or equal to the length
    elif diameter > width and diameter <= length:
        angle = acos((0.5 * width) / radius)
        theta = pi - 2*angle
        area_triangle = 0.5 * width * sqrt((radius ** 2) - (0.5 * width) ** 2)
        area_sector = 0.5 * (radius ** 2) * theta
        area_taken = (2*(area_sector)) + (2*area_triangle)
        volume_taken = area_taken * height
        area_rectangle = length * width
        volume_rectangle = area_rectangle * height
        volume_left = volume_rectangle - volume_taken
        return volume_left
    # function for a whole that has a diameter larger than the length and width but it is a rectangle
    elif diameter >= width and diameter > length and length != width:
        angle_triangle = acos(0.5 * width / radius)
        angle_triangle_1 = 0.5 * sqrt((radius ** 2) - (.5 * width) ** 2) * width
        theta_sector = (pi/2)-angle_triangle*2
        area_sector = 0.5 * radius ** 2 * theta_sector
        area_quad = angle_triangle*2 + area_sector
        area_taken = area_quad*4
        rectangle_volume = length * width * height
        volume_taken = area_taken * height
        volume_left = rectangle_volume - volume_taken
        return volume_left


# user input for length width and height of the block as well as the radius of the hole
user_length = float(input("Enter the length of the block in meters(must be greater than or equal to the width): "))
user_width = float(input("Enter the width of the block in meters (must be less than or equal to the length): "))
user_height = float(input("Enter the height of the block in meters: "))
user_radius = float(input("Enter the radius of the hole in meters: "))
user_diameter = user_radius*2

diagonal_top_block = sqrt(user_width**2 + user_length**2)

#call the function
print("The volume remaining is: %s meters\u00b3" % volume_of_parts_left(user_length, user_width, user_height, user_radius,
                                                                    user_diameter, diagonal_top_block))