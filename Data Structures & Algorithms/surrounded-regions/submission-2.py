class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        q = deque()
        non_surrounded = set()

        for i in range(ROWS):
            for l in range(COLS):
                if board[i][l] == 'O' and (i == 0 or l == 0 or i == ROWS - 1 or l == COLS - 1):
                    q.append((i, l))
                    non_surrounded.add((i, l))
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                rn, cn = r + dr, c + dc

                if 0 <= rn < ROWS and 0 <= cn < COLS and board[rn][cn] == 'O' and (rn, cn) not in non_surrounded:
                    non_surrounded.add((rn, cn))
                    q.append((rn, cn))

        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in non_surrounded:
                    board[i][j] = 'X'
                        

        
        