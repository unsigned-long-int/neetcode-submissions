class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def is_palindrome(word):
            l = 0
            r = len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False

                l += 1
                r -= 1
            return True

        pal = ""
        def dfs(i, pal):
            if i == len(s):
                if all(is_palindrome(item) for item in subset):
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
                
                dfs(i + 1, pal)

                subset.pop()
                subset.pop()
                subset.append(prev)

        dfs(0, "")

        return res
            

            