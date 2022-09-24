name_of_the_movie = input()
student_tickets_counter = 0
standard_tickets_counter = 0
kids_tickets_counter = 0
total_tickets_counter = 0

while name_of_the_movie != "Finish":
    number_of_free_seats = int(input())
    total_seats = number_of_free_seats
    sold_tickets = 0
    while number_of_free_seats >0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets_counter +=1
        elif ticket_type == "standard":
            standard_tickets_counter +=1
        elif ticket_type == "kid":
            kids_tickets_counter +=1
        number_of_free_seats -= 1
        sold_tickets += 1
        total_tickets_counter += 1
    print(f"{name_of_the_movie} - {sold_tickets/total_seats*100:.2f}% full.")
    name_of_the_movie = input()
print(f"Total tickets: {total_tickets_counter}")
print(f"{student_tickets_counter/total_tickets_counter*100:.2f}% student tickets.")
print(f"{standard_tickets_counter/total_tickets_counter*100:.2f}% standard tickets.")
print(f"{kids_tickets_counter/total_tickets_counter*100:.2f}% kids tickets.")
