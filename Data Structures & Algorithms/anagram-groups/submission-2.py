class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for item in strs:
            count = [0] * 26
            for c in item:
                count[ord(c) - ord('a')] += 1
            hash_map[tuple(count)].append(item)
        return list(hash_map.values())
