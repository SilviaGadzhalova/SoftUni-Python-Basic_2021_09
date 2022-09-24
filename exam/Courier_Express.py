kg = float(input())
type_of_service = input()
km = int(input())

if type_of_service == "standard":
    time_for_delivery = 3
    if kg < 1:
        price_km = km*0.03
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
    elif 1 <= kg < 10:
        price_km = km * 0.05
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
    elif 10 <= kg < 40:
        price_km = km * 0.10
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
    elif 40 <= kg < 90:
        price_km = km * 0.15
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
    elif 90 <= kg <150:
        price_km = km * 0.20
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
elif type_of_service == "express":
    time_for_delivery = 1
    if kg < 1:
        price_km = km * 0.03
        kg_procent = 0.03 * 0.8
        total_procent = kg * kg_procent
        total = price_km + (km * total_procent)
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
    elif 1 <= kg < 10:
        price_km = km * 0.05
        kg_procent = 0.05 * 0.4
        total_procent = kg * kg_procent
        total = price_km + (km * total_procent)
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
    elif 10 <= kg < 40:
        price_km = km * 0.10
        kg_procent = 0.10 * 0.05
        total_procent = kg * kg_procent
        total = price_km + (km * total_procent)
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")
    elif 40 <= kg < 90:
        price_km = km*0.15
        kg_procent = 0.15*0.02
        total_procent = kg*kg_procent
        total = price_km + (km*total_procent)
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {total:.2f} lv.")
    elif 90 <= kg < 150:
        price_km = km * 0.2
        kg_procent = 0.2 * 0.01
        total_procent = kg * kg_procent
        total = price_km + (km * total_procent)
        print(f"The delivery of your shipment with weight of {kg:.3f} kg. would cost {price_km:.2f} lv.")



