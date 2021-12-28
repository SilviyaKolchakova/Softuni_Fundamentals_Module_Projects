import re

pattern = r'(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+\.?[a-z]+?\.[a-z]+'
text = input()


matches = [el.group() for el in re.finditer(pattern, text)]
print(*matches, sep='\n')

