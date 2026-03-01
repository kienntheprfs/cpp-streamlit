#include "bits/stdc++.h"
using namespace std;

string On(string s, int n) {
    int lastPos[26] = {-1};

    int n = 
    for (int i = 0; i < n; ++i) {
        lastPos[s[i] - 'a'] = i;
    }

    for (int i = 0; i < n; ++i) {
        // Check for a smaller character that is in wrong position
        if (lastPos[i] )
    }

    return s;
}

string O2(string s, int n) {
    // Try to find the best swap
    for (int i = 0; i < n; i++) {
        int minPos = -1;
        
        // Find the smallest character to the right that is smaller than s[i]
        // If there are multiple occurrences, pick the rightmost one
        for (int j = i + 1; j < n; j++) {
            if (s[j] < s[i]) {
                if (minPos == -1 || s[j] <= s[minPos]) {
                    minPos = j;
                }
            }
        }
        
        // If found a beneficial swap, do it and break
        if (minPos != -1) {
            swap(s[i], s[minPos]);
            break;
        }
    }
}

int main() {
    freopen("list.inp", "r", stdin);
    freopen("list.out", "w", stdout);
    
    string s;
    cin >> s;
    int n = s.length();
    
    On(s, n)
    O2(s, n);
    
    cout << s;
    
    return 0;
}