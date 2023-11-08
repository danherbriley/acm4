from queue import Queue


def solve_dep(n, a):

    neigh_idx = {}
    for idx, x in enumerate(a):
        if x not in neigh_idx:
            neigh_idx[x] = [idx]
        elif idx == n - 1 or a[idx + 1] != x:
            neigh_idx[x].append(idx)

    q = Queue()
    q.put((0, 0))
    res_dep = 0
    while not q.empty():
        i, removed = q.get()
        if i >= n:
            res_dep = max(res_dep, removed)
            continue
        val = a[i]

        for j in neigh_idx[val]:
            if j > i and removed + n - j > res_dep:
                q.put((j + 1, removed + j - i + 1))

        if removed + n - i > res_dep:
            q.put((i + 1, removed))

    print(res_dep)


def solve_dep_2(n, a):
    res = []
    neigh_idx = {}
    for idx, x in enumerate(a):
        res.append(0)
        if x not in neigh_idx:
            neigh_idx[x] = [idx]
        elif idx == n - 1 or a[idx + 1] != x or (idx != 0 and a[idx - 1] != x):
            neigh_idx[x].append(idx)
    res.append(0)

    found_cnt = {}
    for i, x in enumerate(a):
        start_neigh_idx = 1
        neighbour_indexes = neigh_idx[x]
        if x not in found_cnt:
            found_cnt[x] = 1
        elif neighbour_indexes[found_cnt[x]] == i:
            start_neigh_idx += found_cnt[x]
            found_cnt[x] += 1
        else:
            res[i + 1] = max(res[i], res[i + 1])
            continue

        for k in range(start_neigh_idx, len(neighbour_indexes)):
            j = neighbour_indexes[k]
            if j > i:  # should always be true
                res[j + 1] = max(res[j + 1], res[i] + j - i + 1)

        res[i + 1] = max(res[i], res[i + 1])

    print(max(res))


def solve(n, a):
    best = (n + 1) * [-1]
    cut_len = n * [n]
    for j, x in enumerate(a):
        if best[x] == -1:
            best[x] = j
            if j == 0:
                cut_len[j] = 1
            else:
                cut_len[j] = cut_len[j - 1] + 1
        else:
            if cut_len[j - 1] + 1 < cut_len[best[x]]:
                cut_len[j] = cut_len[j - 1] + 1
                best[x] = j
            else:
                cut_len[j] = cut_len[best[x]] - 1

    print(n - cut_len[n - 1])


if __name__ == '__main__':
    for _ in range(int(input())):
        nn = int(input())
        aa = [int(x) for x in input().split()]
        solve(nn, aa)
