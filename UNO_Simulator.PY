import sys


class Card:
    def __init__(self, card: list[str]):
        self.value = card[0]
        self.color = (
            card[1]
            if len(card) > 1 and (self.value != "wild" or self.value != "+4")
            else ""
        )

    def __repr__(self):
        color_code = {"red": 31, "yellow": 33, "green": 32, "blue": 36}
        if self.color is None:
            ansi_code = 0
        else:
            ansi_code = color_code[self.color]
        return f"\033[{ansi_code}m{self.value}\033[0m"

    def __str__(self):
        return f"{self.value} {self.color}" if self.color else self.value

    def update_color(self, color: str):
        if self.value == "wild" or self.value == "+4":
            self.color = color


class Player:
    def __init__(self, game, id):
        self.hand: list[Card] = []
        self.game: Game = game
        self.id = id

    def add_card(self, card: Card):
        self.hand.append(card)

    def is_usable(self, target_card: Card, top_card: Card):
        return (
            target_card.color == top_card.color
            or target_card.value == top_card.value
            or target_card.value == "wild"
            or target_card.value == "+4"
        )

    def choose_color(self):
        color_count = {"red": 0, "yellow": 0, "green": 0, "blue": 0, "": 0}
        for card in self.hand:
            color_count[card.color] += 1

        max_color = max(color_count, key=color_count.get)

        return max_color if max_color != "" and color_count[max_color] > 0 else "red"

    def play(self, top_card: Card):
        usable_cards: list[list[int | Card]] = [
            [i, card]
            for i, card in enumerate(self.hand)
            if self.is_usable(card, top_card)
        ]

        # Sort usable cards by 1. Number cards 2. Skip 3. Reverse 4. Draw Two 5. Wild 6. Wild Draw Four
        usable_cards.sort(
            key=lambda x: (
                x[1].value.isdigit(),
                x[1].value == "skip",
                x[1].value == "reverse",
                x[1].value == "+2",
                x[1].value == "wild",
                x[1].value == "+4",
            ),
            reverse=True,
        )

        if usable_cards:
            i, card = usable_cards[0]
            card = self.game.special_card_action(card, self)
            self.hand.pop(i)
            self.game.top_card = card

            if not self.hand:
                self.game.winner = self
            return

        if self.game.pile:
            card = self.game.draw_card()

            if not self.is_usable(card, top_card):
                self.add_card(card)
            else:
                card = self.game.special_card_action(card, self)
                self.game.top_card = card


class Game:
    def __init__(self, deck):
        self.players: list[Player] = []
        self.pile: list[Card] = deck
        self.turn = 0
        self.direction = 1  # 1 for clockwise, -1 for counter-clockwise
        self.top_card: Card = None
        self.winner: Player = None

    def __str__(self):
        player_str_list = [str(player.id) for player in self.players]
        player_str_list[self.turn] += "  <- next"

        players_str = "\n".join(player_str_list)
        game_str = f"""{"=" * 10}\nTop Card: {self.top_card}\n\nPlayers:\n{players_str}\n{"=" * 10}"""
        return game_str

    def add_player(self, players):
        for p in players:
            self.players.append(p)

    def start_game(self):
        self.deal_cards()
        self.top_card = self.draw_card()

    def deal_cards(self):
        for _ in range(5):
            for player in self.players:
                card = self.draw_card()
                player.add_card(card)

    def draw_card(self):
        return self.pile.pop(0)

    def special_card_action(self, card: Card, player: Player):
        if card.value == "skip":
            self.turn = (self.turn + self.direction) % 5
        elif card.value == "reverse":
            self.direction *= -1
        elif card.value == "wild":
            card.update_color(player.choose_color())
        elif card.value == "+2":
            for _ in range(2):
                self.players[(self.turn + self.direction) % 5].add_card(
                    self.draw_card()
                )
        elif card.value == "+4":
            card.update_color(player.choose_color())
            for _ in range(4):
                self.players[(self.turn + self.direction) % 5].add_card(
                    self.draw_card()
                )

        return card


if __name__ == "__main__":
    input_str = sys.stdin.read().splitlines()
    pile = [
        Card(card.strip().split("-"))
        for card in input_str
        if card.strip().split("-")[0] != "q"
    ]

    game = Game(pile)
    game.add_player([Player(game, id) for id in range(5)])
    game.start_game()

    while not game.winner:
        cur_player = game.players[game.turn]
        cur_player.play(game.top_card)
        game.turn = (game.turn + game.direction) % 5

    print(f"Player {game.winner.id} win!")
