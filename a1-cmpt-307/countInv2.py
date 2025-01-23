def merge(l, m, r, arr):

    lenL = m - l + 1
    lenR = r - m
    total = 0
    
    L = [0] * lenL
    R = [0] * lenR

    for i in range(lenL):
        L[i] = arr[l + i]
    for i in range(lenR):
        R[i] = arr[m + 1 + i]

    i, j = 0, 0
    k = l
    while i < lenL and j < lenR:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
            total += lenL - i

    while i < lenL:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < lenR:
        arr[k] = R[j]
        j += 1
        k += 1
    
    return total


def countInversions(arr, l, r):
   
    total = 0
    if l < r:
        m = l + (r - l) // 2
        total += countInversions(arr, l, m)
        total += countInversions(arr, m + 1, r)
        total += merge(l, m, r, arr)
    
    return total

print(countInversions([2,3,1], 0, 2))
    
    