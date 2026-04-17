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
        pivot=l
        print(pivot,nums[pivot])

        def bins(l,r,target):
            while l<=r:
                m=(l+r)//2
                if target==nums[m]:
                    return m
                elif target>nums[m]:
                    l=m+1
                else:
                    r=m-1
            return -1

        if nums[l]<=target<=nums[-1]:
            return bins(l,len(nums)-1,target)
        else:
            return bins(0,l-1,target)

        