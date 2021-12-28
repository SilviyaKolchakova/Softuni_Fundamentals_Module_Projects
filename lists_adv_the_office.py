happiness_as_string = input().split()
factor = int(input())

happy_count = list(map(int, happiness_as_string))
happy_count_multiplied = [el * factor for el in happy_count]
average_happiness = sum(happy_count_multiplied) / len(happy_count_multiplied)
only_happy_list = [el for el in happy_count_multiplied if el >= average_happiness]
if len(only_happy_list) >= len(happy_count_multiplied) / 2:
    print(f'Score: {len(only_happy_list)}/{len(happy_count_multiplied)}. Employees are happy!')
else:
    print(f'Score: {len(only_happy_list)}/{len(happy_count_multiplied)}. Employees are not happy!')

