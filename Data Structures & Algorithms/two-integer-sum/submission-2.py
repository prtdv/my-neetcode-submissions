class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={} #storing (value,index) for comparison in one pass.
        for i in range(0,len(nums)):
            value=target-nums[i]
            if value in hash:
                c=[hash[value],i]
                return c
            else:
                hash[nums[i]]=i
                    