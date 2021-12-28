def odd_even_sum(number: str):
    number_as_number = [int(el) for el in number]
    even_sum = 0
    odd_sum = 0
    for number1 in number_as_number:
        if number1 % 2 == 0:
            even_sum += number1
        else:
            odd_sum += number1

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number_as_string = input()
print(odd_even_sum(number_as_string))