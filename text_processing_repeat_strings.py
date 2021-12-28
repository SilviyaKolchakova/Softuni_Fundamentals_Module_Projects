strings = input().split()
repeated_strings = []
for item in strings:
    repeated_item = item*len(item)
    repeated_strings.append(repeated_item)
new_item = ''
for item in repeated_strings:
    new_item += item
print(new_item)



