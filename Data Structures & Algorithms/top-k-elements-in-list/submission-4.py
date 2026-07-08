class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
        return [item[0] for item in sorted(list(hash_map.items()), reverse=True, key=lambda x: x[1])[:k]]