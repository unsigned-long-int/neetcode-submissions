import sys
sys.setrecursionlimit(20000)
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        deq = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    deq.append((i, j))


        RIGHT, LEFT, UP, DOWN = (1, 0), (-1, 0), (0, 1), (0, -1)

        dist = 0
        while deq:
            dist += 1
            for _ in range(len(deq)):
                o_r, o_c = deq.popleft()
                for r_dir, c_dir in (RIGHT, LEFT, UP, DOWN):
                    n_r, n_c = o_r + r_dir, o_c + c_dir
                    
                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 2147483647:
                        grid[n_r][n_c] = dist
                        deq.append((n_r, n_c))



        