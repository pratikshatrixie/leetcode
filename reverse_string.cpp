#include <iostream>
#include <cctype>

using namespace std;

int main()
{
    string s = "the sky is blue";
    string output = "";

    int length = s.length();
    int wordEnd = length - 1;

    for (int i = length - 1; i >= 0; i--)
    {
        if (!isalpha(s[i]))
        {
            if (i < wordEnd)
            {
                for (int j = i + 1; j <= wordEnd; j++)
                {
                    output += s[j];
                }
                output += ' ';
            }
            wordEnd = i - 1;
        }
    }

    if (wordEnd >= 0)
    {
        for (int j = 0; j <= wordEnd; j++)
        {
            output += s[j];
        }
    }

    cout << output << endl;

    return 0;
}