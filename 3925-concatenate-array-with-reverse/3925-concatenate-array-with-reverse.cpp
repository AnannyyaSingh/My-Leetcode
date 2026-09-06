class Solution {
public:
    vector<int> concatWithReverse(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n * 2);

        for (int i = 0; i < n; ++i) {
            res[i] = nums[i];
        }

        for (int i = n, j = n - 1; i < n * 2; ++i, --j) {
            res[i] = nums[j];
        }

        return res;
    }
};