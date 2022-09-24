x = float(input())
y = float(input())
h = float(input())

front_back = (x*x - 1.2*2) + x*x
sides = 2*(x*y) - 2*(1.5*1.5)
green_paint = (front_back + sides) /3.4

front_back_roof = 2*(x*h/2)
sides_roof = 2*x*y
red_paint = (front_back_roof+sides_roof)/ 4.3
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")