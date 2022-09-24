rent = int(input())

statuets = rent - rent*0.3
ketaring = statuets - statuets*0.15
dj = ketaring/2

total = rent + statuets + ketaring + dj

print(f"{total:.2f}")
