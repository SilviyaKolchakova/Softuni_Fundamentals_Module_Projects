substrings = input().split(', ')
strings = input().split(', ')
new_list = []
for el in substrings:
    for el2 in strings:
        if el2.find(el) > -1:
            new_list.append(el)
            break

print(new_list)
