string = input()

while not string == 'end':

    next_string = string
    reversed_string = next_string[::-1]
    print(f'{next_string} = {reversed_string}')
    string = input()

