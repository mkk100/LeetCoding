class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        count = {}
        longest = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest


# Time complexity: O(26*n)
# Space complexity: O(N) since the count dictionary will have at most 26 keys
# approach: (r - l + 1) - max(count.values()), this is key, current window char - most recurring char < k


# optimized solution
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        count = {}
        longest = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

        return longest


# you don't need to decrement maxf because at one point, maxf was valid and it won't affect the end result.
# def gotta do it again.
