def max_heapify(arr, size, i):
    l = 2 * i
    r = 2 * i + 1

    largest = i

    if l < size and arr[largest] < arr[l]:
        largest = l
    if r < size and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, size, largest)

def dary_max_heapify(arr, size, i, d):
    largest = i
    for j in range(1, d + 1):
        child = d * i + j
        if child < size and arr[largest] < arr[child]:
            largest = child

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        dary_max_heapify(arr, size, largest, d)

def build_max_heap(a):
    arrLen = len(a)
    for i in range(arrLen // 2, -1, -1):
        max_heapify(a, arrLen, i)


def maxHeapSort(a):
    build_max_heap(a)

    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)


def min_heapify(arr, size, i):
    l = 2 * i
    r = 2 * i + 1
    smallest = i

    if l < size and arr[l] < arr[smallest]:
        smallest = l
    if r < size and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, size, smallest)


def build_min_heap(a):
    for i in range((len(a) // 2), -1, -1):
        min_heapify(a, len(a), i)


def minHeapSort(a):
    build_min_heap(a)

    for i in range(len(a) - 1, -1, -1):
        a[0], a[i] = a[i], a[0]
        min_heapify(a, i, 0)


def extract_min(a):
    if not a:
        return None
    a[0], a[-1] = a[-1], a[0]
    res = a.pop()
    maxHeapSort(a)
    return res


def heap_decrease_key(a, i, key):
    if key > a[i]:
        return None
    a[i] = key
    while i > 0 and a[i // 2] > a[i]:
        a[i], a[i // 2] = a[i // 2], a[i]
        i = i // 2


def min_heap_insert(a, value):
    a.append(value)
    i = len(a) - 1
    while i > 0 and a[(i - 1) // 2] > a[i]:
        a[i], a[(i - 1) // 2] = a[(i - 1) // 2], a[i]
        i = i // 2
    


a = [10, 7, 11, 4, 4, 13]
build_min_heap(a)
print(a)

extract_min(a)
print(a)

heap_decrease_key(a, 2, 3)
print(a)

min_heap_insert(a, 2)
print(a)
