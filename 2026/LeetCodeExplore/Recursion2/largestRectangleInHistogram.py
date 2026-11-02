# Divide and Conquer
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        def divideAndConquer(l ,r):
            if l > r:
                return 0
            if l == r:
                return heights[l]
            
            minH = l
            for i in range(l + 1, r + 1):
                if heights[i] < heights[minH]:
                    minH = i
            
            c_area = heights[minH] * (r - l + 1)
            l_area = divideAndConquer(l, minH - 1)
            r_area = divideAndConquer(minH + 1, r)

            return max(c_area,l_area,r_area)
        return divideAndConquer(0, len(heights) - 1)

