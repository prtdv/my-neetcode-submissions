class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix=[0]*len(nums)
        for i in range(0,len(nums)):
            if i==0:
                prefix[i]=nums[i]
            else:
                prefix[i]=nums[i]*prefix[i-1]
            
        print(prefix)
            
        postfix=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix[i]=nums[i]
            else:
                postfix[i]=nums[i]*postfix[i+1]
            
        print(postfix)

        output=[0]*len(nums)
        for i in range(0,len(nums)):
            if i==0:
                output[i]=1*postfix[1]
            elif i==len(nums)-1:
                output[i]=1*prefix[-2]
            else:
                output[i]=prefix[i-1]*postfix[i+1]
        
        return output




