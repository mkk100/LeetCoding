def max_heapify(arr, size, i):
    l = 2 * i
    r = 2 * i + 1

    largest = i

    if l < size and arr[i] < arr[l]:
        largest = l
    if r < size and arr[i] < arr[r]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, size, largest)


def build_max_heap(a):
    arrLen = len(a)
    for i in range(arrLen // 2 - 1, -1, -1):
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

    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        min_heapify(a, i, 0)


a = [10, 7, 11, 5, 4, 13]
minHeapSort(a)
print(a)
