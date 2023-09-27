def inc_dec(x, y, n):
    if y - x < ((n - 1) * n) / 2:
        print("-1")
    else:
        output = [y]
        diff = 1
        while n > 2:
            output.append(output[-1] - diff)
            n -= 1
            diff += 1

        output.append(x)

        for x in reversed(output):
            print(x, end=" ")

        print()


if __name__ == "__main__":
    lines = int(input())

    for i in range(lines):
        line = input()
        x, y, n = [int(x) for x in line.split(" ")]
        inc_dec(x, y, n)
