#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>


struct Shark {
    Shark * previous_shark;
    Shark * next_shark;
    long long int prime_div_cnt;
    long long int range;
};


void solve(int prime, const std::vector<std::pair<int, int>> & sharks) {
    long long int total_possibilities = 1;
    long long int number_of_all_thousands = 0;

    Shark * first_shark = nullptr;
    Shark * prev_shark = nullptr;
    for (unsigned int i = 0; i < sharks.size(); ++i) {
        const std::pair<int, int>& pair = sharks[i];
        long long int prime_div_cnt = (pair.second / prime) - ((pair.first - 1) / prime);

        long long int range = pair.second - pair.first + 1;
        total_possibilities *= range;

        Shark * shark = new Shark{prev_shark, nullptr, prime_div_cnt, range};
        if (prev_shark)
            prev_shark->next_shark = shark;
        else
            first_shark = shark;
        prev_shark = shark;
    }
    first_shark->previous_shark = prev_shark;
    prev_shark->next_shark = first_shark;

    while (1) {
        long long int other_possibilities = (total_possibilities / first_shark->range);
        number_of_all_thousands += (2 * ((first_shark->prime_div_cnt * other_possibilities) + 
                                         (first_shark->prime_div_cnt * other_possibilities))
                                    );
        number_of_all_thousands -= 2 * ((first_shark->prime_div_cnt * first_shark->next_shark->prime_div_cnt) * (other_possibilities / first_shark->next_shark->range));
        if (first_shark == prev_shark)
            break;
        first_shark = first_shark->next_shark;
    }

    first_shark = first_shark->next_shark;
    while (true) {
        first_shark = first_shark->next_shark;
        delete first_shark->previous_shark;
        if (first_shark == prev_shark) {
            delete first_shark;
            break;
        }
    }

    // std::cout << number_of_all_thousands << " " << total_possibilities << std::endl;
    long double res = ((double) (number_of_all_thousands * 1000) / total_possibilities);
    std::cout << std::setprecision(10) << res << std::endl;
}


int main() {
    int n, p;
    std::cin >> n >> p;
    std::vector<std::pair<int, int>> sharks = {};

    for (int i = 0; i < n; ++i) {
        int l, r;
        std::cin >> l >> r;
        sharks.push_back(std::make_pair(l, r));
    }

    solve(p, sharks);
}