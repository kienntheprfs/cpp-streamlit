#include "bits/stdc++.h"

using namespace std;

// N = 15
// GCD (15,12) + 12
// GCD (12, 15 mod 12) + 12
// GCD (12, 3) + 12 = 15 


void func1(){
    int  a = 12, b = 15;

    // (a + x) % b == 0 && (b+x) % a == 0
    // (a + x) % b == 0 -> a >= b, 1 <= x < b, a % b == x  
    
    // a % b == x
    // (k.b + x) % b == x
    // (b+x) % a == 0 -> b >= a
    // b % a == x
    // (k.a + x) % a == x

    int x = 1;
    while (true){
        if ((a + x) % b == 0 && (b+x) % a == 0) {
            cout << x << endl;
            break;
        }
        ++x;
    }
}

void func2() {

    int N = 100;

    double S = 0;
    for (int i = 2; i <= N; ++i) {
        S += (double) sqrt(1 + (double)1/((i*i)) + (double)1/((i + 1)*(i + 1)));
    }
    cout << setprecision(2) << fixed << S << endl;
}

int main(){
    // func1()
    func2();
}