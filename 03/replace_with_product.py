MAX_NON_ONE_NUMBERS_TO_SUM = 30


def solve():
    all_sum = 0
    all_product = 1
    not_ones = []

    for idx, a_val in enumerate(input().split()):
        a = int(a_val)
        if a != 1:
            not_ones.append((idx, a))
            all_product *= a
        all_sum += a

    if all_product >= 2**MAX_NON_ONE_NUMBERS_TO_SUM:
        print(not_ones[0][0] + 1, not_ones[-1][0] + 1)
        return

    best = (all_sum, 0, 0)  # (product + (all_sum - sum), l, r)
    aa_idx: tuple
    for i, aa_idx in enumerate(not_ones):
        last_aa_idx = aa_idx[0]
        last_product = last_sum = not_ones[i][1]
        for j in range(i + 1, len(not_ones)):
            last_product = last_product * not_ones[j][1]
            last_sum = last_sum + (not_ones[j][0] - last_aa_idx - 1) + not_ones[j][1]
            last_aa_idx = not_ones[j][0]

            candidate = last_product + (all_sum - last_sum)
            if candidate > best[0]:
                best = (candidate, not_ones[i][0], not_ones[j][0])

    print(best[1] + 1, best[2] + 1)


if __name__ == '__main__':
    for _ in range(int(input())):
        _ = int(input())
        solve()
