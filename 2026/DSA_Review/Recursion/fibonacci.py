def fibo(num): # two base cases
    if num == 0:
        return 0
    if num == 1:
        return 1
    return fibo(num - 1) + fibo(num - 2)