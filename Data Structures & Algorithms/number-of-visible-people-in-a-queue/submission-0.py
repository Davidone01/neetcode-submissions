class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        output = [0]*len(heights)

        for i in range(len(heights)):
            count = 0
            if i==len(heights):
                output[i] = 0
                return output
            for j in range(i+1,len(heights)):
                if (j-i == 1):
                    count += 1
                    continue
                # j = 2, i. = 0
                local_min = min(heights[i], heights[j])
                flag = False
                for x in range(i+1, j):
                    if local_min < heights[x]:
                        flag= True
                        break
                if not flag:
                    count += 1

            output[i] = count

        return output



 