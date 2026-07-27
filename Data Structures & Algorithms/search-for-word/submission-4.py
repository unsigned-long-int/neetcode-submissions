sys.setrecursionlimit(10000)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or c >= COLS or r >= ROWS or (r, c) in visited or board[r][c] != word[i]:
                return False
            visited.add((r, c))
            found = dfs(r + 1, c, i + 1) or dfs(r-1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            visited.discard((r, c))
            return found
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

