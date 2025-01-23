def findPeak(l, r, m, arr):
    if l > r:
        return -1
    if arr[m - 1] < arr[m] and arr[m] > arr[m + 1]:
        return m

    if arr[m - 1] > arr[m]:
        return findPeak(l, m - 1, l + ((r - l) // 2), arr)
    else:
        return findPeak(m + 1, r, l + ((r - l) // 2), arr)


arr = [5, 7, 8, 10, 9, 6, 4]

print(findPeak(0, len(arr) - 1, len(arr) // 2, arr))
