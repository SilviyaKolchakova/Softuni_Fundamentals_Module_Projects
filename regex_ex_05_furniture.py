import re

pattern = r'\>>(?P<furniture>[A-Za-z]+)\<<(?P<price>\d+(\.\d+)?)+\!(?P<qty>\d+)'

command = input()
furniture_names = []
total_cost = 0
while not command == 'Purchase':
    match = re.match(pattern, command)
    if match:
        data = match.groupdict()
        furniture_names.append(data['furniture'])
        total_cost += int(data['qty']) * float(data['price'])
    command = input()

print('Bought furniture:')
for furniture in furniture_names:
    if furniture:
        print(furniture,end='\n')
print(f'Total money spend: {total_cost:.2f}')

