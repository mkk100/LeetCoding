class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # left
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if target < nums[l] or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


# need to come back to this
# Time complexity: O(logn)
# Space complexity: O(1)