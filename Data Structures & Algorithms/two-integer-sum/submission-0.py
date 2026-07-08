class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = len(nums) - 2
        matched = []
        for i in range(len(nums)):
            l = i + 1
            while l < len(nums):
                sum_ = nums[i] + nums[l]
                if sum_ == target:
                    matched.append(i)
                    matched.append(l)
                l += 1

        return matched

