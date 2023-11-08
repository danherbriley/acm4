#include <iostream>
#include <vector>
#include <unordered_map>


int compute_potion( int idx,
                    const std::unordered_map<int, std::vector<int>> & graph,
                    const std::vector<int> &costs, 
                    std::vector<int> & minimum_costs
) {
    if (minimum_costs[idx] != -1)
        return minimum_costs[idx];

    int mix = 0;
    for (auto& pt : graph.at(idx)) {
        if (minimum_costs[pt] != -1)
            mix += minimum_costs[pt];
        else
            mix += compute_potion(pt, graph, costs, minimum_costs);
        if (mix > costs[idx]) {
            minimum_costs[idx] = costs[idx];
            return costs[idx];
        }
    }

    minimum_costs[idx] = mix;
    return mix;
}


void solve( int n,
            const std::unordered_map<int, std::vector<int>> & graph, 
            const std::vector<int> &costs, 
            std::vector<int> & minimum_costs
) {
    for (int i = 0; i < n; ++i) {
        if (minimum_costs[i] != -1)
            continue;
        compute_potion(i, graph, costs, minimum_costs);
    }

    for (auto& x : minimum_costs)
        std::cout << x << " ";
    std::cout << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, k;
        std::cin >> n >> k;
        std::vector<int> costs = {};
        int x;
        for (int j = 0; j < n; ++j) {
            std::cin >> x;
            costs.push_back(x);
        }
        std::vector<int> minimum_costs(n, -1);
        for (int j = 0; j < k; ++j) {
            std::cin >> x;
            minimum_costs[x - 1] = 0;
        }

        std::unordered_map<int, std::vector<int>> graph;

        for (int i = 0; i < n; ++i) {
            int m;
            std::cin >> m;
            graph[i] = std::vector<int>();
            if (m == 0) {
                if (minimum_costs[i] == -1) {
                    minimum_costs[i] = costs[i];
                }
            } else {
                int e;
                for (int j = 0; j < m; ++j) {
                    std::cin >> e;
                    graph[i].push_back(e - 1);
                }
            }
        }

        solve(n, graph, costs, minimum_costs);
    }
    return 0;
}
