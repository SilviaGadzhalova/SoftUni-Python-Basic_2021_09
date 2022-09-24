import sys
min_number = sys.maxsize

while True:
    current_number = input()
    if current_number == "Stop":
        break
    elif int(current_number) < min_number:
        min_number = int(current_number)

print(min_number)