class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        if n == 0:
            return -1
        if nums[l]>= target or nums[r]< target:
            if nums[l] == target:
                return l
            else: return -1
        while r-l>1:
            mid = (r+l)//2
    
            if nums[mid] < target:
                l = mid
            else:
                r = mid
        if nums[r]==target:
                    return r
            
        return -1