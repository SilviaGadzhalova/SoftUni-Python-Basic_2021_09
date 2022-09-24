n = int(input())
sum = 0
rating_all = 0
for i in range(n):
    current_number = int(input())
    text = str(current_number)
    rating = int(text[2])
    sales = int(text[0] + text[1])
    if rating == 2:
        profit = 0
    elif rating == 3:
        profit = 0.5
    elif rating == 4:
        profit = 0.7
    elif rating == 5:
        profit = 0.85
    elif rating == 6:
        profit = 1
    total_model = profit*sales
    sum +=total_model
    rating_all +=rating
total_rating = rating_all/n
print(f"{sum:.2f}")
print(f"{total_rating:.2f}")
