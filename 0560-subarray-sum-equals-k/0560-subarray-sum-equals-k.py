class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = {0:1}
        current_sum = 0
        answer = 0

        for value in nums:
            current_sum = current_sum + value
            needed = current_sum - k
            answer += prefix_count.get(needed, 0)
            prefix_count[current_sum] = (
                prefix_count.get(current_sum, 0) + 1
            )
        return answer