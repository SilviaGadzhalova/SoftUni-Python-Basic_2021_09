number_of_flours = int(input())
number_of_rooms = int(input())
rooms_number = " "

for f in range(number_of_flours, 0, -1):
    for r in range(number_of_rooms):
        current_number_of_rooms = f * 10 + r
        if f == number_of_flours:
            print(f"L{current_number_of_rooms}",end=" ")
        elif f % 2 !=0:
            rooms_number += f"A{current_number_of_rooms} "
        else:
            rooms_number += f"O{current_number_of_rooms} "
    print(rooms_number)
    rooms_number = ""