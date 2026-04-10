class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=[]
        l=0
        maxc=0
        for r in range(0,len(s)):

            while l<r and s[r] in x:
                x.pop(0)
                l+=1
            
            x.append(s[r])
            maxc=max(maxc,len(x))
        return maxc
        