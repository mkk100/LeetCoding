def min_heapify(arr, size, i):
    l = 2 * i + 1
    r = 2 * i + 2
    smallest = i

    if l < size and arr[l] < arr[smallest]:
        smallest = l
    elif r < size and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heapify(arr, size, smallest)


def build_min_heap(a):
    for i in range((len(a) // 2) - 1, -1, -1):
        min_heapify(a, len(a), i)


def minHeapSort(a):
    build_min_heap(a)

    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        min_heapify(a, i, 0)


a = [10, 7, 11, 5, 4, 13]
minHeapSort(a)
print(a)