import math
name_of_series = str(input())
duration_of_the_episode = int(input())
duration_of_the_break = int(input())

lunch_time = duration_of_the_break * 0.125
relax_time = duration_of_the_break * 0.25

total_time = duration_of_the_break - lunch_time - relax_time


if total_time >= duration_of_the_episode:
    remaining_time = total_time - duration_of_the_episode
    remaining_time = math.ceil(remaining_time)
    print(f"You have enough time to watch {name_of_series} and left with {remaining_time} minutes free time.")
else:
    needed_time = duration_of_the_episode - total_time
    needed_time = math.ceil(needed_time)
    print(f"You don't have enough time to watch {name_of_series}, you need {needed_time} more minutes.")