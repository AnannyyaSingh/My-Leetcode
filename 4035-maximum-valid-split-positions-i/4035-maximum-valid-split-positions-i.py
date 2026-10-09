class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n, best = len(nums), 0
        for arr in chain([nums], (nums[:j] + nums[j + 1:] for j in range(n))):
            pre = list(accumulate(arr, gcd))  # pre[i] = gcd(arr[:i + 1])
            suf = list(accumulate(reversed(arr), gcd))[::-1]  # suf[i] = gcd(arr[i:])
            best = max(best, sum(map(eq, pre, islice(suf, 1, None))))
        return best