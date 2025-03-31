def max_profit(stock):
    stock_sorted = sorted(stock)
    l = len(stock_sorted)
    max_profit = 0
    # print(stock_sorted)

    for i in range(l):
        # get all price later than stock[i]
        compare_arr = []
        for j in range(l - 1):
            if stock[i] == stock_sorted[j]:
                compare_arr = stock_sorted[j + 1 :]
                # print(f"stock[i]: {stock[i]}, arr: {compare_arr}")
                break

        for j in range(i, l):
            if stock[j] in compare_arr:
                profit = stock[j] - stock[i]
                if profit > max_profit:
                    max_profit = profit
                    # print(f"profit: {profit}, max_profit: {max_profit}")
    return max_profit


stock_str = input().split()
stock = [int(x) for x in stock_str]

profit = max_profit(stock)

print(profit)
