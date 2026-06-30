class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        target = n-1

        for i in range(target, -1, -1):
            if nums[i]+i>= target:
                target = i
            
        return target == 0
        
        