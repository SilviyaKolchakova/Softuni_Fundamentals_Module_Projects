chat_list = []

command = input()

while not command == 'end':
    next_command = command.split(" ")
    if next_command[0] == 'Chat':
        chat_list.append(next_command[1])
    elif next_command[0] == 'Delete':
        message = next_command[1]
        if message in chat_list:
            chat_list.remove(message)
    elif next_command[0] == 'Edit':
        message = next_command[1]
        new_message = next_command[2]
        if message in chat_list:
            index = chat_list.index(message)
            chat_list[index] = new_message
    elif next_command[0] == 'Pin':
        message = next_command[1]
        if message in chat_list:
            chat_list.append(chat_list.pop(chat_list.index(message)))
    elif next_command[0] == 'Spam':
        message1 = next_command[1::]
        chat_list.extend(message1)
    command = input()
print("\n".join(chat_list))



