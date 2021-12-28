data = input().split()
username_lenght = False
for username in data:
    if len(username) >= 3:
        username_lenght = True

for username in data:
    for i in username:
        if i.isalnum():
            isalphanumeric = True











