def sum_numbers(num_1, num_2):
    result = num_1 + num_2
    return result

def subtract(sum_of_the_first_two, num_3):
    result_2 = sum_of_the_first_two - num_3
    return result_2

def add_and_subtract(num_1, num_2, num_3):
    sum_first_two = sum_numbers(num_1, num_2)
    return sum_first_two(first, second) + third

first = int(input())
second = int(input())
third = int(input())

print(subtract(sum_numbers(first, second), third))

