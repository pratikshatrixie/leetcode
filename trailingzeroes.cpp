#include <iostream>
using namespace std;

int trailingZeroes(int n) {
    if (n == 0 || n == 1)
        return 1; // The factorial of 0 and 1 is 1, which has 1 trailing zero.
    
    int factorial = 1;
    for (int i = 2; i <= n; i++) {
        factorial *= i;
    }

    // Count the number of trailing zeroes in the factorial
    int count = 0;
    while (factorial % 10 == 0) {
        count++;
        factorial /= 10;
    }

    return count;
}

int main() {
    cout << trailingZeroes(3) << endl;
    return 0;
}





