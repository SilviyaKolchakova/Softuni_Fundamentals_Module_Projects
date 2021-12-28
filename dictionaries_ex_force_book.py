command = input()

side_user_dict = {}

while not command == 'Lumpawaroo':
    if '|' in command:
        next_command = command.split(' | ')
        side = next_command[0]
        user = next_command[1]
        for side, user in side_user_dict.items():
            if user not in side_user_dict:
                if side not in side_user_dict:
                    side_user_dict[side] = []
                    side_user_dict[side].append(user)
                else:
                    side_user_dict[side].append(user)
                side_user_dict[side] = []
                side_user_dict[side].append(user)
            else:
                continue
        #for side, users in side_user_dict.items():
            #if user in users:
                #continue
    if '->' in command:
        next_command = command.split(' -> ')
        user = next_command[0]
        side = next_command[1]
        for side, users in side_user_dict.items():
            if user not in side_user_dict:
                if side not in side_user_dict:
                    side_user_dict[side] = []
                    side_user_dict[side].append(user)
                else:
                    side_user_dict[side].append(user)
            else:
                side_user_dict[side].remove(user)
            side_user_dict[side].append(user)


        #for side, users in side_user_dict.items():
            #if user in users:
                #side_user_dict[side].remove(user)
            #side_user_dict[side].append(user)

        #if user not in side_user_dict.values():
           # side_user_dict[side].append(user)
        #elif side not in side_user_dict and user not in side_user_dict:
         #   side_user_dict[side] = []
          #  side_user_dict[side].append(user)
        print(f"{user} joins the {side} side!" )

    command = input()

for side, user in sorted(side_user_dict.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(user) > 0:
        print(f'Side: {side}, Members: {len(user)}')

        for user1 in sorted(user):
            print(f'! {user1}')