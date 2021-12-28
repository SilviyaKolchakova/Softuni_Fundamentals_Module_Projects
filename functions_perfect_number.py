def perfect_number_found(number_to_check):
    divisors_list = []

    for position in range(1, number_to_check + 1):
        if number_to_check % position == 0:
            divisors_list.append(position)
    if sum(divisors_list) // 2 == number_to_check:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


number = int(input())

perfect_number_found(number)





