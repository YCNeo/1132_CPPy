# 1A2B game
import random
import string

# random 4 different digits
ans = "".join(random.sample(string.digits, 4))
print("Welcome to the 1A2B game!")

while True:
    guess = input("Enter guess: ")
    if guess == "q":
        break

    a = 0
    b = 0
    for i in range(4):
        if guess[i] == ans[i]:
            a += 1
        elif guess[i] in ans:
            b += 1

    if a == 4:
        print("Congratulations! You guessed the number!")
        break
    print(f"{a}A{b}B")