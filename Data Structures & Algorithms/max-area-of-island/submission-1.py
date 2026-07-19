class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if c < 0 or r < 0 or c >= COLS or r >= ROWS or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in visited:
                    new_s = dfs(i, j)
                    max_area = max(max_area, new_s)
        return max_area
