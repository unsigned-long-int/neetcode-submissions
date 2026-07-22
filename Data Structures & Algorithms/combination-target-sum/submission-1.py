class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, sum_):
            if i >= len(nums) or sum(subset) > target:
                return 

            if sum(subset) == target:
                res.append(subset.copy())
                return

            
            subset.append(nums[i])
            dfs(i, nums[i] + sum_)
            subset.pop()
            dfs(i + 1, sum_)

        dfs(0, 0)

        return res

            
            