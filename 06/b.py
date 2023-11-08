

def solve(a: list):
    valid = []
    prefix = []
    for idx, el in enumerate(a):
        valid.append(bool(el < idx + 1))
    for idx, el in enumerate(a):
        if idx == 0:
            prefix.append(int(valid[idx]))
        else:
            prefix.append(prefix[idx - 1] + int(valid[idx]))

    res = 0
    for idx, el in enumerate(a):
        if valid[idx]:
            y = el - 2
            if y >= 0:
                res += prefix[y]

    print(res)


if __name__ == '__main__':
    for _ in range(int(input())):
        nn = int(input())
        aa = [int(x) for x in input().split()]
        solve(aa)
