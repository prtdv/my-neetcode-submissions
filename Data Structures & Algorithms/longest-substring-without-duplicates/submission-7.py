class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=[]
        l=0
        maxc=0
        for r in range(len(s)):

            while l<r and s[r] in window:
                window.pop(0)
                l+=1
            
            window.append(s[r])
            maxc=max(maxc,len(window))
        return maxc

        