def characters_in_range(start_element, end_element):
    next_element = [chr(element) for element in range(ord(start_element) + 1, ord(end_element))]
    return " ".join(next_element)



a = input()
b = input()

print(characters_in_range(a, b))






