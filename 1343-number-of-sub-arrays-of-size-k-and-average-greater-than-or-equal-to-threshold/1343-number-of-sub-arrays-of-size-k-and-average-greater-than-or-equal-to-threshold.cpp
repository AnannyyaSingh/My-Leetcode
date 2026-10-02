class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int targetSum = threshold * k;
        int windowSum = accumulate(arr.begin(), arr.begin() + k, 0);

        int count = (windowSum >= targetSum) ? 1 : 0;
      
        for (int i = k; i < arr.size(); ++i) {
            windowSum += arr[i] - arr[i - k];
            if (windowSum >= targetSum) {
                count++;
            }
        }
      
        return count;
    }
};
