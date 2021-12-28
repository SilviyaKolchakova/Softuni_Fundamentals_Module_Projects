initial_gifts_list = input().split()
command = input()

while command != 'No Money':
    next_list = command.split()
    if next_list[0] == 'OutOfStock':
        for element in range(len(initial_gifts_list)):
            if initial_gifts_list[element] == str(next_list[1]):
                initial_gifts_list[element] = 'None'
    elif next_list[0] == 'Required':
        if 0 <= int(next_list[2]) < len(initial_gifts_list):
            initial_gifts_list[int(next_list[2])] = next_list[1]
    elif next_list[0] == 'JustInCase':
        initial_gifts_list[-1] = next_list[1]
    command = input()
new_list = []
for i in initial_gifts_list:
    if i == 'None':
        continue
    new_list.append(i)

print(' '.join(new_list))