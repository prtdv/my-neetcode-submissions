class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def areaf(h1,h2,l,r):
            area=min(h1,h2)*abs(l-r)
            return area

        l=0
        r=len(heights)-1
        maxW=0
        while l<r:
            x=areaf(heights[l],heights[r],l,r)
            maxW=max(x,maxW)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxW