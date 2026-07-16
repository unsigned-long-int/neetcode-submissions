class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())

            for i in range(len(nums)):
                if used[i]:
                    continue

                subset.append(nums[i])
                used[i] = True
                dfs()
                subset.pop()
                dfs()
                used[i] = False
        dfs()
        return res