import sys


def search(graph, vert_set, visited, curr):
    visited[curr] = True
    neighbours = [v for v in graph[curr] if v not in visited]
    if not neighbours:
        if curr in vert_set:
            return 1
        else:
            return 0

    sum_vals = 0
    for neighbour in neighbours:
        sum_vals += search(graph, vert_set, visited, neighbour)

    if sum_vals > 1:
        return 2
    if curr in vert_set:
        return 1
    else:
        return sum_vals


def passable(graph, vert_set: dict):
    if not vert_set:
        print("YES")
        return True
    if len(vert_set) < 3:
        print("YES")
        return True

    start = [k for k in vert_set][0]
    sum_vals = 0
    visited = dict()
    visited[start] = True
    for neighbour in graph[start]:
        res = search(graph, vert_set, visited, neighbour)
        if res > 1:
            print("NO")
            return True
        else:
            sum_vals += res
    if sum_vals > 2:
        print("NO")
        return True
    print("YES")
    return True


if __name__ == "__main__":
    n = int(input())
    sys.setrecursionlimit(100000000)
    graph = dict()
    for i in range(n - 1):
        u, v = [int(x) for x in input().split()]
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]

    q = int(input())
    for i in range(q):
        set_size = int(input())
        vert_set = {int(x): True for x in input().split()}
        passable(graph, vert_set)
