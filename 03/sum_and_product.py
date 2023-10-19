

def solve(n, a, q, queries):
    res = []
    query_d = {query: idx for idx, query in enumerate(queries)}
    for idx, query in enumerate(queries):
        res.append(0)
        if query not in query_d:
            query_d[query] = [idx]
        else:
            query_d[query].append(idx)

    for i in range(n):
        for j in range(i + 1, n):
            for idx in query_d.get((a[i] + a[j], a[i] * a[j]), []):
                res[idx] += 1

    for w in range(q - 1):
        print(res[w], end=" ")
    print(res[-1])


if __name__ == '__main__':
    for _ in range(int(input())):
        nn = int(input())
        aa = [int(a_) for a_ in input().split()]
        qq = int(input())
        queries_ = []
        for _ in range(qq):
            x = input().split()
            queries_.append((int(x[0]), int(x[1])))
        solve(nn, aa, qq, queries_)
