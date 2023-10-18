def solve(a, b, k, c):
    if k == 0:
        return 0

    if c != a and c != b:
        return 0

    return (((2**k) * k) // 2) % 1_000_000_007


if __name__ == "__main__":
    a, b, k, c = [int(x) for x in input().split()]
    print(solve(a, b, k, c))
