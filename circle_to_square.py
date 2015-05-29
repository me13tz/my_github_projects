import math
from math import sqrt

circ = float(input("Please enter the circumference of a circle: "))

diam = circ/math.pi

radius = diam/2

sq = radius*radius

area_circle = sq*math.pi
squareside = sqrt(area_circle)
area_string = str(area_circle)

#print("%.2f" % a)
print ("The Area of the circle is %.2f" % area_circle)
print ("Diameter: %.2f" % diam)
print ("Radius: %.2f" % radius)
print()

print ("The length of the side of a square with the same area is %.2f" % squareside)

tribase = (area_circle * 2)/(sqrt(area_circle))

print ("The height of an equilateral triangle with the same area is %.2f" % tribase)
