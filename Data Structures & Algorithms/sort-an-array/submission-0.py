class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        n = len(nums)
        swap = True
        while swap:
            swap = False
            for i in range(1, n):
                if nums[i-1]>nums[i]:
                    tmp = nums[i-1]
                    nums[i-1] = nums[i]
                    nums[i] = tmp
                    swap = True

        return nums