class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, longest = 0, 0

        for value in nums:
            if value == 1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 0
        return longest