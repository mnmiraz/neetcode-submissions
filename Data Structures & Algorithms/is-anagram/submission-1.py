class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        for char in count_s:
            if count_t[char] != count_s[char]:
                return False
        return True