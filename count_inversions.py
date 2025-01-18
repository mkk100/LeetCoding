def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    res = 0
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            res += (n1-i)
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    return res

def merge_sort(arr, left, right):
    res = 0
    if left < right:
        mid = (left + right) // 2

        res += merge_sort(arr, left, mid)
        res += merge_sort(arr, mid + 1, right)
        res += merge(arr, left, mid, right)
    return res
        
def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

# Driver code
if __name__ == "__main__":
    arr = [2,3,1]
    print("Given array is")
    print_list(arr)

    print('hi',merge_sort(arr, 0, len(arr) - 1))

    print("\nSorted array is")
    print_list(arr)