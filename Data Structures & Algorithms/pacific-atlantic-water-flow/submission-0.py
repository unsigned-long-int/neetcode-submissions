class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        reachables = [[[False, False] for _ in range(COLS)] for _ in range(ROWS)]
        def dfs(r, c, prev_val, index):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or reachables[r][c][index] or heights[r][c] < prev_val:
                return 
            
            reachables[r][c][index] = True
            dfs(r + 1, c, heights[r][c], index)
            dfs(r - 1, c, heights[r][c], index)
            dfs(r, c + 1, heights[r][c], index)
            dfs(r, c - 1, heights[r][c], index)

        for r in range(ROWS):
            for c in range(COLS):
                if c == 0 or r == 0:
                    dfs(r, c, heights[r][c], 0)
                if c == COLS - 1 or r == ROWS - 1:
                    dfs(r, c, heights[r][c], 1)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if all(reachables[r][c]):
                    res.append([r, c])
        return res
