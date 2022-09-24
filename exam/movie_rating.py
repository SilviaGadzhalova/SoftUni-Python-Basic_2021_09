import sys
number_of_films = int(input())
max_rating = -sys.maxsize
min_rating = sys.maxsize
total_rating = 0
condition = False
for i in range(number_of_films+1):
    name_of_movie = input()
    rating = float(input())
    if rating > max_rating:
        max_rating = rating
        total_rating += rating
        condition = True
    if rating < min_rating:
        min_rating = rating
        total_rating += rating
        condition = True
if condition:
    print(f"{name_of_movie} is with highest rating: {rating}")
else:
    print(f"{name_of_movie} is with lowest rating: {rating}")
average_rating = total_rating / number_of_films
print(f"{average_rating:.2}")