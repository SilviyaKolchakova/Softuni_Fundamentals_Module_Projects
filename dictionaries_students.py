data = input()

courses = {}

while ":" in data:
    name, id, course = data.split(":")
    if course not in courses:
        courses[course] = {}
    courses[course][id] = name
    data = input()

searched_course = data
searched_course_as_list = data.split("_")
searched_course = " ".join(searched_course_as_list)


for item in courses:
    if item == searched_course:
        for id, name in courses[item].items():
            print(f'{name} - {id}')

