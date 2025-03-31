def add_to_list(lst, exit_item, to_add_item):
    for l in lst:
        if exit_item in l:
            l.append(to_add_item)
    return lst


def find_index(lst, item):
    for i in range(len(lst)):
        if item in lst[i]:
            return i
    return -1


def merge_list(lst, item1, item2):
    for l in lst:
        if (item1 in l and item2 not in l) or (item2 in l and item1 not in l):
            index = find_index(lst, item2) if item1 in l else find_index(lst, item1)
            for i in lst[index]:
                l.append(i)
            del lst[index]


def main():
    n = int(input())

    city_list = [[str(i + 1)] for i in range(n)]
    # print(city_list)

    while True:
        input_pair = input().strip()
        if input_pair == "q":
            break

        splitted = input_pair.split()
        splitted = [x.replace("City", "") for x in splitted]

        not_exist_amount = 0
        to_add_index = []

        for i in range(len(splitted)):
            if find_index(city_list, splitted[i]) == -1:
                to_add_index.append(i)
                not_exist_amount += 1

        if not_exist_amount == 2:
            city_list.append(splitted)
        elif not_exist_amount == 1:
            city_list = add_to_list(
                city_list, splitted[1 - to_add_index[0]], splitted[to_add_index[0]]
            )
        else:
            merge_list(city_list, splitted[0], splitted[1])

    # print(city_list)
    print(len(city_list))


if __name__ == "__main__":
    main()
