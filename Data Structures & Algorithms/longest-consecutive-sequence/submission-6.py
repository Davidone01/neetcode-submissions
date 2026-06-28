class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        left = 0
        max_len = 1

        for right in range(1, len(nums)):
            if nums[right] - nums[right - 1] == 1:
                max_len = max(max_len, right -left +1)
            else:
                left = right
            
        return max_len