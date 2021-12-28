commands_count = int(input())

users_registered = {}

for i in range(commands_count):
    command = input()
    next_command = command.split()
    if next_command[0] == 'register':
        username = next_command[1]
        plate_number = next_command[2]
        if username not in users_registered:
            users_registered[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    if next_command[0] == 'unregister':
        username = next_command[1]
        if username not in users_registered:
            print(f"ERROR: user {username} not found")
        else:
            plate = users_registered.pop(username)
            print(f"{username} unregistered successfully")


for k, v in users_registered.items():
    print(f"{k} => {v}")


