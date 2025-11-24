#Calculate circumference and area of circle

import math
radius = float(input("Enter a Radius :"))
def find_cirumference_area_of_circle(radius):
    C = 2 * math.pi * radius
    A = math.pi * (radius ** 2)
    return C, A
C,A = find_cirumference_area_of_circle(radius)

print(f"Circumference of the radius {radius} is {round(C,2)} and Area of circle is {round(A,2)}")