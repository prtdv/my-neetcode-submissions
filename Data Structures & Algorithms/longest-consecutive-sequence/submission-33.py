class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        longest=0

        for i in num:
            if i-1 not in num:
                streak=1
                while i+streak in num:
                    streak+=1
                longest=max(longest,streak)

        return longest
