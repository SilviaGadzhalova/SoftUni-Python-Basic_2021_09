number_bad_grade = int(input())
failed_times = 0
solve_problems_counter = 0
grades_sum = 0
last_problem = " "
has_failed = True
while failed_times < number_bad_grade:
    name_of_the_tax = input()
    if name_of_the_tax == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
      failed_times += 1
    grades_sum += grade
    solve_problems_counter += 1
    last_problem = name_of_the_tax
if has_failed:
    print(f"You need a break, {number_bad_grade} poor grades.")
else:
    average_grade = grades_sum/solve_problems_counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {solve_problems_counter}")
    print(f"Last problem: {last_problem}")
