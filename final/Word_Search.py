dirX = [0, 1, 0, -1]
dirY = [1, 0, -1, 0]


def is_valid(x, y, edgeX, edgeY):
    return x >= 0 and y >= 0 and x < edgeX and y < edgeY


def dfs(table, curX, curY, edgeX, edgeY, word, word_index):
    for i in range(4):
        newX = curX + dirX[i]
        newY = curY + dirY[i]
        if is_valid(newX, newY, edgeX, edgeY) and table[newX][newY] == word[word_index]:
            if word_index + 1 == len(word):
                return True
            else:
                return dfs(table, newX, newY, edgeX, edgeY, word, word_index + 1)

    return False


if __name__ == "__main__":
    [x, y] = input().strip().split(" ")
    x = int(x)
    y = int(y)

    table = []
    for _ in range(x):
        line = input().strip().split(" ")
        table.append(line)

    search_str = input().strip().split(",")

    found_words = []
    for word in search_str:
        is_found = False
        for i in range(x):
            if is_found:
                break
            for j in range(y):
                if word[0] == table[i][j] and dfs(table, i, j, x, y, word, 1) == True:
                    found_words.append(word)
                    is_found = True
                    break

    print(found_words)
