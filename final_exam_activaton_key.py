activation_key = input()

command = input()

while not command == 'Generate':
    operation = command.split('>>>')
    next_operation = operation[0]
    if next_operation == 'Contains':
        substring = operation[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif next_operation == 'Flip':
        case = operation[1]
        start_index = int(operation[2])
        end_index = int(operation[3])
        substring = activation_key[start_index:end_index]
        if case == 'Upper':
            activation_key = activation_key.replace(substring, substring.upper())
        elif case == 'Lower':
            activation_key = activation_key.replace(substring, substring.lower())
        print(activation_key)
    elif next_operation == 'Slice':
        start_index = int(operation[1])
        end_index = int(operation[2])
        substring_to_remove = activation_key[start_index:end_index]
        activation_key = activation_key.replace(substring_to_remove, '')
        print(activation_key)
    command = input()

print(f'Your activation key is: {activation_key}')