budget= float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = video_cards*250
processors_price = processors * (video_cards_price*0.35)
ram_price = ram * (video_cards_price*0.1)
if video_cards >processors:
    total_price = video_cards_price+processors_price+ram_price -((video_cards_price+processors_price+ram_price)*0.15)
else:
    total_price = video_cards_price+processors_price+ram_price

if total_price <=budget:
    remaining_money = budget - total_price
    print(f"You have {remaining_money:.2f} leva left!")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
