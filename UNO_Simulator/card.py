class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __repr__(self):
        color_code = {"red": 31, "yellow": 33, "green": 32, "blue": 36}
        if self.color is None:
            ansi_code = 0
        else:
            ansi_code = color_code[self.color]
        return f"\033[{ansi_code}m{self.value}\033[0m"

    def __str__(self):
        return f"{self.color} {self.value}"
