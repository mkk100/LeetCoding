class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = strs[0]
        for i in range(1,len(strs)):
            res = res[:len(strs[i])] 
            for j in range(min(len(res),len(strs[i]))):
                if strs[i][j] != res[j]:
                    res = res[:j]
                    break      
        return res



        