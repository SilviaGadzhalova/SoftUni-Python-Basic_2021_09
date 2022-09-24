number_of_tabs = int(input())
salary = int(input())

fine_from_the_salary = False

for _ in range(number_of_tabs):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        fine_from_the_salary = True
        break
if fine_from_the_salary:
    print(f"You have lost your salary.")
else:
    print(salary)

