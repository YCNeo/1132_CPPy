class Player:
    def __init__(self, game):
        self.game = game

    def play(self):
        while True:
            self.game.display()
            if self.game.is_game_over():
                print("Game Over!")
                break
            self.game.play_turn()
            if self.game.is_winner():
                print(f"{self.game.current_player.name} wins!")
                break
            self.game.next_player()
