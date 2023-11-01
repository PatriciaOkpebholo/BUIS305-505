#### Write a program to calculate the area of a circle;
# you need to collect input from the user which will be the radius and use that to calculate the area of a circle.
# {Hints: You can use the Math Function for constant}


import math

PI = 3.14
r = float(input('enter the radius of a circle:'))
area = PI * r * r
print("Area of a circle = %.2f" %area)