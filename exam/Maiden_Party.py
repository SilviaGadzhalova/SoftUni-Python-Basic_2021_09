price_for_party = float(input())
number_love_letters = int(input())
number_wax_roses = int(input())
number_keychains = int(input())
number_cartoons = int(input())
number_surprises = int(input())

love_letters = 0.60
wax_roses = 7.20
keychains = 3.60
cartoons = 18.20
surprises = 22.00
total =  number_love_letters * love_letters + number_wax_roses * wax_roses + number_keychains * keychains \
         + number_cartoons * cartoons + number_surprises * surprises
number_of_articles = number_love_letters + number_wax_roses + number_keychains + number_cartoons + number_surprises
if number_of_articles > 25:
    total = total - total*0.35
    hosting = total*0.10
    profit = total - hosting
else:
    total = total
    hosting = total * 0.10
    profit = total - hosting
difference = abs(profit - price_for_party)
if total >= price_for_party:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")









