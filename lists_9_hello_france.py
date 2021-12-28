clothes_list = input().split('|')
budget = float(input())
price_of_products = 0
target_sum = 150
new_item_price_list = []
total_price_new_products = 0
profit = 0
for item in clothes_list:
    next_item = item.split('->')
    if float(next_item[1]) > budget:
        continue
    if next_item[0] == 'Clothes' and float(next_item[1]) > 50.00:
        continue
    if next_item[0] == 'Shoes' and float(next_item[1]) > 35.00:
        continue
    if next_item[0] == 'Accessories' and float(next_item[1]) > 20.50:
        continue
    budget -= float(next_item[1])
    price_of_products += float(next_item[1])
    new_product_price = float(next_item[1]) + (float(next_item[1]) * 0.40)
    new_item_price_list.append(new_product_price)
    total_price_new_products += new_product_price
    profit = total_price_new_products - price_of_products

for price in range(0, len(new_item_price_list)):
    print(f'{float(new_item_price_list[price]):.2f}', end=' ')

print(f'\nProfit: {profit:.2f}')

if budget + total_price_new_products >= target_sum:
    print('Hello, France!')
else:
    print('Time to go.')


