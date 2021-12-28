text = input()
digits = ''
letters = ''
others = ''

for item in text:
    if item.isdigit():
        digits += item
    elif item.isalpha():
        letters += item
    else:
        others += item
print(digits)
print(letters)
print(others)