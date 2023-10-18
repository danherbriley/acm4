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
    else{
        std::cout << ((long long int)(std::pow((long long int)2, k) * k) / 2) % 1000000007 << std::endl;
    }
    return 0;
}