class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return False
        res = []
        subset = []
        memo = {}
        def is_pal(s):
            if s in memo:
                return memo[s]
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    memo[s] = False
                    return memo[s]
                l += 1
                r -= 1
            memo[s] = True
            return memo[s]
        
        def backtrack(i, pal):
            if i == len(s):
                if all(is_pal(i) for i in subset):
                    res.append(subset.copy())
                return
            
            if subset:
                prev = subset.pop()
            else:
                prev = ""
            pal += s[i]
            subset.append(pal)
            backtrack(i + 1, pal)
            if prev:
                subset.pop()
                subset.append(prev)
                subset.append(s[i])
                backtrack(i + 1, s[i])
                subset.pop()
                subset.pop()
                subset.append(prev)
        backtrack(0, "")
        return res 
            

            