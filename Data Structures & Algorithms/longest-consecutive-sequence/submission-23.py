class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest=0

        for n in num:
            if n-1 not in num: #if no left neightbor, start counting.
                streak=0
                while n+streak in num: #check further sequence
                    streak+=1
                longest=max(streak,longest) #update longest for each sequence found

        return longest