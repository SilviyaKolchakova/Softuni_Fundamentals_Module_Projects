data = input()
emoticon = ''
for i in range(len(data)):
    if data[i] == ':':
        print(data[i] + data[i + 1])

