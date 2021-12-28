import re

pattern = r'(?P<surr>\$|\%)(?P<tag>[A-Z][a-z]+)(?P=surr): \[(?P<number1>\d+)\]\|\[(?P<number2>\d+)\]\|\[(?P<number3>\d+)\]\|($|(?=\s))'
count = int(input())
tags = {}

for tag in range(count):
    new_tag = input()
    matched_tags = re.match(pattern, new_tag)
    if matched_tags:
        data = matched_tags.groupdict()
        print(data)
        print(f"{data['tag']}: {chr(int(data['number1']))+chr(int(data['number2']))+ chr(int(data['number3']))}")
    else:
        print('Valid message not found!')