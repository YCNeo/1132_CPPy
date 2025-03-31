def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True

    for i in range(3, n + 1):
        if n == i:
            return True
        elif n % i == 0:
            return False
    return True


def max_prime(n):
    if n < 2:
        return 0

    max = 2

    for i in range(2, n + 1):
        if is_prime(i) and max < i:
            max = i
    return max


n = int(input())

if max_prime(n) == 0:
    print(f"{n} is not a prime number.")
else:
    print(f"Largest Prime Number: {max_prime(n)}")



#########
# by 小黑

# n = int(input())

# isPrime = [True] * (n + 1)
# isPrime[1] = False

# i = 2
# while i * i <= n:
#     if isPrime[i]:
#         j = i * i
#         while j <= n:
#             isPrime[j] = False
#             j += i
#     i += 1

# maxPrime = -1
# x = n
# while x >= 2:
#     if isPrime[x]:
#         maxPrime = x
#         break
#     x -= 1

# if maxPrime == -1:
#     print("1 is not a prime number.")
# else:
#     print(f"Largest Prime Number: {maxPrime}")