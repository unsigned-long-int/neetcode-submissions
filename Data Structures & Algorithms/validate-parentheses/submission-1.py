class Solution:
    def isValid(self, s: str) -> bool:
        hash_map = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        stacked = []
        for l in s:
            if l in '[({':
                stacked.append(l)
            if l in '])}':
                if not stacked:
                    return False
                latest = stacked.pop()
                if hash_map[l] != latest:
                    return False 
        return len(stacked) == 0