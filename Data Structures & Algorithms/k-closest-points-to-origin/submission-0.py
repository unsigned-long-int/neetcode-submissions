class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.sqrt((float(x[0])**2 + float(x[1])**2)), x) for x in points]
        heapq.heapify_max(heap)
        while heap and len(heap) > k:
            heapq.heappop_max(heap)
        return [h[1] for h in heap]