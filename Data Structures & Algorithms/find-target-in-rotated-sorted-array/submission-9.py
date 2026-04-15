class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<r: 
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            else:
                r=m
        pivot=l #returns lowest in the list.

        def bin_search(l,r,target):
            r=r-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    return m
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return -1
        print(pivot)
        if pivot==0:
            return bin_search(pivot,len(nums),target)
        elif nums[pivot]<=target<=nums[-1]: #check if it belongs in the right half.
            return bin_search(pivot,len(nums),target)
        else: 
            return bin_search(0,pivot,target)
