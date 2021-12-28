messages_capacity = int(input())
users = {}
data = input()

while not data == 'Statistics':
    command = data.split('=')
    if command[0] == 'Add':
        user, sent, received = command[1], int(command[2]), int(command[3])
        if user not in users:
            users[user] = {'sent': sent, 'received': received}
        else:
            data = input()
            continue
    elif command[0] == 'Message':
        sender = command[1]
        receiver = command[2]
        if sender in users and receiver in users:
            users[sender]['sent'] += 1
            users[receiver]['received'] += 1
            if users[sender]['sent'] + users[sender]['received'] >= messages_capacity:
                print(f"{sender} reached the capacity!")
                users.pop(sender)
            elif users[receiver]['sent'] + users[receiver]['received'] >= messages_capacity:
                print(f"{receiver} reached the capacity!")
                users.pop(receiver)
    elif command[0] == 'Empty':
        user = command[1]
        if user in users:
            users.pop(user)
        elif user == 'All':
            users.clear()
    data = input()
print(f'Users count: {len(users)}')

sorted_result = sorted(users.items(), key=lambda kvp: (-kvp[1]['received'], kvp[0]))
print(sorted_result)
for user, messages in sorted_result:
    print(f'{user} - {sum(messages.values())}')