name_of_the_agency = input()
number_tickets_for_adults = int(input())
number_kids_tickets = int(input())
net_price_for_adults_ticket = float(input())
tax = float(input())

net_price_for_kids_ticket = net_price_for_adults_ticket - net_price_for_adults_ticket*0.7

price_adult = net_price_for_adults_ticket + tax
price_kids = net_price_for_kids_ticket +tax

total_sale = number_kids_tickets* price_kids + number_tickets_for_adults*price_adult
profit = total_sale*0.2
print(f"The profit of your agency from {name_of_the_agency} tickets is {profit:.2f} lv.")

