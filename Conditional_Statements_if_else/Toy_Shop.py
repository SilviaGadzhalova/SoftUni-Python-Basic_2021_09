excursion_price = float(input())
puzzles = int(input())
talking_dolLs = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

sum = puzzles*2.60 + talking_dolLs*3 + teddy_bears*4.10 + minions*8.20 + trucks*2
total_toys = puzzles + talking_dolLs + teddy_bears + minions + trucks
if total_toys >=50:
    total_price = sum - sum * 0.25
else:
    total_price = sum

rent = total_price *0.1
profit= total_price - rent
remaining_money = profit - excursion_price
if profit >= excursion_price:
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    remaining_money = excursion_price - profit
    print(f"Not enough money! {remaining_money:.2f} lv needed.")
