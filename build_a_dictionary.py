dictionary = (input()).split(",")
dictionary.sort()

# print(dictionary)

while True:
    word = input()
    if word == "#":
        break

    first_char = word[0]
    char_position = -1
    is_found = False

    for i in range(len(dictionary)):
        if dictionary[i][0] == first_char and char_position == -1:
            char_position = i

        if dictionary[i] == word:
            print(f"{first_char.upper()} {i - char_position + 1}")
            is_found = True
            break

    is_found == False and print("NOT FOUND")
