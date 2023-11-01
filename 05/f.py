import math

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l, r = [int(x) for x in input().split()]

        mx = math.floor(math.log(r, 2) - math.log(l, 2)) + 1

        sq_pure_2 = r // 2 ** (mx - 1)

        if mx > 1:
            sq_2_3 = r // ((2 ** (mx - 2)) * 3)
        else:
            sq_2_3 = l - 1

        print(mx, (sq_pure_2 - l + 1 + (sq_2_3 - l + 1) * (mx - 1)) % 998244353)
