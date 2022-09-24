country = input()
device = input()

if device == "ribbon":
    if country == "Russia":
        difficulty = 9.100
        performance = 9.400
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
    elif country == "Bulgaria":
        difficulty = 9.600
        performance = 9.400
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
    elif country == "Italy":
        difficulty = 9.200
        performance = 9.500
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
elif device == "hoop":
    if country == "Russia":
        difficulty = 9.300
        performance = 9.800
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
    elif country == "Bulgaria":
        difficulty = 9.550
        performance = 9.750
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
    elif country == "Italy":
        difficulty = 9.450
        performance = 9.350
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
elif device == "rope":
    if country == "Russia":
        difficulty = 9.600
        performance = 9.000
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
    elif country == "Bulgaria":
        difficulty = 9.500
        performance = 9.400
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")
    elif country == "Italy":
        difficulty = 9.700
        performance = 9.150
        total = difficulty+performance
        points = 20 - total
        procent = (points / 20) * 100
        print(f"The team of {country} get {total:.3f} on {device}.")
        print(f"{procent:.2f}%")