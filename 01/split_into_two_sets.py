

def determine_bfs(start, edges, seen):
    found_vertices = 0
    previous = -1
    current = start
    while current != start or previous == -1:
        if current not in edges:
            return False
        seen.add(current)
        found_vertices += 1
        tmp = previous
        previous = current
        current = edges[current][0] if edges[current][0] != tmp else edges[current][1]
    if found_vertices % 2 == 0:
        return True
    return False


def determine_result(n, edges):
    seen = set()
    for i in range(n):
        if (i + 1) not in seen:
            res = determine_bfs(i + 1, edges, seen)
            if not res:
                return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        edges = {}
        is_possible = True
        correct_numbers = 0
        for _ in range(n):
            a, b = tuple(int(x) for x in input().split())
            if not is_possible:
                continue

            if a == b:
                is_possible = False

            if a not in edges:
                edges[a] = [b]
            else:
                edges[a].append(b)
                correct_numbers += 1
                if len(edges[a]) > 2:
                    is_possible = False
            if b not in edges:
                edges[b] = [a]
            else:
                edges[b].append(a)
                correct_numbers += 1
                if len(edges[b]) > 2:
                    is_possible = False

        if not is_possible or correct_numbers != n:
            print("NO")
            continue

        good_result = determine_result(n, edges)
        if good_result:
            print("YES")
        else:
            print("NO")

