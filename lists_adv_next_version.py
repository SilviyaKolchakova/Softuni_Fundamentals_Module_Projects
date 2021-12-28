initial_version = input().split('.')
initial_version_string = [''.join(initial_version)]
next_version = int(*initial_version_string) + 1
next_version_str = str(next_version)
next_version_list = list(next_version_str)

print(f'{".".join(next_version_list)}')