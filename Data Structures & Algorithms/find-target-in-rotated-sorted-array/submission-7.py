class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums)==1:
            if len(nums)==1 and nums[0]==target:
                return 0
            else:
                return -1
        l = 0
        r = len(nums) - 1

        #cerco il punto in cui l'array si divide
        def cut_point(nums):
            l = 0
            r = len(nums)-1
            if nums[l]>nums[r]:
                while (r-l)>1:
                    mid = (r+l)//2
                    if nums[mid]>nums[l]:
                        l = mid
                    else: 
                        r = mid
                return r
            else:
                return 0

        def binary_search(nums, l, r, target):
            while (r-l) > 1:
                mid = (l+r)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]<target:
                    l = mid
                else:
                    r = mid
            return l if nums[l]==target else r if nums[r]==target else -1
        

        x = cut_point(nums)
        print(x)

        if nums[len(nums)-1] >= target:
            return binary_search(nums, x, len(nums)-1, target)
            
        else:
            return binary_search(nums, 0, x-1, target)
            