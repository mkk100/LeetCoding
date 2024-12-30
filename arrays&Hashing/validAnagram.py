class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashS = {}
        hashT = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1
        
        if hashS == hashT:
            return True
        return False

        # OR
        
        for c in hashS: # this is faster
            if hashS[c] != hashT.get(c, 0):
                return False
        return True
        