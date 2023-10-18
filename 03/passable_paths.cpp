#include <iostream>
#include <vector>
#include <map>
#include <set>


int search(const std::map<int, std::vector<int>>& graph, const std::set<int>& vert_set, std::map<int, bool>& visited, int curr) {
    visited[curr] = true;
    std::vector<int> neighbours = graph.at(curr);
    
    if (neighbours.empty()) {
        if (vert_set.count(curr)) {
            return 1;
        } else {
            return 0;
        }
    }

    int sum_vals = 0;
    for (int neighbour : neighbours) {
        if (!visited[neighbour]) {
            sum_vals += search(graph, vert_set, visited, neighbour);
        }
    }

    if (sum_vals > 1) {
        return 2;
    }
    
    if (vert_set.count(curr)) {
        return 1;
    } else {
        return sum_vals;
    }
}

bool passable(const std::map<int, std::vector<int>>& graph, const std::set<int>& vert_set) {
    if (vert_set.empty()) {
        std::cout << "YES" << std::endl;
        return true;
    }

    if (vert_set.size() < 3) {
        std::cout << "YES" << std::endl;
        return true;
    }

    int start = *vert_set.begin();
    int sum_vals = 0;
    std::map<int, bool> visited;
    visited[start] = true;
    
    for (int neighbour : graph.at(start)) {
        int res = search(graph, vert_set, visited, neighbour);
        if (res > 1) {
            std::cout << "NO" << std::endl;
            return true;
        } else {
            sum_vals += res;
        }
    }
    
    if (sum_vals > 2) {
        std::cout << "NO" << std::endl;
        return true;
    }

    std::cout << "YES" << std::endl;
    return true;
}

int main() {
    int n;
    std::cin >> n;
    std::map<int, std::vector<int>> graph;

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        std::cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int q;
    std::cin >> q;
    for (int i = 0; i < q; ++i) {
        int set_size;
        std::cin >> set_size;
        std::set<int> vert_set;
        for (int j = 0; j < set_size; ++j) {
            int x;
            std::cin >> x;
            vert_set.insert(x);
        }
        passable(graph, vert_set);
    }

    return 0;
}
