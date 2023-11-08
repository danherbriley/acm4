#include <iostream>
#include <vector>
#include <unordered_map>

void solve(int n, const std::vector<int>& a) {
    std::vector<int> best(n + 1, -1);
    std::vector<int> cut_len(n, n);

    for (int j = 0; j < n; ++j) {
        int x = a[j];
        if (best[x] == -1) {
            best[x] = j;
            if (j == 0) {
                cut_len[j] = 1;
            } else {
                cut_len[j] = cut_len[j - 1] + 1;
            }
        } else {
            if (cut_len[j - 1] + 1 < cut_len[best[x]]) {
                cut_len[j] = cut_len[j - 1] + 1;
                best[x] = j;
            } else {
                cut_len[j] = cut_len[best[x]] - 1;
            }
        }
    }

    std::cout << n - cut_len[n - 1] << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        int n;
        std::cin >> n;
        std::vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> a[i];
        }
        solve(n, a);
    }
    return 0;
}
