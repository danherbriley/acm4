#include <iostream>
#include <cmath>
#include <string>
#include <memory>
#include <vector>

const int MAX_NON_ONE_NUMBERS_TO_SUM = 30;

void solve() {
    long long all_sum = 0;
    long long all_product = 1;
    std::vector<int> not_ones_idxs;
    std::vector<int> aa;

    int n;
    std::cin >> n;

    for (int i = 0; i < n; i++) {
        long long a;
        std::cin >> a;
        aa.push_back(a);
        all_sum += a;
        all_product *= a;
        if (a != 1) {
            not_ones_idxs.push_back(i);
        }
    }

    if (all_product >= std::pow(2, MAX_NON_ONE_NUMBERS_TO_SUM)) {
        std::cout << not_ones_idxs[0] + 1 << " " << not_ones_idxs[not_ones_idxs.size() - 1] + 1 << std::endl;
        return;
    }

    std::tuple<long long, int, int> best = {all_sum, 0, 0};  // (product + (all_sum - sum), l, r)
    for (size_t i = 0; i < not_ones_idxs.size(); i++) {
        long long last_aa_idx = not_ones_idxs[i];
        long long last_product = aa[not_ones_idxs[i]];
        long long last_sum = aa[not_ones_idxs[i]];
        for (size_t j = i + 1; j < not_ones_idxs.size(); j++) {
            last_product = last_product * aa[not_ones_idxs[j]];
            last_sum = last_sum + (not_ones_idxs[j] - last_aa_idx - 1) + aa[not_ones_idxs[j]];
            last_aa_idx = not_ones_idxs[j];

            long long candidate = last_product + (all_sum - last_sum);
            if (candidate > std::get<0>(best)) {
                best = {candidate, not_ones_idxs[i], not_ones_idxs[j]};
            }
        }
    }

    std::cout << std::get<1>(best) + 1 << " " << std::get<2>(best) + 1 << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; i++) {
        solve();
    }

    return 0;
}
