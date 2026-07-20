class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, n-1
        if n == 0: 
            return 0
        if nums[l] > target:
            return 0
        if nums[r] < target:
            return n
        while (r-l)>1:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid
            else:
                r = mid
        return r

