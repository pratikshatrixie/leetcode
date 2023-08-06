#include <iostream>
using namespace std;

int minSubArrayLen(int k, int arr[], int n) {
    int i = 0; // Starting index of the window
    int ans = n + 1; // Initialize ans to a value greater than the array size (acts as a placeholder for the minimal length found)

    for (int j = 0; j < n; j++) {
        k -= arr[j]; // Subtract the current element from the target k
        while (k <= 0) {
            ans = min(ans, j - i + 1); // Calculate the current window size and update the minimum window size found so far
            k += arr[i++]; // Add the element at the start of the window to k and move the window to the right
        }
    }
    return ans % (n + 1); // Return the minimal length found
}

int main()
{
    int arr[] = {2,3,1,2,4,3};
    int k = 7;
    int n = 6;

    int output = minSubArrayLen(k, arr, n);

    cout << output;

}