def sum_numbers(num_1, num_2):
    result = num_1 + num_2
    return result


def subtract(sum_numbers, num_3):
    result_2 = sum_numbers - num_3
    return result_2(sum_numbers, third)


def add_and_subtract(num_1, num_2, num_3):
    return sum_numbers(first, second) - num_3(third)



first = int(input())
second = int(input())
third = int(input())


print(subtract(first, second, third))
