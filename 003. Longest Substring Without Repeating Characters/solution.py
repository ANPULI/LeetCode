class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = dict()
        res = i = j = 0
        n = len(s)
        while i + res < n and j < n:
            c = s[j]
            if lookup.get(c, -1) != -1:
                i = max(lookup[c] + 1, i)
            res = max(res, j - i + 1)
            lookup[c] = j
            j += 1
        return res