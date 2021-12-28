import re

pattern = r'(?P<name>[A-Z]([a-z]+){3,} [A-Z]([a-z]+){3,})(\#+)((?P<position>[A-Z][a-zA-Z]+)(\&{1})?)((?P<position2>([A-Z][a-zA-Z]+)\&?)?((?P<position3>[A-Z][a-zA-Z]+))?)(\d{2})(?P<company>([A-Z][a-zA-Z\d]+)\s(JSC|Ltd.))'
lines = int(input())
text = input()

while lines != 0:
    for match in re.finditer(pattern, text):
        data = match.groupdict()
        if data['position2'] == None and data['position3'] == None:
            print(f"{data['name']} is {data['position']} at {data['company']}")
        elif data['position3'] == None:
            print(f"{data['name']} is {data['position']} {data['position2']} at {data['company']}")
        else:
            print(f"{data['name']} is {data['position']} {data['position2']} {data['position3']} at {data['company']}")
    lines -= 1
    text = input()