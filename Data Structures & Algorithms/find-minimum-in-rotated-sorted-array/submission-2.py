class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = 0
        r = len(nums)-1

        while (r-l)>1:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid
            else: 
                r = mid
        return min(nums[r],nums[l])