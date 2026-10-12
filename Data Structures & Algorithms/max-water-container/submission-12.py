class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        result=0
        def maxWater(l,r):
            return min(heights[l],heights[r])*(r-l)

        while l<r:
            area=maxWater(l, r)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            result=max(result, area)
        
        return result

