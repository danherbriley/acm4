import math

if __name__ == "__main__":
    n, m, t = [int(x) for x in input().split()]

    sm = 0

    for k in range(4, min(t, n + 1)):
        sm += math.comb(n, k) * math.comb(m, t - k)

    print(sm)
