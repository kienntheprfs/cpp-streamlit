/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;
// N == 1:  (N = 1) = 1
// N == 2: (N = 1, 1), (N = 2) = 1 + 1 = 2
// N == 3: (N = 1, 2), (N = 2, 1), (N = 3) = 1 + 2 + 1 = 4
// N == 4: (N = 1, 3), (N = 2, 2), (N = 3, 1) = 1 + 2 + 4 = 7
int func(int N) {
    if (N == 1) return 1;
    if (N == 2) return 2;
    if (N == 3) return 4;
    
    return func(N - 1) + func(N - 2) + func(N - 3);
}

int main()
{
    cout << func(4);

    return 0;
}