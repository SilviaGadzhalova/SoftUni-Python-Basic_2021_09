budjet = int(input())
sezon = input()
broi_ribari = int(input())

if sezon == "Spring":
    cena_lodka = 3000
    if broi_ribari == 6:
        price = cena_lodka - cena_lodka * 0.1
    elif broi_ribari <= 11:
        price = cena_lodka - cena_lodka * 0.15
    else:
        price = cena_lodka - cena_lodka * 0.25

elif sezon == "Summer" or sezon == "Autumn":
    cena_lodka = 4200
    if broi_ribari == 6:
        price = cena_lodka - cena_lodka * 0.1
    elif broi_ribari <= 11:
        price = cena_lodka - cena_lodka * 0.15
    else:
        price = cena_lodka - cena_lodka * 0.25

elif sezon == "Winter":
    cena_lodka = 2600
    if broi_ribari == 6:
        price = cena_lodka - cena_lodka * 0.1
    elif broi_ribari <= 11:
        price = cena_lodka - cena_lodka * 0.15
    else:
        price = cena_lodka - cena_lodka * 0.25

if sezon != "Autumn" and broi_ribari %2 == 0:
    price = price - price * 0.05
else:
    price = price


difference = abs(budjet - price)
if budjet >= price:
    print(f"Yes! You have {difference:.2f} leva left.")

else:
    print(f"Not enought money! You need {difference:.2f} leva.")
