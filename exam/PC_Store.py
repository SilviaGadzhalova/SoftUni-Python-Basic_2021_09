price_processor_dollars = float(input())
price_videocard_dollars = float(input())
price_ram_dollars = float(input())
number_of_ram = int(input())
discount = float(input())
dollar = 1.57

price_processor_lev = price_processor_dollars * dollar
price_videocard_lev = price_videocard_dollars * dollar
price_ram_lev = price_ram_dollars * dollar
total_ram = price_ram_lev * number_of_ram
processor_discount = price_processor_lev - price_processor_lev*discount
videocard_discount =  price_videocard_lev - price_videocard_lev*discount
total = processor_discount + videocard_discount + total_ram
print(f"Money needed - {total:.2f} leva.")
