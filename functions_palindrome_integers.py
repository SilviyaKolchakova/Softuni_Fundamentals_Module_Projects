def found_palindromes(words: list):
    forward = words
    backward = [ch[::-1]for ch in words]

    matches = ['True' if i == j else 'False' for i, j in zip(forward, backward)]
    return matches


integers_list = input().split(', ')

print("\n".join(found_palindromes(integers_list)))
