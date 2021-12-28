command = input()
resources = []
while not command == 'stop':
    next_resource = command
    resources.append(next_resource)
    command = input()
resources_dict = {}
for el in range(0, len(resources), 2):
    keys = resources[el]
    values = (int(resources[el + 1]))
    if resources[el] not in resources_dict:
        resources_dict[keys] = values
    else:
        resources_dict[keys] += values

for key, value in resources_dict.items():
    print(f'{key} -> {value}')
