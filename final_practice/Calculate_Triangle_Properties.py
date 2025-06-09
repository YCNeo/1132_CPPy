import math

if __name__ == "__main__":
    sides: list[float] = []
    perimeter = 0
    for i in range(3):
        sides.append(float(input()))
        perimeter += sides[i]

    s = perimeter / 2
    area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))

    if sides[0] == sides[1] == sides[2]:
        type = "Equilateral"
    elif sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        type = "Isosceles"
    else:
        type = "Scalene"

    print(
        f"Perimeter: {round(perimeter, 1)}\nArea: {round(area, 1)}\nType: {type} Triangle"
    )
