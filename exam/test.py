number_sea = int(input())
number_mountain = int(input())

sea_price = 680
mountain_price = 499
total_sea = 0
total_mountain = 0
total = 0
condition = False
while True:
    current_excursion = input()
    if current_excursion == "Stop":
        break
    elif current_excursion == "sea":
        total_sea += sea_price
        number_sea -=1
        if number_sea < 0:
            total_sea -= sea_price
            number_sea = 0

    elif current_excursion == "mountain":
        total_mountain += mountain_price
        number_mountain -= 1
        if number_mountain < 0:
            total_mountain -= mountain_price
            number_mountain = 0

    if number_sea == 0 and number_mountain == 0:
        condition = True
    total = total_sea + total_mountain

    if condition:
        break
if condition:
    print("Good job! Everything is sold.")
    print(f"Profit: {total} leva.")
else:
    print(f"Profit: {total} leva.")
