name_of_the_film = input()
number_of_days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
profit = int(input())/100

sum_for_day = number_of_tickets * ticket_price
sum_period = number_of_days * sum_for_day
total = sum_period - sum_period*profit
print(f"The profit from the movie {name_of_the_film} is {total:.2f} lv.")
