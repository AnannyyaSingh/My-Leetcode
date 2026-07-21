class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        int sum = 0;
        for(int i: nums) sum += i;
        int l = sum/k;
        return sum - k * l;
    }
};