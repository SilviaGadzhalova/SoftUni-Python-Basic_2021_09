days_for_stay = int(input())
type_of_the_room = input()
rating = input()

room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
nights = days_for_stay - 1

if type_of_the_room == "room for one person":
    total_room_for_one_person = room_for_one_person *nights
    if rating == "positive":
        total_room_for_one_person = total_room_for_one_person + total_room_for_one_person*0.25
        print(f"{total_room_for_one_person:.2f}")
    else:
        total_room_for_one_person = total_room_for_one_person - total_room_for_one_person*0.1
        print(f"{total_room_for_one_person:.2f}")

elif type_of_the_room == "apartment":
    total_apartment = apartment*nights
    if days_for_stay < 10:
        total_apartment = total_apartment - total_apartment * 0.3
    elif days_for_stay <= 15 or days_for_stay == 10:
        total_apartment = total_apartment - total_apartment * 0.35
    else:
        total_apartment = total_apartment - total_apartment * 0.5
    if rating == "positive":
        total_apartment = total_apartment + total_apartment * 0.25
        print(f"{total_apartment:.2f}")
    else:
        total_apartment = total_apartment - total_apartment * 0.1
        print(f"{total_apartment:.2f}")

elif type_of_the_room == "president apartment":
    total_president_apartment = president_apartment * nights
    if days_for_stay < 10:
        total_president_apartment = total_president_apartment - total_president_apartment * 0.1
    elif days_for_stay <= 15 or days_for_stay == 10:
        total_president_apartment = total_president_apartment - total_president_apartment * 0.15
    else:
        total_president_apartment = total_president_apartment - total_president_apartment * 0.2
    if rating == "positive":
        total_president_apartment = total_president_apartment + total_president_apartment * 0.25
        print(f"{total_president_apartment:.2f}")
    else:
        total_president_apartment = total_president_apartment - total_president_apartment * 0.1
        print(f"{total_president_apartment:.2f}")