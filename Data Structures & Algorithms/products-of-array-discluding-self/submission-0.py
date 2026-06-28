class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = 0
        result = []
        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if j != counter:
                    prod *=  nums[j]
            result.append(prod)
            counter += 1
        return result

