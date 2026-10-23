class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def helper(n):
            if n == 0:
                return 1
            res = helper(n // 2)
            res *= res
            return x * res if n % 2 == 1 else res # if odd exponent
        res = helper(abs(n))
        return res if n > 0 else 1 / res # handling negative case
            
