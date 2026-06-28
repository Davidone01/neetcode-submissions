class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        out = 1
        max_len = out

        for n in nums:
            if n-1 not in nums:
                flag = True
                while flag:
                    if n+1 in nums:
                        out +=1
                        n+=1
                    else:
                        flag  = False
                        max_len = max(out, max_len)
                        out = 1

         
        return max_len