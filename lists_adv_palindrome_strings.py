words = input().split()
searched_palindrome = input()
palindromes = []
found_palindrome = 0

for el in words:
    if el == el[::-1]:
        palindromes.append(el)
    if el == searched_palindrome:
        found_palindrome += 1
print(palindromes)
print(f'Found palindrome {found_palindrome} times')

