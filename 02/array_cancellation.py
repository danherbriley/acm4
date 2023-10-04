
def helper(a, add_idx, dec_idx, positions, decreasing: bool):
    x = min(a[dec_idx], -a[add_idx])
    a[add_idx] += x
    a[dec_idx] -= x

    # print(f"{add_idx = }, {dec_idx = }")
    if a[dec_idx] == 0 and not decreasing:
        positions.dec_idx_end_pos -= 1
    if a[add_idx] == 0:
        positions.add_idx_start_pos += 1

    if dec_idx > add_idx:
        return x
    return 0


class Positions:

    def __init__(self, len_dec):
        self.add_idx_start_pos = 0
        self.dec_idx_end_pos = len_dec - 1


def solve(n, a):
    to_add_idxs = []
    to_dec_idxs = []
    for idx, a_val in enumerate(a):
        if a_val > 0:
            to_dec_idxs.append(idx)
        elif a_val < 0:
            to_add_idxs.append(idx)

    coins = 0
    idx = 0

    positions = Positions(len(to_dec_idxs))
    while idx != len(a):

        add_idx: int
        dec_idx: int

        if a[idx] > 0:
            dec_idx = idx
            add_idx = to_add_idxs[positions.add_idx_start_pos]
            coins += helper(a, add_idx, dec_idx, positions, decreasing=True)
        elif a[idx] < 0:
            add_idx = idx
            dec_idx = to_dec_idxs[positions.dec_idx_end_pos]
            coins += helper(a, add_idx, dec_idx, positions, decreasing=False)

        if a[idx] == 0:
            idx += 1

    print(coins)


if __name__ == '__main__':
    for _ in range(int(input())):
        nn = int(input())
        aa = [int(a_el) for a_el in input().split()]
        solve(nn, aa)
