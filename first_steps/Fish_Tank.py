lenght = int(input())
wight = int(input())
Hight = int(input())
procent = float(input())

liters = ((lenght * wight * Hight )/ 1000 ) * (1 - procent/100)

print(liters)