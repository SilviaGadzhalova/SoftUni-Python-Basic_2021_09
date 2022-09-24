number_packs_of_pens = int(input())
number_packs_of_markers = int(input())
liters_of_cleaning_liquid = int(input())
procent_of_sales = int(input())

sale_procent = procent_of_sales/100

total_pens_price = number_packs_of_pens * 5.8
total_markers_price = number_packs_of_markers * 7.2
total_cleaning_liquid_price = liters_of_cleaning_liquid * 1.2
total_sum = total_cleaning_liquid_price + total_markers_price + total_pens_price
total_price = total_sum - total_sum * sale_procent
print(total_price)



