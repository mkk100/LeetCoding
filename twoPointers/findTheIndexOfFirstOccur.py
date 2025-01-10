class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle)
        if haystack == needle:
            return 0
        while l < len(haystack) or r < len(haystack):
            if haystack[l:r] != needle:
                l += 1
                r = l + len(needle)
            elif haystack[l:r] == needle:
                return l
        return -1

# sliding window