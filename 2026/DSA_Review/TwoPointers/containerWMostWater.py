class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        while l < r:
            area = min(heights[l],heights[r]) * (r - l)
            maxArea = max(area, maxArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxArea

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)