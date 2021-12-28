command = input()

cities = {}
while not command == 'Sail':
    next_city = command.split('||')
    city, population, gold = next_city[0], int(next_city[1]), int(next_city[2])
    if city in cities:
        cities[city]['population'] += population
        cities[city]['gold'] += gold
    else:
        cities[city] = {'population': population, 'gold': gold}
    command = input()
command = input()
while not command == 'End':
    event = command.split('=>')
    action = event[0]
    if action == 'Plunder':
        city = event[1]
        cities[city]['population'] -= int(event[2])
        cities[city]['gold'] -= int(event[3])
        print(f"{city} plundered! {event[3]} gold stolen, {event[2]} citizens killed.")
        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            print(f'{city} has been wiped off the map!')
            del cities[city]
    elif action == 'Prosper':
        city = event[1]
        if int(event[2]) > 0:
            cities[city]['gold'] += int(event[2])
            print(f"{int(event[2])} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")
    command = input()
if cities:
    print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')
    sorted_cities = sorted(cities.items(), key=lambda kvp: (-kvp[1]['gold'], kvp[0]))
    for city, items in sorted_cities:
        print(f"{city} -> Population: {items['population']} citizens, Gold: {items['gold']} kg")



