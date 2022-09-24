price_kg_vegetables = float(input())
price_kg_fruits = float(input())
kg_vegetables = int(input())
kg_fruits = int(input())

total_vegetables = price_kg_vegetables * kg_vegetables
total_fruits = price_kg_fruits*kg_fruits
sum = total_fruits + total_vegetables
final_euro = sum/1.94

print(f"{final_euro:.2f}")
