flowers = input()
number_of_flowers = int(input())
budget = int(input())
flowers_price = 0

if flowers == "Roses":
    flowers_price = number_of_flowers * 5
    if number_of_flowers > 80:
        flowers_price = flowers_price - flowers_price*0.1
    else:
        flowers_price = flowers_price
elif flowers == "Dahlias":
    flowers_price = number_of_flowers * 3.8
    if number_of_flowers > 90:
        flowers_price = flowers_price - flowers_price*0.15
    else:
        flowers_price = flowers_price
elif flowers == "Tulips":
    flowers_price = number_of_flowers * 2.8
    if number_of_flowers > 80:
        flowers_price = flowers_price - flowers_price*0.15
    else:
        flowers_price = flowers_price
elif flowers == "Narcissus":
    flowers_price = number_of_flowers * 3
    if number_of_flowers < 120:
        flowers_price = flowers_price + flowers_price*0.15
    else:
        flowers_price = flowers_price
elif flowers == "Gladiolus":
    flowers_price = number_of_flowers * 2.5
    if number_of_flowers < 80:
        flowers_price = flowers_price + flowers_price * 0.2
    else:
        flowers_price = flowers_price
difference = abs(budget - flowers_price)
if budget >= flowers_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
