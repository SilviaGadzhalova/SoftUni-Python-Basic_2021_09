price_kg_skumriq = float(input())
price_kg_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())
price_kg_midi = 7.5
price_kg_palamud = price_kg_skumriq + price_kg_skumriq * 0.6
price_kg_safrid = price_kg_caca + price_kg_caca * 0.8

price_midi = kg_midi * price_kg_midi
price_palamud = kg_palamud * price_kg_palamud
price_safrid = kg_safrid * price_kg_safrid

total = price_safrid + price_palamud +price_midi
print(f"{total:.2f}")
