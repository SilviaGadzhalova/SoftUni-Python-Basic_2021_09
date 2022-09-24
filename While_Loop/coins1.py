change_price = float(input())
change_price = int(change_price*100)
coins_counter = 0

while change_price >0:
    if change_price - 200 >= 0:
        coins_counter +=1
        change_price -= 200
        continue
    elif change_price - 100 >= 0:
        coins_counter +=1
        change_price -= 100
        continue
    elif change_price - 50 >= 0:
        coins_counter +=1
        change_price -= 50
        continue
    elif change_price - 20 >= 0:
        coins_counter +=1
        change_price -= 20
        continue
    elif change_price - 10 >= 0:
        coins_counter +=1
        change_price -= 10
        continue
    elif change_price - 5 >= 0:
        coins_counter +=1
        change_price -= 5
        continue
    elif change_price - 2 >= 0:
        coins_counter +=1
        change_price -= 2
        continue
    elif change_price - 1 >= 0:
        coins_counter +=1
        change_price -= 1
print(coins_counter)
