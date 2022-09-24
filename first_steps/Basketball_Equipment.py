year_tax = int(input())

basketball_shoes = year_tax - (year_tax * 0.4)
basketball_clothes = basketball_shoes - (basketball_shoes * 0.2)
basketball_ball = basketball_clothes * 0.25
basketball_accessories = basketball_ball * 0.2

total_price = basketball_clothes + basketball_accessories + basketball_ball + basketball_shoes + year_tax

print(total_price)