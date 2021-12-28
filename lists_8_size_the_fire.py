fires_list = input().split('#')
amount_water = int(input())
total_fire = 0
effort = 0
next_fire = []
cells_list = []

for fire in range(0, len(fires_list)):
    next_fire = fires_list[fire].split(' = ')
    if amount_water < int(next_fire[1]):
        continue
    if amount_water <= 0:
        break
    if 'High' in next_fire and 81 <= int(next_fire[1]) <= 125:
        amount_water -= int(next_fire[1])
        effort += int(next_fire[1]) * 0.25
        total_fire += int(next_fire[1])
        cells_list.append(next_fire[1])
    elif 'Medium' in next_fire and 51 <= int(next_fire[1]) <= 80:
        amount_water -= int(next_fire[1])
        effort += int(next_fire[1]) * 0.25
        total_fire += int(next_fire[1])
        cells_list.append(next_fire[1])
    elif 'Low' in next_fire and 1 <= int(next_fire[1]) <= 50:
        amount_water -= int(next_fire[1])
        effort += int(next_fire[1]) * 0.25
        total_fire += int(next_fire[1])
        cells_list.append(next_fire[1])

print('Cells:')
for cell in cells_list:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {int(total_fire)}')

