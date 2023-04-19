n_students = int(input())
students_dict = {}

for _ in range(n_students):
    current_student = input().split()
    name = current_student[0]
    grade = float(current_student[1])

    if name not in students_dict.keys():
        students_dict[name] = []
    students_dict[name].append(grade)

for k, v in students_dict.items():
    total_grades = ' '.join(f"{gr:.2f}" for gr in v)
    return_grade_to_float = list(map(float, total_grades.split(" ")))
    average_grade = sum(return_grade_to_float) / len(return_grade_to_float)
    print(f"{k} -> {total_grades} (avg: {average_grade:.2f})")
