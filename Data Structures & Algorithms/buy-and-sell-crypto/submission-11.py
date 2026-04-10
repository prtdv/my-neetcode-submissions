class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        l=0
        r=l+1
        while r<len(prices): #condition, prices[r] must be > than prices[l]
            if prices[l]<prices[r]:
                profit=max(profit,prices[r]-prices[l])
                r+=1
            else:
                l=r
                r+=1
            

        return profit


            



            

            



