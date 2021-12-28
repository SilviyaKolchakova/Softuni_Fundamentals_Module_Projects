words = input().split()
filtered_words = [el for el in words if len(el) % 2 == 0]
print("\n".join(filtered_words))