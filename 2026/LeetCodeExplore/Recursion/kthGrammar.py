class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l, r = 1, 2**(n-1)
        cur = 0
        for _ in range(n - 1):
            mid = (l + r) // 2
            if k > mid:
                l = mid + 1
                cur = 0 if cur else 1
            else:
                r = mid - 1
                
        return cur