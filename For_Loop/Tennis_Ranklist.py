import math
tournament = int(input())
points = int(input())
wins = 0
current_points = 0
for _ in range(tournament):
    final_place = input()
    if final_place == "W":
        wins += 1
        current_points += 2000
    elif final_place == "F":
        current_points += 1200
    else:
        current_points += 720
print(f"Final points: {points + current_points}")
print(f"Average points: {math.floor(current_points / tournament)}")
print(f"{(wins / tournament) * 100:.2f}%")