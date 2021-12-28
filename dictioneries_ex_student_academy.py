rows = int(input())
students_grades = {}

for item in range(rows):
    student = input()
    grade = input()
    if student not in students_grades:
        students_grades[student] = [float(grade)]
    else:
        students_grades[student].append(float(grade))
students_average_grades = {}
for k, v in students_grades.items():
    student = k
    average_grade = sum(v) / len(v)
    students_average_grades[student] = [average_grade]


for student, grade in sorted(students_average_grades.items(), key=lambda x: x[1], reverse=True):
    if sum(grade) / len(grade) >= 4.50:
        print(f'{student} -> {sum(grade) / len(grade):.2f}')