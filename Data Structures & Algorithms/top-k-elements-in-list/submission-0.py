class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hMap = {}
        for num in nums:
            if num not in hMap:
                hMap[num] = 0
            hMap[num] += 1

        return [num for num, count_ in sorted(hMap.items(), key=lambda x: x[1])][-k:]