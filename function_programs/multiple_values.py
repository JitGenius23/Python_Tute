# create a function that returns both the area and circumference of a circle given its radius.

import math

def circle(radius):
    area = round(math.pi * (radius ** 2), 2)
    circumference = round(2 * math.pi * radius, 2)
    return area, circumference

area, circumference = circle(4)

print('area:', area, 'circumference:', circumference)