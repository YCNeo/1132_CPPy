class Game:
    def __init__(self):
        self.players = []
        self.deck = []
        self.current_player_index = 0
        self.direction = 1  # 1 for clockwise, -1 for counter-clockwise
        self.discard_pile = []
        self.current_card = None
        self.winner = None

    def __str__(self):
        player_str_list = [str(player) for player in self.players]
        player_str_list[self.turn] += "  <- next"

        players_str = "\n".join(player_str_list)
        game_str = f"""{"=" * 10}\nTop Card: {self.top_card}\n\nPlayers:\n{players_str}\n{"=" * 10}"""
        return game_str

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        self.shuffle_deck()
        self.deal_cards()
        self.current_card = self.draw_card()
        print(f"Starting card: {self.current_card}")

    def shuffle_deck(self):
        import random

        random.shuffle(self.deck)
