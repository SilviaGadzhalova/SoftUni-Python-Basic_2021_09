change_price = float(input())
change_price = int(change_price*100)
coins_counter = 0

coins_counter += change_price//200
change_price %= 200
coins_counter += change_price//100
change_price %= 100
coins_counter += change_price//50
change_price %= 50
coins_counter += change_price//20
change_price %= 20
coins_counter += change_price//10
change_price %= 10
coins_counter += change_price//5
change_price %= 5
coins_counter += change_price//2
change_price %= 2
coins_counter += change_price//1
change_price %= 1
print(coins_counter)
