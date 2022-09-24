city = str(input())
sales_volume = float(input())
comissions = 0

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        comissions = sales_volume * 0.05
        print(f"{comissions:.2f}")
    elif 500 < sales_volume <= 1000:
        comissions = sales_volume * 0.07
        print(f"{comissions:.2f}")
    elif 1000 < sales_volume <= 10000:
        comissions = sales_volume * 0.08
        print(f"{comissions:.2f}")
    elif sales_volume > 10000:
        comissions = sales_volume * 0.12
        print(f"{comissions:.2f}")
    elif sales_volume<0:
        print("error")

elif city == "Varna":
    if 0 <= sales_volume <= 500:
        comissions = sales_volume * 0.045
        print(f"{comissions:.2f}")
    elif 500 < sales_volume <= 1000:
        comissions = sales_volume * 0.075
        print(f"{comissions:.2f}")
    elif 1000 < sales_volume <= 10000:
        comissions = sales_volume * 0.1
        print(f"{comissions:.2f}")
    elif sales_volume > 10000:
        comissions = sales_volume * 0.13
        print(f"{comissions:.2f}")
    elif sales_volume < 0:
        print("error")

elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        comissions = sales_volume * 0.055
        print(f"{comissions:.2f}")
    elif 500 < sales_volume <= 1000:
        comissions = sales_volume * 0.08
        print(f"{comissions:.2f}")
    elif 1000 < sales_volume <= 10000:
        comissions = sales_volume * 0.12
        print(f"{comissions:.2f}")
    elif sales_volume > 10000:
        comissions = sales_volume * 0.145
        print(f"{comissions:.2f}")
    elif sales_volume < 0:
        print("error")
else:
    print("error")


