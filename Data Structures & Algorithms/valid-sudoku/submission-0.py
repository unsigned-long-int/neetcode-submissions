class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for ri in range(9):
            for ci in range(9):
                if not board[ri][ci].isdigit():
                    continue
                if board[ri][ci] in rows[ri]:
                    return False
                rows[ri].add(board[ri][ci])
                if board[ri][ci] in cols[ci]:
                    return False
                cols[ci].add(board[ri][ci])
                if board[ri][ci] in grid[(ri // 3, ci // 3)]:
                    return False
                grid[(ri // 3, ci // 3)].add(board[ri][ci])

        return True
