

def solve(n: int):
    valid = [(int(x), idx + 1) for idx, x in enumerate(input().split()) if int(x) < idx + 1]

    res = 0
    for i in range(len(valid)):
        for j in range(i + 1, len(valid)):
            if valid[i][0] < valid[i][1] < valid[j][0] < valid[j][1]:
                res += 1

    print(res)


if __name__ == '__main__':
    for _ in range(int(input())):
        nn = int(input())
        solve(nn)
