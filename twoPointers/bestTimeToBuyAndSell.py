class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        mostProfit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            mostProfit = max(profit, mostProfit)

            if prices[l] > prices[r]:
                l = r
            r += 1
        return mostProfit


# O(N) - time
# O(1) - space
# prices[l] > prices[r] means we found a really low price so we'll go there to right price
# l is the low price, r finds the sellable prices