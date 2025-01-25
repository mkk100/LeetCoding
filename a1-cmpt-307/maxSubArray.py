import time
import random
from typing import List

# Brute-force algorithm
def maxSubArrayBruteForce(nums: List[int]) -> int:
    ans = float('-inf')
    for i in range(len(nums)):
        cur = 0
        for j in range(i, len(nums)):
            cur += nums[j]
            ans = max(cur, ans)
    return ans

# Divide-and-conquer algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def maxSubArray(A, L, R):
            if L > R: return float('-inf')
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)

# Function to measure running times
def measure_time(func, nums):
    start_time = time.time()
    func(nums)
    end_time = time.time()
    return end_time - start_time

# Test and compare running times
n_values = [10, 50, 100, 500, 1000, 5000, 10000]
brute_force_times = []
divide_and_conquer_times = []

for n in n_values:
    nums = [random.randint(0, 100) for _ in range(n)]
    brute_force_time = measure_time(maxSubArrayBruteForce, nums)
    divide_and_conquer_time = measure_time(Solution().maxSubArray, nums)
    brute_force_times.append(brute_force_time)
    divide_and_conquer_times.append(divide_and_conquer_time)
    print(f"n = {n}: Brute-force = {brute_force_time:.6f}s, Divide-and-conquer = {divide_and_conquer_time:.6f}s")

# Determine the minimum n0
n0 = None
for i in range(len(n_values)):
    if divide_and_conquer_times[i] < brute_force_times[i]:
        n0 = n_values[i]
        break

print(f"The minimum n0 for which the divide-and-conquer algorithm runs faster than the brute-force algorithm is {n0}.")