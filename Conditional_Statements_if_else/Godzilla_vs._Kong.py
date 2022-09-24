film_budget = float(input())
statists = int(input())
clothes_for_statist = float(input())

decor = film_budget * 0.1

if statists > 150:
    total_clothes_for_statist = statists * clothes_for_statist - ((statists * clothes_for_statist)*0.1)
else:
    total_clothes_for_statist= statists * clothes_for_statist
total_money_need = decor + total_clothes_for_statist

if total_money_need > film_budget:
    money_need = total_money_need - film_budget
    print("Not enough money!")
    print(f"Wingard needs {money_need:.2f} leva more.")

else:
    remain_money = film_budget - total_money_need
    print("Action!")
    print(f"Wingard starts filming with {remain_money:.2f} leva left.")
