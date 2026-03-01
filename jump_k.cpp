#include <iostream>

using namespace std;

/*
 * Function: jump_k
 * ----------------
 * Calculates the maximum cost to reach the last stone, where you can jump up to k stones at a time.
 *
 * Parameters:
 *   arr[]: An array of integers representing the heights/values of the stones.
 *   N: The number of stones (size of arr).
 *   k: The maximum number of stones you can jump over in one move.
 *
 * Returns:
 *   The maximum cost to reach the last stone from the first stone.
 *
 * Approach:
 *   Uses dynamic programming. dp[i] stores the maximum cost to reach stone i.
 *   For each stone i, consider all possible jumps from stones i-j (1 <= j <= k, j <= i),
 *   and take the maximum value of dp[i-j] + abs(arr[i] - arr[i-j]).
 */
int jump_k(int arr[], int N, int k) {
    int dp[N];
    dp[0] = 0; // Base case: dp[0] is the cost of jumping to the first stone

    for (int i = 1; i < N; i++) {
        int max_value = -1e7;

        for (int j = 1; j <= k && j <= i; j++) {
            max_value = max(max_value, dp[i - j] + abs(arr[i] - arr[i - j]));
        }

        dp[i] = max_value;
    }

    return dp[N - 1];
}

/**
 * @brief Recursively calculates the maximum cost to reach a given stone index, allowing jumps up to k stones.
 *
 * @param arr Array of integers representing the heights/values of the stones.
 * @param N The number of stones (size of arr).
 * @param k The maximum number of stones you can jump over in one move.
 * @param index The current stone index to reach.
 * @return The maximum cost to reach the stone at the given index from the first stone.
 *
 * @note This implementation is not memoized and may be slow for large N.
 */
int jump_k_recursive(int arr[], int N, int k, int index) {
    if (index == 0) return 0; // Base case: cost of jumping to the first stone

    int max_value = -1e7;

    for (int j = 1; j <= k && j <= index; j++) {
        max_value = max(max_value, jump_k_recursive(arr, N, k, index - j) + abs(arr[index] - arr[index - j]));
    }

    return max_value;
}

// int main() {
//     // int N;
//     // cin >> N;
//     int N = 14;
//     int arr[N] = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28};
//     int k = 8;

//     // int N = 4;
//     // int arr[N] = {2, 5, 1, 7};
//     // int k = 2;

//     int result = jump_k(arr, N, k);
//     cout << result << endl;

//     int result_recursive = jump_k_recursive(arr, N, k, N - 1);
//     cout << result_recursive << endl;

//     return 0;
// }