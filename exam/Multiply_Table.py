n = int(input())
text = str(n)
a = int(text[2])
b = int(text[1])
c = int(text[0])
for x in range(1,a+1):
    for y in range(1,b+1):
        for z in range(1,c+1):
            result = x*y*z
            print(f"{x} * {y} * {z} = {result};")