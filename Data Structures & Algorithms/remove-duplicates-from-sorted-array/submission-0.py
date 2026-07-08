class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0 
        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            else:
                nums[j]=nums[i]
                j+=1

        return j