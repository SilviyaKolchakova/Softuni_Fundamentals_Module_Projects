import re

pattern = r'(::|\*\*)(?P<emoji>[A-Z]{1}[a-z]{2,})\1'

text = input()
digits = []
threshold = 1
for i in text:
    if i.isdigit():
        digits.append(i)

for digit in digits:
    threshold *= int(digit)
print(f'Cool threshold: {threshold}')
emoji_count = 0
emoji_list = []
cool_emojis = []
for match in re.finditer(pattern, text):
    data = match.groupdict()
    emoji = data['emoji']
    emoji_list.append(emoji)
    emoji_coolness = [ord(i) for i in emoji]
    if sum(emoji_coolness) >= threshold:
        cool_emojis.append(match.group())

print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
print(*cool_emojis, sep='\n')








