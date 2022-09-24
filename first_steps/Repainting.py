quantity_nylon = int(input())
quantity_paint = int(input())
quantity_thinner = int(input())
number_working_hours = int(input())

total_nylon_price = (quantity_nylon + 2) * 1.5
total_paint_price = (quantity_paint * 1.1) * 14.5
total_thinner_price = quantity_thinner * 5
bags = 0.4
money_for_workers = ((total_nylon_price + total_paint_price + total_thinner_price + bags) * 0.3) \
                    * number_working_hours
total_sum = total_nylon_price + total_paint_price + total_thinner_price + bags + money_for_workers
print(total_sum)