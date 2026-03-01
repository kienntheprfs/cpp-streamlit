#include <iostream>
// Declare the function you want to test (adjust signature as needed)
int jump_k(int a[], int n, int k);

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = 5;
    int k = 2;
    int result = jump_k(arr, n, k);
    std::cout << "Result: " << result << std::endl;
    // Add more test cases as needed
    return 0;
}
