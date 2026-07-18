class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def is_palindrome(word):
            l, r = 0, len(word) - 1

            while l < r:
                if word[r] != word[l]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i, pal):
            if i >= len(s):
                if all(is_palindrome(l) for l in subset):
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
                subset.pop() # popping pal
                subset.pop() # popping # prev
                subset.append(prev) # adding prev back

        dfs(0, "")

        return res

            