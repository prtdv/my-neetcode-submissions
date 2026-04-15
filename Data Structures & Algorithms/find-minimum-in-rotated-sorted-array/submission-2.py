class Solution:
    def findMin(self, nums: List[int]) -> int:
        minm=nums[0]
        for i in nums:
            minm=min(minm,i)

        return minm