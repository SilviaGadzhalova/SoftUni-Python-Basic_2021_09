name = input()
classes = 0
total_grade = 0
counter = 0
while True:
    grade = float(input())
    if grade >= 4:
        total_grade += grade
        classes += 1
    if grade < 4:
        counter += 1
        if counter > 1:
            classes += 1
            print(f"{name} has been excluded at {classes} grade")
            break
    if classes == 12:
        average_grade = total_grade / classes
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break