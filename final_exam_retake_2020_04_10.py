message = input()
command = input()


while not command == 'Reveal':
    next_command = command.split(':|:')
    instruction = next_command[0]
    if instruction == 'InsertSpace':
        index = int(next_command[1])
        message = message[:index] + ' ' + message[index:]
        print(message)
    elif instruction == 'Reverse':
        substring = next_command[1]
        old_message = message
        new_message = message.replace(substring, "", 1)
        if old_message == new_message:
            print('error')
        else:
            substring = substring[::-1]
            message = new_message+substring
            print(message)
    elif instruction == 'ChangeAll':
        substring = next_command[1]
        replacement = next_command[2]
        for i in range(len(message)):
            if message[i] == substring:
                message[i].replace(substring, replacement)
                pass



