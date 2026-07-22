class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heapify(min_heap)

        for point in points:
            distance = math.sqrt((point[0]**2 + point[1]**2))
            heapq.heappush(min_heap, (distance, point))

        res = []
        while min_heap and len(res) < k:
            res.append(heapq.heappop(min_heap)[1])
        return res
