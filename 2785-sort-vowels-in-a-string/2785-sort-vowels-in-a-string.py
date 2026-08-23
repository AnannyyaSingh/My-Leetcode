class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_set = set("aeiouAEIOU")

        sorted_vowels = sorted(ch for ch in s if ch in vowel_set)

        res = []
        v_idx = 0
        for ch in s:
            if ch in vowel_set:
                res.append (sorted_vowels[v_idx])
                v_idx += 1
            else:
                res.append(ch)
        return "".join(res)