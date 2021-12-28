text = input()
new_list = [text[0]]
chars = 0
for char in range(1,len(text)):
    current_item = text[char]
    if chars < len(text) -2:
        next_item = text[char +1]
        if next_item == current_item:
            chars += 1
            continue

        else:
            new_list.append(next_item)
            chars += 1
print("".join(new_list))


