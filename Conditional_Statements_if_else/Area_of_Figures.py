import math

figure = input()

if figure == "square":
    num1 = float(input())
    square_area = num1 * num1
    print(f"{square_area:.3f}")

elif figure == "rectangle":
    length_of_side_a = float(input())
    length_of_side_b = float(input())
    rectangle_area = length_of_side_a * length_of_side_b
    print(f"{rectangle_area:.3f}")

elif figure == "circle":
    radius = float(input())
    circle_area = radius * radius * math.pi
    print(f"{circle_area:.3f}")

else:
    a = float(input())
    ha = float(input())
    triangle_area = a*ha/2
    print(f"{triangle_area:.3f}")