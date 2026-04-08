class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm={} #storing (value,index) for comparison in one pass.
        for i in range(0,len(nums)):
            value=target-nums[i]
            if value in hashm:
                return [hashm[value],i]
            else:
                hashm[nums[i]]=i