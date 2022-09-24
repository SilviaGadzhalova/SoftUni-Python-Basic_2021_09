steps_counter = 0

while steps_counter < 10000:
    steps = input()
    if steps == "Going home":
        steps = input()
        steps_counter += int(steps)
        break
    else:
        steps_made = int(steps)
        steps_counter += steps_made

difference = round(abs(10000 - steps_counter))
if steps_counter < 10000:
    print(f"{difference} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
