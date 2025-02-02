
arr = []
arrLen = len(arr) - 1
s1Len = arrLen // 2 - 1
s2Len = arrLen // 2

def s1push(element):
    if s1Len >= 0:
        arr[s1Len] = element
        s1Len -= 1
    else:
        print("Stack 1 overflow")

def s2push(element):
    if s2Len <= arrLen:
        arr[s2Len] = element
        s2Len += 1
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