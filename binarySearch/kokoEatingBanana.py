class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2
            if k_works(m):
                r = m
            else:
                l = m + 1
        
        return r

# Time complexity: O(nlogm), where n is the number of piles and m is the maximum number of bananas in a pile
# Space complexity: O(1)