import math

    # Calculate the area of circle and assign the value to a variable name area_of_circle
pi = 3.14
r = 30
area_of_circle = pi * (r ** 2)      # Using the formula for area of circle
print("Area of circle:", area_of_circle)

    # Calculate the circumference of a circle and assign the value to a variable name circum_of_circle
circum_of_circle = 2 * pi * r      # Using circumference of circle formula
print("Circumference of a circle:", circum_of_circle)

    #Take the radius as user input and calculate the area.
rad = float(input("Enter the radius of the circle: "))
area_of_circle = pi * (rad ** 2)
print(area_of_circle)