old_genres = input().split(' | ')

command = input()

while not command == 'Stop!':
    next_command = command.split()
    if next_command[0] == 'Join':
        genre = next_command[1]
        if genre not in old_genres:
            old_genres.append(genre)
    elif next_command[0] == 'Drop':
        genre = next_command[1]
        if genre in old_genres:
            old_genres.remove(genre)
    elif next_command[0] == 'Replace':
        genre = next_command[1]
        new_genre = next_command[2]
        if genre in old_genres and new_genre not in old_genres:
            index = old_genres.index(genre)
            old_genres[index] = new_genre
    command = input()

print(' '.join(old_genres))

