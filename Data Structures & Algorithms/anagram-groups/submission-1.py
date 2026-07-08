class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            sorted_ = ''.join(sorted(item))
            if sorted_ not in groups:
                groups[sorted_] = []

            groups[sorted_].append(item)
        resp = [item for item in groups.values()]
        return resp
        