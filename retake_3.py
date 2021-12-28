command = input()
foods = {}
sold = []
while not command == 'Complete':
    next_command = command.split(' ')
    action = next_command[0]
    qty = int(next_command[1])
    next_food = next_command[2]
    if action == 'Receive':
        if qty <= 0:
            command = input()
            continue
        if next_food in foods:
            foods[next_food] += qty
        else:
            foods[next_food] = {'quantity': qty}
    elif action == 'Sell':
        if next_food not in foods:
            print(f"You do not have any {next_food}.")
            command = input()
            continue
        if foods[next_food]['quantity'] < qty:
            print(f"There aren't enough {next_food}. You sold the last {foods[next_food]['quantity']} of them.")
            foods.pop(next_food)
        else:
            foods[next_food]['quantity'] -= qty
            print(f"You sold {qty} {next_food}.")
            sold.append(qty)
            if foods[next_food]['quantity'] <= 0:
                foods.pop(next_food)
    command = input()

sorted_result = sorted(foods.items(), key=lambda kvp: kvp[0])

for food, qty in sorted_result:
    print(f"{food}: {qty['quantity']}")
print(f"All sold: {sum(sold)} goods")


