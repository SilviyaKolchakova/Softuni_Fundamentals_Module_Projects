import re
text = input()
pattern = r'www\.[a-zA-Z0-9-]+(\.[a-z]+)+'
valids = []
while text:
    matches = [i.group() for i in re.finditer(pattern, text)]
    if matches:
        print(*matches, sep='\n')
        #valids.extend(matches)

    text = input()
#print(*valids, sep='\n')