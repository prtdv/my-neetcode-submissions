class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        l=0
        maxc=0
        for r in range(0, len(s)):
            while l<r and s[r] in window:
                window.remove(s[l]) #always remove from the left side, shrink from left.
                l+=1
            window.add(s[r])
            maxc=max(maxc,len(window))

        return maxc
        