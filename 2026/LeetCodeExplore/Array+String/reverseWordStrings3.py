class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        l, r = 0, 0
        s = list(s)
        def swap(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
            
        while r < len(s):
            l = r
            while r < len(s) and s[r] != " ":
                r += 1
            swap(l, r - 1)
            r += 1
        return ("").join(s)
                
                
        