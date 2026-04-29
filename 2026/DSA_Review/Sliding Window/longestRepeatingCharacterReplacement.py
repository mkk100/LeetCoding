class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, longest = 0, 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            max_count = max(count.values())

            while (r - l + 1) - max_count > k:
                count[s[l]] = count.get(s[l]) - 1
                l += 1
            
            longest = max(r - l + 1, longest)
        return longest
