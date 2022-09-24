sum = 0

while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())

    while budget > sum:
        current_budget = float(input())
        sum += current_budget
    if sum >= budget:
        print(f"Going to {destination}!")
        sum = 0
    else:
        break




