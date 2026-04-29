class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        cur_sum = 0
        count = 0
        for r in range(len(arr)):
            cur_sum += arr[r]
            if r - l + 1 > k:
                cur_sum -= arr[l]
                l += 1
            if r - l + 1 == k: # once r have iterated enough
                avg = cur_sum / k
                if avg >= threshold:
                    count += 1
        return count
        