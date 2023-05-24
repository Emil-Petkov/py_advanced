def average_grade(value):
    return (sum(value)) / len(value)


students = {}

for _ in range(int(input())):
    data = input().split()
    name = data[0]
    grade = float(data[1])

    if name not in students:
        students[name] = []
    students[name].append(grade)

for key, value in students.items():
    grades = " ".join("{:.2f}".format(v) for v in value)

    print(f"{key} -> {grades} (avg: {average_grade(value):.2f})")

# for k, v in dict.items():
#     print(f"{k} -> {' '.join([f'{g:.2f}' for g in v])} (avg: {average_grade(v):.2f})")
