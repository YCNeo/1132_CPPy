def find_max(dic):
    max_words = []
    max = -1
    for i in list(dic):
        if dic[i] > max:
            max = dic[i]
            max_words.clear()
            max_words.append(i)
        elif dic[i] == max:
            max_words.append(i)

    max_words = sorted(max_words)
    return max_words, max


if __name__ == "__main__":
    string = input().strip().split(" ")

    dic = {}

    for word in string:
        if word.lower() in dic:
            dic[word.lower()] += 1
        else:
            dic[word.lower()] = 1

    max_words, max = find_max(dic)
    word_str = " ".join(max_words)
    print(f"{word_str}\nTimes: {max}", end="")
