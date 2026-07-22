class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n*m-1

        
        while l<=r:
            index_mid = (l+r)//2
            mid = matrix[index_mid//m][index_mid%m]
            if mid==target:
                return True
            if mid < target:
                l = index_mid + 1
            else:
                r = index_mid - 1
        return False

