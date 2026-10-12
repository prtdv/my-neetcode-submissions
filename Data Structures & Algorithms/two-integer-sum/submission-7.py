class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashm={}
        for i,num in enumerate(nums):

            if target-num in hashm:
                return [hashm[target-num], i]
            else:
                hashm[num]=i
        