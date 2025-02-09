arr = []
arrLen = len(arr) - 1
s1Len = arrLen // 2 + 1
s2Len = arrLen // 2


def s1push(element):
    if s1Len >= 0:
        s1Len -= 1
        arr[s1Len] = element
    else:
        print("Stack 1 overflow")


def s2push(element):
    if s2Len <= arrLen:
        s2Len += 1
        arr[s2Len] = element
    else:
        print("Stack 2 overflow")


def s1pop():
    if s1Len > 0:
        ret = arr[s1Len]
        s1Len += 1
        return ret
    else:
        print("Nth to pop")


def s2pop():
    if s2Len < arrLen:
        ret = arr[s2Len]
        s2Len -= 1
        return ret
    else:
        print("Nth to pop")
