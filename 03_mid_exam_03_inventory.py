inventory = input().split(', ')

command = input()

while not command == 'Craft!':
    next_command = command.split(' - ')
    if next_command[0] == "Collect":
        item = next_command[1]
        if item not in inventory:
            inventory.append(item)
    elif next_command[0] == "Drop":
        item = next_command[1]
        if item in inventory:
            inventory.remove(item)
    elif next_command[0] == "Combine Items":
        second_part = next_command[1].split(":")
        old_item = second_part[0]
        new_item = second_part[1]
        if old_item in inventory:
            index = inventory.index(old_item)
            inventory.insert(int(index) + 1, new_item)
    elif next_command[0] == "Renew":
        item = next_command[1]
        if item in inventory:
            inventory.append(inventory.pop(inventory.index(item)))
    command = input()
print(", ".join(inventory))


