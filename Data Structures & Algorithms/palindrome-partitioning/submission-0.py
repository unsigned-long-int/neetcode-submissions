class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        def dfs(i, pal):
            if i >= len(s):
                if all(l == l[::-1] for l in subset):
                    res.append(subset.copy())
                return
            
            pal += s[i]
            if subset:
                prev = subset.pop()
            else:
                prev = ""
            subset.append(pal)
            dfs(i + 1, pal)

            subset.pop()
            if prev:
                pal = s[i]
                subset.append(prev)
                subset.append(pal)
                dfs(i+1, pal)
                subset.pop() 
                subset.pop() 
                subset.append(prev)

        dfs(0, "")

        return res

            