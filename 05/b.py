import math


def count(string):
    res = 0
    blanks = 0
    for char in string:
        if char == "+":
            res += 1
        elif char == "-":
            res -= 1
        elif char == "?":
            blanks += 1
    return res, blanks


if __name__ == "__main__":
    og, _ = count(input())
    rec, blanks = count(input())

    dist = abs(og - rec)

    if not blanks and not dist:
        print(1)
    elif not blanks and dist:
        print(0)
    elif dist > blanks:
        print(0)
    else:
        print(math.comb(blanks, ((blanks - dist) // 2) + dist) / (2**blanks))
