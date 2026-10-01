class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {}
        def recurse(n):
            if n in cache:
                return cache[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            res = recurse(n - 1) + recurse(n - 2)
            cache[n] = res
            return res
        return recurse(n)
        
            