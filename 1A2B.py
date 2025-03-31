from itertools import permutations


def count_ab(secret, guess):
    A = sum(s == g for s, g in zip(secret, guess))
    B = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - A
    return A, B


def main():
    # Read input
    guess_feedback = []
    while True:
        line = input().strip()
        if line == "q":
            break
        if "->" not in line:
            continue
        guess_part, fb_part = line.split("->")
        digits = list(map(int, guess_part.strip().split()))
        a = int(fb_part.strip()[0])
        b = int(fb_part.strip()[2])
        guess_feedback.append((digits, a, b))

    # Generate all 4-digit distinct permutations from 0-9
    all_candidates = list(permutations(range(10), 4))

    valid_codes = []
    for code in all_candidates:
        if all(count_ab(code, guess) == (a, b) for guess, a, b in guess_feedback):
            valid_codes.append(code)

    # Output
    if valid_codes:
        print("Possible codes:")
        for code in sorted(valid_codes):
            print(" ".join(map(str, code)))
    else:
        print("No valid codes")


if __name__ == "__main__":
    main()
