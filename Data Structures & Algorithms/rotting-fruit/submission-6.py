class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return -1
        ROWS, COLS = len(grid), len(grid[0])

        rotting = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotting.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        mins = 0
        while rotting:
            if fresh:
                mins += 1
            for _ in range(len(rotting)):
                r, c = rotting.popleft()
                for rdir, cdir in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = rdir + r, cdir + c
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotting.append((nr, nc))
                        fresh -= 1
        return mins if not fresh else -1
