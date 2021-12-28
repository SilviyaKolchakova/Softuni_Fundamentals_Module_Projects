room_number = int(input())
rooms_list = []
next_room = input()

while next_room:
    rooms_list.append(next_room)
    next_room = input()
print(rooms_list)

needed_chairs_in_room = [for el in range(len(rooms_list)) if len(int(el[0]) != int(el[1])]