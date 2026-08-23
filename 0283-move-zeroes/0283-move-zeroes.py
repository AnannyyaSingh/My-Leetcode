class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0

        for current in range (len(nums)):
            if nums[current] != 0:
                nums[insert_pos], nums[current] = nums[current], nums[insert_pos]
                insert_pos += 1 