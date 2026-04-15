class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                # drop is in right half
                l = m + 1
            else:
                # drop is in left half (including m)
                r = m

        return nums[l]