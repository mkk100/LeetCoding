class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not self.isAlnum(s[l]): l += 1
            while l < r and not self.isAlnum(s[r]): r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isAlnum(self, a):
        return (
            (ord('a') <= ord(a) <= ord('z')) or
            (ord('A') <= ord(a) <= ord('Z')) or
            (ord("0") <= ord(a) <= ord("9"))
        )

# trivial solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for a in s:
            if a.isalnum():
                newS += a.lower()
        return newS == newS[::-1]