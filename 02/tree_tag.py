def find_dist(a, b, graph, dist=0, visited=set()):
    visited.add(a)
    if a == b:
        return dist
    for vert in graph[a]:
        if vert not in visited:
            d = find_dist(vert, b, graph, dist + 1, visited)
            if d:
                return d


def longest_path(graph, vert, dist=0, visited=set()):
    visited.add(vert)
    unv_n = list(filter(lambda x: x not in visited, graph[vert]))
    if not unv_n:
        return (dist, vert, visited)
    results = list()
    for v in unv_n:
        results.append(longest_path(graph, v, dist + 1, visited))
    return max(results, key=lambda x: x[0])


def max_jump(graph, start):
    v1 = longest_path(graph, start, 0, set())[1]
    return longest_path(graph, v1, 0, set())[0]


def tree_tag(n, a, b, da, db, graph):
    if find_dist(a, b, graph, 0, set()) <= da:
        print("Alice")
    elif db <= 2 * da or max_jump(graph, a) <= 2 * da:
        print("Alice")
    else:
        print("Bob")


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, a, b, da, db = [int(x) for x in input().split()]
        graph = dict()
        for i in range(n - 1):
            v1, v2 = [int(x) for x in input().split()]
            if v1 in graph:
                graph[v1].add(v2)
            else:
                graph[v1] = set([v2])
            if v2 in graph:
                graph[v2].add(v1)
            else:
                graph[v2] = set([v1])
        tree_tag(n, a, b, da, db, graph)
