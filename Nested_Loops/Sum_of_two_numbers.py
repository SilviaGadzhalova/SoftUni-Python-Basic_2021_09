start = int(input())
final = int(input())
magic_n = int(input())
combo = 0
condition = False

for i in range(start, final+1):
    for x in range(start, final + 1):
        combo +=1
        if i+x == magic_n:
            condition = True
            print(f"Combination N:{combo} ({i} + {x} = {magic_n})")
            break
    if condition:
        break
if not condition:
    print(f"{combo} combinations - neither equals {magic_n}")