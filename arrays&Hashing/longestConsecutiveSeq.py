class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                if length > longest:
                    longest = length
        return longest

# time complexity - O(N)
# space complexity - O(N)
# if there's no left neighbour means the start of the new sequence.