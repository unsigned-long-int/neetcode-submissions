class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heap = stones
        heapq.heapify_max(self.heap)

        res = 0
        while len(self.heap) > 1:
            stone_1 = heapq.heappop_max(self.heap)
            stone_2 = heapq.heappop_max(self.heap)

            res = stone_1 - stone_2
            if res != 0:
                heapq.heappush_max(self.heap, res)

        return res if not self.heap else self.heap[0]