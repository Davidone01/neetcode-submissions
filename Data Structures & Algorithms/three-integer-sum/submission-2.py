class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = []
        nums.sort()
        for i in range(n):
            if nums[i]>0:
                break
            elif i > 0 and nums[i]==nums[i-1]:
                continue
            
            lo = i+1
            hi = n-1
            while lo < hi:
                if sum([nums[i], nums[lo], nums[hi]])==0:
                    results.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo<hi and nums[lo] == nums[lo-1]:
                        lo += 1
                    while lo<hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                elif sum([nums[i], nums[lo], nums[hi]])>0:
                        hi -= 1
                elif sum([nums[i], nums[lo], nums[hi]])<0:
                        lo += 1


        return results
