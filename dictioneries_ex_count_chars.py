text = input().split(' ')

chars = {}

for char in text:
    for char1 in char:
        key = char1
        if key not in chars:
            chars[key] = 0
        chars[key] += 1

for key, value in chars.items():
    print(f'{key} -> {value}')
