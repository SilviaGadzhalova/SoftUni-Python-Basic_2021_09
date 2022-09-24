number_of_groups = int(input())

total_people = 0
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0

for _ in range(number_of_groups):
    people_in_group = int(input())
    total_people += people_in_group
    if people_in_group <= 5:
        group1 += people_in_group
    elif 6 <= people_in_group <= 12:
        group2 += people_in_group
    elif 13 <= people_in_group <= 25:
        group3 += people_in_group
    elif 26 <= people_in_group <= 40:
        group4 += people_in_group
    else:
        group5 += people_in_group
percent_group1 = group1 / total_people * 100
percent_group2 = group2 / total_people * 100
percent_group3 = group3 / total_people * 100
percent_group4 = group4 / total_people * 100
percent_group5 = group5 / total_people * 100

print(f'{percent_group1:.2f}%')
print(f'{percent_group2:.2f}%')
print(f'{percent_group3:.2f}%')
print(f'{percent_group4:.2f}%')
print(f'{percent_group5:.2f}%')