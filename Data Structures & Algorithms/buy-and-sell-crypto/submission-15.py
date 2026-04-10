class Solution:
    def maxProfit(self, prices):
        l = 0
        res = 0

        for r in range(len(prices)):
            
            # while window is invalid
            while l < r and prices[l] > prices[r]:
                l += 1   # shrink window

            # now window is valid
            res = max(res, prices[r] - prices[l])

        return res