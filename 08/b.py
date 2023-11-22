from math import factorial, comb


def compute_permutation(arr):
    # print(arr)
    if arr[0] == 0:
        fct = factorial(sum(arr))
        for num in arr:
            if num > 1:
                fct //= factorial(num)
        return fct
    else:
        sm = sum(arr)
        if sm == 1:
            return 1
        zeros = comb(sm - 1, arr[0])
        sm -= arr[0]
        fct = factorial(sm)
        for num in arr[1:]:
            if num > 1:
                fct //= factorial(num)
        return fct * zeros


def rec(present_digits, digit_idx, counts, perm, count_self=True):
    res = 0
    if count_self:
        res = compute_permutation(perm)

    if digit_idx >= len(present_digits):
        return res
    digit = present_digits[digit_idx]

    new_perm1 = perm[:]
    res += rec(present_digits, digit_idx + 1, counts, new_perm1, False)
    while perm[digit] < counts[digit]:
        perm[digit] += 1
        new_perm = perm[:]
        res += rec(present_digits, digit_idx + 1, counts, new_perm)

    return res


def solve(n):
    tmp = n
    counts = 10 * [0]
    while tmp != 0:
        counts[tmp % 10] += 1
        tmp = tmp // 10

    present_digits = [idx for idx, cnt in enumerate(counts) if cnt]
    start = [1 if idx in present_digits else 0 for idx in range(10)]
    res = rec(present_digits, 0, counts, start)
    print(res)


if __name__ == '__main__':
    solve(int(input()))
