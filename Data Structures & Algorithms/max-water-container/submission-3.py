class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #take width in consideration (r-l)
        #take min height of l r's heights.

        def areaf(h1,h2,i1,i2):
            area=min(h1,h2)*abs(i1-i2)
            return area
        
        maxWeight=0
        l=0
        r=len(heights)-1

        #pass 1
        while l<r:
            x=areaf(heights[l],heights[r],l,r)
            maxWeight=max(x,maxWeight)

            if heights[l]>heights[r]: #find better wall, width always decreases so just find a better wall.
                r-=1
            else:
                l+=1
            


        
        return maxWeight

            


