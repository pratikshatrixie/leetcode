#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    int nums[5] = {2,3,1,1,4};
    int n = 5;
    int jumps = 0, end = 0, farthest = 0;
    for (int i = 0; i < n - 1; i++) {
        farthest = max(farthest, i + nums[i]); // update the maximum reach
        if (i == end) { // if the current index is equal to the end, update end and increment jumps
            end = farthest;
            jumps++;
        }
    }
    cout<<jumps;
    return jumps;
}


 