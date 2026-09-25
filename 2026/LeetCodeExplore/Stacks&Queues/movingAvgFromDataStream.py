from collections import deque

class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.q = deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        return sum(self.q) / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

m = MovingAverage(3)
print(m.next(1))   # expect 1.0    -> window: [1]
print(m.next(10))  # expect 5.5    -> window: [1, 10]
print(m.next(3))   # expect 4.66666... -> window: [1, 10, 3]
print(m.next(5))   # expect 6.0    -> window: [10, 3, 5]  (1 got pushed out)

m2 = MovingAverage(1)
print(m2.next(4))  # expect 4.0
print(m2.next(9))  # expect 9.0  (window size 1, always just the latest value)

m3 = MovingAverage(5)
print(m3.next(2))  # expect 2.0
print(m3.next(2))  # expect 2.0
print(m3.next(2))  # expect 2.0  (window never exceeds size, so nothing gets evicted yet)