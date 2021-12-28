data = input()
products = {}

while not data.lower() == 'buy':
    next_product = data.split(' ')
    for item in range(0, len(next_product), 3):
        product = next_product[item]
        price = float(next_product[item + 1])
        qty = int(next_product[item + 2])
        if product not in products:
            products[product] = [price, qty]
        else:
            products[product][0] = price
            products[product][1] += qty
    data = input()
for k, v in products.items():
    print(f"{k} -> {v[0] * v[1]:.2f}")