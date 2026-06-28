class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        v_row = [0] * ROWS
        v_col = [0] * COLS

        for r in range(ROWS):
            v_row[r] = sum(grid[r])

        for r in range(ROWS):
            for c in range(COLS):
                v_col[c] += grid[r][c]
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                 if grid[r][c] and (v_col[c]>1 or v_row[r]>1):
                    res += 1

        return res

