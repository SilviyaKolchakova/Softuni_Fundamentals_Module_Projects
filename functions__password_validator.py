password = list(input())
lenght_check = False
if 6 <= len(password) <= 10:
    lenght_check = True
second_check = False
second_check_digit = []
for el in password:
    if 48 <= ord(el) <= 57 or 97 <= ord(el.lower()) <= 122:
        second_check_digit.append(True)
        if len(second_check_digit) == len(password):
            second_check = True


digits_check = False
digits_count = 0
for el in password:
    if 48 <= ord(el) <= 57:
        digits_count += 1
        if digits_count >= 2:
            digits_check = True

if lenght_check == False:
    print('Password must be between 6 and 10 characters')
if second_check == False:
    print("Password must consist only of letters and digits")
if digits_check == False:
    print('Password must have at least 2 digits')
if lenght_check == True and second_check == True and digits_check == True:
    print('Password is valid')


