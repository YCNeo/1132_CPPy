def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count != 2:
        return False

    return True


if __name__ == "__main__":
    number = int(input())
    max_prime = 1
    for i in range(1, number + 1):
        if is_prime(i):
            max_prime = i

    if max_prime == 1:
        print("1 is not a prime number.")
    else:
        print(f"Largest Prime Number: {max_prime}")
