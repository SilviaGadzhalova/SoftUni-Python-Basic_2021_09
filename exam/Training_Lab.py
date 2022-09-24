height = float(input())
width = float(input())
width_sm = width*100
height_sm = height*100
corridor = 100
one_working_place = 70 * 120
door =one_working_place
teacher_place = 160*120
teacher_place = 2*one_working_place
left_width_space = width_sm - corridor
number_of_working_tables = left_width_space//70
rows = height_sm//120

total_sits = number_of_working_tables*rows - 3
print(round(total_sits))