string = input()
command = input()

while not command == 'Done':
    if 'Change' in command:
        next_command = command.split()
        char = next_command[1]
        replacement = next_command[2]
        string = string.replace(char, replacement)
        print(string)
    elif 'Include' in command:
        next_command = command.split()
        other_string = next_command[1]
        if other_string in string:
            print('True')
        else:
            print('False')
    elif 'End' in command:
        next_command = command.split()
        other_string = next_command[1]
        length = len(other_string)
        if string[-length:] == other_string:
            print('True')
        else:
            print('False')
    elif 'Uppercase' in command:
        string = string.upper()
        print(string.upper())
    elif 'FindIndex' in command:
        next_command = command.split()
        char = next_command[1]
        print(string.find(char))
    elif 'Cut' in command:
        next_command = command.split()
        start_index = int(next_command[1])
        length = int(next_command[2])
        string = string[start_index:(start_index+length)]
        print(string)
    command = input()