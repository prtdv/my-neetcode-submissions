class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP=0
        l=0
        for r in range(1,len(prices)):

            while prices[l]>prices[r]:
                l+=1
            
            maxP=max(maxP,prices[r]-prices[l])
        return maxP
