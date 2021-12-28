string_list = input().split(', ')
even_numbers = [position for position in range(len(string_list)) if int(string_list[position]) % 2 == 0]
print(even_numbers)
