import math
figure = str(input())
result = float()
if figure == "square":
    a = float(input())
    result = pow(a, 2)
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    result = a*b
elif figure == "circle":
    pi = math.pi
    r = float(input())
    result = pi*(pow(r, 2))
elif figure == "triangle":
    a = float(input())
    h = float(input())
    result = (1/2*(a*h))
print(result)