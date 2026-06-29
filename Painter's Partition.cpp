#include <iostream>
#include <vector>
using namespace std;

bool isPossible(vector<int>& arr, int n, int k, int maxAllowedTime) {
    int painter = 1;
    int time = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] > maxAllowedTime) {
            return false;
        }

        if (time + arr[i] <= maxAllowedTime) {
            time += arr[i];
        } 
        else {
            painter++;
            time = arr[i];

            if (painter > k) {
                return false;
            }
        }
    }

    return true;
}

int painterPartition(vector<int>& arr, int n, int k) {
    int st = 0, end = 0;
    int ans = -1;

    for (int x : arr) {
        st = max(st, x);
        end += x;
    }

    while (st <= end) {
        int mid = st + (end - st) / 2;

        if (isPossible(arr, n, k, mid)) {
            ans = mid;
            end = mid - 1;
        } else {
            st = mid + 1;
        }
    }

    return ans;
}

int main() {
    vector<int> arr = {10, 20, 30, 40};
    int n = arr.size();
    int k = 2;

    cout << painterPartition(arr, n, k);
}