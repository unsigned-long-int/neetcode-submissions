class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def backtrack(r, c):
            if c < 0 or r < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            max_area = 1 + backtrack(r + 1, c) +  backtrack(r - 1, c) + backtrack(r, c + 1) + backtrack(r, c - 1)
            #visited.discard((r, c))
            return max_area

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(backtrack(r, c), max_area)

        return max_area

            
