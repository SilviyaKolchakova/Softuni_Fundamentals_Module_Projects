data = input()

companies = {}

while not data == 'End':
    next_company = data.split(' -> ')
    company = next_company[0]
    id = next_company[1]

    if company not in companies:
        companies[company] = []

    if id not in companies[company]:
        companies[company].append(id)
    data = input()
for k, v in sorted(companies.items(), key=lambda x: x[0]):
    print(k)
    for v1 in v:
        print(f'-- {v1}')


