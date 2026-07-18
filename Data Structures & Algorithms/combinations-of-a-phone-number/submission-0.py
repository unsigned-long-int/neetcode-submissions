class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_ = {
            2: {"a", "b", "c"},
            3: {"d", "e", "f"},
            4: {"g", "h", "i"},
            5: {"j", "k", "l"},
            6: {"m", "n", "o"},
            7: {"p", "q", "r", "s"},
            8: {"t", "u", "v"},
            9: {"w", "x", "y", "z"}
        }
        res = []
        subset = []
        if not digits:
            return res
        def dfs(i):
            if len(subset) == len(digits):
                res.append(''.join(subset))
                return
            if i >= len(digits):
                return

            dig = digits[i]
            for l in map_[int(dig)]:
                subset.append(l)
                dfs(i + 1)
                subset.pop()
        dfs(0)
        return res