

def solve(x, y):
    res = []

    for idx in range(len(x)):
        p1 = x[idx]
        p2 = y[idx]
        if not res:
            res.append((p1, p2, 0))
        else:
            choose1 = max(res[idx - 1][1], res[idx - 1][2]) + p1
            choose2 = max(res[idx - 1][0], res[idx - 1][2]) + p2
            res.append((choose1, choose2, max(res[idx - 1])))

    print(max(res[len(x) - 1]))


if __name__ == '__main__':
    _ = input()
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    solve(a, b)
