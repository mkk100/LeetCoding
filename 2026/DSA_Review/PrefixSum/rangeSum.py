class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArr = []
        cur = 0
        for n in nums:
            cur += n
            self.prefixArr.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixArr[right]
        leftSum = self.prefixArr[left - 1] if left > 0 else 0
        return rightSum - leftSum 

# self.prefixArr[right] - self.prefixArr[left - 1], you
# get the range sum of that range.