class Solution:
    def calc(self, n):
        res = 0
        while n:
            res += (n % 10)**2
            n //= 10
        return res

    def isHappy(self, n: int) -> bool:
        slow = self.calc(n)
        fast = self.calc(slow)
        while slow != fast:
            slow = self.calc(slow)
            fast = self.calc(self.calc(fast))

        return slow == 1