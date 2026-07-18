class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def dfs(open_i, close_i):
            if open_i == close_i == n:
                res.append(''.join(stack))
                return

            if open_i < n:
                stack.append("(")
                dfs(open_i+1, close_i)
                stack.pop()

            if close_i < open_i:
                stack.append(")")
                dfs(open_i, close_i + 1)
                stack.pop()

        dfs(0, 0)
        return res
        