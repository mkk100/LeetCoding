def binarySearch(l, r, m, target, arr):
    if arr[m] == target:
        return m
    if l > r:
        return -1
    if arr[m] > target:
        return binarySearch(l, m - 1, (l + (m - 1)) // 2, target, arr)
    elif arr[m] < target:
        return binarySearch(m + 1, r, (l + (m + 1)) // 2, target, arr)


arr = [1, 2, 3, 4, 5, 6]
print(binarySearch(0, len(arr) - 1, 2, 4, arr))
