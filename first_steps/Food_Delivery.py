chiken_menu = int(input())
fish_menu = int(input())
vegi_menu = int(input())

chiken_price = chiken_menu * 10.35
fish_price = fish_menu * 12.4
vegi_price = vegi_menu * 8.15

desert_price = (chiken_price + fish_price + vegi_price) * 0.2

total_price = chiken_price + fish_price + vegi_price + desert_price + 2.5

print(round(total_price,2))