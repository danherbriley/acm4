def prefix(arr):
    i = 0
    while arr[i] == 1 and i != len(arr) - 1:
        i += 1
    return i


def suffix(arr):
    i = len(arr) - 1
    while arr[i] == 1:
        i -= 1
    return i


def count_not_ones(arr):
    not_ones = []
    for i in range(len(arr)):
        if arr[i] != 1:
            not_ones.append(i)
    return not_ones


def sum_interval(arr, not_ones, i, j):
    sum_pre = sum(arr[: not_ones[i]])

    prod = 1
    for x in range(i, j + 1):
        prod *= arr[not_ones[x]]

    sum_post = 0
    if j + 1 < len(not_ones):
        sum_post = sum(arr[(not_ones[j] + 1) :])

    return sum_pre + prod + sum_post


def bounds(arr):
    not_ones = count_not_ones(arr)
    if len(not_ones) > 18:
        return 0, len(arr) - 1
    else:
        tmp = 0
        max = sum(arr)
        bounds = 0, 0
        for i in range(len(not_ones)):
            for j in range(i, len(not_ones)):
                tmp = sum_interval(arr, not_ones, i, j)
                if tmp > max:
                    max = tmp
                    bounds = not_ones[i], not_ones[j]
        return bounds


def solve(arr):
    px_len = prefix(arr)
    if px_len == len(arr) - 1:
        print("1 1")
        return
    sx_len = suffix(arr)
    start, end = bounds(arr[px_len : sx_len + 1])
    print(px_len + start + 1, px_len + end + 1)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        solve(arr)
