class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        l,r = 0, len(s) - 1
        res = []
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
            
        def swap(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
                
        l, r = 0, 0
        for r in range(len(s)): # not sure
            if r == len(s) - 1:
                swap(l, r)
            if s[r] == " ":
                swap(l, r - 1)
                l = r + 1
                
        final = []
        i = 0
        while i < len(s):
            res = ""
            while i < len(s) and s[i] != " ":
                res += s[i]
                i += 1
            if res: 
                final.append(res)
            i += 1
        
        return " ".join(final)
                
# there's a way you can do it with O(1), look for that approach