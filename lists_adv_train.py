wagons = int(input())
train = [0] * wagons

command = input()

while not command == 'End':
    next_command = command.split()
    if next_command[0] == 'add':
        train[-1] += int(next_command[1])
    elif next_command[0] == 'insert':
        index = int(next_command[1])
        number_of_people = int(next_command[2])
        train[index] += number_of_people
    elif next_command[0] == 'leave':
        index = int(next_command[1])
        number_of_people = int(next_command[2])
        train[index] -= number_of_people
    command = input()
print(train)


