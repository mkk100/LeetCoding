class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(nums)
        while len(nums) > k: # remove the minheap until k elements remain
            heapq.heappop(nums)

        return nums[0]

