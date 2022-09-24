record_seconds = float(input())
distance_metres = float(input())
time_for_meter = float(input())

time_for_distance = distance_metres*time_for_meter          # time_for_distance = distance_metres*time_for_meter
                                                            # +delay

if distance_metres >= 15:                                   # delay = distance_metres //15*12.5
    slowing_distance = distance_metres//15
    slowing_time= slowing_distance *12.5
    total_time = time_for_distance + slowing_time
else:
    total_time = time_for_distance

if total_time < record_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    missing_seconds = total_time - record_seconds
    print(f"No, he failed! He was {missing_seconds:.2f} seconds slower.")
