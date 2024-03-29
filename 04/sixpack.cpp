#include <iostream>
#include <vector>

#define MOD 1000000007


std::vector<int> SUM_CNT = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1};  // SUM_CNT[idx] gives you the number of different ordered pairs (x, y) whose sum equals to idx


long long int solve(const std::vector<std::pair<int, int>> & predefined, int n, int k, int curr_col, int last_col_sum, int last_last_col_sum, long long int res_cnt) {
    if (curr_col == n) {
        return res_cnt % MOD;
    }

    if (predefined[curr_col].first != -1 || predefined[curr_col].second != -1) {  // if at least one of the cells is predefined
        int col_sum = predefined[curr_col].first + predefined[curr_col].second;
        if (predefined[curr_col].first != -1 && predefined[curr_col].second != -1) {  // if both cells are predefined
            if ((last_last_col_sum != -1 && col_sum == k - last_col_sum - last_last_col_sum) ||  // third to last column
                (last_last_col_sum == -1 && last_col_sum != -1 && col_sum <= k - last_col_sum) ||  // second column
                (last_col_sum == -1 && col_sum <= k) // first column
                ) {
                return solve(predefined, n, k, curr_col + 1, col_sum, last_col_sum, res_cnt) % MOD;
            }
            return 0;
        }

        // if only one cell is predefined
        int predefined_cell = col_sum + 1;  // because above the col_sum is defined as the sum of those predefined cells, but we know one was equal to -1
        long long int res = 0;

        if (last_last_col_sum != -1) {  // third to last column
            if (k - last_col_sum - last_last_col_sum - predefined_cell >= 0 && k - last_col_sum - last_last_col_sum - predefined_cell <= 9)
                return solve(predefined, n, k, curr_col + 1, k - last_col_sum - last_last_col_sum, last_col_sum, res_cnt) % MOD;
            return 0;
        }
        else if (last_col_sum != -1) {  // second column
            for (int i = 0; predefined_cell + i <= k - last_col_sum && i <= 9; ++i) {
                res += solve(predefined, n, k, curr_col + 1, predefined_cell + i, last_col_sum, res_cnt) % MOD;
            }
            return res;
        } else {  // first column
            for (int i = 0; predefined_cell + i <= k && i <= 9; ++i) {
                res += solve(predefined, n, k, curr_col + 1, predefined_cell + i, last_col_sum, res_cnt) % MOD;
            }
            return res;
        }
    } else {  // if no cells are predefined
        if (last_last_col_sum != -1) {  // third to last column
            if (k - last_col_sum - last_last_col_sum < 0 || k - last_col_sum - last_last_col_sum > 18)
                return 0;
            return solve(predefined, n, k, curr_col + 1, k - last_col_sum - last_last_col_sum, last_col_sum, SUM_CNT[k - last_col_sum - last_last_col_sum] * res_cnt % MOD) % MOD;
        }
        else if (last_col_sum != -1) {  // second column
            long long int res = 0;
            for (int i = 0; i <= k - last_col_sum && i <= 18; ++i) {
                res += solve(predefined, n, k, curr_col + 1, i, last_col_sum, SUM_CNT[i]*res_cnt % MOD) % MOD;
            }
            return res;
        } else {  // first column
            long long int res = 0;
            for (int i = 0; i <= k && i <= 18; ++i) {
                res += solve(predefined, n, k, curr_col + 1, i, last_col_sum, SUM_CNT[i]*res_cnt % MOD) % MOD;
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