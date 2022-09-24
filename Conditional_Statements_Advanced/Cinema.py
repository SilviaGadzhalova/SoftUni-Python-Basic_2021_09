projection = input()
r = int(input())
c = int(input())


if projection == "Premiere":
    total_income = r*c*12.00
    print(f"{total_income:.2f}leva")
elif projection == "Normal":
    total_income = r * c * 7.50
    print(f"{total_income:.2f}leva")
elif projection == "Discount":
    total_income = r * c * 5.00
    print(f"{total_income:.2f}leva")