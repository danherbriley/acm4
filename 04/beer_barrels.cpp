#include <iostream>
#include <cmath>

int main(){
    long long int a, b, k, c;
    std::cin >> a >> b >> k >> c;
    if (k == 0) {
        std::cout << 0 << std::endl;
    }
    else if (c != a && c != b) {
        std::cout << 0 << std::endl;
    }
    else if (c == a && c == b) {
        std::cout << k << std::endl;
    }
    else{
        long long int res = (long long int)(std::pow(2, k - 1)) % 1000000007;
        res = (res * k) % 1000000007;
        std::cout << res << std::endl;
    }
    return 0;
}
