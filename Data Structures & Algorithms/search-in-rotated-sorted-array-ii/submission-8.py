class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        def find_minimum(nums):
            l = 0
            r = len(nums)-1
           
            while l<r and nums[l]==nums[r]:
                l+=1
            if nums[l]<nums[r]:
                return l
            while (r-l)>1:
                mid = (l+r)//2
                if nums[mid]>nums[r]:
                    l = mid
                else:
                    r = mid
            return r

        
        def find_target(nums, l, r, target):
            while (r-l)>1:
                mid = (l+r)//2
                if nums[mid] < target:
                    l = mid 
                else:
                    r = mid
            
            return nums[r] == target or nums[l]==target

      
        if not nums:
            return False
        if len(nums)==1:
            return nums[0]==target
        # trova il minimo
        minimum = find_minimum(nums)
        print(minimum)
        #vettore completamente odinato bs su tutto il vettore
        if minimum == 0:
            return find_target(nums, 0, len(nums)-1, target)
        else:
            if target > nums[len(nums)-1]:
                print("entro qua")
                return find_target(nums, 0, minimum -1, target)
            else:
                return find_target(nums, minimum, len(nums)-1, target)

