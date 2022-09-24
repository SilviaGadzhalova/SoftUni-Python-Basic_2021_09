budget = int(input())
season = input()
number_of_fishermans = int(input())
boat_rent = 0

if season == "Spring":
    boat_rent = 3000
    if number_of_fishermans <= 6:
       boat_rent = 3000 - 3000*0.1
    elif number_of_fishermans <= 11:
        boat_rent = 3000 - 3000*0.15
    else:
        boat_rent = 3000 - 3000*0.25

elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
    if number_of_fishermans <= 6:
       boat_rent = 4200 - 4200*0.1
    elif number_of_fishermans <= 11:
        boat_rent = 4200 - 4200*0.15
    else:
        boat_rent = 4200 - 4200*0.25

elif season == "Winter":
    boat_rent = 2600
    if number_of_fishermans <= 6:
       boat_rent = 2600 - 2600*0.1
    elif number_of_fishermans <= 11:
        boat_rent = 2600 - 2600*0.15
    else:
        boat_rent = 2600 - 2600*0.25
if season != "Autumn" and number_of_fishermans % 2 ==0:
    boat_rent = boat_rent - boat_rent*0.05
difference = abs(budget - boat_rent)
if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")

