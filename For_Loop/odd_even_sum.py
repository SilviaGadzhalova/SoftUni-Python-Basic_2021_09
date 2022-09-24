number = int(input())
odd_sum = 0
even_sum = 0
for num in range(1,number+1):
    current_number = int(input())
    if num % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number
if odd_sum == even_sum:
    print("Yes")
    print(f"Sum =",abs(even_sum))
else:
    diff = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff =",diff)