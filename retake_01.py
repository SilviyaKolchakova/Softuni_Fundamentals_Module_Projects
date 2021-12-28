email = input()
command = input()
is_alphanum = False
upperdigit = 0
is_upperdigit = False
lowerdigit = 0
is_lower = False
digit = 0
is_digit = False

while not command == 'Valid':
    next_command = command.split(' ')
    action_name = next_command[0]
    if action_name == 'Upper':
        index = int(next_command[1])
        letter = email[index]
        email = email.replace(letter, letter.upper())
        print(email)
    elif action_name == 'Lower':
        index = int(next_command[1])
        letter = email[index]
        email = email.replace(letter, letter.lower())
        print(email)
    elif action_name == 'Insert':
        index = int(next_command[1])
        char = next_command[2]
        email = email[:index] + char + email[index:]
        print(email)
    elif action_name == 'Change':
        char_to_change = next_command[1]
        value = int(next_command[2])
        new_char = chr(ord(char_to_change) + value)
        email = email.replace(char_to_change, new_char)
        print(email)
    elif action_name == 'Validation':
        if len(email) < 6:
            print("Email must be at least 6 characters long!")
        for digit in email:
            if digit.isalnum() or digit == '@':
                is_alphanum = True
            if digit.isupper():
                upperdigit += 1
                if upperdigit >= 1:
                    is_upperdigit = True
            if digit.islower():
                lowerdigit += 1
                if lowerdigit >= 1:
                    is_lower = True
            if digit.isdigit():
                digit += 1
                if digit >= 1:
                    is_digit = True
        if not is_alphanum:
            print("Email must consist only of letters, digits and @!")
        if not is_upperdigit:
            print("Email must consist at least one uppercase letter!")
        if not is_lower:
            print("Email must consist at least one lowercase letter!")
        if not is_digit:
            print("Email must consist at least one digit!")
    command = input()
