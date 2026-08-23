class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        highest = 0

        for change in gain:
            curr += change
            highest = max(highest, curr)
        return highest