number_bitcoins = int(input())
number_chinese_yuan = float(input())
commission = float(input())/100

bitcoin = 1168

euro = 1.95
chinese_yuan = 0.15 * number_chinese_yuan
dollar = 1.76*chinese_yuan

total_bitcoin = number_bitcoins*bitcoin
total = (total_bitcoin + dollar)/euro

commission_price = total*commission
final = total - commission_price
print(f"{final:.2f}")