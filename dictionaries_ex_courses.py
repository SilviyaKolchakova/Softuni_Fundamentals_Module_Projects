command = input()
courses = {}
while not command == 'end':
    next_command = command.split(' : ')
    course_name = next_command[0]
    student_name = next_command[1]
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)
    command = input()
for (k, v) in sorted(courses.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{k}: {len(v)}")
    for user in sorted(v,key=lambda x: x):
        print(f"-- {user}")
