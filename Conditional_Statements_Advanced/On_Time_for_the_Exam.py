hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_of_the_exam = hour_of_exam*60 + minutes_of_exam
time_of_the_arrival = hour_of_arrival*60 +minutes_of_arrival

if time_of_the_arrival > time_of_the_exam:
    print("Late")
elif time_of_the_exam -30 <= time_of_the_arrival <= time_of_the_exam:
    print("On time")
else:
    print("Early")
difference = abs(time_of_the_arrival - time_of_the_exam)
if time_of_the_exam -60 < time_of_the_arrival<time_of_the_exam:
    print(f"{difference} minutes before the start")
elif time_of_the_arrival <= time_of_the_exam -60:
    hours = difference//60
    minutes = difference % 60
    if minutes <10:
        print(f"{hours}:0{minutes} hours before the start")
        #print(f"{hours}:{minutes:02d} hours before the start")
    else:
        print(f"{hours}:{minutes} hours before the start")
elif time_of_the_exam < time_of_the_arrival < time_of_the_exam +60:
    print(f"{difference} minutes after the start")
elif time_of_the_arrival >= time_of_the_exam +60:
    hours = difference // 60
    minutes = difference % 60
    if minutes < 10:
        print(f"{hours}:{minutes:02d} hours after the start")
    else:
        print(f"{hours}:{minutes} hours after the start")