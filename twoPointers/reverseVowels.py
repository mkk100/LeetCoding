class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        s = list(s)
        while l <= r:
            while s[r].lower() not in vowels and l < r:
                r -= 1
            while s[l].lower() not in vowels and l < r:
                l += 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)