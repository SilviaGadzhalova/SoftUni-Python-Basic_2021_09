budget = float(input())
season = input()

if budget <= 100:
    if season == "summer":
        price = budget*0.3
        print("Somewhere in Bulgaria")
        print(f"Camp - {price:.2f}")
    else:
        price = budget*0.7
        print("Somewhere in Bulgaria")
        print(f"Hotel - {price:.2f}")

elif budget<= 1000:
    if season == "summer":
        price = budget*0.4
        print("Somewhere in Balkans")
        print(f"Camp - {price:.2f}")
    else:
        price = budget*0.8
        print("Somewhere in Balkans")
        print(f"Hotel - {price:.2f}")
else:
    price = budget*0.9
    print("Somewhere in Europe")
    print(f"Hotel - {price:.2f}")


