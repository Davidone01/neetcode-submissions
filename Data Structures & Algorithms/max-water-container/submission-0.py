class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        current_max = 0
        while i<j:
            local_min = min(heights[i], heights[j])
            value = (j-i) * local_min
            if value > current_max:
                current_max = value
            if heights[i]==local_min:
                i += 1
            else:
                j -= 1

        return current_max
