for i in range(11):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

    import math
 # Have user to enter a radius #

radius=float(input('enter the radius of the circle'))


PI = 3.14
r = float(input('enter the radius of a circle:'))
area = PI * r * r
print("Area of a circle = %.2f" %area)

#-Length of the rectangle using the imput function #
#-Width of the rectangle using the input function#
#- Calculate the area of the rectangle and print the area using value from length and width


Length= float(input('enter the Length of a rectangle:'))
Width = float(input('enter the Width of a rectangle:'))
Area = Length*Width
print('Area of a rectangle is:%.2f' % Area)


#check if input parameters are greater than 0 #




if Length > 0 and Width > 0:
    area = Length * Width
    print('the area of the rectangle is : ', area)
else:
    print('input parameter are not greater than 0. Cannot compute area of the requested polygon.')






