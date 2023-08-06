#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int arr[n];
    int product[n];

    for (int i=0; i<n; i++)
    {
        cin >> arr[i];
    }

    for (int i=0; i<n; i++)
    {
        int k = 1;

        for (int j=0; j<n; j++)
        {
            if (j == i)
            {
                continue;
            }
            
            k = k*arr[j];
        }

        product[i] = k;

    }

    for (int i=0; i<n; i++)
    {
        cout << product[i] << ",";
    }
}