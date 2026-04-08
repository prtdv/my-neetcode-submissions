class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[]
        for i in range(0,len(nums)):
            new=nums.copy()
            new.pop(i)
            mul=1
            for j in range(0,len(nums)-1):
                    mul*=new[j]
            arr.append(mul)
        return arr
