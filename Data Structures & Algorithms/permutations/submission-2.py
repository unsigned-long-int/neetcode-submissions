class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        visited = set()


        def dfs(i):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return

            if i >= len(nums):
                return

            for j in range(len(nums)):
                if nums[j] in visited:
                    continue 
                visited.add(nums[j])
                subset.append(nums[j])
                dfs(j)
                visited.remove(nums[j])
                subset.pop()
        dfs(0)
        return res
