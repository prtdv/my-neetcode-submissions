class Solution:
    def findMin(self, nums: List[int]) -> int:
        minm=nums[0]
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                return nums[i]

        return nums[0]


        