class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 

        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        visited = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r, c) in visited:
                return
            
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1 , c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands
