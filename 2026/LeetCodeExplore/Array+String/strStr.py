class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack == needle:
            return 0
        
        l = 0
        for r in range(len(needle), len(haystack) + 1):
            if haystack[l:r] == needle:
                return l
            l += 1
        return -1



        