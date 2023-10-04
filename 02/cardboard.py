def cardboard(n, c, arr_s):
    sum_1 = sum(arr_s)
    sum_2 = sum([x**2 for x in arr_s])

    D = 16 * sum_1**2 - 16 * n * (sum_2 - c)

    w1 = (-4 * sum_1 + D ** (1 / 2)) / (8 * n)
    w2 = (-4 * sum_1 - D ** (1 / 2)) / (8 * n)
    print(int(max(w1, w2)))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, c = [int(x) for x in input().split()]
        arr_s = [int(x) for x in input().split()]
        cardboard(n, c, arr_s)
