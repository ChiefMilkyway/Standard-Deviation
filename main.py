import numpy
from math import sqrt

heights = [175, 180, 190]
new_heights = []
x = len(heights)
z = numpy.mean(heights)

for i in heights:
    y = i - z
    y = y**2
    new_heights.append(y)

for i in range(x):  
    e = new_heights[i] / x
    new_heights[i] = e

std_dev = sqrt(sum(new_heights))
print(std_dev)