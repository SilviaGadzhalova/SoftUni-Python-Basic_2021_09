number_sea = int(input())
number_mountain = int(input())

sea_price = 680
mountain_price = 499
total_sea = 0
counter_sea = 0
total_mountain = 0
counter_mountain = 0
condition = False

while True:
    current_excursion = input()
    if current_excursion == "Stop":
        break
    if current_excursion == "sea":
        total_sea += sea_price
        counter_sea +=1
    elif current_excursion == "mountain":
        total_mountain += mountain_price
        counter_mountain += 1
    total = total_sea + total_mountain
    if counter_mountain > number_mountain:
        pass
    elif counter_sea >number_sea:
        pass
    elif counter_mountain == number_mountain and counter_sea ==number_sea:
        condition = True
    current_excursion = input()


    if condition:
        print("Good job! Everything is sold.")
        print(f"Profit: {total:.2f} leva.")

    else:
        print(f"Profit: {total:.2f} leva.")





