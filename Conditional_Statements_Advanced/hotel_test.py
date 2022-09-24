month = input()
number_of_nights = int(input())
price_for_apartment = 0
price_for_studio = 0
if month == "May" or month == "October":
    price_for_studio = 50 * number_of_nights
    price_for_apartment = 65 * number_of_nights
elif month == "June" or month == "September":
    price_for_studio = 75.2 * number_of_nights
    price_for_apartment = 68.7 * number_of_nights
elif month == "July" or month == "August":
    price_for_studio = 76 * number_of_nights
    price_for_apartment = 77 * number_of_nights
if 14 >= number_of_nights > 7 and (month == "May" or month == "October"):
    price_for_studio *= 0.95
elif 14 < number_of_nights and (month == "May" or month == "October"):
    price_for_studio *= 0.70
elif 14 < number_of_nights and (month == "June" or month == "September"):
    price_for_studio *= 0.80
if 14 < number_of_nights:
    price_for_apartment *= 0.9
print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")