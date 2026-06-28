class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        prev = nums[0]
        output = 1
        m = output
        for n in nums:
            if n == (prev + 1): 
                output += 1
            else:
                if output > m:
                    m = output
                output = 1  
            prev = n
        return max(m, output)


        