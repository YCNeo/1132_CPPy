import math


def cal(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    type = ""
    if a == b == c:
        type = "Equilateral"
    elif a == b or b == c or a == c:
        type = "Isosceles"
    else:
        type = "Scalene"

    print(f"Perimeter: {round(2*s, 1)}")
    print(f"Area: {round(area, 1)}")
    print(f"Type: {type} Triangle")


a = float(input())
b = float(input())
c = float(input())
cal(a, b, c)
