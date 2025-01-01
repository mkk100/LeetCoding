class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        mostWater = 0
        while l <= r:
            cur = min(height[l], height[r]) * (r - l)
            if cur > mostWater:
                mostWater = cur
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mostWater


# O(N) time
# O(1) Space
# try to undrestand the problem and use the two pointers method, take into account the distance between l and r.
