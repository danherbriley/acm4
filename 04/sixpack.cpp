#include <iostream>
#include <vector>

#define MOD 1000000007


std::vector<int> SUM_CNT = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};


long long int solve(const std::vector<std::pair<int, int>> & predefined, int n, int k, int curr_col, int last_col_sum, int last_last_col_sum, int res_cnt) {
    if (curr_col == n) {
        return res_cnt % MOD;
    }

    if (predefined[curr_col].first != -1 || predefined[curr_col].second != -1) {
        int col_sum = predefined[curr_col].first + predefined[curr_col].second;
        if (predefined[curr_col].first != -1 && predefined[curr_col].second != -1) {
            if ((col_sum == k - last_col_sum - last_last_col_sum) || 
                (last_col_sum == -1 && col_sum <= k) ||
                (last_last_col_sum == -1 && col_sum <= k - last_col_sum)
                ) {
                return solve(predefined, n, k, curr_col + 1, col_sum, last_col_sum, res_cnt);
            }
            return 0;
        }
        int predefined_cell = col_sum + 1;
        long long int res = 0;
        if (last_col_sum != -1) {
            if (k - last_col_sum - last_last_col_sum - predefined_cell >= 0 && k - last_col_sum - last_last_col_sum - predefined_cell <= 9)
                return solve(predefined, n, k, curr_col + 1, k - last_col_sum - last_last_col_sum, last_col_sum, res_cnt) % MOD;
            return 0;
        } else {
            int top = k - last_col_sum - last_last_col_sum;
            if (last_last_col_sum == -1)
                top = k - last_col_sum;
            for (int i = 0; predefined_cell + i <= top && i <= 9; ++i) {
                res += solve(predefined, n, k, curr_col + 1, predefined_cell + i, last_col_sum, res_cnt) % MOD;
            }
            return res;
        }
    } else {
        if (last_last_col_sum != -1) {
            if (k - last_col_sum - last_last_col_sum < 0 || k - last_col_sum - last_last_col_sum > 18)
                return 0;
            return solve(predefined, n, k, curr_col + 1, k - last_col_sum - last_last_col_sum, last_col_sum, SUM_CNT[k - last_col_sum - last_last_col_sum] * res_cnt) % MOD;
        }
        else if (last_col_sum != -1) {
            long long int res = 0;
            for (int i = 0; i <= k - last_col_sum && i <= 18; ++i) {
                res += solve(predefined, n, k, curr_col + 1, i, last_col_sum, SUM_CNT[i]*res_cnt) % MOD;
            }
            
            return res;
        } else {
            long long int res = 0;
            for (int i = 0; i <= k && i <= 18; ++i) {
                res += solve(predefined, n, k, curr_col + 1, i, last_col_sum, SUM_CNT[i]*res_cnt) % MOD;
            }
            return res;
        }
    }

}

int main() {
    int n, k, m;
    std::cin >> n >> k >> m;

    std::vector<std::pair<int, int>> predefined(n, std::make_pair(-1, -1));

    int c, r, v;
    for (int i = 0; i < m; ++i) {
        std::cin >> c >> r >> v;
        if (r == 0) {
            predefined[c].first = v;
        } else {
            predefined[c].second = v;
        }
    }

    long long int res = solve(predefined, n, k, 0, -1, -1, 1);
    std::cout << res << std::endl;
}


/*

0 0 => 3 
0 0 

0 0 => 4 * 2 = 8
0 1

0 0 => 6 * 1 = 6
1 1

0 0 => 4 * 1 = 4
0 2

*/