notes = [0] * 10
next_command = input()

while not next_command == 'End':
    importance, command = next_command.split('-')
    index = int(importance) - 1
    notes[index] = command
    next_command = input()
print([el for el in notes if not el == 0])