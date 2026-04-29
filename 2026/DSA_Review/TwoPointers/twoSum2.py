class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r  = 0, len(numbers) - 1
        while l <= r:
            summed_val = numbers[l] + numbers[r] 
            if summed_val > target:
                r -= 1
            elif summed_val < target:
                l += 1
            elif summed_val == target:
                return [l + 1, r + 1]
