class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashm=defaultdict(list)
        nums.sort()
        print(nums)
        count=[1]*len(nums)
        k=0
        if len(nums)==0:
            return 0
        for i in range(0,len(nums)-1):
            if nums[i+1]-1==nums[i]:
                count[k]+=1
            elif nums[i+1]==nums[i]:
                continue
            else:
                k+=1
        count.sort(reverse=True)
        return count[0]

            


                

