class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set()

        def backtrack():
            if len(subset) == len(nums):
                res.append(subset.copy())

            for i in range(len(nums)):
                if nums[i] in visited:
                    continue 
                subset.append(nums[i])
                visited.add(nums[i])
                backtrack()
                subset.pop()
                visited.discard(nums[i])
        backtrack()
        return res