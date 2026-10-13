class Solution:
    def checkString(self, s: str) -> bool:
        s = list(s)
        return sorted(s) == s