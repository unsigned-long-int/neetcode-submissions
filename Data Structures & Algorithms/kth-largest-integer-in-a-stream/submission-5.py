class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)


    def add(self, val) -> int:
        heapq.heappush(self.nums, val)
        while self.nums and len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
 
        
