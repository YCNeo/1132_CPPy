cards = [
    ["1", "red"],
    ["2", "yellow"],
    ["2", "yellow"],
    ["3", "green"],
    ["3", "green"],
    ["3", "green"],
    ["4", "blue"],
    ["skip", "red"],
    ["reverse", "yellow"],
    ["wild", "green"],
    ["+4", "blue"],
]

choosen_cards = [card for card in cards if card[0].isdigit()]

color_count = {
    "red": 0,
    "yellow": 0,
    "green": 0,
    "blue": 0,
}
for card in choosen_cards:
    color_count[card[1]] += 1
max_color = max(color_count, key=color_count.get)

print(color_count)
print(max_color)  # This will print the color with the maximum count

a = "+4"
print(a.isdigit())  # This will print False since "+4" is not a digit
