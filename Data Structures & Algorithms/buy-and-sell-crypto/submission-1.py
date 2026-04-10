class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i in range(len(prices)):
            min1=prices[i]
            for j in range(i+1,len(prices)):
                max1=prices[j]
                res=max(res,max1-min1)
        return res

            



