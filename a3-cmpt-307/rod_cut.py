def cutRod(i, price, memo):
    if i in memo:
        return memo[i]
    if i <= 0:
        return 0
    ans = 0
    for j in range(1, i):
        res = price[j-1] + cutRod(i - j, price, memo)
        ans = max(ans, res)
    memo[i] = ans

    return ans


def cutRod(price):
    n = len(price)
    memo = {}
    return cutRod(n, price, memo)


if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(price))
