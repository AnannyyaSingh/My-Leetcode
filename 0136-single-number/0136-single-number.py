class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0

        for value in nums:
            ans ^= value
        return ans