# TC 2^t(t=target value)

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or target < total:
                return
            
            # pick the num
            cur.append(nums[i])
            backtrack(i, cur, nums[i] + total)
            cur.pop()

            # not pick
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)
        return res