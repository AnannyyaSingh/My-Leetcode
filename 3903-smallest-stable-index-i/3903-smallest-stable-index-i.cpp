class Solution {
public:
inline static int suf[100];
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size();
        suf[n-1] = nums.back();

        for(int i = n - 2; i >= 0; i--){
            suf[i] = min(suf[i+1], nums[i]);
        }

        int curr_max = 0;
        for(int i = 0; i < n; i++){
            curr_max = max(curr_max, nums[i]);
            if(curr_max - suf[i] <= k){
                return i;
            }
        }
        return -1;
    }
};