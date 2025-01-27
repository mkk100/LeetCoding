def max_heapify(arr, size, i):
    l = 2 * i
    r = 2 * i + 1
    
    largest = i
    
    if arr[i] < arr[l]:
        largest = l
    elif arr[i] < arr[r]:
        largest = r
    
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, size, i)
    
    
def build_max_heap(a):
    arrLen = len(a)
    for i in range(arrLen//2,0,-1):
        max_heapify(a, arrLen, i)

def heapSort(a):
    build_max_heap(a)
    
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)