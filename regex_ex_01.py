import re
nums = []
pattern = r"\d+"
data = input()


while data:
    matches = re.findall(pattern, data)
    nums.extend(matches)
    data = input()


print(*nums)