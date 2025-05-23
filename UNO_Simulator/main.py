import sys
import game
import player
import card

if __name__ == "__main__":
    input_str = sys.stdin.read()
    actions = input_str.splitlines()
    actions = [tuple(act.strip().split("-")) for act in actions]

    for act in actions:
        if act[0] == "q":
            break
