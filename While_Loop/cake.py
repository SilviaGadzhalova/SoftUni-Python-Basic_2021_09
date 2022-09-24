width = int(input())
length = int(input())
cake = width*length
cake_peace = 1*1
there_is_more_cake = True

peace = input()
while peace != "STOP" and cake >=0:
    peaces_of_cake = int(peace)
    cake -= peaces_of_cake
    if cake <0:
        there_is_more_cake = False
        break
    peace = input()
if there_is_more_cake:
    print(f"{cake} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake)} pieces more.")
