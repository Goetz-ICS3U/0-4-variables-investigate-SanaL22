"""
var_make.py

"""
# Input

circle_radius = int(input("The radius of the circle: "))
rectange_lenght = int(input("The length of the rectangle: "))
rectangle_width = int(input("The width of the rectangle: "))
octagon_side = int(input("A side length of the octagon: "))

pi = 3.14159
circle_area = pi * circle_radius **2
circles_perimeter = 2 * pi * circle_radius

rectangle_area = rectange_lenght * rectangle_width
rectangle_perimeter = 2 * (rectange_lenght + rectangle_width)

octagon_area = 2 * (1 + 2 ** 0.5) * octagon_side ** 2
octagon_perimeter = 8 * octagon_side


# Processing
# Output.

print(f"The circle has an area of {circle_area} and a perimeter of {circles_perimeter}")
print(f"The rectangle has an area of {rectangle_area} and a perimeter of {rectangle_perimeter}")
print(f"The octagon has an area of {octagon_area} and a perimeter of {octagon_perimeter}")