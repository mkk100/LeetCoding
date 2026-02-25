def binarySearch(l, r, m, arr, x):
    while l <= r:
        m = l + r // 2
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            return m
    return -1

def findPeak(l, r, m, arr, x):
    if l < r:
        return -1
    if arr[m - 1] < arr[m] and arr[m + 1] < arr[m]:
        return arr[m]
    if arr[m] < arr[m + 1]: # if right neighbour bigger, search right
        l = m + 1
    if arr[m] < arr[m - 1]: # if left neighbour bigger, search left
        r = m - 1
        
def merge(left, right): 
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1
    
    # add any remaining from left and right to results
    return result


def mergeSort(arr): # stable sort
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftPortion = mergeSort(arr[:mid])
    rightPortion = mergeSort(arr[mid:])
    return merge(leftPortion,rightPortion)

def inversionCount(left, right): 
    result = []
    i = j = 0
    total = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            total += len(left) - i
            result.append(right[i])
            j += 1
    
    # add any remaining from left and right to results
    return total, result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    total = 0
    mid = len(arr) // 2
    totalLeft, left = mergeSort(arr[:mid])
    totalRight, right = mergeSort(arr[mid:])
    
    totalMerge = inversionCount(left, right)
    
    return totalLeft +  totalRight + totalMerge

def maxHeapify(arr, i):
    left = 2*i
    right = 2*i + 1
    largest = i
    
    if left > arr[largest]:
        largest = left 
    else:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)

def buildHeapMax(arr):
    for i in range(len(arr)//2, -1):
        maxHeapify(arr, i)

def heapSort(a): # not stable sort
    buildHeapMax(a)
    for i in range(len(a), 2):
        a[1], a[i] = a[i], a[1]
        a.size = a.size - 1
        maxHeapify(a, 1)
    

# heap and merge
# graph algos and their run time
# masters theorem
# dynamic programming
    
