class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for i in range(n1): # initializing count1 bc it won't change
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        if count1 == count2:
            return True
        
        for r in range(n1, n2):
            count2[ord(s2[r]) - ord('a')] += 1
            count2[ord(s2[r - n1]) - ord('a')] -= 1
            if count1 == count2:
                return True
        return False

# Time complexity: O(N)
# Space complexity: O(N)
# Approach: populate the counts with s1 value first, check if they are equal if not start sliding window, 
# this is the left ptr, ord(s2[r - n1]) - ord('a')
