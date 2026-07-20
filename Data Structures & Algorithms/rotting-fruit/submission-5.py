class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        rotten = deque()
        fresh = 0
        for i in range(ROWS):
            for l in range(COLS):
                if grid[i][l] == 2:
                    rotten.append((i, l))
                elif grid[i][l] == 1:
                    fresh += 1

        LEFT, RIGHT, DOWN, UP = (-1, 0), (1, 0), (0, -1), (0, 1)
        time = 0

        if not fresh:
            return 0

        while rotten:
            time += 1
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for rd, cd in (LEFT, RIGHT, DOWN, UP):
                    nr, nc = r + rd, c + cd

                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten.append((nr, nc))
                        fresh -= 1

        return time - 1 if fresh == 0 else -1