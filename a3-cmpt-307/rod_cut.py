# Python program to find maximum
# profit from rod of size n 

def cutRodRecur(i, price):
    
    # Base case
    if i == 0:
        return 0
    
    ans = 0

    # Find maximum value for each cut.
    # Take value of rod of length j, and 
    # recursively find value of rod of 
    # length (i-j).
    for j in range(1, i + 1):
        ans = max(ans, price[j - 1] + cutRodRecur(i - j, price))

    return ans

def cutRod(price):
    n = len(price)

    return cutRodRecur(n, price)

if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(price))
