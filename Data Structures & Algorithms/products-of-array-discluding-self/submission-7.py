class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(0,len(nums)):
            mul=1
            for j in range(0,len(nums)):
                if j==i:
                    continue
                else:
                    mul*=nums[j]
            arr.append(mul)
        return arr
