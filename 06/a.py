import sys

sys.setrecursionlimit(1_000_000)


def solve(graph, costs, minimum_costs):
    def compute_potion(idx):
        if minimum_costs[idx] != -1:
            return minimum_costs[idx]

        mix = 0
        for pt in graph[idx]:
            if minimum_costs[pt] != -1:
                mix += minimum_costs[pt]
            else:
                mix += compute_potion(pt)
            if mix > costs[idx]:
                minimum_costs[idx] = costs[idx]
                return costs[idx]

        minimum_costs[idx] = mix
        return mix

    for i in range(len(minimum_costs)):
        if minimum_costs[i] != -1:
            continue
        compute_potion(i)

    for x in minimum_costs:
        print(x, end=" ")
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        costs = [int(x) for x in input().split()]
        minimum_costs = [-1 for _ in range(n)]
        for x in input().split():
            minimum_costs[int(x) - 1] = 0

        graph = {}

        for i in range(n):
            line = [int(x) - 1 for x in input().split()]
            m = line[0] + 1
            if m == 0:
                graph[i] = []
                if minimum_costs[i] == -1:
                    minimum_costs[i] = costs[i]
            else:
                graph[i] = line[1:]

        solve(graph, costs, minimum_costs)
