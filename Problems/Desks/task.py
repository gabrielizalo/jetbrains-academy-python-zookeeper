students_class_1 = int(input())
students_class_2 = int(input())
students_class_3 = int(input())

desks_class_1 = (students_class_1 // 2) + (students_class_1 % 2)
desks_class_2 = (students_class_2 // 2) + (students_class_2 % 2)
desks_class_3 = (students_class_3 // 2) + (students_class_3 % 2)

total_desks = desks_class_1 + desks_class_2 + desks_class_3
print(total_desks)
