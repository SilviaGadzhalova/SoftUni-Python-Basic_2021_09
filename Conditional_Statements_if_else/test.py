sum = int(input())
r_dni = 365 - sum
pochivni_dni = sum * 127
rabotni_dni = r_dni *63
game = pochivni_dni + rabotni_dni
norma = abs(30000 - game)
hours = abs(norma // 60)
minu = norma % 60

if game>30000:
    print (f"Tom will run away! {hours} hours and {minu} minutes more to play")
else:
    print(f"Tom sleeps well! {hours} hours and {minu} minutes less for play.")