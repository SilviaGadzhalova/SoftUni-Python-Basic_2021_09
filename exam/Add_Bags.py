price_baggage_over20kg = float(input())
kg_baggage = float(input())
days_till_trip = int(input())
numbers_of_baggage = int(input())
price_baggage = 0
if kg_baggage < 10:
    price_baggage = price_baggage_over20kg*0.2
elif 10 <= kg_baggage <= 20:
    price_baggage = price_baggage_over20kg/2
elif kg_baggage > 20:
    price_baggage = price_baggage_over20kg

if days_till_trip > 30:
    price_baggage = price_baggage + price_baggage*0.1
elif 7 <= days_till_trip <= 30:
    price_baggage = price_baggage + price_baggage * 0.15
else:
    price_baggage = price_baggage + price_baggage * 0.4

total_price = numbers_of_baggage * price_baggage
print(f"The total price of bags is: {total_price:.2f} lv.")



