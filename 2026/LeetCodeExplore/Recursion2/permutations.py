class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, sol = [], []
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol[:])

            for n in nums:
                if n not in sol:
                    sol.append(n)
                    backtrack()
                    sol.pop()
        backtrack()
        return res
