number_of_pages = int(input())
pages_per_hour = int(input())
number_of_days = int(input())

total_time_for_reading = number_of_pages / pages_per_hour
hours_for_daily_reading = total_time_for_reading / number_of_days
rounded_value = round(hours_for_daily_reading)
print(rounded_value)