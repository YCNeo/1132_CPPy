def print_order(name, item):
    print(f"Customer: {name}")
    print(f"Number of Items: {len(item)}")
    print("Order Details:")
    total = 0

    for i in range(len(item)):
        subtotal = 0
        discount = float(1)

        # handle DISCOUNT and NONE
        if item[i][3] != "None":
            numberic_part = ""
            for char in item[i][3]:
                if char.isdigit():
                    numberic_part += char
            if numberic_part:
                discount = 1 - int(numberic_part) / 100

        subtotal = round(int(item[i][1]) * float(item[i][2]) * discount, 2)

        print(
            f"{i+1}. {item[i][0]} - Quantity: {item[i][1]}, Unit Price: {float(item[i][2]):.2f} TWD, Subtotal: {subtotal:.2f} TWD"
        )
        total += subtotal
    print(f"Total Cost: {total:.2f} TWD\n")


n = int(input())

for i in range(n):
    name = str(input())
    amount = int(input())
    item = []

    for j in range(amount):
        order = str(input())
        item.append(order.split(";"))

    print_order(name, item)
